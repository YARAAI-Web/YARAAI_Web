rule auto_rule_20250727004644_2150 {
  strings:
    $o0 = "dword_455A14" wide ascii nocase
    $o1 = "__crtGetEnvironmentStringsA" wide ascii nocase
  condition:
    all of them
}