rule auto_rule_20250726180728_5781 {
  strings:
    $o0 = "dword_464298" wide ascii nocase
    $o1 = "get_int64_arg" wide ascii nocase
    $o2 = "word_465490" wide ascii nocase
    $o3 = "MbCh" wide ascii nocase
    $o4 = "_heap_alloc_dbg" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726180731_5653 {
  strings:
    $o0 = "_CrtMemCheckpoint" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726180735_4673 {
  condition:
    auto_rule_20250726180728_5781 or auto_rule_20250726180731_5653
}