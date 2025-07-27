rule auto_rule_20250726130921_0440 {
  strings:
    $o0 = "bPrevious" wide ascii nocase
    $o1 = "hsz2" wide ascii nocase
    $o2 = "cbOff" wide ascii nocase
  condition:
    3 of ($o*)
}