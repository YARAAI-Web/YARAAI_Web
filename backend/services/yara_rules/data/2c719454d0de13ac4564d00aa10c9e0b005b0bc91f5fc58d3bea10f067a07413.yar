rule auto_rule_20250726110648_6532 {
  strings:
    $o0 = "lpNumberOfFreeClusters" wide ascii nocase
    $o1 = "dword_44E090" wide ascii nocase
  condition:
    all of them
}