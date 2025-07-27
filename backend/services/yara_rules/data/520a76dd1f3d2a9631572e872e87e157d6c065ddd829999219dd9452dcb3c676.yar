rule auto_rule_20250726131854_6224 {
  strings:
    $o0 = "cause" wide ascii nocase
    $o1 = "_filbuf" wide ascii nocase
    $o2 = "fill_with_EOS_dwords" wide ascii nocase
    $o3 = "_set_errno" wide ascii nocase
    $o4 = "off_446CFC" wide ascii nocase
  condition:
    5 of ($o*)
}