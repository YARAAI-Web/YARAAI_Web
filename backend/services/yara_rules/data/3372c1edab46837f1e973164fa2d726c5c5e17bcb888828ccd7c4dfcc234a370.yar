rule auto_rule_20250726112331_9513 {
  strings:
    $o0 = "dword_446074" wide ascii nocase
    $o1 = "shadows" wide ascii nocase
  condition:
    all of them
}