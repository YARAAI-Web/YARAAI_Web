rule auto_rule_20250726101937_7126 {
  strings:
    $o0 = "a1system32Cscri_0" wide ascii nocase
    $o1 = "lpOverlapped" wide ascii nocase
    $o2 = "ScrollWindow" wide ascii nocase
  condition:
    3 of ($o*)
}