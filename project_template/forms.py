from django import forms
from django.utils.translation import ugettext_lazy as _

from project_template import constants
from project_template.datamodels.real_estate_type import RealEstateType
from project_template.datamodels.attainment_type import AttainmentType

YEAR_CHOICES = ('2008', '2009', '2010', '2011', '2012', '2013',
                '2014', '2015', '2016', '2017', '2018', '2019')


def get_table_of_contents():
    return {"buildings": 1, "automobiles": 1, "jewelry": 2, "bank_accounts": 2, "investments": 2, "land": 1, "debts": 3, "goods": 3, "gifts_spouse": 3, "gifts_kids": 3, "salaries": 4, "independent_activities": 4, "income_investments": 4, "pensions": 4, "agriculture": 4, "other_sources": 5}


table_of_contents = get_table_of_contents()


class TranscribeInitialInformation(forms.Form):
    name = forms.CharField(
        label=_("What is the name of the current politician?"))
    surname = forms.CharField(
        label=_("What is the surname of the current politician?"))
    position = forms.CharField(
        label=_("What is the position of the current politician?"))
    date = forms.DateField(label=_("Date"), widget=forms.SelectDateWidget(
        years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])


class TranscribeDebtsTableRowsCount(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['debts'], table_of_contents['debts']))


class TranscribeOwnedGoodsOrServicesPerSpouse(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['gifts_spouse'], table_of_contents['debts']))


class TranscribeOwnedIncomeFromOtherSourcesTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['other_sources'], table_of_contents['debts']))


class TranscribeOwnedInvestmentsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['bank_accounts'], table_of_contents['debts']))


class TranscribeOwnedJewelry(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['jewelry'], table_of_contents['debts']))


class TranscribeOwnedAutomobile(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['automobiles'], table_of_contents['debts']))


class TranscribeOwnedIncomeFromSalaries(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['salaries'], table_of_contents['debts']))


class TranscribeOwnedIncomeFromGamblingTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['gambling'], table_of_contents['debts']))


class TranscribeOwnedIncomeFromAgriculturalActivitiesTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['agriculture'], table_of_contents['debts']))


class TranscribeIndependentActivities(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['independent_activities'], table_of_contents['debts']))


class TranscribeOwnedIncomeFromDeferredUseOfGoods(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['deferred_use'], table_of_contents['debts']))


class TranscribeOwnedIncomeFromPensionsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['pensions'], table_of_contents['debts']))


class TranscribeOwnedIncomeFromInvestmentsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['income_investments'], table_of_contents['debts']))


class TranscribeOwnedGoodsOrServicesPerChildTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['gifts_kids'], table_of_contents['debts']))


class TranscribeOwnedGoodsOrServicesPerOwnerTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['goods'], table_of_contents['debts']))


class TranscribeOwnedLandTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['land'], table_of_contents['debts']))


class TranscribeOwnedBuildingsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['buildings'], table_of_contents['debts']))


class TranscribeOwnedBankAccountsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {0} on page {1}?".format(
        constants.DECLARATION_TABLES['bank_accounts'], table_of_contents['debts']))


class TranscribeOwnedLandSingleRowEntry(forms.Form):
    judet = forms.CharField(
        label="Care este judetul in care se gaseste terenul detinut?")
    localitate = forms.CharField(
        label="Care este localitatea in care se gaseste terenul detinut?")
    comuna = forms.CharField(
        label="Care este comuna in care se gaseste terenul detinut?")
    categorie = forms.ChoiceField(
        label="Care este categoria de teren?", choices=RealEstateType.return_as_iterable())
    an_dobandire = forms.DateField(label="Care este anul cand terenul a fost dobandit?",
                                   widget=forms.SelectDateWidget(years=YEAR_CHOICES), input_formats=['%Y-%m-%d'])
    mod_dobandire = forms.ChoiceField(
        label="Care este modul in care terenul a fost dobandit?", choices=AttainmentType.return_as_iterable())
    suprafata = forms.CharField(label="Care este suprafata terenului? (mp)")
    cota_parte = forms.IntegerField(
        label="Care este cota parte din acest teren? (in procente)", max_value=100, min_value=0)
    nume_proprietar = forms.CharField(label="Care este numele proprietarului?")
    prenume_proprietar = forms.CharField(
        label="Care este prenumele proprietarului")
