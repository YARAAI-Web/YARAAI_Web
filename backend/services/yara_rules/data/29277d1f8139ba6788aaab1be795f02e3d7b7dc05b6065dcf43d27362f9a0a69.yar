rule auto_rule_20250726094015_9433 {
  strings:
    $o0 = "_fltout" wide ascii nocase
    $o1 = "x40108C" wide ascii nocase
    $o2 = "GetStringTypeW" wide ascii nocase
    $o3 = "_cfltcvt" wide ascii nocase
  condition:
    4 of ($o*)
}