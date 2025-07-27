rule auto_rule_20250726122845_7191 {
  strings:
    $o0 = "dword_424004" wide ascii nocase
    $o1 = "dword_427E34" wide ascii nocase
    $o2 = "byte_427FA1" wide ascii nocase
    $o3 = "strncnt" wide ascii nocase
    $o4 = "__shl_12" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726122849_3839 {
  strings:
    $o0 = "UnwindUp4_0" wide ascii nocase
    $o1 = "_ctype" wide ascii nocase
    $o2 = "off_427524" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726122854_8317 {
  condition:
    auto_rule_20250726122845_7191 or auto_rule_20250726122849_3839
}