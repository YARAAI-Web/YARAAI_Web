rule auto_rule_20250726174518_9775 {
  strings:
    $o0 = "dword_44BEA4" wide ascii nocase
    $o1 = "dword_44C520" wide ascii nocase
  condition:
    all of them
}