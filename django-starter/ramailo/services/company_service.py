
from ramailo.models import Company
from ramailo.serializers.company_serializer import CompanySerializer

class CompanyService:

    def get_all_companies(self):
        companies = Company.objects.all()
        return CompanySerializer(companies, many=True).data

    def find_company_by_idx(self, idx):
        companies = Company.objects.filter(idx=idx)
        if companies.exists():
            return companies.first()
        return None

    def find_company_by_name(self, name):
        companies = Company.objects.filter(name=name)
        if companies.exists():
            return companies.first()
        return None