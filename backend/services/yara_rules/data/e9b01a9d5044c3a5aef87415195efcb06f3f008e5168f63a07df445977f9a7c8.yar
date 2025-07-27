rule auto_rule_20250727013415_2627 {
  strings:
    $o0 = "nProgram" wide ascii nocase
    $o1 = "fill_with_EOS_dwords" wide ascii nocase
    $o2 = "dword_44A004" wide ascii nocase
    $o3 = "dword_449EC0" wide ascii nocase
    $o4 = "__crtMessageBoxA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727013418_4275 {
  strings:
    $o0 = "byte_449B80" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727013422_5139 {
  condition:
    auto_rule_20250727013415_2627 or auto_rule_20250727013418_4275
}