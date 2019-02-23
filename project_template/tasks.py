import datetime
 
from moonsheep import verifiers
from moonsheep.decorators import register

import project_template.models as models
import project_template.forms as forms
from project_template.task_templates import DigitalizationTask, CountTableRowsTask

#@register()
class TaskGetInitialInformation(DigitalizationTask):
    task_form = forms.TranscribeInitialInformation
    template_name = 'tasks/general_information_task.html'

    def save_verified_data(self, verified_data):
        politician, created = models.Politician.objects.get_or_create(
            name=verified_data['name'],
            surname=verified_data['surname'],
            position=verified_data['position']
        )

        politician.add_position(verified_data['position'])

        income_declaration, created = models.IncomeDeclaration.objects.get_or_create(
            url=self.url,
            politician=politician,
            date=verified_data['date']
        )


#@register()
class TaskOwnedGoodsOrServicesPerSpouse(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerSpouse
    storage_model = models.OwnedGoodsOrServicesPerSpouseTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskTranscribeOwnedInvestmentsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedInvestmentsTable
    storage_model = models.OwnedInvestmentsTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskTranscribeOwnedIncomeFromOtherSourcesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromOtherSourcesTable
    storage_model = models.OwnedIncomeFromOtherSourcesTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskOwnedJewelry(CountTableRowsTask):
    task_form = forms.TranscribeOwnedJewelry
    storage_model = models.OwnedJewelryTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskOwnedAutomobile(CountTableRowsTask):
    task_form = forms.TranscribeOwnedAutomobile
    storage_model = models.OwnedAutomobileTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskTranscribeOwnedIncomeFromDeferredUseOfGoods(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromDeferredUseOfGoods
    storage_model = models.OwnedIncomeFromDeferredUseOfGoodsTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskTranscribeIndependentActivities(CountTableRowsTask):
    task_form = forms.TranscribeIndependentActivities
    storage_model = models.OwnedIncomeFromIndependentActivitiesTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskOwnedIncomeFromGamblingTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromGamblingTable
    storage_model = models.OwnedIncomeFromGamblingTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskOwnedIncomeFromAgriculturalActivitiesTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromAgriculturalActivitiesTable
    storage_model = models.OwnedIncomeFromAgriculturalActivitiesTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskGetDebtsTableRowsCount(CountTableRowsTask):
    task_form = forms.TranscribeDebtsTableRowsCount
    storage_model = models.OwnedDebtsTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskOwnedIncomeFromSalariesCount(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromSalaries
    storage_model = models.OwnedIncomeFromSalariesTable
    # TODO - add child_class
    child_class = None


class TaskOwnedIncomeFromPensionsRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsSingleRowEntry
    template_name = "tasks/empty_template.html"

    def save_verified_data(self, verified_data):
        owned_income_from_pensions, created = models.OwnedIncomeFromPensionsTableEntry.objects.get_or_create(
            address_source_of_goods="Judet: {}, Localitate: {}, Comuna: {}".format(verified_data['county'], verified_data['town'], verified_data['village']),
            income_provider="Nume: {}, Prenume: {}".format(verified_data['owner_surname'], verified_data['owner_name']),
            name_source_of_goods=verified_data['name_source_of_goods'],
            goods_name=verified_data['goods_name'],
            annual_income=verified_data['annual_income'],
            annual_income_currency=verified_data['annual_income_currency']
        )
        

@register()
class TaskOwnedIncomeFromPensionsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedIncomeFromPensionsTable
    storage_model = models.OwnedIncomeFromPensionsTable
    # TODO - add child_class
    child_class = TaskOwnedIncomeFromPensionsRowEntry


#@register()
class TaskOwnedGoodsOrServicesPerChildTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerChildTable
    storage_model = models.OwnedGoodsOrServicesPerChildTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskOwnedGoodsOrServicesPerOwnerTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedGoodsOrServicesPerOwnerTable
    storage_model = models.OwnedGoodsOrServicesPerOwnerTable
    # TODO - add child_class
    child_class = None


class TaskOwnedLandRowEntry(DigitalizationTask):
    task_form = forms.TranscribeOwnedLandSingleRowEntry
    template_name = "tasks/owned_land.html"

    def save_verified_data(self, verified_data):
        owned_land, created = models.OwnedLandTableEntry.objects.get_or_create(
            address="Judet: {}, Localitate: {}, Comuna: {}".format(verified_data['county'], verified_data['town'], verified_data['village']),
            category=verified_data['category'],
            acquisition_year=verified_data['acquisition_year'],
            surface=verified_data['area'],
            share_ratio=verified_data['share'],
            attainment_type=verified_data['acquisition_mode'],
            owner="{} {}".format(verified_data['owner_surname'], verified_data['owner_name']),
            observations=""
        )


#@register()
class TaskOwnedLandTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedLandTable
    storage_model = models.OwnedLandTable
    child_class = TaskOwnedLandRowEntry


#@register()
class TaskOwnedBuildingsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBuildingsTable
    storage_model = models.OwnedBuildingsTable
    # TODO - add child_class
    child_class = None


#@register()
class TaskOwnedBankAccountsTable(CountTableRowsTask):
    task_form = forms.TranscribeOwnedBankAccountsTable
    storage_model = models.OwnedBankAccountsTable
    # TODO - add child_class
    child_class = None
