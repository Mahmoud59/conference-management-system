import pytest
from django.urls import reverse
from rest_framework import status

from conferences.models import Conference
from tests.constants import (CONFERENCE_DESCRIPTION_1, CONFERENCE_END_DATE_1,
                             CONFERENCE_START_DATE_1, CONFERENCE_TITLE_1)


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

    def test_list_conferences_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_conference_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_retrieve_conference_without_authorization_header(
            self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_conference_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_conference_without_authorization_header(self, drf_client):
        response = drf_client.get(self.url_list)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
