rule auto_rule_20250726124217_5126 {
  strings:
    $o0 = "pptSrc" wide ascii nocase
    $o1 = "lpNextSize" wide ascii nocase
  condition:
    all of them
}