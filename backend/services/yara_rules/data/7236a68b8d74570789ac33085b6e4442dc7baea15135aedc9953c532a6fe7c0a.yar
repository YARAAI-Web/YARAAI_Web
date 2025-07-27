rule auto_rule_20250726200829_7126 {
  strings:
    $o0 = "dwInfoType" wide ascii nocase
    $o1 = "off_45C58C" wide ascii nocase
    $o2 = "dword_45C440" wide ascii nocase
  condition:
    3 of ($o*)
}