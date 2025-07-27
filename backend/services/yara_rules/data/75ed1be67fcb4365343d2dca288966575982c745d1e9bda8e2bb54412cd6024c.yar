rule auto_rule_20250726091057_1494 {
  strings:
    $o0 = "EditStreamPaste" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
  condition:
    all of them
}