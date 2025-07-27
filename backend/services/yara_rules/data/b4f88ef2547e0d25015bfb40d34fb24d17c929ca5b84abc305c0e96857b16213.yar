rule auto_rule_20250727023037_7143 {
  strings:
    $o0 = "GetTextMetricsW" wide ascii nocase
    $o1 = "nResult" wide ascii nocase
    $o2 = "x17000u" wide ascii nocase
  condition:
    3 of ($o*)
}