rule auto_rule_20250726105527_6524 {
  strings:
    $o0 = "lpCollectDataTimeout" wide ascii nocase
    $o1 = "x6EDB" wide ascii nocase
  condition:
    all of them
}