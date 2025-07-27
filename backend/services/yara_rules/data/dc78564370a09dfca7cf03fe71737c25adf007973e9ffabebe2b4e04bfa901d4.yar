rule auto_rule_20250726235518_0557 {
  strings:
    $o0 = "Handler" wide ascii nocase
    $o1 = "dword_46C1A4" wide ascii nocase
  condition:
    all of them
}