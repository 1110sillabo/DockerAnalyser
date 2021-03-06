/**
 * Global utilities.
 * @module common/utilities
 */

 /**
 * Checks with a reguarl expression if a string rappresents a date in ISO 8601 format
 * @see {@link https://www.regextester.com/97766}
 * @param {string} str the string you want to check
 */
export function is_date(str) {
    return str.match(/^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(.[0-9]+)?(Z)?$/);
}