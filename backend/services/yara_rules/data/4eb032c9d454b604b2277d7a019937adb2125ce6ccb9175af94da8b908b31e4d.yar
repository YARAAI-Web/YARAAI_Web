rule auto_rule_20250726214926_3387 {
  strings:
    $o0 = "stru_14004B790" wide ascii nocase
  condition:
    all of them
}