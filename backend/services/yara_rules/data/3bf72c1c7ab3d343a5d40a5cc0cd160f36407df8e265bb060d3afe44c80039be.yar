rule auto_rule_20250726103558_8897 {
  strings:
    $o0 = "GetLastActivePopup_0" wide ascii nocase
    $o1 = "x80000u" wide ascii nocase
    $o2 = "dword_464018" wide ascii nocase
  condition:
    3 of ($o*)
}