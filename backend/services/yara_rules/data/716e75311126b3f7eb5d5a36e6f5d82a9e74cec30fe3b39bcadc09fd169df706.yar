rule auto_rule_20250726202243_8574 {
  strings:
    $o0 = "VirtualAllocEx" wide ascii nocase
    $o1 = "lpWndClass" wide ascii nocase
    $o2 = "nBar" wide ascii nocase
    $o3 = "SetUserObjectInformationW" wide ascii nocase
  condition:
    4 of ($o*)
}