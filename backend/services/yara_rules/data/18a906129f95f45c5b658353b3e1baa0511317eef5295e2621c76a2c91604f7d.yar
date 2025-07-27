rule auto_rule_20250726113503_8609 {
  strings:
    $o0 = "PathCommonPrefixA" wide ascii nocase
    $o1 = "PathFileExistsA" wide ascii nocase
  condition:
    all of them
}