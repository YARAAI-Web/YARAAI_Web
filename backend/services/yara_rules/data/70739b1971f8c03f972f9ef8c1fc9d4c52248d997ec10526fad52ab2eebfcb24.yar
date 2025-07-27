rule auto_rule_20250726113729_8824 {
  strings:
    $o0 = "xF89C853D" wide ascii nocase
    $o1 = "x89BC" wide ascii nocase
    $o2 = "BinaryType" wide ascii nocase
    $o3 = "x1CAE" wide ascii nocase
  condition:
    4 of ($o*)
}