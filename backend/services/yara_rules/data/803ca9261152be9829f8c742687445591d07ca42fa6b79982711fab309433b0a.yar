rule auto_rule_20250726062057_2705 {
  strings:
    $o0 = "__crtExitProcess" wide ascii nocase
    $o1 = "dword_46ED30" wide ascii nocase
    $o2 = "_c_exit" wide ascii nocase
    $o3 = "__sbh_alloc_new_group" wide ascii nocase
    $o4 = "_heap_alloc" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726062100_4342 {
  strings:
    $o0 = "dwInfoType" wide ascii nocase
    $o1 = "byte_46ED61" wide ascii nocase
    $o2 = "dword_46E008" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726062110_8935 {
  condition:
    auto_rule_20250726062057_2705 or auto_rule_20250726062100_4342
}