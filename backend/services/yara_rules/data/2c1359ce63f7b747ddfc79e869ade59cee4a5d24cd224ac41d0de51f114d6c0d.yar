rule auto_rule_20250727012122_5206 {
  strings:
    $o0 = "dword_449ED4" wide ascii nocase
    $o1 = "xcptlookup" wide ascii nocase
  condition:
    all of them
}