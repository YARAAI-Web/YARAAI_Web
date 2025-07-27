rule auto_rule_20250726143115_8128 {
  strings:
    $o0 = "_free_osfhnd" wide ascii nocase
    $o1 = "dword_467CB4" wide ascii nocase
    $o2 = "_seh_longjmp_unwind" wide ascii nocase
    $o3 = "assertion" wide ascii nocase
    $o4 = "_CrtDbgReport" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726143116_7457 {
  strings:
    $o0 = "dword_468D7C" wide ascii nocase
    $o1 = "_isctype" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726143120_5539 {
  condition:
    auto_rule_20250726143115_8128 or auto_rule_20250726143116_7457
}