rule auto_rule_20250726171729_3652 {
  strings:
    $o0 = "xcptlookup" wide ascii nocase
    $o1 = "dword_40BCA4" wide ascii nocase
    $o2 = "LoadBitmapA" wide ascii nocase
    $o3 = "_cinit" wide ascii nocase
    $o4 = "_nh_malloc" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726171732_7445 {
  strings:
    $o0 = "LibraryA" wide ascii nocase
    $o1 = "byte_40B688" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726171743_3872 {
  condition:
    auto_rule_20250726171729_3652 or auto_rule_20250726171732_7445
}