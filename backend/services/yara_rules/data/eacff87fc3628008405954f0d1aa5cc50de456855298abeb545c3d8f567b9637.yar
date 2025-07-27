rule auto_rule_20250726142641_1294 {
  strings:
    $o0 = "flProtect" wide ascii nocase
    $o1 = "chCount" wide ascii nocase
    $o2 = "uIDNewItem" wide ascii nocase
    $o3 = "uCommand" wide ascii nocase
    $o4 = "fInherit" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726142644_8377 {
  strings:
    $o0 = "uCode" wide ascii nocase
    $o1 = "VkKeyScanExW" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726142652_1049 {
  condition:
    auto_rule_20250726142641_1294 or auto_rule_20250726142644_8377
}