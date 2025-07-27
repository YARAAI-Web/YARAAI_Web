rule auto_rule_20250726170745_4072 {
  strings:
    $o0 = "dword_640303E8" wide ascii nocase
    $o1 = "dword_6402E98C" wide ascii nocase
    $o2 = "dword_6402E994" wide ascii nocase
  condition:
    3 of ($o*)
}