rule auto_rule_20250726123547_0647 {
  strings:
    $o0 = "dword_1001EB30" wide ascii nocase
  condition:
    all of them
}