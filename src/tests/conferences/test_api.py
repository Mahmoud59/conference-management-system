from unittest.mock import MagicMock, patch

import pytest
from django.urls import reverse
from rest_framework import status

from conferences.models import Conference
from tests.constants import (CONFERENCE_DESCRIPTION_1,
                             CONFERENCE_DESCRIPTION_2,
                             CONFERENCE_DESCRIPTION_3, CONFERENCE_END_DATE_1,
                             CONFERENCE_END_DATE_2, CONFERENCE_END_DATE_3,
                             CONFERENCE_START_DATE_1, CONFERENCE_START_DATE_2,
                             CONFERENCE_START_DATE_3, CONFERENCE_TITLE_1,
                             CONFERENCE_TITLE_2, CONFERENCE_TITLE_3)


@pytest.mark.django_db
class TestConferenceEndpoints:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.conference = Conference.objects.create(
            title=CONFERENCE_TITLE_1,
            description=CONFERENCE_DESCRIPTION_1,
            start_date=CONFERENCE_START_DATE_1,
            end_date=CONFERENCE_END_DATE_1,
        )
        self.url_list = reverse('conferences-list')
        self.url_detail = reverse('conferences-detail',
                                  kwargs={'pk': self.conference.id})

    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_list_conferences_success(self, mock_authenticate, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_200_OK

    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_create_conference_success(self, mock_authenticate, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        body = {
            "title": CONFERENCE_TITLE_2,
            "description": CONFERENCE_DESCRIPTION_2,
            "start_date": CONFERENCE_START_DATE_2,
            "end_date": CONFERENCE_END_DATE_2,
        }
        response = drf_client.post(self.url_list, data=body, format="json")
        assert response.status_code == status.HTTP_201_CREATED

    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_create_conference_failed_missing_title(
            self, mock_authenticate, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        body = {
            "description": CONFERENCE_DESCRIPTION_2,
            "start_date": CONFERENCE_START_DATE_2,
            "end_date": CONFERENCE_END_DATE_2,
        }
        response = drf_client.post(self.url_list, data=body, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_create_conference_failed_start_date_before_today(
            self, mock_authenticate, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        body = {
            "title": CONFERENCE_TITLE_3,
            "description": CONFERENCE_DESCRIPTION_3,
            "start_date": CONFERENCE_START_DATE_3,
            "end_date": CONFERENCE_END_DATE_2,
        }
        response = drf_client.post(self.url_list, data=body, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_create_conference_failed_end_date_before_start_date(
            self, mock_authenticate, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        body = {
            "title": CONFERENCE_TITLE_3,
            "description": CONFERENCE_DESCRIPTION_3,
            "start_date": CONFERENCE_START_DATE_2,
            "end_date": CONFERENCE_END_DATE_3,
        }
        response = drf_client.post(self.url_list, data=body, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_retrieve_conference_success(
            self, mock_authenticate, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        response = drf_client.get(self.url_detail)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_update_conference_sucess(self, mock_authenticate, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        body = {
            "title": CONFERENCE_TITLE_2,
            "description": CONFERENCE_DESCRIPTION_2,
            "start_date": CONFERENCE_START_DATE_2,
            "end_date": CONFERENCE_END_DATE_2,
        }
        response = drf_client.patch(self.url_detail, data=body, format="json")
        assert response.status_code == status.HTTP_200_OK

    @patch('rest_framework_simplejwt.authentication.JWTAuthentication.'
           'authenticate')
    def test_delete_conference_sucess(self, mock_authenticate, drf_client):
        mock_authenticate.return_value = (MagicMock(), [])
        response = drf_client.delete(self.url_detail)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
