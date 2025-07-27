rule auto_rule_20250727012414_4315 {
  strings:
    $o0 = "dword_4605E0" wide ascii nocase
    $o1 = "_commit" wide ascii nocase
    $o2 = "nProgram" wide ascii nocase
    $o3 = "main_loop_entrance" wide ascii nocase
    $o4 = "__sbh_alloc_new_region" wide ascii nocase
  condition:
    5 of ($o*)
}