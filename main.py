def prediction_loop(label_df: pd.DataFrame, vertex_issue_prompt: str, text_col: List[str], json_output_path: Path) -> List[dict]:
    output_json_list = read_existing_json(json_output_path)
    existing_issue_ids = {item['issue_id'] for item in output_json_list}

    # Use the LLM generator
    llm_generator = get_llm()

    for i, row in label_df.iterrows():
        issue_id = row['issue_id']  # Adjust according to your DataFrame structure
        if issue_id in existing_issue_ids:
            continue  # Skip already processed issues

        text = row[text_col].to_dict()
        json_str = json.dumps(text, indent=4)  # Convert context to JSON string
        cooked_prompt = vertex_issue_prompt.format(issue_text=json_str)

        # Generate content with retry strategy
        try:
            llm = next(llm_generator)  # Get the LLM instance from the generator
            result_text = generate_content_with_retry(cooked_prompt)
            result_json = extract_json(result_text)  # Assuming this function is defined

            result_json.update({'issue_id': issue_id, 'issue_name': row['issue_name']})  # Add issue id and name
            output_json_list.append(result_json)

            # Save after each iteration
            save_json_output(json_output_path, output_json_list)

        except Exception as e:
            print(f"An error occurred while processing issue {issue_id}: {e}")

    return output_json_list
