#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyslicer.exceptions as exceptions

from collections import defaultdict


__mapped_errors = {
    # Authentication and Authorization errors (10 - 19)
    10: exceptions.AuthMissingHeaderException,
    11: exceptions.AuthAPIKeyException,
    12: exceptions.AuthInvalidAPIKeyException,
    13: exceptions.AuthIncorrectPermissionException,
    14: exceptions.AuthInvalidRemoteException,
    16: exceptions.CustomKeyInvalidPermissionForFieldException,
    17: exceptions.CustomKeyInvalidOperationException,
    18: exceptions.CustomKeyNotPermittedException,
    19: exceptions.CustomKeyRouteNotPermittedException,
    # Request validations (20 - 29)
    21: exceptions.RequestMissingContentTypeException,
    22: exceptions.RequestIncorrectContentTypeValueException,
    23: exceptions.RequestRateLimitException,
    24: exceptions.RequestInvalidJsonException,
    # Account Errors (30 - 39)
    30: exceptions.AccountMissingPaymentMethodException,
    31: exceptions.AccountPaymentRequiredException,
    32: exceptions.AccountBannedException,
    33: exceptions.AccountDisabledException,
    # Field errors (40 - 59)
    40: exceptions.FieldMissingParamException,
    41: exceptions.FieldTypeException,
    42: exceptions.FieldIntegerValuesException,
    43: exceptions.FieldAlreadyExistsException,
    44: exceptions.FieldLimitException,
    45: exceptions.FieldTimeSeriesLimitException,
    46: exceptions.FieldTimeSeriesSystemLimitException,
    47: exceptions.FieldDecimalTypeException,
    48: exceptions.FieldStorageValueException,
    49: exceptions.FieldInvalidApiNameException,
    50: exceptions.FieldInvalidNameException,
    51: exceptions.FieldInvalidDescriptionException,
    53: exceptions.FieldInvalidCardinalityException,
    54: exceptions.FieldDecimalLimitException,
    55: exceptions.FieldRangeLimitException,
    # Index errors (60 - 79)
    60: exceptions.IndexEntityKeyTypeException,
    61: exceptions.IndexEntityValueTypeException,
    62: exceptions.IndexFieldNameTypeException,
    63: exceptions.IndexFieldTypeException,
    64: exceptions.IndexEntityNameTooBigException,
    65: exceptions.IndexFieldValueTooBigException,
    66: exceptions.IndexDateFormatException,
    67: exceptions.IndexFieldNotActiveException,
    68: exceptions.IndexIdLimitException,
    69: exceptions.IndexFieldLimitException,
    71: exceptions.IndexFieldStringEmptyValueException,
    72: exceptions.IndexFieldTimeseriesInvalidParameterException,
    73: exceptions.IndexFieldNumericInvalidValueException,
    74: exceptions.IndexFieldTimeseriesMissingValueException,
    75: exceptions.QueryTimeSeriesInvalidPrecisionSecondsException,
    76: exceptions.QueryTimeSeriesInvalidPrecisionMinutesException,
    77: exceptions.QueryTimeSeriesInvalidPrecisionHoursException,
    # Query errors (80 - 109)
    80: exceptions.QueryMissingQueryException,
    81: exceptions.QueryInvalidTypeException,
    82: exceptions.QueryMissingTypeParamException,
    83: exceptions.QueryInvalidOperatorException,
    84: exceptions.QueryIncorrectOperatorUsageException,
    85: exceptions.QueryFieldNotActiveException,
    86: exceptions.QueryMissingOperatorException,
    87: exceptions.QueryIncompleteException,
    88: exceptions.QueryEventCountQueryException,
    89: exceptions.QueryDateFormatException,
    90: exceptions.QueryIntegerException,
    91: exceptions.QueryFieldLimitException,
    92: exceptions.QueryLevelLimitException,
    93: exceptions.QueryBadAggsFormationException,
    94: exceptions.QueryInvalidAggFilterException,
    95: exceptions.QueryMetricsLevelException,
    96: exceptions.QueryTimeSeriesException,
    97: exceptions.QueryMetricsTypeException,
    98: exceptions.QueryContainsNumericException,
    99: exceptions.QueryExistsEntityLimitException,
    100: exceptions.QueryMultipleFiltersException,
    101: exceptions.QueryContainsValueTypeException,
    102: exceptions.QueryMissingNameParamException,
    103: exceptions.QuerySavedAlreadyExistsException,
    104: exceptions.QuerySavedNotExistsException,
    105: exceptions.QuerySavedInvalidTypeException,
    106: exceptions.MethodNotAllowedException,
    107: exceptions.QueryExistsMissingIdsException,
    108: exceptions.QueryInvalidFormatException,
    109: exceptions.QueryTopValuesParameterEmptyException,
    110: exceptions.QueryDataExtractionLimitValueException,
    111: exceptions.QueryDataExtractionLimitValueTooBigException,
    112: exceptions.QueryDataExtractionLimitAndPageTokenValueException,
    113: exceptions.QueryDataExtractionPageTokenValueException,
    114: exceptions.QueryDataExtractionFieldLimitException,
    115: exceptions.QueryExistsEntityEmptyException,
    116: exceptions.QuerySavedInvalidQueryValueException,
    117: exceptions.QuerySavedInvalidCachePeriodValueException,
    118: exceptions.QuerySavedInvalidNameException,
    119: exceptions.QueryCountInvalidParameterException,
    120: exceptions.QueryAggregationInvalidParameterException,
    121: exceptions.QueryAggregationInvalidFilterQueryException,
    # Internal errors (110 - 120)
    130: exceptions.InternalException,
    131: exceptions.FieldCreateInternalException
}

slicer_exceptions = defaultdict(
    lambda: exceptions.SlicingDiceException,
    __mapped_errors
)