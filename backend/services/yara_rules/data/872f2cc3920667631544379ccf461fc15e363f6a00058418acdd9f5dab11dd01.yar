rule auto_rule_20250727043138_9900 {
  strings:
    $o0 = "_pyinstaller_pyz" wide ascii nocase
    $o1 = "Maximum" wide ascii nocase
    $o2 = "qword_140043F30" wide ascii nocase
  condition:
    3 of ($o*)
}