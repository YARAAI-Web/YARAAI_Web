rule auto_rule_20250726160845_3072 {
  strings:
    $o0 = "SHEmptyRecycleBinW" wide ascii nocase
    $o1 = "lprcDst" wide ascii nocase
    $o2 = "puiLo" wide ascii nocase
    $o3 = "lpCC" wide ascii nocase
  condition:
    4 of ($o*)
}