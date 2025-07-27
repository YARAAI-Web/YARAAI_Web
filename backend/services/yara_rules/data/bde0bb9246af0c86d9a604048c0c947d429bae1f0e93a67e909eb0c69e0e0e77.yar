rule auto_rule_20250726113629_8866 {
  strings:
    $o0 = "GetStringTypeA" wide ascii nocase
    $o1 = "Press" wide ascii nocase
    $o2 = "pUserData" wide ascii nocase
  condition:
    3 of ($o*)
}