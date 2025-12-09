import json
import os
import logging
from typing import Any, Dict, List, Optional

import requests

Logging = logging.getLogger()
Logging.setLevel(logging.INFO)


class AtsClient:
    """
    Simple ATS Client Wrapper

    - Ats Base Url Should Point To ATS Api Root
      For Example With A Generic ATS:
      Ats Base Url = "http://localhost:8080"
    - Ats Api Key Is A Secret Token Or Api Key
      For Local Testing, Use A Dummy Key
    """

    def __init__(self) -> None:
        self.AtsBaseUrl = os.environ.get("AtsBaseUrl")
        self.AtsApiKey = os.environ.get("AtsApiKey")
        self.AtsApplicationsPath = os.environ.get("AtsApplicationsPath", "/applications")

        if not self.AtsBaseUrl or not self.AtsApiKey:
            raise ValueError("Missing AtsBaseUrl Or AtsApiKey Environment Variables")

        # Normalize Base Url
        self.AtsBaseUrl = self.AtsBaseUrl.rstrip("/")

    def _GetHeaders(self) -> Dict[str, str]:
        """
        Return Default Headers For Ats Api.
        Generic Auth: Bearer Token
        """
        return {
            "Authorization": f"Bearer {self.AtsApiKey}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    # -----------------------
    # Jobs / Offers
    # -----------------------
    def GetJobsFromAts(self, Page: Optional[int] = None, PerPage: Optional[int] = None) -> Dict[str, Any]:
        """
        Fetch Jobs From Ats.

        Generic Endpoint: GET {BaseUrl}/offers
        """
        Params: Dict[str, Any] = {}
        if Page is not None:
            Params["page"] = Page
        if PerPage is not None:
            Params["per_page"] = PerPage

        Url = f"{self.AtsBaseUrl}/offers"
        Response = requests.get(Url, headers=self._GetHeaders(), params=Params, timeout=15)

        if not Response.ok:
            raise RuntimeError(f"Ats Jobs Error: {Response.status_code} {Response.text}")

        return Response.json()

    # -----------------------
    # Candidates
    # -----------------------
    def CreateCandidateInAts(self, CandidatePayload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create Candidate In Ats.

        Generic Endpoint: POST {BaseUrl}/candidates
        """
        Url = f"{self.AtsBaseUrl}/candidates"
        Response = requests.post(Url, headers=self._GetHeaders(), json=CandidatePayload, timeout=20)

        if not Response.ok:
            raise RuntimeError(f"Ats Create Candidate Error: {Response.status_code} {Response.text}")

        return Response.json()

    def GetCandidatesFromAts(self, Page: Optional[int] = None, PerPage: Optional[int] = None) -> Dict[str, Any]:
        """
        Fetch Candidates From Ats.

        Generic Endpoint: GET {BaseUrl}/candidates
        """
        Params: Dict[str, Any] = {}
        if Page is not None:
            Params["page"] = Page
        if PerPage is not None:
            Params["per_page"] = PerPage

        Url = f"{self.AtsBaseUrl}/candidates"
        Response = requests.get(Url, headers=self._GetHeaders(), params=Params, timeout=15)

        if not Response.ok:
            raise RuntimeError(f"Ats Candidates Error: {Response.status_code} {Response.text}")

        return Response.json()

    # -----------------------
    # Applications / Pipeline
    # -----------------------
    def CreateApplicationInAts(self, CandidateId: str, JobId: str) -> Dict[str, Any]:
        """
        Attach Candidate To Job (Create Application / Pipeline Entry).

        Generic Pattern:
            POST {BaseUrl}{AtsApplicationsPath}
            Body:
              {
                "candidate_id": "...",
                "job_id": "...",
                "initial_stage_id": null Or Concrete Stage Id
              }
        """
        Url = f"{self.AtsBaseUrl}{self.AtsApplicationsPath}"
        Payload = {
            "candidate_id": CandidateId,
            "job_id": JobId,
        }

        Response = requests.post(Url, headers=self._GetHeaders(), json=Payload, timeout=20)

        if not Response.ok:
            raise RuntimeError(f"Ats Create Application Error: {Response.status_code} {Response.text}")

        return Response.json()

    def GetApplicationsFromAts(
        self,
        JobId: Optional[str] = None,
        Page: Optional[int] = None,
        PerPage: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Fetch Applications For A Given Job From Ats.
        Generic Endpoint: GET {BaseUrl}{AtsApplicationsPath}?job_id=...
        """
        Url = f"{self.AtsBaseUrl}{self.AtsApplicationsPath}"
        Params: Dict[str, Any] = {}

        if JobId is not None:
            Params["job_id"] = JobId

        if Page is not None:
            Params["page"] = Page
        if PerPage is not None:
            Params["per_page"] = PerPage

        Response = requests.get(Url, headers=self._GetHeaders(), params=Params, timeout=20)

        if not Response.ok:
            raise RuntimeError(f"Ats Applications Error: {Response.status_code} {Response.text}")

        return Response.json()


# -----------------------
# Helper Response Builder
# -----------------------
def _Response(StatusCode: int, BodyDict: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "statusCode": StatusCode,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(BodyDict),
    }


# -----------------------
# Lambda Handlers
# -----------------------
def Hello(Event, Context):
    """
    Simple Health Check For Serverless Offline.
    """
    Body = {
        "Message": "Hello From Serverless Offline Python",
        "Path": Event.get("rawPath") if isinstance(Event, dict) else None,
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(Body),
    }


def GetJobs(Event, Context):
    """
    GET /jobs
    Returns Jobs In Unified Format:
        {
          "jobs": [
            {
              "id": "string",
              "title": "string",
              "location": "string",
              "status": "OPEN|CLOSED|DRAFT",
              "external_url": "string"
            }
          ]
        }
    """
    try:
        Client = AtsClient()
        QueryParams = Event.get("queryStringParameters") or {}
        PageRaw = QueryParams.get("page")
        PerPageRaw = QueryParams.get("per_page")

        Page = int(PageRaw) if PageRaw is not None else None
        PerPage = int(PerPageRaw) if PerPageRaw is not None else None

        RawJobs = Client.GetJobsFromAts(Page=Page, PerPage=PerPage)

        # "data" Key Is Common, Fallback To Raw List
        RawJobsList: List[Dict[str, Any]] = RawJobs.get("data", RawJobs if isinstance(RawJobs, list) else [])

        UnifiedJobs: List[Dict[str, Any]] = []
        for Job in RawJobsList:
            UnifiedJobs.append(
                {
                    "id": str(Job.get("id")),
                    "title": Job.get("title") or Job.get("job_title"),
                    "location": Job.get("location") or Job.get("city") or Job.get("country"),
                    "status": _NormalizeJobStatus(Job.get("status")),
                    "external_url": Job.get("url") or Job.get("apply_url") or Job.get("careers_url"),
                }
            )

        return _Response(200, {"jobs": UnifiedJobs})

    except Exception as Ex:
        Logging.exception("GetJobs Failed")
        return _Response(
            500,
            {
                "error": "JobsFetchFailed",
                "message": str(Ex),
            },
        )


def CreateCandidate(Event, Context):
    """
    POST /candidates

    Request Body:
        {
          "name": "string",
          "email": "string",
          "phone": "string",
          "resume_url": "string",
          "job_id": "string"
        }

    Steps:
      1. Create Candidate In Ats
      2. Attach Candidate To Given Job (Create Application / Pipeline Entry)
    """
    try:
        Client = AtsClient()

        BodyRaw = Event.get("body") or "{}"
        Payload = json.loads(BodyRaw)

        Name = Payload.get("name")
        Email = Payload.get("email")
        Phone = Payload.get("phone")
        ResumeUrl = Payload.get("resume_url")
        JobId = Payload.get("job_id")

        if not Name or not Email or not JobId:
            return _Response(
                400,
                {
                    "error": "ValidationError",
                    "message": "Name, Email And job_id Are Required",
                },
            )

        # Split Name Naively Into First / Last
        NameParts = str(Name).strip().split(" ", 1)
        FirstName = NameParts[0]
        LastName = NameParts[1] if len(NameParts) > 1 else ""

        # Map To A Generic Candidate Payload
        AtsCandidatePayload: Dict[str, Any] = {
            "first_name": FirstName,
            "last_name": LastName,
            "emails": [{"value": Email, "type": "work"}],
            "phones": [{"value": Phone, "type": "mobile"}] if Phone else [],
            "photo_url": None,
            "social_links": [],
            "cv_url": ResumeUrl,
        }

        CreatedCandidate = Client.CreateCandidateInAts(AtsCandidatePayload)
        CandidateId = str(CreatedCandidate.get("id") or CreatedCandidate.get("candidate_id"))

        # Attach Candidate To Job (Create Application / Pipeline Entry)
        CreatedApplication = Client.CreateApplicationInAts(CandidateId=CandidateId, JobId=str(JobId))

        UnifiedApplication = {
            "id": str(CreatedApplication.get("id", "")),
            "job_id": str(JobId),
            "candidate_id": CandidateId,
            "status": _NormalizeApplicationStatus(CreatedApplication.get("status")),
        }

        UnifiedCandidate = {
            "id": CandidateId,
            "name": Name,
            "email": Email,
            "phone": Phone,
        }

        return _Response(
            201,
            {
                "candidate": UnifiedCandidate,
                "application": UnifiedApplication,
            },
        )

    except Exception as Ex:
        Logging.exception("CreateCandidate Failed")
        return _Response(
            500,
            {
                "error": "CandidateCreateFailed",
                "message": str(Ex),
            },
        )


def GetCandidates(Event, Context):
    """
    GET /candidates
    Returns Candidates In Unified Format:
        {
          "candidates": [
            {
              "id": "string",
              "name": "string",
              "email": "string",
              "phone": "string"
            }
          ]
        }
    """
    try:
        Client = AtsClient()
        QueryParams = Event.get("queryStringParameters") or {}
        PageRaw = QueryParams.get("page")
        PerPageRaw = QueryParams.get("per_page")

        Page = int(PageRaw) if PageRaw is not None else None
        PerPage = int(PerPageRaw) if PerPageRaw is not None else None

        RawCandidates = Client.GetCandidatesFromAts(Page=Page, PerPage=PerPage)

        RawCandidatesList: List[Dict[str, Any]] = RawCandidates.get("data", RawCandidates if isinstance(RawCandidates, list) else [])

        UnifiedCandidates: List[Dict[str, Any]] = []
        for Candidate in RawCandidatesList:
            UnifiedCandidates.append(
                {
                    "id": str(Candidate.get("id")),
                    "name": Candidate.get("name") or f"{Candidate.get('first_name', '')} {Candidate.get('last_name', '')}".strip(),
                    "email": Candidate.get("email") or (Candidate.get("emails") or [{}])[0].get("value"),
                    "phone": (Candidate.get("phones") or [{}])[0].get("value"),
                }
            )

        return _Response(200, {"candidates": UnifiedCandidates})

    except Exception as Ex:
        Logging.exception("GetCandidates Failed")
        return _Response(
            500,
            {
                "error": "CandidatesFetchFailed",
                "message": str(Ex),
            },
        )


def CreateApplication(Event, Context):
    """
    POST /applications

    Request Body:
        {
          "candidate_id": "string",
          "job_id": "string"
        }

    Creates An Application Linking Candidate To Job.
    """
    try:
        Client = AtsClient()

        BodyRaw = Event.get("body") or "{}"
        Payload = json.loads(BodyRaw)

        CandidateId = Payload.get("candidate_id")
        JobId = Payload.get("job_id")

        if not CandidateId or not JobId:
            return _Response(
                400,
                {
                    "error": "ValidationError",
                    "message": "candidate_id And job_id Are Required",
                },
            )

        CreatedApplication = Client.CreateApplicationInAts(CandidateId=str(CandidateId), JobId=str(JobId))

        UnifiedApplication = {
            "id": str(CreatedApplication.get("id", "")),
            "candidate_id": str(CandidateId),
            "job_id": str(JobId),
            "status": _NormalizeApplicationStatus(CreatedApplication.get("status")),
        }

        return _Response(
            201,
            {
                "application": UnifiedApplication,
            },
        )

    except Exception as Ex:
        Logging.exception("CreateApplication Failed")
        return _Response(
            500,
            {
                "error": "ApplicationCreateFailed",
                "message": str(Ex),
            },
        )


def GetApplications(Event, Context):
    """
    GET /applications?job_id=... (optional)

    Returns:
        {
          "applications": [
            {
              "id": "string",
              "candidate_name": "string",
              "email": "string",
              "status": "APPLIED|SCREENING|REJECTED|HIRED"
            }
          ]
        }
    """
    try:
        Client = AtsClient()

        QueryParams = Event.get("queryStringParameters") or {}
        JobId = QueryParams.get("job_id")
        PageRaw = QueryParams.get("page")
        PerPageRaw = QueryParams.get("per_page")

        Page = int(PageRaw) if PageRaw is not None else None
        PerPage = int(PerPageRaw) if PerPageRaw is not None else None

        RawApplications = Client.GetApplicationsFromAts(JobId=JobId, Page=Page, PerPage=PerPage)

        RawApplicationsList: List[Dict[str, Any]] = RawApplications.get(
            "data",
            RawApplications if isinstance(RawApplications, list) else [],
        )

        UnifiedApplications: List[Dict[str, Any]] = []
        for Application in RawApplicationsList:
            CandidateInfo = Application.get("candidate", {})
            UnifiedApplications.append(
                {
                    "id": str(Application.get("id")),
                    "candidate_name": CandidateInfo.get("name")
                    or f"{CandidateInfo.get('first_name', '')} {CandidateInfo.get('last_name', '')}".strip(),
                    "email": CandidateInfo.get("email")
                    or (CandidateInfo.get("emails") or [{}])[0].get("value"),
                    "status": _NormalizeApplicationStatus(Application.get("status")),
                }
            )

        return _Response(200, {"applications": UnifiedApplications})

    except Exception as Ex:
        Logging.exception("GetApplications Failed")
        return _Response(
            500,
            {
                "error": "ApplicationsFetchFailed",
                "message": str(Ex),
            },
        )


# -----------------------
# Normalization Helpers
# -----------------------
def _NormalizeJobStatus(Status: Optional[str]) -> str:
    if not Status:
        return "OPEN"
    StatusLower = str(Status).lower()
    if "draft" in StatusLower:
        return "DRAFT"
    if "close" in StatusLower or "archive" in StatusLower:
        return "CLOSED"
    return "OPEN"


def _NormalizeApplicationStatus(Status: Optional[str]) -> str:
    if not Status:
        return "APPLIED"
    StatusLower = str(Status).lower()
    if "screen" in StatusLower or "review" in StatusLower:
        return "SCREENING"
    if "reject" in StatusLower or "fail" in StatusLower:
        return "REJECTED"
    if "hire" in StatusLower or "offer_accepted" in StatusLower:
        return "HIRED"
    return "APPLIED"