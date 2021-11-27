import pytest
from django.core.exceptions import ObjectDoesNotExist

from conferences.models import Conference
from tests.constants import (CONFERENCE_DESCRIPTION_1,
                             CONFERENCE_DESCRIPTION_2, CONFERENCE_END_DATE_1,
                             CONFERENCE_END_DATE_2, CONFERENCE_START_DATE_1,
                             CONFERENCE_START_DATE_2, CONFERENCE_TITLE_1,
                             CONFERENCE_TITLE_2)


@pytest.mark.django_db
class TestPromoModel:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.conference = Conference.objects.create(
            title=CONFERENCE_TITLE_1,
            description=CONFERENCE_DESCRIPTION_1,
            start_date=CONFERENCE_START_DATE_1,
            end_date=CONFERENCE_END_DATE_1,
        )

    def test_list_conferences_objects_success(self):
        assert Conference.objects.all().count() == 1

    def test_create_conference_objects_success(self):
        Conference.objects.create(
            title=CONFERENCE_TITLE_2,
            description=CONFERENCE_DESCRIPTION_2,
            start_date=CONFERENCE_START_DATE_2,
            end_date=CONFERENCE_END_DATE_2,
        )
        assert Conference.objects.all().count() == 2

    def test_retrieve_conference_object_success(self):
        assert len(Conference.objects.filter(pk=self.conference.id)) == 1

    def test_retrieve_conference_object_fail_with_not_exist_id(self):
        with pytest.raises(ObjectDoesNotExist):
            Conference.objects.get(pk=5)
