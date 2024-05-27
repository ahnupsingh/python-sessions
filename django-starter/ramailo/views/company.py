
from rest_framework.views import APIView
from ramailo.builders.response_builder import ResponseBuilder
from ramailo.serializers.company_serializer import CompanySerializer
from ramailo.services.company_service import CompanyService

class CompanyView(APIView):

    def get(self, request, *args, **kwargs):
        response_builder = ResponseBuilder()
        try:
            company_service = CompanyService()
            companies = company_service.get_all_companies()
            field_to_know = response_builder.result_object(companies).success().ok_200().get_response()
            return field_to_know
        except Exception as e:
            print(f"CompanyView get :: exception:: {e}")
            return response_builder.result_object({'message': "Unable to get companies"}).fail().internal_error_500().message("Internal Error").get_response()


class CompanyDetailView(APIView):
    def get(self, request, company_id, *args, **kwargs):
        response_builder = ResponseBuilder()
        try:
            company_service = CompanyService()
            company = company_service.find_company_by_idx(company_id)
            serialized_data = CompanySerializer(company).data
            if company:
                return response_builder.result_object(serialized_data).success().ok_200().get_response()
            else:
                return response_builder.result_object({'message': "Company not found"}).fail().not_found_404().message("Not Found").get_response()
        except Exception as e:
            print(f"CompanyDetailView get :: exception:: {e}")
            return response_builder.result_object({'message': "Unable to get company details"}).fail().internal_error_500().message("Internal Error").get_response()