rule auto_rule_20250726090717_4295 {
  strings:
    $o0 = "nProgram" wide ascii nocase
    $o1 = "dword_40B020" wide ascii nocase
    $o2 = "dword_410E0C" wide ascii nocase
    $o3 = "tMIXERCONTROLDETAILS" wide ascii nocase
    $o4 = "main_loop_1" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726090720_9577 {
  strings:
    $o0 = "_IncMan" wide ascii nocase
    $o1 = "_CopyMan" wide ascii nocase
    $o2 = "dword_4105C4" wide ascii nocase
    $o3 = "x_ismbbtype" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726090723_3432 {
  condition:
    auto_rule_20250726090717_4295 or auto_rule_20250726090720_9577
}