function Error(msg, obj) {
    alert(msg); obj.focus(); obj.select(); return false;
}
function Focus(obj) {
    obj.focus(); obj.select();
}
function GetValue(obj) {
    return obj.value.replace(/\s/g, '');
}
function IsEmpty(obj) {
	return GetValue(obj).length == 0;
}
function IsInRange(obj, low, high, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	return (parseInt(str) >= low) && (parseInt(str) <= high);
}
function IsValidMAC(obj, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	return str.search(/^[0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){5}$/) >= 0;
}
function IsValidIP(obj, zero) {
	var str = GetValue(obj);
	if (zero && str.length == 0) {
		return true;
	}
	var fields = str.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/);
	if (fields != null) {
		var tmp = fields[1] | fields[2] | fields[3] | fields[4];
		return (tmp < 256) && (zero || tmp > 0);
	} else {
		return false;
	}
}
function IsValidPort(obj, empty) {
	var str = GetValue(obj);
	if (empty && str.length == 0) return true;
	var value = parseInt(str);
	return (value > 0) && (value < 65536);
}


