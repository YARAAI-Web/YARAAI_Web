rule auto_rule_20250727013518_8612 {
  strings:
    $o0 = "dword_418F90" wide ascii nocase
    $o1 = "nProgram" wide ascii nocase
  condition:
    all of them
}