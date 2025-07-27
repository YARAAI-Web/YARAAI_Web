rule auto_rule_20250727012827_0440 {
  strings:
    $o0 = "write_char" wide ascii nocase
    $o1 = "dbgheap" wide ascii nocase
    $o2 = "dword_446ED4" wide ascii nocase
    $o3 = "dword_4482C4" wide ascii nocase
    $o4 = "dword_446D78" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727012830_5591 {
  strings:
    $o0 = "_calloc_dbg" wide ascii nocase
    $o1 = "dword_446F54" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727012834_4349 {
  condition:
    auto_rule_20250727012827_0440 or auto_rule_20250727012830_5591
}