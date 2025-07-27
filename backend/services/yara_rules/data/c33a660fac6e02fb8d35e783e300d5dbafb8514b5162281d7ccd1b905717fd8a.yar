rule auto_rule_20250727033712_8690 {
  strings:
    $o0 = "__castguard_check_failure_user_handled_wrapper" wide ascii nocase
  condition:
    all of them
}