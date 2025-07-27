rule auto_rule_20250726224412_1442 {
  strings:
    $o0 = "dwInfoType" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "GetStringTypeW" wide ascii nocase
    $o3 = "GetActiveWindow_0" wide ascii nocase
    $o4 = "dword_45CF44" wide ascii nocase
  condition:
    5 of ($o*)
}