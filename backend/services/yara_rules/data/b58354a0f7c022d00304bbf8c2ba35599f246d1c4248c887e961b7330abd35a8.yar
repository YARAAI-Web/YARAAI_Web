rule auto_rule_20250726094818_6108 {
  strings:
    $o0 = "byte_467B9C" wide ascii nocase
    $o1 = "Detected" wide ascii nocase
    $o2 = "dword_467CB4" wide ascii nocase
  condition:
    3 of ($o*)
}