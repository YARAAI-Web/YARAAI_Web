rule auto_rule_20250726110337_3694 {
  strings:
    $o0 = "report_failure" wide ascii nocase
    $o1 = "x_ismbbtype" wide ascii nocase
    $o2 = "dword_44C624" wide ascii nocase
    $o3 = "main_loop_2" wide ascii nocase
    $o4 = "x41C4u" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726110340_5669 {
  strings:
    $o0 = "dword_418018" wide ascii nocase
    $o1 = "dword_44BE94" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726110348_1796 {
  condition:
    auto_rule_20250726110337_3694 or auto_rule_20250726110340_5669
}