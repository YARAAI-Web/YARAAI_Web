rule auto_rule_20250726195210_3847 {
  strings:
    $o0 = "byte_401E59" wide ascii nocase
  condition:
    all of them
}