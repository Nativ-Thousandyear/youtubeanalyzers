 import streamlit as st
import pandas as pd
import requests

# Streamlit code setup
st.title("YouTube Analytics")

# Load the data
file_url = "https://github.com/Nativ-Thousandyear/youtubeanalyzers/blob/main/YoutubeAnalyzer.csv"
try:
    videos = pd.read_csv(file_url)
    st.write(videos.head())  # Display first few rows
except Exception as e:
    st.error(f"Error loading the CSV: {e}")

# Further Streamlit processing and UI components go here

[
  {
    "{": "" ""cells"": [""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""initial_id""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:07:42.354731Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:07:42.343282Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# Import needed libraries\n""""
  },
  {
    "{": ""    ""import pandas as pd\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""### This is for loading the data\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# The crawl dataset we are using do not have column names or headings so we need to handle that\n""""
  },
  {
    "{": ""    ""column_names = ['videoID'""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Load YouTube data for each depth file(we have 4 depths in total starting from 0)\n""""
  },
  {
    "{": ""    ""def load_depth(path""
  },
  {
    "{": ""    ""    # Initialize a list to store the valid rows\n""""
  },
  {
    "{": ""    ""    valid_rows = []\n""""
  },
  {
    "{": ""    ""    # Read our dataset line by line\n""""
  },
  {
    "{": ""    ""    # We were using pandas to load/read data at first but there were errors when the 1st row only has 1 or 2 column and pandas were assuming that's all the columns we have (inconsistent)\n""""
  },
  {
    "{": ""    ""    # so we decided to go with this route instead and it works\n""""
  },
  {
    "{": ""    ""    with open(path""
  },
  {
    "{": ""    ""        for line in file:\n""""
  },
  {
    "{": ""    ""            # Split the line by tab and check if it has at least 2 columns\n""""
  },
  {
    "{": ""    ""            # Some rows might have only 1 or 2 columns which is not useful for us""
  },
  {
    "{": ""    ""            # this way it helps with fixing the issues with some rows having only 1 column as well\n""""
  },
  {
    "{": ""    ""            split_line = line.strip().split('\\t')\n""""
  },
  {
    "{": ""    ""            if len(split_line) >= 2:\n""""
  },
  {
    "{": ""    ""                valid_rows.append(split_line)       \n""""
  },
  {
    "{": ""    ""    # Convert the list into pandas dataframe\n""""
  },
  {
    "{": ""    ""    depth_data = pd.DataFrame(valid_rows)\n""""
  },
  {
    "{": ""    ""    depth_data['crawl_date'] = crawl_date\n""""
  },
  {
    "{": ""    ""    depth_data['depth'] = depth\n""""
  },
  {
    "{": ""    ""    return depth_data\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Load all depth files for a single crawl\n""""
  },
  {
    "{": ""    ""def load_crawl(path""
  },
  {
    "{": ""    ""    # Load depth file 0""
  },
  {
    "{": ""    ""    depth_files = [f\""{path}/{i}.txt\"" for i in range(4)]\n""""
  },
  {
    "{": ""    ""    depth_dframe = []\n""""
  },
  {
    "{": ""    ""    # Loop through the total depth files and add the dataframe to depth_dframe list\n""""
  },
  {
    "{": ""    ""    for i""
  },
  {
    "{": ""    ""        depth_dframe.append(load_depth(depth_file""
  },
  {
    "{": ""    ""    # Now for each crawl""
  },
  {
    "{": ""    ""    combined_data = pd.concat(depth_dframe""
  },
  {
    "{": ""    ""    return combined_data""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": []""
  },
  {
    "{": ""   ""execution_count"": 6""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""b16f2c66de2967c8""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:07:42.414177Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:07:42.405901Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""### This is for cleaning and transformation the data (Data Preparation)\n""""
  },
  {
    "{": ""    ""def prepare_data(df):\n""""
  },
  {
    "{": ""    ""    # Since there may be more than 1 related ids""
  },
  {
    "{": ""    ""    combined_related_ids = []\n""""
  },
  {
    "{": ""    ""    # Loop over each row and combine the related IDs\n""""
  },
  {
    "{": ""    ""    for index""
  },
  {
    "{": ""    ""        # We select the related IDs columns (from the 10th column onward) \n""""
  },
  {
    "{": ""    ""        # The dataset description says the related IDs is up to 20 strings only \n""""
  },
  {
    "{": ""    ""        related_ids = row[9:29]  \n""""
  },
  {
    "{": ""    ""        # Join the cleaned related IDs into a single string separated by commas then add to the list\n""""
  },
  {
    "{": ""    ""        combined_related_ids.append('""
  },
  {
    "{": ""    ""    # Add the combined relatedIDs to the DataFrame\n""""
  },
  {
    "{": ""    ""    df['relatedIDs'] = combined_related_ids\n""""
  },
  {
    "{": ""    ""    # Keep only the first 9 columns plus the new combined 'relatedIDs' column\n""""
  },
  {
    "{": ""    ""    depth_data = df.iloc[:""
  },
  {
    "{": ""    ""    depth_data['relatedIDs'] = combined_related_ids \n""""
  },
  {
    "{": ""    ""    # Keep the crawl_date and depth column \n""""
  },
  {
    "{": ""    ""    depth_data[['crawl_date'""
  },
  {
    "{": ""    ""    # Add the column names to each column\n""""
  },
  {
    "{": ""    ""    depth_data.columns = column_names + ['crawl_date'""
  },
  {
    "{": ""    ""    # Remove the leading/trailing whitespace from string columns\n""""
  },
  {
    "{": ""    ""    depth_data['uploader'] = depth_data['uploader'].str.strip()\n""""
  },
  {
    "{": ""    ""    depth_data['category'] = depth_data['category'].str.strip()\n""""
  },
  {
    "{": ""    ""    # Convert these columns to numeric\n""""
  },
  {
    "{": ""    ""    numeric_columns = ['age'""
  },
  {
    "{": ""    ""    for col in numeric_columns:\n""""
  },
  {
    "{": ""    ""        depth_data[col] = pd.to_numeric(depth_data[col])   \n""""
  },
  {
    "{": ""    ""    # Fill in the missing 'rate' values with the mean of the column\n""""
  },
  {
    "{": ""    ""    depth_data['rate'] = depth_data['rate'].fillna(depth_data['rate'].mean())\n""""
  },
  {
    "{": ""    ""    return depth_data""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": []""
  },
  {
    "{": ""   ""execution_count"": 7""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""185e68b1be917648""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:08:48.536443Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:07:42.429192Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# testing = (load_depth(\""data/080331/2.txt\""""
  },
  {
    "{": ""    ""# clean = clean_data(testing)\n""""
  },
  {
    "{": ""    ""# print(clean)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Load all the crawls in the given dataset\n""""
  },
  {
    "{": ""    ""crawl1 = load_crawl('data/080327'""
  },
  {
    "{": ""    ""crawl2 = load_crawl('data/080329'""
  },
  {
    "{": ""    ""crawl3 = load_crawl('data/080331'""
  },
  {
    "{": ""    ""# Combine all crawls into a single dataframe\n""""
  },
  {
    "{": ""    ""combined_data = pd.concat([crawl1""
  },
  {
    "{": ""    ""# Prepare the data (clean & transform)\n""""
  },
  {
    "{": ""    ""combined_data = prepare_data(combined_data)\n""""
  },
  {
    "{": ""    ""print(combined_data.head())""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""       videoID           uploader   age         category  length   views  \\\n""""
  },
  {
    "{": ""      ""0  gFa1YMEJFag            sxephil  1135    Entertainment     270  101384   \n""""
  },
  {
    "{": ""      ""1  pSJ4hv28zaI  thecomputernerd01  1136           Comedy     216     458   \n""""
  },
  {
    "{": ""      ""2  uHVEDq6RVXc    barelypolitical  1134  News & Politics      56  555203   \n""""
  },
  {
    "{": ""      ""3  K7Om0QZy-38          SouljaBoy  1134            Music     185   91293   \n""""
  },
  {
    "{": ""      ""4  DCAO6bZa31o    AssociatedPress  1134  News & Politics      45  108095   \n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""   rate  ratings  comments                                         relatedIDs  \\\n""""
  },
  {
    "{": ""      ""0  4.72     3407      2887  QuRYeRnAuXM""
  },
  {
    "{": ""      ""1  4.80      133      2183  dh6dF1XY3uI""
  },
  {
    "{": ""      ""2  4.70     3574      2117  aYHBqH_xbCw""
  },
  {
    "{": ""      ""3  3.19     1063      1132  UCeA4K2-wNk""
  },
  {
    "{": ""      ""4  3.58      264      1069  5vLbA7n8EG0""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""   crawl_date  depth  \n""""
  },
  {
    "{": ""      ""0  2008-03-27      0  \n""""
  },
  {
    "{": ""      ""1  2008-03-27      0  \n""""
  },
  {
    "{": ""      ""2  2008-03-27      0  \n""""
  },
  {
    "{": ""      ""3  2008-03-27      0  \n""""
  },
  {
    "{": ""      ""4  2008-03-27      0  \n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 8""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""28e03963de74113b""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:09:32.441554Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:08:48.586961Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# Data ingestion and connection with MongoDB\n""""
  },
  {
    "{": ""    ""from pymongo import MongoClient\n""""
  },
  {
    "{": ""    ""# Connect to MongoDb database that we have created\n""""
  },
  {
    "{": ""    ""uri = 'mongodb://localhost:27017/'\n""""
  },
  {
    "{": ""    ""client = MongoClient(uri)\n""""
  },
  {
    "{": ""    ""db = client[\""youtubedb\""]\n""""
  },
  {
    "{": ""    ""collection = db[\""youtube_vids\""]\n""""
  },
  {
    "{": ""    ""# this prevents duplicate from running this section more than once\n""""
  },
  {
    "{": ""    ""collection.delete_many({})\n""""
  },
  {
    "{": ""    ""# Convert the DataFrame into a list of dictionaries\n""""
  },
  {
    "{": ""    ""insert_data = combined_data.to_dict('records')\n""""
  },
  {
    "{": ""    ""# Insert the data into the collection\n""""
  },
  {
    "{": ""    ""collection.insert_many(insert_data)""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""data"": {""
  },
  {
    "{": ""      ""text/plain"": [""
  },
  {
    "{": ""       ""InsertManyResult([ObjectId('6753a039f38132043599ccb5')""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""     }""
  },
  {
    "{": ""     ""execution_count"": 9""
  },
  {
    "{": ""     ""metadata"": {}""
  },
  {
    "{": ""     ""output_type"": ""execute_result""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 9""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""b1b431fb-5ac4-453b-a3e7-921701e09b87""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:09:34.160229Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:09:32.636622Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# Validation Queries\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Query 1: Validate Document Count\n""""
  },
  {
    "{": ""    ""document_count = collection.count_documents({})\n""""
  },
  {
    "{": ""    ""print(\""Total documents:\""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Query 2: Check Category Distribution\n""""
  },
  {
    "{": ""    ""category_counts = collection.aggregate([\n""""
  },
  {
    "{": ""    ""    { \""$group\"": { \""_id\"": \""$category\""""
  },
  {
    "{": ""    ""])\n""""
  },
  {
    "{": ""    ""print(\""Category distribution:\"")\n""""
  },
  {
    "{": ""    ""for category in category_counts:\n""""
  },
  {
    "{": ""    ""    print(category)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Query 3: Check Average and Max Views\n""""
  },
  {
    "{": ""    ""view_stats = collection.aggregate([\n""""
  },
  {
    "{": ""    ""    { \""$group\"": { \""_id\"": None""
  },
  {
    "{": ""    ""])\n""""
  },
  {
    "{": ""    ""print(\""View statistics:\"")\n""""
  },
  {
    "{": ""    ""for stats in view_stats:\n""""
  },
  {
    "{": ""    ""    print(stats)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Query 4: Validate Related IDs Format\n""""
  },
  {
    "{": ""    ""related_id_check = collection.find({\""relatedIDs\"": {\""$exists\"": True""
  },
  {
    "{": ""    ""print(\""Sample related IDs:\"")\n""""
  },
  {
    "{": ""    ""for doc in related_id_check:\n""""
  },
  {
    "{": ""    ""    print(doc['relatedIDs'])\n""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Total documents: 645731\n""""
  },
  {
    "{": ""      ""Category distribution:\n""""
  },
  {
    "{": ""      ""{'_id': 'Howto & Style'""
  },
  {
    "{": ""      ""{'_id': 'UNA'""
  },
  {
    "{": ""      ""{'_id': 'Comedy'""
  },
  {
    "{": ""      ""{'_id': 'Travel & Events'""
  },
  {
    "{": ""      ""{'_id': 'News & Politics'""
  },
  {
    "{": ""      ""{'_id': 'Entertainment'""
  },
  {
    "{": ""      ""{'_id': 'Nonprofits & Activism'""
  },
  {
    "{": ""      ""{'_id': 'Education'""
  },
  {
    "{": ""      ""{'_id': 'Pets & Animals'""
  },
  {
    "{": ""      ""{'_id': 'Music'""
  },
  {
    "{": ""      ""{'_id': 'Autos & Vehicles'""
  },
  {
    "{": ""      ""{'_id': 'Film & Animation'""
  },
  {
    "{": ""      ""{'_id': 'People & Blogs'""
  },
  {
    "{": ""      ""{'_id': 'Science & Technology'""
  },
  {
    "{": ""      ""{'_id': 'Sports'""
  },
  {
    "{": ""      ""View statistics:\n""""
  },
  {
    "{": ""      ""{'_id': None""
  },
  {
    "{": ""      ""Sample related IDs:\n""""
  },
  {
    "{": ""      ""QuRYeRnAuXM""
  },
  {
    "{": ""      ""dh6dF1XY3uI""
  },
  {
    "{": ""      ""aYHBqH_xbCw""
  },
  {
    "{": ""      ""UCeA4K2-wNk""
  },
  {
    "{": ""      ""5vLbA7n8EG0""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 10""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""4535ff3b-a8ed-4402-8d84-a42a18e194f0""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:04.467768Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:09:34.639521Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""import time\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Clear the collection to avoid duplicate entries\n""""
  },
  {
    "{": ""    ""collection.delete_many({})\n""""
  },
  {
    "{": ""    ""print(\""Collection cleared.\"")\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Start timer\n""""
  },
  {
    "{": ""    ""start_time = time.time()\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Ingest data (insert many records)\n""""
  },
  {
    "{": ""    ""collection.insert_many(insert_data)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# End timer\n""""
  },
  {
    "{": ""    ""end_time = time.time()\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Calculate and print ingestion time\n""""
  },
  {
    "{": ""    ""ingestion_time = end_time - start_time\n""""
  },
  {
    "{": ""    ""print(f\""Data ingestion took {ingestion_time:.2f} seconds\"")\n""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Collection cleared.\n""""
  },
  {
    "{": ""      ""Data ingestion took 15.06 seconds\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 11""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""b0a863e2-6488-4d10-a662-9a607141701d""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:04.854144Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:04.497206Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""import time\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Measure execution time for document count\n""""
  },
  {
    "{": ""    ""start_time = time.time()\n""""
  },
  {
    "{": ""    ""document_count = collection.count_documents({})\n""""
  },
  {
    "{": ""    ""end_time = time.time()\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Print results\n""""
  },
  {
    "{": ""    ""print(\""Total documents:\""""
  },
  {
    "{": ""    ""print(f\""Document count query took {end_time - start_time:.4f} seconds\"")\n""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Total documents: 645731\n""""
  },
  {
    "{": ""      ""Document count query took 0.3521 seconds\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 12""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""158889be-f784-46e1-a43f-c11ff8a84031""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:05.375655Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:04.888567Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# Measure execution time for category distribution query\n""""
  },
  {
    "{": ""    ""start_time = time.time()\n""""
  },
  {
    "{": ""    ""category_counts = collection.aggregate([\n""""
  },
  {
    "{": ""    ""    { \""$group\"": { \""_id\"": \""$category\""""
  },
  {
    "{": ""    ""])\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Collect results to ensure the query executes fully\n""""
  },
  {
    "{": ""    ""categories = list(category_counts)\n""""
  },
  {
    "{": ""    ""end_time = time.time()\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Print results and time\n""""
  },
  {
    "{": ""    ""print(\""Category distribution:\"")\n""""
  },
  {
    "{": ""    ""for category in categories:\n""""
  },
  {
    "{": ""    ""    print(category)\n""""
  },
  {
    "{": ""    ""print(f\""Category distribution query took {end_time - start_time:.4f} seconds\"")\n""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Category distribution:\n""""
  },
  {
    "{": ""      ""{'_id': 'Howto & Style'""
  },
  {
    "{": ""      ""{'_id': 'UNA'""
  },
  {
    "{": ""      ""{'_id': 'Comedy'""
  },
  {
    "{": ""      ""{'_id': 'Travel & Events'""
  },
  {
    "{": ""      ""{'_id': 'News & Politics'""
  },
  {
    "{": ""      ""{'_id': 'Entertainment'""
  },
  {
    "{": ""      ""{'_id': 'Nonprofits & Activism'""
  },
  {
    "{": ""      ""{'_id': 'Education'""
  },
  {
    "{": ""      ""{'_id': 'Pets & Animals'""
  },
  {
    "{": ""      ""{'_id': 'Music'""
  },
  {
    "{": ""      ""{'_id': 'Autos & Vehicles'""
  },
  {
    "{": ""      ""{'_id': 'Film & Animation'""
  },
  {
    "{": ""      ""{'_id': 'People & Blogs'""
  },
  {
    "{": ""      ""{'_id': 'Science & Technology'""
  },
  {
    "{": ""      ""{'_id': 'Sports'""
  },
  {
    "{": ""      ""Category distribution query took 0.4798 seconds\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 13""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""a7e1f2b4-3f7a-458a-9cc2-e1041f50c426""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:06.108212Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:05.409248Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# Measure execution time for view statistics query\n""""
  },
  {
    "{": ""    ""start_time = time.time()\n""""
  },
  {
    "{": ""    ""view_stats = collection.aggregate([\n""""
  },
  {
    "{": ""    ""    { \""$group\"": { \""_id\"": None""
  },
  {
    "{": ""    ""])\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Collect results to ensure the query executes fully\n""""
  },
  {
    "{": ""    ""view_stats_result = list(view_stats)\n""""
  },
  {
    "{": ""    ""end_time = time.time()\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Print results and time\n""""
  },
  {
    "{": ""    ""print(\""View statistics:\""""
  },
  {
    "{": ""    ""print(f\""View statistics query took {end_time - start_time:.4f} seconds\"")\n""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""View statistics: [{'_id': None""
  },
  {
    "{": ""      ""View statistics query took 0.6919 seconds\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 14""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""7b586804-b789-4b02-abfb-be84f4444aa6""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:06.139909Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:06.133201Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# Measure execution time for related IDs format check\n""""
  },
  {
    "{": ""    ""start_time = time.time()\n""""
  },
  {
    "{": ""    ""related_id_check = collection.find({\""relatedIDs\"": {\""$exists\"": True""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Collect results to ensure the query executes fully\n""""
  },
  {
    "{": ""    ""related_ids = list(related_id_check)\n""""
  },
  {
    "{": ""    ""end_time = time.time()\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Print results and time\n""""
  },
  {
    "{": ""    ""print(\""Sample related IDs:\"")\n""""
  },
  {
    "{": ""    ""for doc in related_ids:\n""""
  },
  {
    "{": ""    ""    print(doc['relatedIDs'])\n""""
  },
  {
    "{": ""    ""print(f\""Related IDs check query took {end_time - start_time:.4f} seconds\"")\n""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Sample related IDs:\n""""
  },
  {
    "{": ""      ""QuRYeRnAuXM""
  },
  {
    "{": ""      ""dh6dF1XY3uI""
  },
  {
    "{": ""      ""aYHBqH_xbCw""
  },
  {
    "{": ""      ""UCeA4K2-wNk""
  },
  {
    "{": ""      ""5vLbA7n8EG0""
  },
  {
    "{": ""      ""Related IDs check query took 0.0020 seconds\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 15""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""f75f83204e0715aa""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:19.764991Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:06.193622Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# Running aggregation functions (from aggregations.py) and displaying results\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""from pymongo import MongoClient\n""""
  },
  {
    "{": ""    ""from aggregations import (\n""""
  },
  {
    "{": ""    ""    calculate_view_statistics""
  },
  {
    "{": ""    ""    calculate_avg_rating_by_category""
  },
  {
    "{": ""    ""    calculate_total_comments_and_ratings_by_category""
  },
  {
    "{": ""    ""    calculate_avg_length_by_category""
  },
  {
    "{": ""    ""    avg_views_per_video_by_category""
  },
  {
    "{": ""    ""    most_viewed_videos""
  },
  {
    "{": ""    ""    most_viewed_video_in_each_category""
  },
  {
    "{": ""    ""    top_uploader_by_views""
  },
  {
    "{": ""    ""    top_commented_videos\n""""
  },
  {
    "{": ""    "")\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# MongoDB connection setup\n""""
  },
  {
    "{": ""    ""uri = 'mongodb://localhost:27017/'\n""""
  },
  {
    "{": ""    ""client = MongoClient(uri)\n""""
  },
  {
    "{": ""    ""db = client[\""youtubedb\""]\n""""
  },
  {
    "{": ""    ""collection = db[\""youtube_vids\""]\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# 1. Platform-wide View Statistics\n""""
  },
  {
    "{": ""    ""view_stats = list(calculate_view_statistics(collection))[0]\n""""
  },
  {
    "{": ""    ""print(\""\\nPlatform-Wide View Statistics:\"")\n""""
  },
  {
    "{": ""    ""print(f\""  - Average Views: {view_stats['avgViews']:.2f}\"")\n""""
  },
  {
    "{": ""    ""print(f\""  - Maximum Views: {view_stats['maxViews']}\"")\n""""
  },
  {
    "{": ""    ""print(f\""  - Minimum Views: {view_stats['minViews']}\"")\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# 2. Average Rating by Category\n""""
  },
  {
    "{": ""    ""avg_rating_by_category = list(calculate_avg_rating_by_category(collection))\n""""
  },
  {
    "{": ""    ""rating_df = pd.DataFrame(avg_rating_by_category)\n""""
  },
  {
    "{": ""    ""rating_df.columns = [\""Category\""""
  },
  {
    "{": ""    ""rating_df[\""Average Rating\""] = rating_df[\""Average Rating\""].round(2)\n""""
  },
  {
    "{": ""    ""print(\""\\nAverage Rating by Category:\"")\n""""
  },
  {
    "{": ""    ""display(rating_df)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# 3. Total Comments and Ratings by Category\n""""
  },
  {
    "{": ""    ""comments_ratings_by_category = list(calculate_total_comments_and_ratings_by_category(collection))\n""""
  },
  {
    "{": ""    ""comments_ratings_df = pd.DataFrame(comments_ratings_by_category)\n""""
  },
  {
    "{": ""    ""comments_ratings_df.columns = [\""Category\""""
  },
  {
    "{": ""    ""print(\""\\nTotal Comments and Ratings by Category:\"")\n""""
  },
  {
    "{": ""    ""display(comments_ratings_df)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# 4. Average Video Length by Category\n""""
  },
  {
    "{": ""    ""avg_length_by_category = list(calculate_avg_length_by_category(collection))\n""""
  },
  {
    "{": ""    ""length_df = pd.DataFrame(avg_length_by_category)\n""""
  },
  {
    "{": ""    ""length_df.columns = [\""Category\""""
  },
  {
    "{": ""    ""print(\""\\nAverage Video Length by Category:\"")\n""""
  },
  {
    "{": ""    ""display(length_df)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# 5. Average Views per Video by Category\n""""
  },
  {
    "{": ""    ""avg_views_category = list(avg_views_per_video_by_category(collection))\n""""
  },
  {
    "{": ""    ""avg_views_df = pd.DataFrame(avg_views_category)\n""""
  },
  {
    "{": ""    ""avg_views_df.columns = [\""Category\""""
  },
  {
    "{": ""    ""print(\""\\nAverage Views per Video by Category:\"")\n""""
  },
  {
    "{": ""    ""display(avg_views_df)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# 6. Most Viewed Videos on the Platform\n""""
  },
  {
    "{": ""    ""most_viewed = list(most_viewed_videos(collection""
  },
  {
    "{": ""    ""most_viewed_df = pd.DataFrame(most_viewed)\n""""
  },
  {
    "{": ""    ""print(\""\\nTop 5 Most Viewed Videos on the Platform:\"")\n""""
  },
  {
    "{": ""    ""display(most_viewed_df)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# 7. Most Viewed Video in Each Category\n""""
  },
  {
    "{": ""    ""most_viewed_per_category = list(most_viewed_video_in_each_category(collection))\n""""
  },
  {
    "{": ""    ""most_viewed_category_df = pd.DataFrame(most_viewed_per_category)\n""""
  },
  {
    "{": ""    ""print(\""\\nMost Viewed Videos in Each Category:\"")\n""""
  },
  {
    "{": ""    ""display(most_viewed_category_df)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# 8. Top Uploader by Total Views\n""""
  },
  {
    "{": ""    ""top_uploader = list(top_uploader_by_views(collection))[0]\n""""
  },
  {
    "{": ""    ""print(\""\\nTop Uploader by Total Views:\"")\n""""
  },
  {
    "{": ""    ""print(f\""  - Uploader: {top_uploader['_id']}\"")\n""""
  },
  {
    "{": ""    ""print(f\""  - Total Views: {top_uploader['totalViews']}\"")\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# 9. Top 5 Most Commented Videos\n""""
  },
  {
    "{": ""    ""top_commented = list(top_commented_videos(collection))\n""""
  },
  {
    "{": ""    ""top_commented_df = pd.DataFrame(top_commented)\n""""
  },
  {
    "{": ""    ""print(\""\\nTop 5 Most Commented Videos:\"")\n""""
  },
  {
    "{": ""    ""display(top_commented_df)\n""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""Platform-Wide View Statistics:\n""""
  },
  {
    "{": ""      ""  - Average Views: 82669.37\n""""
  },
  {
    "{": ""      ""  - Maximum Views: 79897120\n""""
  },
  {
    "{": ""      ""  - Minimum Views: 0\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""Average Rating by Category:\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""data"": {""
  },
  {
    "{": ""      ""text/plain"": [""
  },
  {
    "{": ""       ""                 Category  Average Rating\n""""
  },
  {
    "{": ""       ""0          Pets & Animals            3.80\n""""
  },
  {
    "{": ""       ""1                   Music            4.37\n""""
  },
  {
    "{": ""       ""2        Autos & Vehicles            3.65\n""""
  },
  {
    "{": ""       ""3        Film & Animation            4.22\n""""
  },
  {
    "{": ""       ""4    Science & Technology            3.53\n""""
  },
  {
    "{": ""       ""5          People & Blogs            3.70\n""""
  },
  {
    "{": ""       ""6                  Sports            3.98\n""""
  },
  {
    "{": ""       ""7           Howto & Style            3.73\n""""
  },
  {
    "{": ""       ""8                     UNA            3.96\n""""
  },
  {
    "{": ""       ""9                  Comedy            3.79\n""""
  },
  {
    "{": ""       ""10              Education            3.48\n""""
  },
  {
    "{": ""       ""11        News & Politics            3.95\n""""
  },
  {
    "{": ""       ""12  Nonprofits & Activism            3.90\n""""
  },
  {
    "{": ""       ""13          Entertainment            4.00\n""""
  },
  {
    "{": ""       ""14        Travel & Events            3.43""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""      ""text/html"": [""
  },
  {
    "{": ""       ""<div>\n""""
  },
  {
    "{": ""       ""<style scoped>\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th:only-of-type {\n""""
  },
  {
    "{": ""       ""        vertical-align: middle;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th {\n""""
  },
  {
    "{": ""       ""        vertical-align: top;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe thead th {\n""""
  },
  {
    "{": ""       ""        text-align: right;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""</style>\n""""
  },
  {
    "{": ""       ""<table border=\""1\"" class=\""dataframe\"">\n""""
  },
  {
    "{": ""       ""  <thead>\n""""
  },
  {
    "{": ""       ""    <tr style=\""text-align: right;\"">\n""""
  },
  {
    "{": ""       ""      <th></th>\n""""
  },
  {
    "{": ""       ""      <th>Category</th>\n""""
  },
  {
    "{": ""       ""      <th>Average Rating</th>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </thead>\n""""
  },
  {
    "{": ""       ""  <tbody>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>0</th>\n""""
  },
  {
    "{": ""       ""      <td>Pets &amp; Animals</td>\n""""
  },
  {
    "{": ""       ""      <td>3.80</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>1</th>\n""""
  },
  {
    "{": ""       ""      <td>Music</td>\n""""
  },
  {
    "{": ""       ""      <td>4.37</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>2</th>\n""""
  },
  {
    "{": ""       ""      <td>Autos &amp; Vehicles</td>\n""""
  },
  {
    "{": ""       ""      <td>3.65</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>3</th>\n""""
  },
  {
    "{": ""       ""      <td>Film &amp; Animation</td>\n""""
  },
  {
    "{": ""       ""      <td>4.22</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>4</th>\n""""
  },
  {
    "{": ""       ""      <td>Science &amp; Technology</td>\n""""
  },
  {
    "{": ""       ""      <td>3.53</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>5</th>\n""""
  },
  {
    "{": ""       ""      <td>People &amp; Blogs</td>\n""""
  },
  {
    "{": ""       ""      <td>3.70</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>6</th>\n""""
  },
  {
    "{": ""       ""      <td>Sports</td>\n""""
  },
  {
    "{": ""       ""      <td>3.98</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>7</th>\n""""
  },
  {
    "{": ""       ""      <td>Howto &amp; Style</td>\n""""
  },
  {
    "{": ""       ""      <td>3.73</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>8</th>\n""""
  },
  {
    "{": ""       ""      <td>UNA</td>\n""""
  },
  {
    "{": ""       ""      <td>3.96</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>9</th>\n""""
  },
  {
    "{": ""       ""      <td>Comedy</td>\n""""
  },
  {
    "{": ""       ""      <td>3.79</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>10</th>\n""""
  },
  {
    "{": ""       ""      <td>Education</td>\n""""
  },
  {
    "{": ""       ""      <td>3.48</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>11</th>\n""""
  },
  {
    "{": ""       ""      <td>News &amp; Politics</td>\n""""
  },
  {
    "{": ""       ""      <td>3.95</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>12</th>\n""""
  },
  {
    "{": ""       ""      <td>Nonprofits &amp; Activism</td>\n""""
  },
  {
    "{": ""       ""      <td>3.90</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>13</th>\n""""
  },
  {
    "{": ""       ""      <td>Entertainment</td>\n""""
  },
  {
    "{": ""       ""      <td>4.00</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>14</th>\n""""
  },
  {
    "{": ""       ""      <td>Travel &amp; Events</td>\n""""
  },
  {
    "{": ""       ""      <td>3.43</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </tbody>\n""""
  },
  {
    "{": ""       ""</table>\n""""
  },
  {
    "{": ""       ""</div>""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""     }""
  },
  {
    "{": ""     ""metadata"": {}""
  },
  {
    "{": ""     ""output_type"": ""display_data""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""Total Comments and Ratings by Category:\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""data"": {""
  },
  {
    "{": ""      ""text/plain"": [""
  },
  {
    "{": ""       ""                 Category  Total Comments  Total Ratings\n""""
  },
  {
    "{": ""       ""0    Science & Technology          721902         427966\n""""
  },
  {
    "{": ""       ""1                  Comedy        13533334       18943971\n""""
  },
  {
    "{": ""       ""2                     UNA         1250778        1891671\n""""
  },
  {
    "{": ""       ""3           Entertainment        20109031       21227487\n""""
  },
  {
    "{": ""       ""4   Nonprofits & Activism          204920         170565\n""""
  },
  {
    "{": ""       ""5         Travel & Events          573695         566952\n""""
  },
  {
    "{": ""       ""6         News & Politics         6969853        4425202\n""""
  },
  {
    "{": ""       ""7               Education          290630         290641\n""""
  },
  {
    "{": ""       ""8        Autos & Vehicles         1126921        1019226\n""""
  },
  {
    "{": ""       ""9          Pets & Animals         1700101        2056596\n""""
  },
  {
    "{": ""       ""10                  Music        31226791       43629456\n""""
  },
  {
    "{": ""       ""11                 Sports         3872421        3810709\n""""
  },
  {
    "{": ""       ""12          Howto & Style         2316272        1775097\n""""
  },
  {
    "{": ""       ""13       Film & Animation         4872288        7042302\n""""
  },
  {
    "{": ""       ""14         People & Blogs         6808719        6037218""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""      ""text/html"": [""
  },
  {
    "{": ""       ""<div>\n""""
  },
  {
    "{": ""       ""<style scoped>\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th:only-of-type {\n""""
  },
  {
    "{": ""       ""        vertical-align: middle;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th {\n""""
  },
  {
    "{": ""       ""        vertical-align: top;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe thead th {\n""""
  },
  {
    "{": ""       ""        text-align: right;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""</style>\n""""
  },
  {
    "{": ""       ""<table border=\""1\"" class=\""dataframe\"">\n""""
  },
  {
    "{": ""       ""  <thead>\n""""
  },
  {
    "{": ""       ""    <tr style=\""text-align: right;\"">\n""""
  },
  {
    "{": ""       ""      <th></th>\n""""
  },
  {
    "{": ""       ""      <th>Category</th>\n""""
  },
  {
    "{": ""       ""      <th>Total Comments</th>\n""""
  },
  {
    "{": ""       ""      <th>Total Ratings</th>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </thead>\n""""
  },
  {
    "{": ""       ""  <tbody>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>0</th>\n""""
  },
  {
    "{": ""       ""      <td>Science &amp; Technology</td>\n""""
  },
  {
    "{": ""       ""      <td>721902</td>\n""""
  },
  {
    "{": ""       ""      <td>427966</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>1</th>\n""""
  },
  {
    "{": ""       ""      <td>Comedy</td>\n""""
  },
  {
    "{": ""       ""      <td>13533334</td>\n""""
  },
  {
    "{": ""       ""      <td>18943971</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>2</th>\n""""
  },
  {
    "{": ""       ""      <td>UNA</td>\n""""
  },
  {
    "{": ""       ""      <td>1250778</td>\n""""
  },
  {
    "{": ""       ""      <td>1891671</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>3</th>\n""""
  },
  {
    "{": ""       ""      <td>Entertainment</td>\n""""
  },
  {
    "{": ""       ""      <td>20109031</td>\n""""
  },
  {
    "{": ""       ""      <td>21227487</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>4</th>\n""""
  },
  {
    "{": ""       ""      <td>Nonprofits &amp; Activism</td>\n""""
  },
  {
    "{": ""       ""      <td>204920</td>\n""""
  },
  {
    "{": ""       ""      <td>170565</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>5</th>\n""""
  },
  {
    "{": ""       ""      <td>Travel &amp; Events</td>\n""""
  },
  {
    "{": ""       ""      <td>573695</td>\n""""
  },
  {
    "{": ""       ""      <td>566952</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>6</th>\n""""
  },
  {
    "{": ""       ""      <td>News &amp; Politics</td>\n""""
  },
  {
    "{": ""       ""      <td>6969853</td>\n""""
  },
  {
    "{": ""       ""      <td>4425202</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>7</th>\n""""
  },
  {
    "{": ""       ""      <td>Education</td>\n""""
  },
  {
    "{": ""       ""      <td>290630</td>\n""""
  },
  {
    "{": ""       ""      <td>290641</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>8</th>\n""""
  },
  {
    "{": ""       ""      <td>Autos &amp; Vehicles</td>\n""""
  },
  {
    "{": ""       ""      <td>1126921</td>\n""""
  },
  {
    "{": ""       ""      <td>1019226</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>9</th>\n""""
  },
  {
    "{": ""       ""      <td>Pets &amp; Animals</td>\n""""
  },
  {
    "{": ""       ""      <td>1700101</td>\n""""
  },
  {
    "{": ""       ""      <td>2056596</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>10</th>\n""""
  },
  {
    "{": ""       ""      <td>Music</td>\n""""
  },
  {
    "{": ""       ""      <td>31226791</td>\n""""
  },
  {
    "{": ""       ""      <td>43629456</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>11</th>\n""""
  },
  {
    "{": ""       ""      <td>Sports</td>\n""""
  },
  {
    "{": ""       ""      <td>3872421</td>\n""""
  },
  {
    "{": ""       ""      <td>3810709</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>12</th>\n""""
  },
  {
    "{": ""       ""      <td>Howto &amp; Style</td>\n""""
  },
  {
    "{": ""       ""      <td>2316272</td>\n""""
  },
  {
    "{": ""       ""      <td>1775097</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>13</th>\n""""
  },
  {
    "{": ""       ""      <td>Film &amp; Animation</td>\n""""
  },
  {
    "{": ""       ""      <td>4872288</td>\n""""
  },
  {
    "{": ""       ""      <td>7042302</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>14</th>\n""""
  },
  {
    "{": ""       ""      <td>People &amp; Blogs</td>\n""""
  },
  {
    "{": ""       ""      <td>6808719</td>\n""""
  },
  {
    "{": ""       ""      <td>6037218</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </tbody>\n""""
  },
  {
    "{": ""       ""</table>\n""""
  },
  {
    "{": ""       ""</div>""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""     }""
  },
  {
    "{": ""     ""metadata"": {}""
  },
  {
    "{": ""     ""output_type"": ""display_data""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""Average Video Length by Category:\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""data"": {""
  },
  {
    "{": ""      ""text/plain"": [""
  },
  {
    "{": ""       ""                 Category  Average Length\n""""
  },
  {
    "{": ""       ""0    Science & Technology      273.059120\n""""
  },
  {
    "{": ""       ""1                  Comedy      161.027965\n""""
  },
  {
    "{": ""       ""2                     UNA      148.724228\n""""
  },
  {
    "{": ""       ""3           Entertainment      231.014299\n""""
  },
  {
    "{": ""       ""4   Nonprofits & Activism      234.960181\n""""
  },
  {
    "{": ""       ""5         Travel & Events      199.165570\n""""
  },
  {
    "{": ""       ""6               Education      278.578397\n""""
  },
  {
    "{": ""       ""7         News & Politics      265.144017\n""""
  },
  {
    "{": ""       ""8        Autos & Vehicles      135.422935\n""""
  },
  {
    "{": ""       ""9          Pets & Animals      127.602208\n""""
  },
  {
    "{": ""       ""10                  Music      233.846128\n""""
  },
  {
    "{": ""       ""11                 Sports      350.999710\n""""
  },
  {
    "{": ""       ""12          Howto & Style      244.745494\n""""
  },
  {
    "{": ""       ""13       Film & Animation      217.645601\n""""
  },
  {
    "{": ""       ""14         People & Blogs      205.600293""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""      ""text/html"": [""
  },
  {
    "{": ""       ""<div>\n""""
  },
  {
    "{": ""       ""<style scoped>\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th:only-of-type {\n""""
  },
  {
    "{": ""       ""        vertical-align: middle;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th {\n""""
  },
  {
    "{": ""       ""        vertical-align: top;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe thead th {\n""""
  },
  {
    "{": ""       ""        text-align: right;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""</style>\n""""
  },
  {
    "{": ""       ""<table border=\""1\"" class=\""dataframe\"">\n""""
  },
  {
    "{": ""       ""  <thead>\n""""
  },
  {
    "{": ""       ""    <tr style=\""text-align: right;\"">\n""""
  },
  {
    "{": ""       ""      <th></th>\n""""
  },
  {
    "{": ""       ""      <th>Category</th>\n""""
  },
  {
    "{": ""       ""      <th>Average Length</th>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </thead>\n""""
  },
  {
    "{": ""       ""  <tbody>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>0</th>\n""""
  },
  {
    "{": ""       ""      <td>Science &amp; Technology</td>\n""""
  },
  {
    "{": ""       ""      <td>273.059120</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>1</th>\n""""
  },
  {
    "{": ""       ""      <td>Comedy</td>\n""""
  },
  {
    "{": ""       ""      <td>161.027965</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>2</th>\n""""
  },
  {
    "{": ""       ""      <td>UNA</td>\n""""
  },
  {
    "{": ""       ""      <td>148.724228</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>3</th>\n""""
  },
  {
    "{": ""       ""      <td>Entertainment</td>\n""""
  },
  {
    "{": ""       ""      <td>231.014299</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>4</th>\n""""
  },
  {
    "{": ""       ""      <td>Nonprofits &amp; Activism</td>\n""""
  },
  {
    "{": ""       ""      <td>234.960181</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>5</th>\n""""
  },
  {
    "{": ""       ""      <td>Travel &amp; Events</td>\n""""
  },
  {
    "{": ""       ""      <td>199.165570</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>6</th>\n""""
  },
  {
    "{": ""       ""      <td>Education</td>\n""""
  },
  {
    "{": ""       ""      <td>278.578397</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>7</th>\n""""
  },
  {
    "{": ""       ""      <td>News &amp; Politics</td>\n""""
  },
  {
    "{": ""       ""      <td>265.144017</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>8</th>\n""""
  },
  {
    "{": ""       ""      <td>Autos &amp; Vehicles</td>\n""""
  },
  {
    "{": ""       ""      <td>135.422935</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>9</th>\n""""
  },
  {
    "{": ""       ""      <td>Pets &amp; Animals</td>\n""""
  },
  {
    "{": ""       ""      <td>127.602208</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>10</th>\n""""
  },
  {
    "{": ""       ""      <td>Music</td>\n""""
  },
  {
    "{": ""       ""      <td>233.846128</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>11</th>\n""""
  },
  {
    "{": ""       ""      <td>Sports</td>\n""""
  },
  {
    "{": ""       ""      <td>350.999710</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>12</th>\n""""
  },
  {
    "{": ""       ""      <td>Howto &amp; Style</td>\n""""
  },
  {
    "{": ""       ""      <td>244.745494</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>13</th>\n""""
  },
  {
    "{": ""       ""      <td>Film &amp; Animation</td>\n""""
  },
  {
    "{": ""       ""      <td>217.645601</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>14</th>\n""""
  },
  {
    "{": ""       ""      <td>People &amp; Blogs</td>\n""""
  },
  {
    "{": ""       ""      <td>205.600293</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </tbody>\n""""
  },
  {
    "{": ""       ""</table>\n""""
  },
  {
    "{": ""       ""</div>""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""     }""
  },
  {
    "{": ""     ""metadata"": {}""
  },
  {
    "{": ""     ""output_type"": ""display_data""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""Average Views per Video by Category:\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""data"": {""
  },
  {
    "{": ""      ""text/plain"": [""
  },
  {
    "{": ""       ""                 Category  Average Views\n""""
  },
  {
    "{": ""       ""0        Autos & Vehicles   64163.566253\n""""
  },
  {
    "{": ""       ""1                   Music  127125.909294\n""""
  },
  {
    "{": ""       ""2          Pets & Animals  102090.176865\n""""
  },
  {
    "{": ""       ""3           Howto & Style   55242.966114\n""""
  },
  {
    "{": ""       ""4                  Sports   58442.829379\n""""
  },
  {
    "{": ""       ""5    Science & Technology   23326.552396\n""""
  },
  {
    "{": ""       ""6          People & Blogs   57085.917696\n""""
  },
  {
    "{": ""       ""7        Film & Animation   57942.756836\n""""
  },
  {
    "{": ""       ""8                  Comedy  115127.920852\n""""
  },
  {
    "{": ""       ""9                     UNA  236014.072820\n""""
  },
  {
    "{": ""       ""10  Nonprofits & Activism   12124.777376\n""""
  },
  {
    "{": ""       ""11          Entertainment   63325.110427\n""""
  },
  {
    "{": ""       ""12              Education   14951.245337\n""""
  },
  {
    "{": ""       ""13        News & Politics   43908.405460\n""""
  },
  {
    "{": ""       ""14        Travel & Events   35504.505220""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""      ""text/html"": [""
  },
  {
    "{": ""       ""<div>\n""""
  },
  {
    "{": ""       ""<style scoped>\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th:only-of-type {\n""""
  },
  {
    "{": ""       ""        vertical-align: middle;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th {\n""""
  },
  {
    "{": ""       ""        vertical-align: top;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe thead th {\n""""
  },
  {
    "{": ""       ""        text-align: right;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""</style>\n""""
  },
  {
    "{": ""       ""<table border=\""1\"" class=\""dataframe\"">\n""""
  },
  {
    "{": ""       ""  <thead>\n""""
  },
  {
    "{": ""       ""    <tr style=\""text-align: right;\"">\n""""
  },
  {
    "{": ""       ""      <th></th>\n""""
  },
  {
    "{": ""       ""      <th>Category</th>\n""""
  },
  {
    "{": ""       ""      <th>Average Views</th>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </thead>\n""""
  },
  {
    "{": ""       ""  <tbody>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>0</th>\n""""
  },
  {
    "{": ""       ""      <td>Autos &amp; Vehicles</td>\n""""
  },
  {
    "{": ""       ""      <td>64163.566253</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>1</th>\n""""
  },
  {
    "{": ""       ""      <td>Music</td>\n""""
  },
  {
    "{": ""       ""      <td>127125.909294</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>2</th>\n""""
  },
  {
    "{": ""       ""      <td>Pets &amp; Animals</td>\n""""
  },
  {
    "{": ""       ""      <td>102090.176865</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>3</th>\n""""
  },
  {
    "{": ""       ""      <td>Howto &amp; Style</td>\n""""
  },
  {
    "{": ""       ""      <td>55242.966114</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>4</th>\n""""
  },
  {
    "{": ""       ""      <td>Sports</td>\n""""
  },
  {
    "{": ""       ""      <td>58442.829379</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>5</th>\n""""
  },
  {
    "{": ""       ""      <td>Science &amp; Technology</td>\n""""
  },
  {
    "{": ""       ""      <td>23326.552396</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>6</th>\n""""
  },
  {
    "{": ""       ""      <td>People &amp; Blogs</td>\n""""
  },
  {
    "{": ""       ""      <td>57085.917696</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>7</th>\n""""
  },
  {
    "{": ""       ""      <td>Film &amp; Animation</td>\n""""
  },
  {
    "{": ""       ""      <td>57942.756836</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>8</th>\n""""
  },
  {
    "{": ""       ""      <td>Comedy</td>\n""""
  },
  {
    "{": ""       ""      <td>115127.920852</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>9</th>\n""""
  },
  {
    "{": ""       ""      <td>UNA</td>\n""""
  },
  {
    "{": ""       ""      <td>236014.072820</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>10</th>\n""""
  },
  {
    "{": ""       ""      <td>Nonprofits &amp; Activism</td>\n""""
  },
  {
    "{": ""       ""      <td>12124.777376</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>11</th>\n""""
  },
  {
    "{": ""       ""      <td>Entertainment</td>\n""""
  },
  {
    "{": ""       ""      <td>63325.110427</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>12</th>\n""""
  },
  {
    "{": ""       ""      <td>Education</td>\n""""
  },
  {
    "{": ""       ""      <td>14951.245337</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>13</th>\n""""
  },
  {
    "{": ""       ""      <td>News &amp; Politics</td>\n""""
  },
  {
    "{": ""       ""      <td>43908.405460</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>14</th>\n""""
  },
  {
    "{": ""       ""      <td>Travel &amp; Events</td>\n""""
  },
  {
    "{": ""       ""      <td>35504.505220</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </tbody>\n""""
  },
  {
    "{": ""       ""</table>\n""""
  },
  {
    "{": ""       ""</div>""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""     }""
  },
  {
    "{": ""     ""metadata"": {}""
  },
  {
    "{": ""     ""output_type"": ""display_data""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""Top 5 Most Viewed Videos on the Platform:\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""data"": {""
  },
  {
    "{": ""      ""text/plain"": [""
  },
  {
    "{": ""       ""                        _id      videoID       uploader          category  \\\n""""
  },
  {
    "{": ""       ""0  6753a039f38132043599e170  dMH0bHeiRNg  judsonlaipply            Comedy   \n""""
  },
  {
    "{": ""       ""1  6753a03af3813204359a04d0  cQ25-glGRzI     RCARecords             Music   \n""""
  },
  {
    "{": ""       ""2  6753a039f38132043599d1f4  12Z3J1uzd0Q        kaejane  Film & Animation   \n""""
  },
  {
    "{": ""       ""3  6753a03af3813204359a0347  244qR7SvvX0   donotasyoudo     Entertainment   \n""""
  },
  {
    "{": ""       ""4  6753a039f38132043599f84a  ePyRrb2-fzs      1988basti             Music   \n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""      views  \n""""
  },
  {
    "{": ""       ""0  79897120  \n""""
  },
  {
    "{": ""       ""1  77674728  \n""""
  },
  {
    "{": ""       ""2  65341925  \n""""
  },
  {
    "{": ""       ""3  57790943  \n""""
  },
  {
    "{": ""       ""4  45984219  """"
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""      ""text/html"": [""
  },
  {
    "{": ""       ""<div>\n""""
  },
  {
    "{": ""       ""<style scoped>\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th:only-of-type {\n""""
  },
  {
    "{": ""       ""        vertical-align: middle;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th {\n""""
  },
  {
    "{": ""       ""        vertical-align: top;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe thead th {\n""""
  },
  {
    "{": ""       ""        text-align: right;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""</style>\n""""
  },
  {
    "{": ""       ""<table border=\""1\"" class=\""dataframe\"">\n""""
  },
  {
    "{": ""       ""  <thead>\n""""
  },
  {
    "{": ""       ""    <tr style=\""text-align: right;\"">\n""""
  },
  {
    "{": ""       ""      <th></th>\n""""
  },
  {
    "{": ""       ""      <th>_id</th>\n""""
  },
  {
    "{": ""       ""      <th>videoID</th>\n""""
  },
  {
    "{": ""       ""      <th>uploader</th>\n""""
  },
  {
    "{": ""       ""      <th>category</th>\n""""
  },
  {
    "{": ""       ""      <th>views</th>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </thead>\n""""
  },
  {
    "{": ""       ""  <tbody>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>0</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a039f38132043599e170</td>\n""""
  },
  {
    "{": ""       ""      <td>dMH0bHeiRNg</td>\n""""
  },
  {
    "{": ""       ""      <td>judsonlaipply</td>\n""""
  },
  {
    "{": ""       ""      <td>Comedy</td>\n""""
  },
  {
    "{": ""       ""      <td>79897120</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>1</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a03af3813204359a04d0</td>\n""""
  },
  {
    "{": ""       ""      <td>cQ25-glGRzI</td>\n""""
  },
  {
    "{": ""       ""      <td>RCARecords</td>\n""""
  },
  {
    "{": ""       ""      <td>Music</td>\n""""
  },
  {
    "{": ""       ""      <td>77674728</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>2</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a039f38132043599d1f4</td>\n""""
  },
  {
    "{": ""       ""      <td>12Z3J1uzd0Q</td>\n""""
  },
  {
    "{": ""       ""      <td>kaejane</td>\n""""
  },
  {
    "{": ""       ""      <td>Film &amp; Animation</td>\n""""
  },
  {
    "{": ""       ""      <td>65341925</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>3</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a03af3813204359a0347</td>\n""""
  },
  {
    "{": ""       ""      <td>244qR7SvvX0</td>\n""""
  },
  {
    "{": ""       ""      <td>donotasyoudo</td>\n""""
  },
  {
    "{": ""       ""      <td>Entertainment</td>\n""""
  },
  {
    "{": ""       ""      <td>57790943</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>4</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a039f38132043599f84a</td>\n""""
  },
  {
    "{": ""       ""      <td>ePyRrb2-fzs</td>\n""""
  },
  {
    "{": ""       ""      <td>1988basti</td>\n""""
  },
  {
    "{": ""       ""      <td>Music</td>\n""""
  },
  {
    "{": ""       ""      <td>45984219</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </tbody>\n""""
  },
  {
    "{": ""       ""</table>\n""""
  },
  {
    "{": ""       ""</div>""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""     }""
  },
  {
    "{": ""     ""metadata"": {}""
  },
  {
    "{": ""     ""output_type"": ""display_data""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""Most Viewed Videos in Each Category:\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""data"": {""
  },
  {
    "{": ""      ""text/plain"": [""
  },
  {
    "{": ""       ""                      _id      videoID         uploader     views  rate  \\\n""""
  },
  {
    "{": ""       ""0         Travel & Events  p0aQvKDA1K0  cinnamonstar808  12239023  4.73   \n""""
  },
  {
    "{": ""       ""1               Education  VnGb6UQvwJs      aminochka89   2441432  4.56   \n""""
  },
  {
    "{": ""       ""2         News & Politics  SkELRp4wKPs              piu  12730681  4.71   \n""""
  },
  {
    "{": ""       ""3           Entertainment  244qR7SvvX0     donotasyoudo  57790943  1.45   \n""""
  },
  {
    "{": ""       ""4   Nonprofits & Activism  tFxk7glmMbo      VictoryFund   1063928  4.43   \n""""
  },
  {
    "{": ""       ""5                     UNA  8h98jb9Lk74           duyuhp  33880568  3.82   \n""""
  },
  {
    "{": ""       ""6                  Comedy  dMH0bHeiRNg    judsonlaipply  79897120  4.65   \n""""
  },
  {
    "{": ""       ""7          People & Blogs  v3ARyAb_1Bs        MastaBest  31812447  4.52   \n""""
  },
  {
    "{": ""       ""8    Science & Technology  W1czBcnX1Ww          olinerd   3234852  4.82   \n""""
  },
  {
    "{": ""       ""9        Film & Animation  12Z3J1uzd0Q          kaejane  65341925  3.03   \n""""
  },
  {
    "{": ""       ""10          Howto & Style  sLGLum5SyKQ        SouljaBoy  31121122  4.52   \n""""
  },
  {
    "{": ""       ""11                 Sports  vt4X7zFfv4k   abc1008mbs1179  12598542  4.80   \n""""
  },
  {
    "{": ""       ""12                  Music  cQ25-glGRzI       RCARecords  77674728  4.45   \n""""
  },
  {
    "{": ""       ""13         Pets & Animals  LU8DDYz68kM         Jason275  27721690  4.88   \n""""
  },
  {
    "{": ""       ""14       Autos & Vehicles  ZeBd_F2Bz5Y      SupercarAce   8623041  4.55   \n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    comments  \n""""
  },
  {
    "{": ""       ""0       3032  \n""""
  },
  {
    "{": ""       ""1       1957  \n""""
  },
  {
    "{": ""       ""2      15537  \n""""
  },
  {
    "{": ""       ""3      14913  \n""""
  },
  {
    "{": ""       ""4       9628  \n""""
  },
  {
    "{": ""       ""5       4378  \n""""
  },
  {
    "{": ""       ""6     131356  \n""""
  },
  {
    "{": ""       ""7      31065  \n""""
  },
  {
    "{": ""       ""8       6093  \n""""
  },
  {
    "{": ""       ""9       5508  \n""""
  },
  {
    "{": ""       ""10     37301  \n""""
  },
  {
    "{": ""       ""11      6371  \n""""
  },
  {
    "{": ""       ""12    186858  \n""""
  },
  {
    "{": ""       ""13     24004  \n""""
  },
  {
    "{": ""       ""14      6803  """"
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""      ""text/html"": [""
  },
  {
    "{": ""       ""<div>\n""""
  },
  {
    "{": ""       ""<style scoped>\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th:only-of-type {\n""""
  },
  {
    "{": ""       ""        vertical-align: middle;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th {\n""""
  },
  {
    "{": ""       ""        vertical-align: top;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe thead th {\n""""
  },
  {
    "{": ""       ""        text-align: right;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""</style>\n""""
  },
  {
    "{": ""       ""<table border=\""1\"" class=\""dataframe\"">\n""""
  },
  {
    "{": ""       ""  <thead>\n""""
  },
  {
    "{": ""       ""    <tr style=\""text-align: right;\"">\n""""
  },
  {
    "{": ""       ""      <th></th>\n""""
  },
  {
    "{": ""       ""      <th>_id</th>\n""""
  },
  {
    "{": ""       ""      <th>videoID</th>\n""""
  },
  {
    "{": ""       ""      <th>uploader</th>\n""""
  },
  {
    "{": ""       ""      <th>views</th>\n""""
  },
  {
    "{": ""       ""      <th>rate</th>\n""""
  },
  {
    "{": ""       ""      <th>comments</th>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </thead>\n""""
  },
  {
    "{": ""       ""  <tbody>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>0</th>\n""""
  },
  {
    "{": ""       ""      <td>Travel &amp; Events</td>\n""""
  },
  {
    "{": ""       ""      <td>p0aQvKDA1K0</td>\n""""
  },
  {
    "{": ""       ""      <td>cinnamonstar808</td>\n""""
  },
  {
    "{": ""       ""      <td>12239023</td>\n""""
  },
  {
    "{": ""       ""      <td>4.73</td>\n""""
  },
  {
    "{": ""       ""      <td>3032</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>1</th>\n""""
  },
  {
    "{": ""       ""      <td>Education</td>\n""""
  },
  {
    "{": ""       ""      <td>VnGb6UQvwJs</td>\n""""
  },
  {
    "{": ""       ""      <td>aminochka89</td>\n""""
  },
  {
    "{": ""       ""      <td>2441432</td>\n""""
  },
  {
    "{": ""       ""      <td>4.56</td>\n""""
  },
  {
    "{": ""       ""      <td>1957</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>2</th>\n""""
  },
  {
    "{": ""       ""      <td>News &amp; Politics</td>\n""""
  },
  {
    "{": ""       ""      <td>SkELRp4wKPs</td>\n""""
  },
  {
    "{": ""       ""      <td>piu</td>\n""""
  },
  {
    "{": ""       ""      <td>12730681</td>\n""""
  },
  {
    "{": ""       ""      <td>4.71</td>\n""""
  },
  {
    "{": ""       ""      <td>15537</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>3</th>\n""""
  },
  {
    "{": ""       ""      <td>Entertainment</td>\n""""
  },
  {
    "{": ""       ""      <td>244qR7SvvX0</td>\n""""
  },
  {
    "{": ""       ""      <td>donotasyoudo</td>\n""""
  },
  {
    "{": ""       ""      <td>57790943</td>\n""""
  },
  {
    "{": ""       ""      <td>1.45</td>\n""""
  },
  {
    "{": ""       ""      <td>14913</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>4</th>\n""""
  },
  {
    "{": ""       ""      <td>Nonprofits &amp; Activism</td>\n""""
  },
  {
    "{": ""       ""      <td>tFxk7glmMbo</td>\n""""
  },
  {
    "{": ""       ""      <td>VictoryFund</td>\n""""
  },
  {
    "{": ""       ""      <td>1063928</td>\n""""
  },
  {
    "{": ""       ""      <td>4.43</td>\n""""
  },
  {
    "{": ""       ""      <td>9628</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>5</th>\n""""
  },
  {
    "{": ""       ""      <td>UNA</td>\n""""
  },
  {
    "{": ""       ""      <td>8h98jb9Lk74</td>\n""""
  },
  {
    "{": ""       ""      <td>duyuhp</td>\n""""
  },
  {
    "{": ""       ""      <td>33880568</td>\n""""
  },
  {
    "{": ""       ""      <td>3.82</td>\n""""
  },
  {
    "{": ""       ""      <td>4378</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>6</th>\n""""
  },
  {
    "{": ""       ""      <td>Comedy</td>\n""""
  },
  {
    "{": ""       ""      <td>dMH0bHeiRNg</td>\n""""
  },
  {
    "{": ""       ""      <td>judsonlaipply</td>\n""""
  },
  {
    "{": ""       ""      <td>79897120</td>\n""""
  },
  {
    "{": ""       ""      <td>4.65</td>\n""""
  },
  {
    "{": ""       ""      <td>131356</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>7</th>\n""""
  },
  {
    "{": ""       ""      <td>People &amp; Blogs</td>\n""""
  },
  {
    "{": ""       ""      <td>v3ARyAb_1Bs</td>\n""""
  },
  {
    "{": ""       ""      <td>MastaBest</td>\n""""
  },
  {
    "{": ""       ""      <td>31812447</td>\n""""
  },
  {
    "{": ""       ""      <td>4.52</td>\n""""
  },
  {
    "{": ""       ""      <td>31065</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>8</th>\n""""
  },
  {
    "{": ""       ""      <td>Science &amp; Technology</td>\n""""
  },
  {
    "{": ""       ""      <td>W1czBcnX1Ww</td>\n""""
  },
  {
    "{": ""       ""      <td>olinerd</td>\n""""
  },
  {
    "{": ""       ""      <td>3234852</td>\n""""
  },
  {
    "{": ""       ""      <td>4.82</td>\n""""
  },
  {
    "{": ""       ""      <td>6093</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>9</th>\n""""
  },
  {
    "{": ""       ""      <td>Film &amp; Animation</td>\n""""
  },
  {
    "{": ""       ""      <td>12Z3J1uzd0Q</td>\n""""
  },
  {
    "{": ""       ""      <td>kaejane</td>\n""""
  },
  {
    "{": ""       ""      <td>65341925</td>\n""""
  },
  {
    "{": ""       ""      <td>3.03</td>\n""""
  },
  {
    "{": ""       ""      <td>5508</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>10</th>\n""""
  },
  {
    "{": ""       ""      <td>Howto &amp; Style</td>\n""""
  },
  {
    "{": ""       ""      <td>sLGLum5SyKQ</td>\n""""
  },
  {
    "{": ""       ""      <td>SouljaBoy</td>\n""""
  },
  {
    "{": ""       ""      <td>31121122</td>\n""""
  },
  {
    "{": ""       ""      <td>4.52</td>\n""""
  },
  {
    "{": ""       ""      <td>37301</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>11</th>\n""""
  },
  {
    "{": ""       ""      <td>Sports</td>\n""""
  },
  {
    "{": ""       ""      <td>vt4X7zFfv4k</td>\n""""
  },
  {
    "{": ""       ""      <td>abc1008mbs1179</td>\n""""
  },
  {
    "{": ""       ""      <td>12598542</td>\n""""
  },
  {
    "{": ""       ""      <td>4.80</td>\n""""
  },
  {
    "{": ""       ""      <td>6371</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>12</th>\n""""
  },
  {
    "{": ""       ""      <td>Music</td>\n""""
  },
  {
    "{": ""       ""      <td>cQ25-glGRzI</td>\n""""
  },
  {
    "{": ""       ""      <td>RCARecords</td>\n""""
  },
  {
    "{": ""       ""      <td>77674728</td>\n""""
  },
  {
    "{": ""       ""      <td>4.45</td>\n""""
  },
  {
    "{": ""       ""      <td>186858</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>13</th>\n""""
  },
  {
    "{": ""       ""      <td>Pets &amp; Animals</td>\n""""
  },
  {
    "{": ""       ""      <td>LU8DDYz68kM</td>\n""""
  },
  {
    "{": ""       ""      <td>Jason275</td>\n""""
  },
  {
    "{": ""       ""      <td>27721690</td>\n""""
  },
  {
    "{": ""       ""      <td>4.88</td>\n""""
  },
  {
    "{": ""       ""      <td>24004</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>14</th>\n""""
  },
  {
    "{": ""       ""      <td>Autos &amp; Vehicles</td>\n""""
  },
  {
    "{": ""       ""      <td>ZeBd_F2Bz5Y</td>\n""""
  },
  {
    "{": ""       ""      <td>SupercarAce</td>\n""""
  },
  {
    "{": ""       ""      <td>8623041</td>\n""""
  },
  {
    "{": ""       ""      <td>4.55</td>\n""""
  },
  {
    "{": ""       ""      <td>6803</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </tbody>\n""""
  },
  {
    "{": ""       ""</table>\n""""
  },
  {
    "{": ""       ""</div>""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""     }""
  },
  {
    "{": ""     ""metadata"": {}""
  },
  {
    "{": ""     ""output_type"": ""display_data""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""Top Uploader by Total Views:\n""""
  },
  {
    "{": ""      ""  - Uploader: universalmusicgroup\n""""
  },
  {
    "{": ""      ""  - Total Views: 1104279219\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""Top 5 Most Commented Videos:\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""data"": {""
  },
  {
    "{": ""      ""text/plain"": [""
  },
  {
    "{": ""       ""                        _id      videoID         uploader         category  \\\n""""
  },
  {
    "{": ""       ""0  6753a039f38132043599d1bc  kHmvkRoEowc  itschriscrocker    Entertainment   \n""""
  },
  {
    "{": ""       ""1  6753a03af3813204359aeaa0  uSVRuA8RpkU     duelistXmist    Entertainment   \n""""
  },
  {
    "{": ""       ""2  6753a03cf3813204359df18b  -oHivXjiX_w   makedoniatruth  News & Politics   \n""""
  },
  {
    "{": ""       ""3  6753a03af3813204359a04d0  cQ25-glGRzI       RCARecords            Music   \n""""
  },
  {
    "{": ""       ""4  6753a03af3813204359ae964  QjA5faZF1A8         guitar90            Music   \n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""   comments  \n""""
  },
  {
    "{": ""       ""0    259683  \n""""
  },
  {
    "{": ""       ""1    240970  \n""""
  },
  {
    "{": ""       ""2    210672  \n""""
  },
  {
    "{": ""       ""3    186858  \n""""
  },
  {
    "{": ""       ""4    169563  """"
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""      ""text/html"": [""
  },
  {
    "{": ""       ""<div>\n""""
  },
  {
    "{": ""       ""<style scoped>\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th:only-of-type {\n""""
  },
  {
    "{": ""       ""        vertical-align: middle;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe tbody tr th {\n""""
  },
  {
    "{": ""       ""        vertical-align: top;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""\n""""
  },
  {
    "{": ""       ""    .dataframe thead th {\n""""
  },
  {
    "{": ""       ""        text-align: right;\n""""
  },
  {
    "{": ""       ""    }\n""""
  },
  {
    "{": ""       ""</style>\n""""
  },
  {
    "{": ""       ""<table border=\""1\"" class=\""dataframe\"">\n""""
  },
  {
    "{": ""       ""  <thead>\n""""
  },
  {
    "{": ""       ""    <tr style=\""text-align: right;\"">\n""""
  },
  {
    "{": ""       ""      <th></th>\n""""
  },
  {
    "{": ""       ""      <th>_id</th>\n""""
  },
  {
    "{": ""       ""      <th>videoID</th>\n""""
  },
  {
    "{": ""       ""      <th>uploader</th>\n""""
  },
  {
    "{": ""       ""      <th>category</th>\n""""
  },
  {
    "{": ""       ""      <th>comments</th>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </thead>\n""""
  },
  {
    "{": ""       ""  <tbody>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>0</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a039f38132043599d1bc</td>\n""""
  },
  {
    "{": ""       ""      <td>kHmvkRoEowc</td>\n""""
  },
  {
    "{": ""       ""      <td>itschriscrocker</td>\n""""
  },
  {
    "{": ""       ""      <td>Entertainment</td>\n""""
  },
  {
    "{": ""       ""      <td>259683</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>1</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a03af3813204359aeaa0</td>\n""""
  },
  {
    "{": ""       ""      <td>uSVRuA8RpkU</td>\n""""
  },
  {
    "{": ""       ""      <td>duelistXmist</td>\n""""
  },
  {
    "{": ""       ""      <td>Entertainment</td>\n""""
  },
  {
    "{": ""       ""      <td>240970</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>2</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a03cf3813204359df18b</td>\n""""
  },
  {
    "{": ""       ""      <td>-oHivXjiX_w</td>\n""""
  },
  {
    "{": ""       ""      <td>makedoniatruth</td>\n""""
  },
  {
    "{": ""       ""      <td>News &amp; Politics</td>\n""""
  },
  {
    "{": ""       ""      <td>210672</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>3</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a03af3813204359a04d0</td>\n""""
  },
  {
    "{": ""       ""      <td>cQ25-glGRzI</td>\n""""
  },
  {
    "{": ""       ""      <td>RCARecords</td>\n""""
  },
  {
    "{": ""       ""      <td>Music</td>\n""""
  },
  {
    "{": ""       ""      <td>186858</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""    <tr>\n""""
  },
  {
    "{": ""       ""      <th>4</th>\n""""
  },
  {
    "{": ""       ""      <td>6753a03af3813204359ae964</td>\n""""
  },
  {
    "{": ""       ""      <td>QjA5faZF1A8</td>\n""""
  },
  {
    "{": ""       ""      <td>guitar90</td>\n""""
  },
  {
    "{": ""       ""      <td>Music</td>\n""""
  },
  {
    "{": ""       ""      <td>169563</td>\n""""
  },
  {
    "{": ""       ""    </tr>\n""""
  },
  {
    "{": ""       ""  </tbody>\n""""
  },
  {
    "{": ""       ""</table>\n""""
  },
  {
    "{": ""       ""</div>""""
  },
  {
    "{": ""      ]""
  },
  {
    "{": ""     }""
  },
  {
    "{": ""     ""metadata"": {}""
  },
  {
    "{": ""     ""output_type"": ""display_data""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 16""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""3f0046bc1889abb8""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:46.955029Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:19.794690Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""from graphframes import GraphFrame\n""""
  },
  {
    "{": ""    ""from pyspark.sql.functions import col""
  },
  {
    "{": ""    ""from pyspark.sql import SparkSession\n""""
  },
  {
    "{": ""    ""# PageRank for influence analysis\n""""
  },
  {
    "{": ""    ""spark = ((((SparkSession.builder \n""""
  },
  {
    "{": ""    ""            .appName(\""YouTubeAnalyzer\""))\n""""
  },
  {
    "{": ""    ""            .config(\""spark.jars.packages\""""
  },
  {
    "{": ""    ""                    \""graphframes:graphframes:0.8.4-spark3.5-s_2.12\"")\n""""
  },
  {
    "{": ""    ""            .config(\""spark.mongodb.input.uri\""""
  },
  {
    "{": ""    ""            .config(\""spark.mongodb.output.uri\""""
  },
  {
    "{": ""    ""            # The configs below prevents out of memory error that our team ran into and also increase efficiency\n""""
  },
  {
    "{": ""    ""            .config(\""spark.driver.memory\""""
  },
  {
    "{": ""    ""            .config(\""spark.executor.memory\""""
  },
  {
    "{": ""    ""            .config(\""spark.executor.instances\""""
  },
  {
    "{": ""    ""            .config(\""spark.executor.cores\""""
  },
  {
    "{": ""    ""            .config(\""spark.serializer\""""
  },
  {
    "{": ""    ""            .getOrCreate())\n""""
  },
  {
    "{": ""    ""# Read data from Mongodb\n""""
  },
  {
    "{": ""    ""yt_data = (((spark.read.format(\""mongodb\"") \n""""
  },
  {
    "{": ""    ""           .option(\""database\""""
  },
  {
    "{": ""    ""           .option(\""collection\""""
  },
  {
    "{": ""    ""           .load())\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Check to see if the pagerank results already exist in the database\n""""
  },
  {
    "{": ""    ""pagerank_results = (spark.read.format(\""mongodb\"")\n""""
  },
  {
    "{": ""    ""                    .option(\""database\""""
  },
  {
    "{": ""    ""                    .option(\""collection\""""
  },
  {
    "{": ""    ""                    .load())\n""""
  },
  {
    "{": ""    ""# Just load the results and display without having to rerun the whole PageRank algorithm if it already exists in database\n""""
  },
  {
    "{": ""    ""if pagerank_results.count() > 0:\n""""
  },
  {
    "{": ""    ""    print(\""PageRank results already exist in Database. Loading results...\"")\n""""
  },
  {
    "{": ""    ""    sample_results = pagerank_results.select(\""id\""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""else:\n""""
  },
  {
    "{": ""    ""    # Repartition the DF into 128 partitions (for parallel processing)\n""""
  },
  {
    "{": ""    ""    # Our team decided to store repartitioned result in memory to prevent re-computation or reloading\n""""
  },
  {
    "{": ""    ""    # (we believe this can improve performance)\n""""
  },
  {
    "{": ""    ""    yt_data_full = yt_data.repartition(128).cache()\n""""
  },
  {
    "{": ""    ""    # Create dataframe for vertices (videos)\n""""
  },
  {
    "{": ""    ""    vertices = yt_data_full.select(\n""""
  },
  {
    "{": ""    ""        col(\""videoID\"").alias(\""id\"")""
  },
  {
    "{": ""    ""        col(\""uploader\"")""
  },
  {
    "{": ""    ""        col(\""category\"")""
  },
  {
    "{": ""    ""        col(\""views\"")""
  },
  {
    "{": ""    ""        col(\""rate\"")""
  },
  {
    "{": ""    ""        col(\""ratings\"")""
  },
  {
    "{": ""    ""        col(\""comments\"")""
  },
  {
    "{": ""    ""        col(\""depth\"")\n""""
  },
  {
    "{": ""    ""    )\n""""
  },
  {
    "{": ""    ""    # Create dataframe for edges (related connections) and have a new column named dst\n""""
  },
  {
    "{": ""    ""    # Explode will create separate row for each related videoID in dst\n""""
  },
  {
    "{": ""    ""    edges = yt_data_full.select(\n""""
  },
  {
    "{": ""    ""        col(\""videoID\"").alias(\""src\"")""
  },
  {
    "{": ""    ""        split(col(\""relatedIDs\"")""
  },
  {
    "{": ""    ""    ).withColumn(\""dst\""""
  },
  {
    "{": ""    ""    # Create GraphFrame\n""""
  },
  {
    "{": ""    ""    vid_graph = GraphFrame(vertices""
  },
  {
    "{": ""    ""    # PageRank algorithm\n""""
  },
  {
    "{": ""    ""    # resetProbability controls how likely a random surfer will jump to a random page or node\n""""
  },
  {
    "{": ""    ""    # Since link structure is important""
  },
  {
    "{": ""    ""    start_time = time.time()\n""""
  },
  {
    "{": ""    ""    influences = vid_graph.pageRank(resetProbability = 0.15""
  },
  {
    "{": ""    ""    end_time = time.time()\n""""
  },
  {
    "{": ""    ""    # Show total time it takes to apply pagerank algorithm on the whole dataset\n""""
  },
  {
    "{": ""    ""    execution_time = end_time - start_time\n""""
  },
  {
    "{": ""    ""    print(f\""Execution time for applying PageRank on the full dataset: {execution_time}s\"")\n""""
  },
  {
    "{": ""    ""    # Save the PageRank results back to MongoDB\n""""
  },
  {
    "{": ""    ""    (influences.vertices.write.format(\""mongodb\"").mode(\""overwrite\"")\n""""
  },
  {
    "{": ""    ""        .option(\""database\""""
  },
  {
    "{": ""    ""        .option(\""collection\""""
  },
  {
    "{": ""    ""    # Display sample of the results\n""""
  },
  {
    "{": ""    ""    sample_results = influences.vertices.select(\""id\""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""sample_results.show(1000)""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""PageRank results already exist in Database. Loading results...\n""""
  },
  {
    "{": ""      ""+-----------+--------------------+--------------------+-------------------+--------+-------+\n""""
  },
  {
    "{": ""      ""|         id|            uploader|            category|           pagerank|comments|ratings|\n""""
  },
  {
    "{": ""      ""+-----------+--------------------+--------------------+-------------------+--------+-------+\n""""
  },
  {
    "{": ""      ""|-4g7dM75Te4| NICENECOUNCILdotcom|           Education| 0.3610756497129792|      30|      8|\n""""
  },
  {
    "{": ""      ""|-8bNuWtALkE|         Bambam13544|      People & Blogs| 0.6070806184186436|       0|      0|\n""""
  },
  {
    "{": ""      ""|-ZimpqeZDrg|     wrestleguru1987|              Sports| 0.4595333140349387|      60|     72|\n""""
  },
  {
    "{": ""      ""|0Aslygh_1YI|              futi93|               Music| 0.3958020364358823|       6|      5|\n""""
  },
  {
    "{": ""      ""|0EVTrwao4T0|         Promisquo00|    Film & Animation| 0.5656077034267794|     282|    213|\n""""
  },
  {
    "{": ""      ""|0G7MZXGJo60|             shanedk|     News & Politics| 0.3708443288959776|      25|     31|\n""""
  },
  {
    "{": ""      ""|0MXaaGaSwVk|            alpimimi|               Music| 0.6491742108538625|      69|     49|\n""""
  },
  {
    "{": ""      ""|0RXxo1MidkQ|         MELIPAISITA|Science & Technology| 0.5511038708026108|       1|      1|\n""""
  },
  {
    "{": ""      ""|0XcTFmjKzlg|       Blargaldalien|     News & Politics|  0.355430596425427|       9|      6|\n""""
  },
  {
    "{": ""      ""|0lWIGhW_whc|            bossy2k8|      People & Blogs| 0.9009354226091907|       9|      6|\n""""
  },
  {
    "{": ""      ""|15HpI2WisAw|      lanzadelongino|      People & Blogs| 0.3739499449005012|       2|      0|\n""""
  },
  {
    "{": ""      ""|27KsUjY-c_s|             RubenGM|       Entertainment| 0.4464212112279319|      13|     13|\n""""
  },
  {
    "{": ""      ""|2Rl9Ea-mAdA|            bullpalm|       Entertainment| 0.8186994292828124|     190|    166|\n""""
  },
  {
    "{": ""      ""|3ARs7sEJYh0|         StayGDUp109|               Music|0.49321409233252567|      87|     43|\n""""
  },
  {
    "{": ""      ""|3IA-t4sTOc0|          benstjohn2|                 UNA| 0.6118594160918907|       6|      7|\n""""
  },
  {
    "{": ""      ""|3Ylwu6HOeW4|            mwils855|               Music| 0.5397744330853994|       0|      0|\n""""
  },
  {
    "{": ""      ""|3et4_Qi7ksg|              gowant|       Entertainment| 0.7125903664148497|      18|     10|\n""""
  },
  {
    "{": ""      ""|3zD9W9SZj9w|           peglegsam|               Music| 1.0430192992062974|     336|   1364|\n""""
  },
  {
    "{": ""      ""|411Oxbsk1QQ|         dailymirror|       Entertainment| 0.4067097332363624|       0|      9|\n""""
  },
  {
    "{": ""      ""|484bwU794Rg|        videostorito|       Entertainment| 1.6188823231823386|      11|     28|\n""""
  },
  {
    "{": ""      ""|4AhvZGrTYfQ|       WrestleDazzle|              Sports|  0.533053367282725|       7|     10|\n""""
  },
  {
    "{": ""      ""|50L1I2mK_eE|             Paul382|              Comedy|  0.672643691411387|       1|      2|\n""""
  },
  {
    "{": ""      ""|544usLipiR4|    carlespuigdemont|      People & Blogs| 0.6805828236002738|       5|     11|\n""""
  },
  {
    "{": ""      ""|5PsrG1nKDYk|      ThePwnageNinja|       Entertainment|  6.205678620214548|    2811|   2825|\n""""
  },
  {
    "{": ""      ""|5QK2wPR8IpQ|          RonPaul247|     News & Politics|  1.135417352169953|     123|    539|\n""""
  },
  {
    "{": ""      ""|5h2N3iFSSVI|            KpBallin|               Music| 1.1779603134634624|       6|     10|\n""""
  },
  {
    "{": ""      ""|6LDE3NZUhD4|         Frogshark40|       Entertainment|  0.527526244526192|      48|     12|\n""""
  },
  {
    "{": ""      ""|6VXTfDU25qs|       fobgirliegirl|               Music| 0.3644179423354459|       4|      2|\n""""
  },
  {
    "{": ""      ""|6iWaN14DcoM|            mwuerzer|              Sports| 0.4133905018377269|       1|      7|\n""""
  },
  {
    "{": ""      ""|736X1g-yD4o|          danimelow1|    Autos & Vehicles|  0.900597772950033|       2|      3|\n""""
  },
  {
    "{": ""      ""|7OiYRJhnxGs| VancouverFilmSchool|    Film & Animation| 0.6571268182278188|      49|    104|\n""""
  },
  {
    "{": ""      ""|7kbto5RUQN0|          Citysinned|               Music| 0.5880839467891735|      33|     51|\n""""
  },
  {
    "{": ""      ""|9wVU7qCZA4c|            alexlmlo|              Comedy| 1.0608298431051626|       8|     19|\n""""
  },
  {
    "{": ""      ""|AhQ_0BO58aY|              koptop|              Comedy| 1.1035853664487811|      22|     34|\n""""
  },
  {
    "{": ""      ""|ByUVbaB5O-A|          infolivetv|     News & Politics|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|CcweHzpaiHY|         WankWarrior|       Entertainment| 0.7986488945124236|       2|      2|\n""""
  },
  {
    "{": ""      ""|CxYP5OaJvBU|            wavevang|               Music|  0.811257744084369|       5|      5|\n""""
  },
  {
    "{": ""      ""|Daizk-gZYAo|            twilsjoh|    Autos & Vehicles| 0.5671193726653684|      16|      2|\n""""
  },
  {
    "{": ""      ""|DqJ3kshS_xY|              grizzz|       Entertainment| 1.6951544054285803|      70|     21|\n""""
  },
  {
    "{": ""      ""|Dtnmcw3qjHE|        hellodouchey|      People & Blogs| 0.8418129085183533|      53|     32|\n""""
  },
  {
    "{": ""      ""|EPjKHW43WUI|   videomatchfanatic|              Comedy| 1.0866154682829339|       5|     14|\n""""
  },
  {
    "{": ""      ""|EY8wHzyB2kU|         grandehalo2|    Film & Animation| 0.9959387719482251|      24|     30|\n""""
  },
  {
    "{": ""      ""|FX_C_Na8zuo|ItsJustSomeRandomGuy|       Entertainment| 1.6769540489470274|    2454|   5894|\n""""
  },
  {
    "{": ""      ""|FZRV8biSZqU|           latiasman|       Entertainment| 0.3913682890776391|      74|     87|\n""""
  },
  {
    "{": ""      ""|GMqemXx1e9M|     tristarmedianet|       Entertainment| 0.8703953194902275|       2|      1|\n""""
  },
  {
    "{": ""      ""|GOxRUf5nk8w|            Vegarddd|       Entertainment|0.40106884694605843|      23|     19|\n""""
  },
  {
    "{": ""      ""|GV861m_qoBo|           jokalines|      People & Blogs|0.36220466037048954|       4|      1|\n""""
  },
  {
    "{": ""      ""|Gf4-Zo6cZjk|            isvetlac|       Howto & Style| 1.0944036774174948|      79|     71|\n""""
  },
  {
    "{": ""      ""|HDDyW2i8tqo|           jedreport|     News & Politics|0.44769261376070824|     139|    203|\n""""
  },
  {
    "{": ""      ""|HRH5-9R3Mrg|        SorrowExpert|               Music| 0.7313309580296906|      21|     10|\n""""
  },
  {
    "{": ""      ""|HojTAbv9S98|        love4musicuk|       Entertainment|  0.355430596425427|       1|      4|\n""""
  },
  {
    "{": ""      ""|IEW-xFyBiJs|              akayz7|       Entertainment|0.36162753119869945|       7|     13|\n""""
  },
  {
    "{": ""      ""|IqTGsdTAMK4|  mariaeferatapsaria|              Sports| 0.4081279287782587|      11|     34|\n""""
  },
  {
    "{": ""      ""|J7Yj__lNwEI|          jaffatyree|      People & Blogs|  0.355430596425427|       1|      4|\n""""
  },
  {
    "{": ""      ""|KpTG_2ahazc|          TinajeraNP|Science & Technology| 1.7225449116184712|     291|    101|\n""""
  },
  {
    "{": ""      ""|LSD1cBdeW1Q|  IceGiantNinetyNine|       Entertainment|  2.103178831992031|      29|     22|\n""""
  },
  {
    "{": ""      ""|LvGExBJXAGY|           edumusic2|               Music| 0.6254822001349536|       3|      2|\n""""
  },
  {
    "{": ""      ""|M4mRNpi5ZkM|          islamrocks|     News & Politics| 0.8725216122030741|      59|     33|\n""""
  },
  {
    "{": ""      ""|NWxY0b4kHY4|           ALDAG2008|              Comedy| 0.7922155075804642|      23|     16|\n""""
  },
  {
    "{": ""      ""|Nt9yl6jmjZQ|              kr338r|    Autos & Vehicles| 0.9333656567757416|      53|     46|\n""""
  },
  {
    "{": ""      ""|NwH80Xq0E6k|            dance2xs|    Film & Animation| 0.7585115689031273|     150|    428|\n""""
  },
  {
    "{": ""      ""|RUJU8NuM03I|            rusher01|       Entertainment| 0.3649905308240867|      45|     16|\n""""
  },
  {
    "{": ""      ""|S8gA1nigkKM|            tempantz|       Entertainment| 0.4768366304103318|       6|      6|\n""""
  },
  {
    "{": ""      ""|SwNtMp4bJQ0|       feocasagrande|              Sports| 0.4585514589065084|       5|      7|\n""""
  },
  {
    "{": ""      ""|T10ZP4CnSBY|        fingolfin897|    Film & Animation| 0.4219456763904147|      54|     49|\n""""
  },
  {
    "{": ""      ""|TIoqkTiOkFk|     HoshisamaValmor|       Entertainment|0.36052644995135125|      17|      9|\n""""
  },
  {
    "{": ""      ""|U3VRruGsncA|         sxychipmunk|       Entertainment|  0.355430596425427|       1|      0|\n""""
  },
  {
    "{": ""      ""|UunvybRGiB4|       vballgurl1413|       Entertainment| 0.5277810932123095|       8|      8|\n""""
  },
  {
    "{": ""      ""|VFUGZpKXWiI|              grbomr|       Entertainment|  1.937003572154508|      72|    128|\n""""
  },
  {
    "{": ""      ""|WFG1QJQXoeM|              kkdog0|              Sports| 0.6148698348749446|      42|     53|\n""""
  },
  {
    "{": ""      ""|WTVFi30vH48|              dellya|               Music| 1.0348869838537884|      16|     37|\n""""
  },
  {
    "{": ""      ""|X-6eayHPV14|         darthmilo77|    Film & Animation| 1.7946870786114542|     107|    103|\n""""
  },
  {
    "{": ""      ""|X4u76xPIohI|            memed136|               Music| 0.8294104439876475|      11|      4|\n""""
  },
  {
    "{": ""      ""|Xg-pevtEbTI|            tim49980|    Autos & Vehicles|0.46720315351680325|       1|      3|\n""""
  },
  {
    "{": ""      ""|YFZA6gRK4qs|   everythingdigital|       Entertainment| 2.2610449079455095|     481|    391|\n""""
  },
  {
    "{": ""      ""|YOucjGreZyI|           cassidy05|       Entertainment| 0.3615888363754839|      20|     35|\n""""
  },
  {
    "{": ""      ""|YRAcLPmq5M4|   RonPaul2008dotcom|     News & Politics|  0.380494849752574|    1178|   1775|\n""""
  },
  {
    "{": ""      ""|Yg8FT7Gg8O8|          triplex654|               Music| 1.2597776494540716|       7|     25|\n""""
  },
  {
    "{": ""      ""|Z6MLx4MzV5Y|       webmasterygow|    Film & Animation| 1.6022658253690991|      10|     80|\n""""
  },
  {
    "{": ""      ""|ZyDkHLrrRs4|              houney|      People & Blogs| 0.5766910717029067|      48|     27|\n""""
  },
  {
    "{": ""      ""|_bEXN51kX1E|        MagnumBradva|           Education|0.47589059984065696|       3|      3|\n""""
  },
  {
    "{": ""      ""|a9WB_PXjTBo|  McCaskill4Missouri|     News & Politics|  3.573375939663302|    6403|   5116|\n""""
  },
  {
    "{": ""      ""|beMZ-rWJAiA|              heyk07|       Entertainment| 1.2624317307828323|     119|     48|\n""""
  },
  {
    "{": ""      ""|cDcl3TWRhRw|          SallyJ2007|     News & Politics|0.49327228937577705|       8|      4|\n""""
  },
  {
    "{": ""      ""|czN9WtqeNwo|    NazgulzStreicher|    Film & Animation| 0.6997158733581974|      25|     83|\n""""
  },
  {
    "{": ""      ""|d9H9JbdMeS8|      lookuptothesky|    Film & Animation| 0.7614897000807898|      29|     18|\n""""
  },
  {
    "{": ""      ""|ewx9tEJJlWk|              wbeaty|       Howto & Style| 0.5577027105550992|      54|     60|\n""""
  },
  {
    "{": ""      ""|f2ePhsD04cw|            pressmin|       Entertainment| 0.9610573735635927|      18|      3|\n""""
  },
  {
    "{": ""      ""|f3f8TVflgUQ|        GrantDelmore|       Entertainment|  0.677910489616776|      87|     63|\n""""
  },
  {
    "{": ""      ""|f68Xh0yi5PY| casaevideoaglobocom|       Howto & Style| 0.7108157960173455|      10|      7|\n""""
  },
  {
    "{": ""      ""|fEyWCCgRn44|        FootRetro006|              Sports| 0.5386443603962988|       1|      3|\n""""
  },
  {
    "{": ""      ""|fLokV61JvDQ|    andrezabonekinha|     Travel & Events|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|ff3HiYrmrtM|              Bragic|              Comedy| 0.9156510537616825|     145|    152|\n""""
  },
  {
    "{": ""      ""|gXRd4BqCgf0|          fitnessvip|              Sports|   2.86443560767222|      46|     94|\n""""
  },
  {
    "{": ""      ""|ghbViUpzcDA|           kupatange|       Entertainment| 0.3603571883854725|       0|      1|\n""""
  },
  {
    "{": ""      ""|glfEQCWIAvw|     mrsnickjonas729|       Entertainment| 0.9233858693059742|     105|     30|\n""""
  },
  {
    "{": ""      ""|gvu5oTqSFEA|      HipHopForObama|               Music| 0.7083348150802227|      27|     21|\n""""
  },
  {
    "{": ""      ""|h38FFzRKeio|  Ashleytisdalerulez|              Comedy| 0.8054910205049713|      65|     92|\n""""
  },
  {
    "{": ""      ""|h58PiR15bn8|            racks274|       Entertainment| 0.3631430588390696|      12|     47|\n""""
  },
  {
    "{": ""      ""|iZ1cTOEezCU|JohnfrelLuvsMariePaz|               Music| 0.6704655085839009|      15|      5|\n""""
  },
  {
    "{": ""      ""|iatxVlqQTcc|              L7slap|               Music|0.49677630743501555|       5|     22|\n""""
  },
  {
    "{": ""      ""|jI76QY3RnSA|           avrilelif|               Music| 0.4871984268413877|      24|     31|\n""""
  },
  {
    "{": ""      ""|jq3utBjiYuA|          Politicstv|     News & Politics| 0.9397124824635351|     343|    120|\n""""
  },
  {
    "{": ""      ""|jqzM36C3H7Q|        diegogvieira|     Travel & Events| 1.5812303473649019|      72|     61|\n""""
  },
  {
    "{": ""      ""|k3BS_RYxBVM|      johnjayandrich|       Entertainment|  0.908452906420358|       1|      3|\n""""
  },
  {
    "{": ""      ""|kQ1ruRlUz_k|       nspimpette281|               Music| 1.4753516520233216|     123|    173|\n""""
  },
  {
    "{": ""      ""|lOOaDEyavMw|    CountDooku4UTube|              Comedy| 0.8431148084928676|     102|    127|\n""""
  },
  {
    "{": ""      ""|lrHuFoUYEWU|   Robbie2001Terrier|       Entertainment| 0.8585869505784817|      30|     26|\n""""
  },
  {
    "{": ""      ""|mc6IIR9CFCo|              sjp318|               Music| 0.5174611082778775|      16|     15|\n""""
  },
  {
    "{": ""      ""|mwYy17evcUY|           seanp3688|               Music| 0.5410391430547344|      34|     49|\n""""
  },
  {
    "{": ""      ""|nFsJFKyIAiY|           missjeida|               Music| 1.6358536709099822|      64|     79|\n""""
  },
  {
    "{": ""      ""|np8NYfRNTAU|          Videosport|              Sports|0.48886051702909417|      15|     13|\n""""
  },
  {
    "{": ""      ""|o_S6Fc37_jo|             mmcs122|               Music| 1.1585524003572274|      60|     66|\n""""
  },
  {
    "{": ""      ""|p07k8lZpgi4|             guns777|      Pets & Animals|  0.847870177448837|       3|     11|\n""""
  },
  {
    "{": ""      ""|pYXKhEhlJ_4|         HimeAlexjia|    Film & Animation| 0.5995440807861838|       9|     30|\n""""
  },
  {
    "{": ""      ""|pZVdqM8H_Ck|              ajschw|       Howto & Style|0.36836290032054647|       4|      7|\n""""
  },
  {
    "{": ""      ""|qAzphE8utHk|            Gerome84|    Film & Animation|0.47105555425727724|       6|      8|\n""""
  },
  {
    "{": ""      ""|qDQwc-jbhrA|              Smoged|       Entertainment|  0.355430596425427|       1|      0|\n""""
  },
  {
    "{": ""      ""|qFONmKZdTQo|            comadano|      Pets & Animals| 2.8834220353664195|     437|    682|\n""""
  },
  {
    "{": ""      ""|qf3B7iK3zHg|      jenzaxxxxxxxxx|               Music| 0.7905235778783625|      11|     11|\n""""
  },
  {
    "{": ""      ""|qhULtiwNCCs|             stvideo|     News & Politics| 0.4295212159449258|      14|      2|\n""""
  },
  {
    "{": ""      ""|rJWE7fJe5iI|         PTASasa2007|       Entertainment|0.49053106923568124|       9|      4|\n""""
  },
  {
    "{": ""      ""|rnMp9a-Kme0|           spdfrkaby|    Autos & Vehicles| 0.7513643009019032|       4|      5|\n""""
  },
  {
    "{": ""      ""|saJp_tTFy6U|           SoulSeeek|       Entertainment|  0.768756137359254|      97|    158|\n""""
  },
  {
    "{": ""      ""|smsBYJu08bk|          kikikikidd|       Entertainment| 0.6862069658590579|       5|      5|\n""""
  },
  {
    "{": ""      ""|spnmE79W1D0|           eshteni23|               Music|0.45595843327357255|      27|      5|\n""""
  },
  {
    "{": ""      ""|-waYC57znvA|           mirisca87|    Autos & Vehicles| 2.0096227929064763|       6|      4|\n""""
  },
  {
    "{": ""      ""|0Hk7IUgVrFs|          hyperhighs|       Entertainment| 0.5558811601750171|      12|      8|\n""""
  },
  {
    "{": ""      ""|tj-GMIsr9tk|         Daniel39363|    Film & Animation| 0.9319860093680984|      49|     25|\n""""
  },
  {
    "{": ""      ""|0qnF_dYdrvw|       SanteCookware|       Howto & Style| 0.6552985581591684|       0|      2|\n""""
  },
  {
    "{": ""      ""|umv9WeZkdSM|  UnionCountyRealtor|      People & Blogs| 0.3675906765807774|       0|      0|\n""""
  },
  {
    "{": ""      ""|1w8EokOBbBY|              CDN992|              Comedy|0.43400530656846836|       1|      5|\n""""
  },
  {
    "{": ""      ""|vWX_OAcFjK8|            liverach|               Music|  9.364701662662354|    1247|   1475|\n""""
  },
  {
    "{": ""      ""|2bJ93BIzUi4|    tookieclothespen|               Music| 0.3957300393670063|      34|     21|\n""""
  },
  {
    "{": ""      ""|wCBKoXOYsD0|          harmypochi|               Music| 0.5511389483082443|       2|      9|\n""""
  },
  {
    "{": ""      ""|xCpEcHya7Jk|           GunmanRAC|      People & Blogs|  3.111295863431828|     693|    165|\n""""
  },
  {
    "{": ""      ""|2leMBcyHewo|    HAWAiiANPLAYBOii|              Sports| 0.4917496368965554|       1|      0|\n""""
  },
  {
    "{": ""      ""|xCrz9gwjpH4|         magocalipso|       Howto & Style| 0.7640869206609304|       3|      6|\n""""
  },
  {
    "{": ""      ""|32wmKpshu1g|  jazzmanjamesbailie|      People & Blogs| 0.5423046502267714|      24|     13|\n""""
  },
  {
    "{": ""      ""|yj91xOewR1s|            estealer|                 UNA| 1.2316228569238559|       9|     22|\n""""
  },
  {
    "{": ""      ""|3veAHvjRpFk|             PippVid|              Comedy| 0.9131500973856451|      19|     22|\n""""
  },
  {
    "{": ""      ""|z6VVELKyhOg|            rzapatav|       Howto & Style| 2.0823603010298037|      47|     34|\n""""
  },
  {
    "{": ""      ""|423B2vi-9Qg|              cokenl|     News & Politics|  0.568170923525378|       1|      1|\n""""
  },
  {
    "{": ""      ""|zAlnNw9JgpM|              pauliu|       Entertainment| 0.7899030593221251|       2|      0|\n""""
  },
  {
    "{": ""      ""|4HsYsix2gqs|            marjac06|    Autos & Vehicles| 2.3682760774418736|      51|     25|\n""""
  },
  {
    "{": ""      ""|z_dI6Q0cGIA|          rojomalaya|               Music| 1.4148148434408618|      69|    118|\n""""
  },
  {
    "{": ""      ""|4K1rIOqczcU|     welshraider2007|              Comedy|0.43348352389172706|       0|      0|\n""""
  },
  {
    "{": ""      ""|-E0NniVfUyM|      celsoarrudinha|               Music|0.37008343422600687|       1|      4|\n""""
  },
  {
    "{": ""      ""|4ltZOa33oYQ|     witchfairyangel|       Entertainment|  5.451846617859313|    1157|    559|\n""""
  },
  {
    "{": ""      ""|-lWpS7NN3SY|            roschler|      Pets & Animals| 1.2895092502261336|      29|     24|\n""""
  },
  {
    "{": ""      ""|5wtZX1i6OYc|            ant62791|              Comedy|  1.452356071660184|     190|    207|\n""""
  },
  {
    "{": ""      ""|0RkA66YIcEU|             realmcf|              Sports| 0.5003303599561767|       2|      2|\n""""
  },
  {
    "{": ""      ""|7uH6jfn7K1A|      sadjohnson1980|               Music| 0.6857351414804139|       3|      2|\n""""
  },
  {
    "{": ""      ""|0S9i9CtAhdY|            UniChild|       Entertainment|0.45084379753398185|     305|    277|\n""""
  },
  {
    "{": ""      ""|910R7prXhgQ|   BarackObamadotcom|     News & Politics| 0.4685458050785937|       6|     28|\n""""
  },
  {
    "{": ""      ""|0gK7db8DcpI|         Reemasbxnni|    Autos & Vehicles|  0.365283780345518|       0|      1|\n""""
  },
  {
    "{": ""      ""|9EvIQLgyFTM|            terman91|      Pets & Animals| 0.4601819951662434|       0|      4|\n""""
  },
  {
    "{": ""      ""|0ncvaAIeEDA|           fantachan|       Entertainment|  6.518752277735896|    1187|    963|\n""""
  },
  {
    "{": ""      ""|9Lwi1zGqkdA|          nojahbloke|     Travel & Events| 0.9425316409385771|      50|    121|\n""""
  },
  {
    "{": ""      ""|1-DLlE0FiJc|         darkghost08|              Comedy|  0.646030288819373|      23|     41|\n""""
  },
  {
    "{": ""      ""|9ikxZ81Ia8s|               eketc|       Entertainment| 0.5261529431128752|      65|     54|\n""""
  },
  {
    "{": ""      ""|1dvHkcH6VP0| thesubscribermaniac|     Travel & Events| 0.3766450990662587|       6|      2|\n""""
  },
  {
    "{": ""      ""|A6FCKD-_KRU|         batchoflies|               Music| 0.7950571364258949|     551|    401|\n""""
  },
  {
    "{": ""      ""|243wjJ_Z8yI|             beebcaz|    Film & Animation| 1.4879147140858022|      21|     54|\n""""
  },
  {
    "{": ""      ""|A8TjUA5ccaU|            McOshrit|               Music| 1.7523200984793637|     534|    757|\n""""
  },
  {
    "{": ""      ""|2mHm7G52xhY|           heidiseal|      People & Blogs|  0.570763933028586|      64|     38|\n""""
  },
  {
    "{": ""      ""|ABOB0DvddYc|             avex001|               Music|  0.513163475651528|       3|      1|\n""""
  },
  {
    "{": ""      ""|3cdFTQNzhmI|        WarlockWeary|       Howto & Style| 0.4297923133016436|       9|      4|\n""""
  },
  {
    "{": ""      ""|AKRJ_uHQFGU|          Gaming4you|       Entertainment| 1.2639903341033472|      74|     38|\n""""
  },
  {
    "{": ""      ""|3yeynGb4tGY| universalmusicgroup|               Music|  9.232512918676296|    1520|   3326|\n""""
  },
  {
    "{": ""      ""|B8Vk4lrVog8|          BetterLord|              Comedy|0.36431605692479474|       0|      3|\n""""
  },
  {
    "{": ""      ""|41sDKTzjk2g|       DAVIDOVZEMOON|               Music| 0.7344737292278619|       3|      0|\n""""
  },
  {
    "{": ""      ""|BWgO__RG3M4|  VoteForCommonSense|     News & Politics| 0.7364392474195771|     817|    613|\n""""
  },
  {
    "{": ""      ""|4akklIFFjYg|         Saalvatorio|    Film & Animation| 0.3916587128210897|       8|      4|\n""""
  },
  {
    "{": ""      ""|BowviqrxyWE|            zacE1fan|       Entertainment| 1.0244704655180252|     238|     62|\n""""
  },
  {
    "{": ""      ""|5AUI-GpPIcI|             eorelly|      People & Blogs|0.36138356171048197|       1|      0|\n""""
  },
  {
    "{": ""      ""|Bz6CP30hN9Y|   07RonaldoTorres09|              Sports| 1.1735889233955292|      43|     80|\n""""
  },
  {
    "{": ""      ""|5wr5zead_4s|             BravoTV|      People & Blogs| 0.6250384496193115|      44|     94|\n""""
  },
  {
    "{": ""      ""|6pcRpyRnSnc|   preciousKnowledge|     News & Politics|    2.0938952929492|    1306|    196|\n""""
  },
  {
    "{": ""      ""|ChmZ-qz0xQo|              lald04|               Music| 0.7150334606969296|      53|     68|\n""""
  },
  {
    "{": ""      ""|77ZugJzjFwg|      goblinthruster|       Entertainment| 0.5244782557641788|      18|     29|\n""""
  },
  {
    "{": ""      ""|D47oy8IZSK8|             ZteCh93|              Comedy| 0.4121649025559188|      32|     37|\n""""
  },
  {
    "{": ""      ""|7D56N6fA9Ys|             colt605|       Howto & Style| 0.4213017038308825|       8|      4|\n""""
  },
  {
    "{": ""      ""|8KWzKsB6jGg|          NoelieAlex|               Music| 1.4976561520495655|     170|    318|\n""""
  },
  {
    "{": ""      ""|D9WXkQeXQyQ|             edsslbr|      People & Blogs| 0.7405258763715875|      77|    352|\n""""
  },
  {
    "{": ""      ""|8gTKvy_wpDI|           FSNOBREGA|       Howto & Style| 1.0078689575167687|      67|     93|\n""""
  },
  {
    "{": ""      ""|DF0Ggc3iZmk|             RikoEoS|       Entertainment|0.38441054913157696|       2|      1|\n""""
  },
  {
    "{": ""      ""|8iU-zU3MDTU|           mujganbey|               Music|   0.97255569169552|      40|     43|\n""""
  },
  {
    "{": ""      ""|DI4-l8OS06s|         buddadude99|    Autos & Vehicles|  0.765315822863772|      93|     38|\n""""
  },
  {
    "{": ""      ""|9gW02XQyxhs|            OckMan27|              Comedy| 0.4032873501437528|       1|     10|\n""""
  },
  {
    "{": ""      ""|EAkFWZ9CaR0|          yenisafak9|      Pets & Animals|  0.673325702580456|       0|     89|\n""""
  },
  {
    "{": ""      ""|A2n-_FZhb3o|             TerrMys|     Travel & Events| 1.6533680025523942|      71|     81|\n""""
  },
  {
    "{": ""      ""|EOyH98fl65w|              MjOoPi|    Film & Animation| 0.4068357371155655|      25|     18|\n""""
  },
  {
    "{": ""      ""|AOL0y541Y2o|              Adnoku|              Comedy| 0.3676228433552059|       5|      4|\n""""
  },
  {
    "{": ""      ""|EWw7QncBGSM|               DCCRA|     News & Politics|  0.355430596425427|      34|     43|\n""""
  },
  {
    "{": ""      ""|ASYfkvxRuxA|        Violator6996|               Music| 0.4417046544540903|       2|      1|\n""""
  },
  {
    "{": ""      ""|B3ukU2Q4crU|         JinThePanda|              Comedy|0.47572343384567484|       5|     10|\n""""
  },
  {
    "{": ""      ""|EZCe6-6C5pc|          farmsystem|              Sports| 0.6980802214604469|      13|      4|\n""""
  },
  {
    "{": ""      ""|Bbt3DjmN--4|            matt4045|    Film & Animation|  6.123455582948446|    2466|   1780|\n""""
  },
  {
    "{": ""      ""|EapNwQTL49M|      MysticalPigeon|       Entertainment| 0.4248493730329492|       7|      2|\n""""
  },
  {
    "{": ""      ""|C5L90-eMgH8|    Cassthegothangel|              Sports|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|F4vCsXR3KAc|            llVickll|       Entertainment|  0.355430596425427|      10|     26|\n""""
  },
  {
    "{": ""      ""|C6-krfaWHeM|           jenard007|       Entertainment| 0.6598069061033787|       3|      1|\n""""
  },
  {
    "{": ""      ""|FFMQnkGjyJQ|   prehistoricpetstv|      Pets & Animals| 0.7855255753591268|       8|      5|\n""""
  },
  {
    "{": ""      ""|CTWl9sR0dCk|           Gemificus|    Film & Animation|0.42517624948123645|       0|      0|\n""""
  },
  {
    "{": ""      ""|FiHL1CjYrgA|   speculativebubble|     News & Politics| 0.6538908297482708|      23|     32|\n""""
  },
  {
    "{": ""      ""|DAOGBZhyqGA|       Bananakaulitz|       Entertainment| 1.0256610343573862|      82|    114|\n""""
  },
  {
    "{": ""      ""|G1r206kxYxE|            cchrisjk|      People & Blogs|0.42691792976163323|       0|      0|\n""""
  },
  {
    "{": ""      ""|Da9jVVTf8JQ|      andymcgaffigan|      People & Blogs| 0.4167151943286597|      50|     50|\n""""
  },
  {
    "{": ""      ""|GQAkvo0-luI|            chiszle1|               Music| 0.5789416561933888|      13|     31|\n""""
  },
  {
    "{": ""      ""|E110HOH79-w|               Zjiin|       Entertainment| 0.4366518823165179|      12|      8|\n""""
  },
  {
    "{": ""      ""|GR-IURK0D_4|             gardima|              Comedy| 0.5621180341217471|       8|     11|\n""""
  },
  {
    "{": ""      ""|EbIvQIugKrg|              gmougy|      People & Blogs|  0.355430596425427|       0|      2|\n""""
  },
  {
    "{": ""      ""|GrTL6dKmfOo|            scotskid|       Howto & Style| 0.6263695201243131|      83|     40|\n""""
  },
  {
    "{": ""      ""|EchTxGYqLS8|          martamarta|               Music|  5.141661742992397|    1681|   1654|\n""""
  },
  {
    "{": ""      ""|HCPsBMhwesI|          brazdaikis|    Autos & Vehicles| 0.6241243027757497|      62|     60|\n""""
  },
  {
    "{": ""      ""|Emf-rwlo4jc|          darkdrinni|               Music|0.36220466037048954|       1|      0|\n""""
  },
  {
    "{": ""      ""|IH9BkQon0HM|         heyelefante|      People & Blogs| 0.5996884199162497|      39|     21|\n""""
  },
  {
    "{": ""      ""|EqmeFXVDCQ8|        ErikMcLennan|               Music|  1.207487334161541|      65|     68|\n""""
  },
  {
    "{": ""      ""|J-tvgtBaMUQ|      FoxSearchlight|              Comedy| 0.6097974355963135|      15|     28|\n""""
  },
  {
    "{": ""      ""|Ev0IKa18_2U|         lockergnome|       Howto & Style|0.37470253671736176|      35|     18|\n""""
  },
  {
    "{": ""      ""|JMvACD4YVII|             embplus|     News & Politics| 0.4585031906799044|      72|    157|\n""""
  },
  {
    "{": ""      ""|ExxvBiqDBkE|          gnarlyboy5|       Entertainment|0.48582299273131957|      22|     20|\n""""
  },
  {
    "{": ""      ""|FRe0rsXfe4Q|             wowclpe|       Howto & Style| 0.3876506643368029|       1|      0|\n""""
  },
  {
    "{": ""      ""|JWxx5YRsa1Y|              elpamd|     News & Politics| 0.7497091132789842|     113|     42|\n""""
  },
  {
    "{": ""      ""|Fob-U-jdMjE|             Yarpeth|              Sports| 0.8153275135832997|      24|     16|\n""""
  },
  {
    "{": ""      ""|K1A5H_i9gQE|         dragonmodes|              Comedy| 0.4742934092653748|       1|      0|\n""""
  },
  {
    "{": ""      ""|GKmX4zMOi2o|         tvgrapevine|       Entertainment| 0.5434412711616157|       0|      2|\n""""
  },
  {
    "{": ""      ""|Kmi_Xz8AvKA|             pealoaf|      People & Blogs| 0.4247250951823362|      13|     17|\n""""
  },
  {
    "{": ""      ""|HG7JviIqf4E|           flygirlll|               Music|0.36041583828975876|       0|      1|\n""""
  },
  {
    "{": ""      ""|L3B07ahkTgI|            punihser|              Sports| 1.8578924381313546|      29|     45|\n""""
  },
  {
    "{": ""      ""|ID2BEXJ4IKc|               KurtH|       Entertainment| 0.9420658159518177|     113|    156|\n""""
  },
  {
    "{": ""      ""|L8BWe31fTBY|        10centwonder|    Autos & Vehicles| 1.0250922578866482|       3|      2|\n""""
  },
  {
    "{": ""      ""|IENeaYTAMKo|             abbtech|       Howto & Style|  1.030601985530161|      21|     29|\n""""
  },
  {
    "{": ""      ""|LX80eY_bmcg|          cris7geo93|              Sports| 0.5601958121981897|       7|      8|\n""""
  },
  {
    "{": ""      ""|IPgL6T2Lf3Y|      soyuncerdoyque|               Music|0.49452623728536077|      20|      7|\n""""
  },
  {
    "{": ""      ""|LhBz9OXy8SQ|           kornelbmx|    Autos & Vehicles| 0.3853868975382246|       2|      0|\n""""
  },
  {
    "{": ""      ""|IapuO_KwQ_s|           remlinger|      People & Blogs|  1.708770212548531|     217|    104|\n""""
  },
  {
    "{": ""      ""|JOAXGLdpja0|             Hookytr|              Sports| 0.5312536706079513|       1|      0|\n""""
  },
  {
    "{": ""      ""|Lj2_bUhFOhs|       Marsipaanikko|       Entertainment| 0.5210421721175973|      21|     70|\n""""
  },
  {
    "{": ""      ""|JlwJMKuQKzs|         elcarachero|    Film & Animation|0.45603447709684974|      14|     29|\n""""
  },
  {
    "{": ""      ""|MT9eT9Rm4Yc|            S1CKSHO7|       Entertainment| 0.7236465454754872|      53|     36|\n""""
  },
  {
    "{": ""      ""|K5R-8O9-MTk|          zackdotcom|              Comedy| 0.4513993202277971|      14|     29|\n""""
  },
  {
    "{": ""      ""|KfJKTosmul8|            davido83|       Entertainment| 0.7722991391943709|     172|    116|\n""""
  },
  {
    "{": ""      ""|MTR0ktKTmKk|            Bazhenov|              Sports|  2.452646467021393|      79|    107|\n""""
  },
  {
    "{": ""      ""|Kq2troZCzBg|             sexolon|       Entertainment| 1.0243819990521426|      69|     52|\n""""
  },
  {
    "{": ""      ""|MjW62XH6_Sc|      LmfaoXDlink182|      People & Blogs| 0.3747410774116767|       2|      5|\n""""
  },
  {
    "{": ""      ""|LfZ_dxt8MlM|       heathywhodini|      People & Blogs| 2.7531624833996395|      30|    105|\n""""
  },
  {
    "{": ""      ""|O4kDC4sZ5Jg|          jackdakota|       Howto & Style| 2.9631652318455886|     970|    297|\n""""
  },
  {
    "{": ""      ""|PAF6VZQamtw|            Ninjando|               Music| 2.2366143778446217|     119|    311|\n""""
  },
  {
    "{": ""      ""|PzMZB0svIe0|              englew|     News & Politics| 0.3698866917378589|       3|      0|\n""""
  },
  {
    "{": ""      ""|RIzLsW0kr8I|       janestripalot|       Entertainment| 0.3876305438767047|       0|      1|\n""""
  },
  {
    "{": ""      ""|RPQxnhw0TNA|              azul86|       Entertainment| 0.9678662685919098|      16|     13|\n""""
  },
  {
    "{": ""      ""|SHY2GyEE1LU|      AeternusPulvia|      People & Blogs|  0.857925379279906|     167|    102|\n""""
  },
  {
    "{": ""      ""|SdRh2tcPVaw|      FreshMagonline|               Music|  0.789051338184307|      14|     46|\n""""
  },
  {
    "{": ""      ""|TUmql3SiAaI|            tempantz|       Entertainment| 1.0170009078370377|      14|      5|\n""""
  },
  {
    "{": ""      ""|U0-TPvMpmyk|        valentinya84|      People & Blogs|  0.355430596425427|       2|      0|\n""""
  },
  {
    "{": ""      ""|UgIpH7aPC_E|             ara3128|               Music|  0.714056356621005|      12|     15|\n""""
  },
  {
    "{": ""      ""|UgWm7wgSHJs|ladieswrestlingvideo|       Entertainment| 0.6463671293491715|       1|      4|\n""""
  },
  {
    "{": ""      ""|VvBp31vX8Ok|        Carcus0fh3ll|       Entertainment| 0.4199968228747194|      13|     13|\n""""
  },
  {
    "{": ""      ""|Wt-4RLwkwGU|         davidnmiers|       Entertainment|  0.355430596425427|      11|      9|\n""""
  },
  {
    "{": ""      ""|Wx98RDOTCMU|              DJGRIN|               Music| 0.7680080493160509|      18|     51|\n""""
  },
  {
    "{": ""      ""|XYQ2aoFKLvo|               E4U78|               Music| 1.1884497345301457|      35|     62|\n""""
  },
  {
    "{": ""      ""|XhoOo9IEeTs|           TheHill88|      People & Blogs|  1.084160108626147|    1768|   1976|\n""""
  },
  {
    "{": ""      ""|YGhy7yIr8L4|         lockergnome|       Howto & Style| 0.7931867698028485|      51|     31|\n""""
  },
  {
    "{": ""      ""|YLugCoKQ1oE|           08tornado|               Music| 0.4845870293985137|       0|      1|\n""""
  },
  {
    "{": ""      ""|-00-_f5Fams| JoBrosAwsomeness333|       Entertainment| 0.5108408607190752|      11|      3|\n""""
  },
  {
    "{": ""      ""|YPiAXvgD--0|          jaggededge|               Music|  2.470379213736146|      35|    147|\n""""
  },
  {
    "{": ""      ""|YXlzZOGGNEM|           lambiorix|              Sports| 0.4096673283404846|       0|      0|\n""""
  },
  {
    "{": ""      ""|-3Y0g5xqZbo|            luyt4her|              Sports| 0.8150111693086274|      30|     62|\n""""
  },
  {
    "{": ""      ""|Z4uyPRj38LU|         bigboyburge|     Travel & Events| 0.4942172782308289|       0|      2|\n""""
  },
  {
    "{": ""      ""|-bKWzJUt5To|              vamshe|              Comedy| 0.5249125634589584|       0|      4|\n""""
  },
  {
    "{": ""      ""|Zi-geqKxxrk|         schmittharv|               Music| 0.6574571590885642|      11|      7|\n""""
  },
  {
    "{": ""      ""|-qA6pN1aeZ4|           airthugg1|              Sports| 1.5647535803327515|      29|     62|\n""""
  },
  {
    "{": ""      ""|_NwVRFhR8TI|       peskeyplumber|               Music| 0.4943435035268404|      49|     67|\n""""
  },
  {
    "{": ""      ""|00YfdSM9ZGU|            snkkid95|       Entertainment| 3.3587012897483106|      97|     87|\n""""
  },
  {
    "{": ""      ""|_a4MZN2Z9Ys|        Pr2dafullest|       Entertainment| 0.5445839681105925|      18|     15|\n""""
  },
  {
    "{": ""      ""|0lYhNt5WBT4|             jelie2k|       Entertainment| 2.4626823507340716|     290|    122|\n""""
  },
  {
    "{": ""      ""|a24fzD-aSVQ|         FifthDegree|               Music| 0.6271206221344146|      88|     87|\n""""
  },
  {
    "{": ""      ""|0uqlATsFxbE|          joseph17ph|               Music|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|aHFtYjKybko|           gyahahaha|    Film & Animation|  7.470901605878261|     104|    233|\n""""
  },
  {
    "{": ""      ""|aaaTLq20x9A|         allchevelle|               Music| 0.8550482873944656|      57|     77|\n""""
  },
  {
    "{": ""      ""|1MhKdHeyvzI|           Stompdown|               Music| 0.7499851789532591|      51|     56|\n""""
  },
  {
    "{": ""      ""|b94bugnp63k|         tubedoorman|              Comedy|  1.917664101238304|      17|     16|\n""""
  },
  {
    "{": ""      ""|1QejepYJaJ0|          rickey1037|           Education| 0.9093070623709334|      33|     44|\n""""
  },
  {
    "{": ""      ""|c2eO65BqxBE|          Dulcimerea|               Music| 0.5572964097111305|       4|      5|\n""""
  },
  {
    "{": ""      ""|1s0BlSSk-94|       andresagbisit|              Comedy| 1.3918327505943098|      99|    127|\n""""
  },
  {
    "{": ""      ""|c6cgKEh_aYc|    JordanRutledge01|       Entertainment|0.40460164118071296|       3|      3|\n""""
  },
  {
    "{": ""      ""|21GDi-1T_QM|             BLUETIB|     News & Politics| 0.3627752031893919|       2|     11|\n""""
  },
  {
    "{": ""      ""|dYANTO-yNn4|    reinforcepunch20|      People & Blogs| 0.5079428457510065|       2|      5|\n""""
  },
  {
    "{": ""      ""|36vrXC2g62o|           edwinmino|      People & Blogs|0.36548905501051987|       2|      1|\n""""
  },
  {
    "{": ""      ""|dnE-b5pppa4|             tulatix|    Film & Animation| 0.6215247633291925|       5|      5|\n""""
  },
  {
    "{": ""      ""|37VQMiFyzW4|          stopdont94|              Comedy|  0.355430596425427|       3|      3|\n""""
  },
  {
    "{": ""      ""|dvUZQhUdPA8|       SilentChicano|      People & Blogs| 1.4282433102487064|    1171|    227|\n""""
  },
  {
    "{": ""      ""|3Z_J_9EMYKk|           calumweir|       Entertainment| 0.3790485935724093|       5|      6|\n""""
  },
  {
    "{": ""      ""|evKOVYh8TKw|           knrdodson|      Pets & Animals| 3.2772968280751735|     477|    688|\n""""
  },
  {
    "{": ""      ""|3uoD2cqquhg|        datenkrieger|       Entertainment| 1.1503280487868917|     159|    271|\n""""
  },
  {
    "{": ""      ""|fotdoNIyL-U|        shemalevicki|                 UNA| 0.4132255934969202|       9|     27|\n""""
  },
  {
    "{": ""      ""|3vckkFHa_ww|           mrvegas76|       Entertainment|  0.653284666901847|      25|     29|\n""""
  },
  {
    "{": ""      ""|gRvuPRqzTyg|           theanosyl|               Music|0.40488499289155727|       0|      0|\n""""
  },
  {
    "{": ""      ""|40jEs-ZPg7g|           oregonzoo|      Pets & Animals|0.38091236285248137|       0|      2|\n""""
  },
  {
    "{": ""      ""|gUMdPXZQiF8|         dannagarcia|       Entertainment| 0.6854527245041779|       1|      7|\n""""
  },
  {
    "{": ""      ""|4eaVv-gwt_c|            kamaka69|      People & Blogs| 0.4882006467991165|       0|      7|\n""""
  },
  {
    "{": ""      ""|i8LP5kZt40A|         selvatico66|     News & Politics| 0.4508482831385292|      96|      5|\n""""
  },
  {
    "{": ""      ""|4h4uTh98cVE|         issamoffice|               Music|0.36976974610156677|       6|      6|\n""""
  },
  {
    "{": ""      ""|52Ex6jZVaMI|           SPGDUNDGC|               Music| 0.4721171684987103|      14|     12|\n""""
  },
  {
    "{": ""      ""|jDNZiHn_J_4|       Sladeakakevin|              Comedy| 0.7288940357849293|     996|   1236|\n""""
  },
  {
    "{": ""      ""|69GDZFkQz0M|           javachava|       Entertainment| 1.3768380335139063|     270|    230|\n""""
  },
  {
    "{": ""      ""|jVS6DMN3Iiw|       Yoshipower321|    Film & Animation| 1.8479782686888135|      13|     14|\n""""
  },
  {
    "{": ""      ""|6ItDy0ntxWc|            mikereka|               Music|0.42900210969368807|       1|      0|\n""""
  },
  {
    "{": ""      ""|kmhyJia66gc|inlineperformancemag|    Autos & Vehicles|0.39504568553430136|       3|      3|\n""""
  },
  {
    "{": ""      ""|6dOSBlYebeM|            jagungj2|Nonprofits & Acti...| 0.7514732497832762|       2|      1|\n""""
  },
  {
    "{": ""      ""|kuVyBJPM4QY|          Smackfan01|      Pets & Animals|0.43284454903199127|       1|      1|\n""""
  },
  {
    "{": ""      ""|6eV_Akca32E|        doomsday8822|     News & Politics| 0.3876305438767047|       8|      8|\n""""
  },
  {
    "{": ""      ""|lPwxD94IBkE| xrockxxandxxrollerx|               Music|  1.143315185511536|     122|    188|\n""""
  },
  {
    "{": ""      ""|7BIOyrz0SDE|             lrintel|              Sports| 1.0776272645303755|      12|     35|\n""""
  },
  {
    "{": ""      ""|lZQgx6m1M2E|                ldbl|               Music| 0.6253513926148948|      26|     98|\n""""
  },
  {
    "{": ""      ""|7a-c_LfbcZ0|  EdgarSamuelAguilar|      People & Blogs| 0.3612027245055993|       4|      2|\n""""
  },
  {
    "{": ""      ""|8V_wvI1BHCc|         AnneMarie96|       Howto & Style| 0.3712323024560058|       2|      1|\n""""
  },
  {
    "{": ""      ""|lbjssBySHCg|       thehooligan86|              Comedy|  3.637310840994359|     174|    483|\n""""
  },
  {
    "{": ""      ""|8XUhbxpADDE|           Ycaroh130|       Entertainment| 1.2401879924349062|      30|     15|\n""""
  },
  {
    "{": ""      ""|lvRJEWHzGTo|              kenada|       Entertainment| 1.0000493724509876|      71|    137|\n""""
  },
  {
    "{": ""      ""|8jZHeUxqc2Y|           ella13579|               Music| 0.4739562507246917|       6|      3|\n""""
  },
  {
    "{": ""      ""|m-SnifDwLtQ|     freedrumlessons|               Music|0.40695373497762877|       4|     12|\n""""
  },
  {
    "{": ""      ""|904hNkX7gck|         countconner|              Comedy| 0.5972895132084463|      18|     15|\n""""
  },
  {
    "{": ""      ""|m2G5bldFBPY|         xjjeepthing|              Comedy| 0.9059666274366175|      35|     30|\n""""
  },
  {
    "{": ""      ""|9cZncmjmc2c|              hujgup|               Music|  0.355430596425427|      13|     18|\n""""
  },
  {
    "{": ""      ""|AZNf-77IyCQ|            kelp2006|       Howto & Style|0.48409686525948065|       6|      4|\n""""
  },
  {
    "{": ""      ""|m7K41nsLKjs|            sunergy1|     News & Politics| 0.5665282627756036|      20|     10|\n""""
  },
  {
    "{": ""      ""|BEYBkFP9Otw| danielradcliffekath|               Music|   0.69064791169311|       1|      3|\n""""
  },
  {
    "{": ""      ""|nU4vVdLj-0o|            anitasm3|       Entertainment| 0.5687203899761766|      10|     14|\n""""
  },
  {
    "{": ""      ""|BUVZ-rET-YM|          tifatifatm|               Music| 1.1617790614194685|      25|     31|\n""""
  },
  {
    "{": ""      ""|nbrf9r5Kh1E|             alhabon|     News & Politics| 0.6726211821687139|       6|      3|\n""""
  },
  {
    "{": ""      ""|BaE-fcyxpK4|         Marioman555|       Entertainment| 0.9361972008780295|      51|     43|\n""""
  },
  {
    "{": ""      ""|nstdrTbAC_c|        VcodersMedia|     News & Politics|   0.36899053241816|       0|      0|\n""""
  },
  {
    "{": ""      ""|NeT5Lh7EY6c|          Razor61289|              Comedy|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|C9PFSsWYSBM|         heartgeiger|      People & Blogs| 0.4107031378023195|       5|      3|\n""""
  },
  {
    "{": ""      ""|obUdP9vYp2U|           caldera11|    Autos & Vehicles| 0.3759922753697836|      14|     12|\n""""
  },
  {
    "{": ""      ""|CIbb42a6K4I|         FLAWLESS100|               Music| 2.2507636146019028|     449|    339|\n""""
  },
  {
    "{": ""      ""|Cz6mmg55PzU|      PoliticalRealm|     News & Politics|0.38531842841919367|       0|      1|\n""""
  },
  {
    "{": ""      ""|ofa1mHBIRzY|           crabdroid|       Entertainment| 1.0221346199844707|       8|     18|\n""""
  },
  {
    "{": ""      ""|NhHfDh6Uxgw|       expertvillage|       Howto & Style| 0.4793190046546594|       3|     15|\n""""
  },
  {
    "{": ""      ""|D56eqccL9L4|              Maffew|              Sports| 1.2944319959397355|     580|    572|\n""""
  },
  {
    "{": ""      ""|pAzZ0GVlmwM|       slagathor2112|               Music| 1.2471292806497254|     427|    379|\n""""
  },
  {
    "{": ""      ""|DZ-LVUB5ItE|       MagicianJonny|       Entertainment|0.45198487811926397|       4|      6|\n""""
  },
  {
    "{": ""      ""|NtNAw1PAAEo|      techvids052006|       Entertainment| 0.8180731220834604|      14|      0|\n""""
  },
  {
    "{": ""      ""|pEbK3C7bZxU|      xsmartfood007x|               Music| 1.1678383964622343|       7|      2|\n""""
  },
  {
    "{": ""      ""|D_S-Mijm9gQ|                 NBA|              Sports| 1.0940198040205782|      72|     49|\n""""
  },
  {
    "{": ""      ""|NxTNV7IxT2I|              gacipo|       Entertainment|  0.639736843882596|       4|      9|\n""""
  },
  {
    "{": ""      ""|pZXk502_kAc|           eddie7314|               Music| 0.5558709838009838|       1|      0|\n""""
  },
  {
    "{": ""      ""|EAjbKzKkpYc|           ridesepta|     Travel & Events|  0.355430596425427|       1|      1|\n""""
  },
  {
    "{": ""      ""|pyuZAPS12yo|               nalts|              Comedy| 1.2434230637025059|     348|    685|\n""""
  },
  {
    "{": ""      ""|OA4vy9MX91w|    estevanrbdmg2204|               Music|0.47553430744697217|       5|     13|\n""""
  },
  {
    "{": ""      ""|EXMREF-dFcM|           tiggichic|       Entertainment|  1.111803973349571|      25|     17|\n""""
  },
  {
    "{": ""      ""|EnI6Egp64WQ|         Desertphile|       Howto & Style| 0.3674098393758948|      15|     31|\n""""
  },
  {
    "{": ""      ""|pzILRr5db64|        duelistXmist|       Entertainment| 0.8455510000247615|     101|     10|\n""""
  },
  {
    "{": ""      ""|OQcxZnryF0o|           honoluluu|    Film & Animation| 0.6163709205837187|       6|     16|\n""""
  },
  {
    "{": ""      ""|q-1egqOxTM0|           fafadinhu|       Entertainment| 0.3817148489853718|       5|     26|\n""""
  },
  {
    "{": ""      ""|OSfv-b-BZxs|         FabulandCat|    Film & Animation|0.36642834211401343|      15|     24|\n""""
  },
  {
    "{": ""      ""|F9NbPz4gILU|        thomasfromkc|      People & Blogs| 0.3717157198489107|       2|      0|\n""""
  },
  {
    "{": ""      ""|qLQh16A0YDk|          AkoyPinoy2|    Film & Animation|  0.355430596425427|       1|      1|\n""""
  },
  {
    "{": ""      ""|FfGIDve7LPk|           cooliogie|       Entertainment| 0.4208918859415931|       1|      2|\n""""
  },
  {
    "{": ""      ""|PoU41UwL5LI|            mattyohe|     News & Politics|  2.081649619843738|    2147|   1176|\n""""
  },
  {
    "{": ""      ""|rOZPBTLciPA|         ethiopianaa|       Entertainment| 0.6683917952096794|       8|      2|\n""""
  },
  {
    "{": ""      ""|FkwY8SecZ7g|       anilraj271982|              Comedy| 0.6843286924666856|       0|      0|\n""""
  },
  {
    "{": ""      ""|rYjNJ_ad80Q|        reutersvideo|     News & Politics|0.40875041622829905|       0|      1|\n""""
  },
  {
    "{": ""      ""|QWu_fI7aUWg|       AnimeRules365|       Entertainment| 0.3616405862910306|       2|      4|\n""""
  },
  {
    "{": ""      ""|FmiwOFIz69w|           daybeat83|               Music| 1.1910355595912705|      34|     78|\n""""
  },
  {
    "{": ""      ""|tHpOftMwAyo|          sayedh2007|               Music| 0.6497515232874324|      30|     52|\n""""
  },
  {
    "{": ""      ""|QX2z-0b1Aao|           shankargn|      People & Blogs| 1.4591996301429333|       5|      9|\n""""
  },
  {
    "{": ""      ""|GedSJy-mFd0|           lazinhahh|               Music|  0.566657664747938|       6|     24|\n""""
  },
  {
    "{": ""      ""|tKAoLIrowVI|      HarlowJapAutos|    Autos & Vehicles| 0.4360496772630829|       0|      0|\n""""
  },
  {
    "{": ""      ""|GhuCq9Adk38|       CrystalFromOz|       Entertainment|0.38615337128737737|       5|      7|\n""""
  },
  {
    "{": ""      ""|QwHotsSZAM4|       HERVETIREFORT|     News & Politics| 0.5476193283197758|       0|      0|\n""""
  },
  {
    "{": ""      ""|u9Egx-r2D9Y|           thatsshit|              Comedy|   0.50773814241702|      13|     19|\n""""
  },
  {
    "{": ""      ""|RfGhXnk6lYk|              Zebene|       Entertainment|0.38409600341843897|       2|      1|\n""""
  },
  {
    "{": ""      ""|Gj7mtNNBuOY|             nmg1023|              Comedy| 0.5153501909540205|      29|     17|\n""""
  },
  {
    "{": ""      ""|uVvcNEBnV0Q|                jctv|               Music| 0.4594496516714715|       1|      8|\n""""
  },
  {
    "{": ""      ""|GqRsHaSGD4Y|            mashvani|     Travel & Events| 0.3796601879202078|       3|      4|\n""""
  },
  {
    "{": ""      ""|S8yYT8dkfVM|           saptanaga|               Music| 0.8143425805448873|      11|     26|\n""""
  },
  {
    "{": ""      ""|vkOE8j4OUFo|         derbyjunkie|    Autos & Vehicles| 0.4376659167669044|       0|      0|\n""""
  },
  {
    "{": ""      ""|HNdCBxCJt1A|   tokiohotelchannel|               Music| 2.1873407283387016|     574|    925|\n""""
  },
  {
    "{": ""      ""|SVPW74RHcfA|              tori99|    Film & Animation|  2.562911152855574|     121|    314|\n""""
  },
  {
    "{": ""      ""|vlkYM2wgpkI|  generallysarcastic|      People & Blogs| 1.1055981610077932|      92|     77|\n""""
  },
  {
    "{": ""      ""|HOBw9D1oNX0|              may9th|               Music| 0.4710006565050132|      24|     25|\n""""
  },
  {
    "{": ""      ""|SWYWwJlHDKM|          lucylennon|      People & Blogs|0.36186487084403757|       8|      6|\n""""
  },
  {
    "{": ""      ""|Jn9lIGV72S8|  aguirredelcastillo|              Sports|0.36992057277850204|       0|      0|\n""""
  },
  {
    "{": ""      ""|KQvmLBRspH0|          boobacrazy|               Music| 0.9741806836915246|      15|     11|\n""""
  },
  {
    "{": ""      ""|KTcYkTZCgb0|        GOODMagazine|     News & Politics|  0.355430596425427|      26|     28|\n""""
  },
  {
    "{": ""      ""|Kc5D0QCz96U|          tbaganator|               Music|  0.355430596425427|      10|      6|\n""""
  },
  {
    "{": ""      ""|KhNVaXeso-U|           sarahmizz|               Music|0.36175714724591373|      12|      3|\n""""
  },
  {
    "{": ""      ""|KqcdtsQpKrQ|               htfag|    Autos & Vehicles|  7.829312730769632|     799|   1136|\n""""
  },
  {
    "{": ""      ""|LBVhPqVvi5w|         OtisCollege|       Howto & Style| 0.3979782866786205|       5|     10|\n""""
  },
  {
    "{": ""      ""|LM-GVBVgegA|             amgirll|       Entertainment|  4.084831277120256|     233|    517|\n""""
  },
  {
    "{": ""      ""|LXQs3ZN4L_M|            secattin|      Pets & Animals|  0.355430596425427|       0|      1|\n""""
  },
  {
    "{": ""      ""|Ldpw1qUMnzc|           mbmvideos|      People & Blogs| 0.4624006331319434|      31|     67|\n""""
  },
  {
    "{": ""      ""|M3SWaMWgOyU|            sucoyant|     News & Politics|0.36092902495226353|       1|      0|\n""""
  },
  {
    "{": ""      ""|Mt4A6DjqIVE|       ILoveHerberts|       Entertainment| 1.3150471954613954|      61|     35|\n""""
  },
  {
    "{": ""      ""|N70D1E0XCt8|        sailornewfie|      Pets & Animals| 1.5661469039131823|      41|     31|\n""""
  },
  {
    "{": ""      ""|NsqAkSlAjPY|          hayrobert1|              Sports|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|Nzik_DFR2vg|           Tinky1400|      People & Blogs|0.37867637815945626|     128|     97|\n""""
  },
  {
    "{": ""      ""|OpA6iPYixSw|           brbaldwin|       Entertainment| 0.3854428947178305|       9|      4|\n""""
  },
  {
    "{": ""      ""|P1uTloSPAHg|            club4ghz|       Entertainment| 0.5899110263431571|       9|      4|\n""""
  },
  {
    "{": ""      ""|PIuZc7S04sY|          Sirodingus|     News & Politics|  0.396830528862784|       7|     31|\n""""
  },
  {
    "{": ""      ""|PyZQTWpFNmI|         henkepenk93|              Comedy|0.37205784429058053|      10|      6|\n""""
  },
  {
    "{": ""      ""|Q1QK_iCgnyQ|              skychi|       Entertainment|  7.215609667973997|    7432|   6929|\n""""
  },
  {
    "{": ""      ""|Q3iNz07VXKA|  gibsonfan123456789|               Music|0.38177600797647243|       4|      5|\n""""
  },
  {
    "{": ""      ""|RI9n85UlfmY|               apupu|       Howto & Style| 1.0682526501838119|     110|    110|\n""""
  },
  {
    "{": ""      ""|S3vAtGd36Vo|   FireBreathingKiwi|       Entertainment|0.40934295276130866|       2|      2|\n""""
  },
  {
    "{": ""      ""|S4dkGSVp2jA|            werka114|       Entertainment| 0.5425073851041253|      16|     34|\n""""
  },
  {
    "{": ""      ""|TqT6xZtgmKU|       yayobuckbanks|               Music| 0.8546001926041451|      37|     47|\n""""
  },
  {
    "{": ""      ""|U7j69SUxTtM|      nathanthornton|      People & Blogs| 0.6112491164422498|     194|     90|\n""""
  },
  {
    "{": ""      ""|UAPtRmmq-I0|           SouljaBoy|               Music|  4.205479816394151|     758|    751|\n""""
  },
  {
    "{": ""      ""|UIY4MXU3ojs|            mintie22|       Entertainment| 0.4874169027041999|       8|      6|\n""""
  },
  {
    "{": ""      ""|Uf0ABeTOVgU|           magia1974|               Music| 0.5603842036187124|       2|      5|\n""""
  },
  {
    "{": ""      ""|UfkfKOwTR2I|        therisingson|              Comedy| 0.5334372725939986|      35|     34|\n""""
  },
  {
    "{": ""      ""|UwA_7yHmT9k|           greygoose|              Sports| 0.6091339160479984|       6|    109|\n""""
  },
  {
    "{": ""      ""|VGcdjM5hqwE|        hafansmeiter|       Entertainment|0.37178414473724464|       7|      5|\n""""
  },
  {
    "{": ""      ""|WR4WU_4dkYc|       edugeaniyroxy|              Sports|   0.57318887092896|       3|      2|\n""""
  },
  {
    "{": ""      ""|WiBhJZZwvpw|                dafo|       Entertainment|0.42491081221956967|       4|      2|\n""""
  },
  {
    "{": ""      ""|WkvaYPxetdo|           marciluke|               Music| 0.5143739778376619|       3|      2|\n""""
  },
  {
    "{": ""      ""|WtPqE9sa6ZI|    narutowatcher123|       Entertainment| 0.5600073225864112|      22|     24|\n""""
  },
  {
    "{": ""      ""|X07zupz0t5Q|     trunsako95zelda|              Comedy|  0.355430596425427|       1|      2|\n""""
  },
  {
    "{": ""      ""|XARTNiMt-4k|            RackS225|       Howto & Style| 0.3748350897582532|       2|      1|\n""""
  },
  {
    "{": ""      ""|XNe6xNorVuI|         fantomazspb|              Sports| 0.6289098940027325|       1|      5|\n""""
  },
  {
    "{": ""      ""|XObcUnuXf3M|            thepende|              Comedy| 1.7330963116852665|       0|    621|\n""""
  },
  {
    "{": ""      ""|XQXw5gF301o|       kingmitch1983|       Entertainment|  0.473421379627878|       3|      2|\n""""
  },
  {
    "{": ""      ""|Xi7BUeNLbMs|     AbandonedNation|               Music| 2.9249235725078324|     421|    847|\n""""
  },
  {
    "{": ""      ""|Ydc3FJscSTg|            hyugaedd|       Entertainment| 0.4291314765287891|       0|      1|\n""""
  },
  {
    "{": ""      ""|YgHHEygXYc0|         Greysaholic|       Entertainment| 0.9342660244280253|       2|      6|\n""""
  },
  {
    "{": ""      ""|YuiIyDxa750|           elmosaico|               Music| 3.8963307167812515|     162|    304|\n""""
  },
  {
    "{": ""      ""|ZaMs8IFqQqY|             KezniTT|               Music|  1.559176554592701|      57|     65|\n""""
  },
  {
    "{": ""      ""|ZpUtQmhb43k|           BASTARDKO|              Comedy| 0.4072372853204919|      11|     12|\n""""
  },
  {
    "{": ""      ""|_9MIS4aEdls|         lockergnome|       Howto & Style| 0.5845270348366909|      25|     33|\n""""
  },
  {
    "{": ""      ""|_I0LZczjtn4|         BaByDiMpl3z|       Entertainment| 1.0289238129382556|     110|    192|\n""""
  },
  {
    "{": ""      ""|_mAsYhJ4i40|          mxgymbrats|    Autos & Vehicles|  1.154898362736359|      22|     14|\n""""
  },
  {
    "{": ""      ""|am0tr8VAe1g|            BROUGHAM|               Music| 1.7148403370625267|      65|    120|\n""""
  },
  {
    "{": ""      ""|at862rPrPfA|     DevelynFootball|              Sports|  0.376984436250626|       0|      0|\n""""
  },
  {
    "{": ""      ""|bAv1EC_2fBM|           floricica|               Music|  5.732708572672929|     786|   1647|\n""""
  },
  {
    "{": ""      ""|c_Xp98-uwu0|         treeners016|      People & Blogs|0.37613056264410555|      52|     19|\n""""
  },
  {
    "{": ""      ""|cix4o0tRFNY|          kecookie06|               Music| 0.8911190328898848|       4|      0|\n""""
  },
  {
    "{": ""      ""|d4aw2q7eA2w|         bradintampa|               Music|  0.355430596425427|     150|     69|\n""""
  },
  {
    "{": ""      ""|dBCkoDJkIOc|           indubbley|               Music|  4.141022558684761|     764|   1722|\n""""
  },
  {
    "{": ""      ""|eKYC2k2pax4|            toliss55|              Comedy| 0.9931120381269687|       4|      5|\n""""
  },
  {
    "{": ""      ""|f3IOvFA8LLE|        thatisnotart|       Howto & Style|   2.09217472254196|     565|    352|\n""""
  },
  {
    "{": ""      ""|fX0AKeLVRq8|         watseinfeld|       Entertainment|  0.599488412576797|      16|     18|\n""""
  },
  {
    "{": ""      ""|fiiTOH2C7qk|         Mariocenter|       Entertainment| 1.7546347562978766|     367|    299|\n""""
  },
  {
    "{": ""      ""|g7jU2BNcKUk|         ArtieTSMITW|              Comedy| 2.8266739991969043|    3052|   5890|\n""""
  },
  {
    "{": ""      ""|gK94_wI5OgA|            tvkhaled|    Autos & Vehicles| 0.4602194760775338|       4|      4|\n""""
  },
  {
    "{": ""      ""|h6X2JBSmIsA|          StormyHaze|               Music| 0.4540716593117255|       0|      0|\n""""
  },
  {
    "{": ""      ""|h_L6Qrkb8dw|              m1rock|               Music|0.36088503752404877|       5|     12|\n""""
  },
  {
    "{": ""      ""|ilpS5dtHg-Y|          Kaleo96819|     News & Politics| 0.6066706864140212|       5|     27|\n""""
  },
  {
    "{": ""      ""|j1k_yrNpkYI|            balleruk|               Music|  1.307424203048293|      86|     78|\n""""
  },
  {
    "{": ""      ""|jeBt-xmqr3Q|             Slobbko|       Entertainment| 0.6609158295653487|      38|     30|\n""""
  },
  {
    "{": ""      ""|kD1WjlJHP2A|            codyd666|       Entertainment|  0.355430596425427|       5|      3|\n""""
  },
  {
    "{": ""      ""|kbCFCsugwwU|         rakmanenuff|     News & Politics|  1.324004612484716|     145|     84|\n""""
  },
  {
    "{": ""      ""|kf1PJ_ERn6A|            catcat12|              Sports| 0.3685830192615126|       0|      3|\n""""
  },
  {
    "{": ""      ""|kxpL2438tt4|          annielogue|      People & Blogs| 0.4950009149269283|       3|     15|\n""""
  },
  {
    "{": ""      ""|lEIrxDHmskY|           hcraes123|       Entertainment|  0.470132957313768|       9|     13|\n""""
  },
  {
    "{": ""      ""|lHZDFBS_JkE|            Nanukana|       Entertainment|0.36123693694976633|       0|      0|\n""""
  },
  {
    "{": ""      ""|lYdBN9M8lDE|         Scottie2704|       Entertainment| 0.6183665697085909|      75|     41|\n""""
  },
  {
    "{": ""      ""|m8ofphoOdaI|        sewardstreet|    Film & Animation| 0.6281396789395642|      26|     30|\n""""
  },
  {
    "{": ""      ""|meCnZOZqNk0|     10Garmonbozia01|     News & Politics| 0.9217048454922813|       3|     15|\n""""
  },
  {
    "{": ""      ""|mj3wa9-6psE|            Apryl155|               Music| 1.2621851067418348|     511|   1156|\n""""
  },
  {
    "{": ""      ""|mlWs4gANE2c|           daanmogot|               Music| 1.1233406472513245|     132|    120|\n""""
  },
  {
    "{": ""      ""|n6map6OgiPk|        deadhead1065|    Film & Animation|0.38378877739991485|       3|      7|\n""""
  },
  {
    "{": ""      ""|nvBZx3k-Z04|          JewishSong|               Music| 0.4087744093709616|       0|      0|\n""""
  },
  {
    "{": ""      ""|o7dCU5vBLYY|            PromoCon|               Music| 0.3949193072180751|       3|     13|\n""""
  },
  {
    "{": ""      ""|oEchXbi6y6g|          m4tz3m4tz3|       Howto & Style|  1.920675090097176|     127|     64|\n""""
  },
  {
    "{": ""      ""|oP0V1-xTbqk|          YENI140589|      People & Blogs|0.38469255299828364|       0|      0|\n""""
  },
  {
    "{": ""      ""|p3XzDnPxCmQ|         HistChannel|       Entertainment|  1.233724335742349|       7|     10|\n""""
  },
  {
    "{": ""      ""|pGLhAES94G4|             bluugal|       Entertainment| 1.0784914221468764|       0|      6|\n""""
  },
  {
    "{": ""      ""|pVrMEC-THog|         DebraPeters|               Music| 0.5993049449434759|       1|      8|\n""""
  },
  {
    "{": ""      ""|pZ-A-svSzKw|             iggy151|              Sports| 0.4108235526252265|      16|      7|\n""""
  },
  {
    "{": ""      ""|paopa-hbNck|        BUcheerChick|              Sports| 1.3846813151416877|      58|     25|\n""""
  },
  {
    "{": ""      ""|qrHgicnjvV8|              Ryonet|       Howto & Style| 1.1958118588457216|      14|     10|\n""""
  },
  {
    "{": ""      ""|rTh33S9-o4c|   thetormentsofhell|       Entertainment| 1.0681029605998995|      17|     16|\n""""
  },
  {
    "{": ""      ""|ro8Zf0Z_1dA|           OSUBeav06|     News & Politics| 0.4250796246378066|       5|      6|\n""""
  },
  {
    "{": ""      ""|rtHrWaN50as|   gritoproducciones|    Film & Animation| 0.5797475053513217|       0|      0|\n""""
  },
  {
    "{": ""      ""|rtciarv1BII|             avmh131|               Music| 0.7998225559569716|     132|    153|\n""""
  },
  {
    "{": ""      ""|sJD_pJKt6vo|       germanyonline|               Music| 0.9941007170368409|      16|     26|\n""""
  },
  {
    "{": ""      ""|sQkzQLlBWQE|            mergicka|    Film & Animation| 0.4926525111678234|      12|     52|\n""""
  },
  {
    "{": ""      ""|sSh_oEHXjs0|introvertednightmare|       Entertainment| 1.6013549308704131|     512|    708|\n""""
  },
  {
    "{": ""      ""|sp27VFibpYw|             icehype|      People & Blogs|0.36223707215970036|       0|      3|\n""""
  },
  {
    "{": ""      ""|ss0ckdl4RrI|            ItsPat10|              Comedy|  0.355430596425427|      31|     46|\n""""
  },
  {
    "{": ""      ""|stTUwy5sb3U|         sondegaliza|       Entertainment| 0.9184888197714101|      18|     13|\n""""
  },
  {
    "{": ""      ""|t_bwdjDtscI|        thebeachboys|               Music| 0.6880886798449124|      26|     54|\n""""
  },
  {
    "{": ""      ""|tmXVKWFBHRA|    WorldMusicSupply|               Music|  1.991296895399936|      54|     28|\n""""
  },
  {
    "{": ""      ""|u4-RvikfNDs|              paldri|       Entertainment| 0.7111076107779069|      41|    145|\n""""
  },
  {
    "{": ""      ""|uWNvlrXpOOU|             misstoi|               Music| 0.4550169751373685|      20|     12|\n""""
  },
  {
    "{": ""      ""|vaKoM5qn6bQ|             carmanb|              Comedy| 1.4476288417291474|       2|     39|\n""""
  },
  {
    "{": ""      ""|vfzJMVj61Ds|           KenzoDude|              Sports| 0.6025663545053026|      22|     26|\n""""
  },
  {
    "{": ""      ""|w0x9RLL4sqg|           marckgonc|       Entertainment| 0.4074168365864532|       0|      0|\n""""
  },
  {
    "{": ""      ""|wFygpFxlJdY|           RobBoudon|               Music| 0.5721053323080837|      28|     54|\n""""
  },
  {
    "{": ""      ""|xRvzuwsZyNY|           FragQu33n|       Entertainment|0.42063549001426437|      94|     24|\n""""
  },
  {
    "{": ""      ""|xfN0k_k7-PE|         socomshero8|              Comedy| 0.3561932267597994|       0|      2|\n""""
  },
  {
    "{": ""      ""|y5pZLUalu30|              elmorg|              Sports| 2.6958382400294987|     183|    429|\n""""
  },
  {
    "{": ""      ""|yCT76hynFUE|             agentsm|              Sports| 0.8201563730846317|      43|      7|\n""""
  },
  {
    "{": ""      ""|yIp5aghHwpI|          CharmingP3|       Entertainment| 0.5892947897706254|      13|     24|\n""""
  },
  {
    "{": ""      ""|yaQCirSxnvg|         fidelrivera|               Music|  3.449375766310644|    2198|   3195|\n""""
  },
  {
    "{": ""      ""|z8Qw1jfenZ8|         whatuneedtv|       Entertainment| 0.4769452588078788|       1|      2|\n""""
  },
  {
    "{": ""      ""|ztlnKZSPtcw|            starks23|              Sports| 1.0472973416187619|      71|     82|\n""""
  },
  {
    "{": ""      ""|-JREuvxyviQ|            wowhobbs|Science & Technology| 2.8518549107225795|     695|    646|\n""""
  },
  {
    "{": ""      ""|0Q8vl8wFm7g|             jromey5|               Music|0.49506674554675173|      16|     38|\n""""
  },
  {
    "{": ""      ""|0Z5cwH1ziU8|         beatlebrent|              Sports| 0.6741161983898122|       6|      6|\n""""
  },
  {
    "{": ""      ""|SjjEdJbek9I|      TimbalandBeats|               Music| 0.7576675038160153|     114|    286|\n""""
  },
  {
    "{": ""      ""|0q8iFjT8yFQ|               mikma|              Comedy| 0.5595582951172965|   10188|   4392|\n""""
  },
  {
    "{": ""      ""|1GEYfdWzO-U|    insiderexclusive|     News & Politics|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|3ORnxW0Byac|             Ger4ooo|               Music|0.45983087604933215|       5|      2|\n""""
  },
  {
    "{": ""      ""|3sbG1ML-hlE| media4uncontrolable|      People & Blogs| 1.3622668549227295|       9|     15|\n""""
  },
  {
    "{": ""      ""|TRjr0nAxmJI|         Reelmensiko|              Comedy| 0.8307133098356057|      12|      9|\n""""
  },
  {
    "{": ""      ""|4OU7K4oprWA|        utimopadrino|       Entertainment|  6.818806011501291|     120|    194|\n""""
  },
  {
    "{": ""      ""|TvVYqXGsANY|              NakSsS|               Music|  1.773885610010524|     557|    950|\n""""
  },
  {
    "{": ""      ""|UGIGAkQ6MPo|          Cfury4life|              Sports| 0.4396646657777722|       1|      1|\n""""
  },
  {
    "{": ""      ""|UqS_Vmbphdo|         Timothy2035|       Entertainment|  3.082832607500295|      97|     52|\n""""
  },
  {
    "{": ""      ""|V38PwtOCpE4|             rfjason|       Entertainment| 0.9115815781277165|      20|     42|\n""""
  },
  {
    "{": ""      ""|VdPrv1ELgSg|    oneawesomefanboy|      People & Blogs|0.36992057277850204|      12|     28|\n""""
  },
  {
    "{": ""      ""|Vftf8TTve4s|           sawing14s|              Comedy| 0.7019866287384804|      87|    190|\n""""
  },
  {
    "{": ""      ""|VoyBzQYnSo4|            mrseeder|    Film & Animation|0.36396415749907723|      15|     23|\n""""
  },
  {
    "{": ""      ""|WTbYuiewQ_k|        PoynterJones|               Music| 1.3683886424932394|    1343|   1010|\n""""
  },
  {
    "{": ""      ""|Wj8p_R22aaI|        Alexsandercr|      People & Blogs| 0.5982120544388697|      12|     37|\n""""
  },
  {
    "{": ""      ""|XCKuZPUn2nQ|             jospi69|    Autos & Vehicles|  4.927329794203888|     572|    585|\n""""
  },
  {
    "{": ""      ""|XjUoiwGg2ro|      DiarioAventura|               Music|0.45317583691002705|       0|      2|\n""""
  },
  {
    "{": ""      ""|ZQuRhNpJKVU|          fordmodels|       Howto & Style| 1.8648655847182867|      89|    173|\n""""
  },
  {
    "{": ""      ""|ZQxdAsnpMjo| QaoYahngsProduction|           Education|  0.355430596425427|       9|      3|\n""""
  },
  {
    "{": ""      ""|ZYCGtN4e3xU|            leforain|      Pets & Animals| 0.6784213333992919|       7|      8|\n""""
  },
  {
    "{": ""      ""|ZaFqwEH-C6M|        seankingston|               Music|  2.355135662503291|     682|    797|\n""""
  },
  {
    "{": ""      ""|_f3atN0ViAU|         bestofobama|     News & Politics|  0.355430596425427|       0|      2|\n""""
  },
  {
    "{": ""      ""|bmuxljOvBdU|            mkorty23|              Comedy|  4.666189187455338|     773|    915|\n""""
  },
  {
    "{": ""      ""|boq-UOUevmc|       ladybloodrose|      Pets & Animals| 0.3697998229755597|       8|      1|\n""""
  },
  {
    "{": ""      ""|cFicNhXPeeI|          kowboy3272|               Music| 0.3614414596929184|      13|     10|\n""""
  },
  {
    "{": ""      ""|cYwEWsmjQbA|          ocnono1503|       Entertainment| 0.4637554014628825|       1|      9|\n""""
  },
  {
    "{": ""      ""|csPj3bTHiJg|EastHighCheerleading|              Sports| 2.9153452644487188|     325|    148|\n""""
  },
  {
    "{": ""      ""|d18u_9mk4fU|            a037042l|              Sports|0.36868451722779116|       0|      0|\n""""
  },
  {
    "{": ""      ""|d8tz0opytzI|         adambbrowne|       Entertainment|  0.557932611782665|       1|      6|\n""""
  },
  {
    "{": ""      ""|dFTUDcmdRYQ|          roybidisha|    Film & Animation| 0.9525706609442244|       8|      2|\n""""
  },
  {
    "{": ""      ""|eTvnIEa96dQ|            linj2121|               Music|  0.466756416715358|       6|     16|\n""""
  },
  {
    "{": ""      ""|ejrESW7D20E|           lava0aval|               Music|0.46713087086457034|       3|      6|\n""""
  },
  {
    "{": ""      ""|erJc4dzZ3IA|          ACvideosDC|               Music|  16.23350223330055|    2504|   8651|\n""""
  },
  {
    "{": ""      ""|gDUeKl7pFfE|           barrysj74|    Autos & Vehicles| 0.4198803393235561|      14|      7|\n""""
  },
  {
    "{": ""      ""|gN4HfGXvT2Q|        Jubilation86|    Film & Animation|0.36452768684258313|       7|     21|\n""""
  },
  {
    "{": ""      ""|gdWAghcMi8I|         makaveli571|Science & Technology| 0.9327970209120797|      12|     11|\n""""
  },
  {
    "{": ""      ""|gsxj8MlW5F0|            ChrisC80|       Entertainment|0.36088503752404877|       7|      2|\n""""
  },
  {
    "{": ""      ""|h7Q1mPwanLU|           Gozrics21|              Comedy|0.45921505205432644|       5|      9|\n""""
  },
  {
    "{": ""      ""|hVE1IqineRI|              Tedman|       Entertainment| 1.1158710222395407|     201|    479|\n""""
  },
  {
    "{": ""      ""|hiIQXQitZmg|           yehczarny|              Comedy| 3.9882027781305305|     316|    567|\n""""
  },
  {
    "{": ""      ""|i8glCemKiyM|         kingkirby28|    Film & Animation| 1.3025110841833023|     586|   1317|\n""""
  },
  {
    "{": ""      ""|il7qBtQlXMg|           n0iTuloVe|       Entertainment| 0.8121282617457833|      95|     45|\n""""
  },
  {
    "{": ""      ""|j5mAxRsxSk8|            JayOM619|              Sports| 1.0982948963237655|      79|     85|\n""""
  },
  {
    "{": ""      ""|j7XKoMiBpCw|       CaptainDiesel|              Comedy|0.49651904109422057|      26|     39|\n""""
  },
  {
    "{": ""      ""|jN_BWcDtG2M|         Elisgirl013|               Music| 0.9765062477763327|      22|     45|\n""""
  },
  {
    "{": ""      ""|jYDzT1q5mZE|           raptorama|    Autos & Vehicles| 1.3522359492144276|       4|     17|\n""""
  },
  {
    "{": ""      ""|kS7VcfTu97E|          nathanbu19|              Comedy| 2.3113986520971483|     288|    593|\n""""
  },
  {
    "{": ""      ""|kgYsrhmT2tw|            PreditEd|       Entertainment|  0.760152294015399|       8|      3|\n""""
  },
  {
    "{": ""      ""|l2lnMbnBzuM|            Melcland|      People & Blogs| 0.7512917343000535|     104|     64|\n""""
  },
  {
    "{": ""      ""|lyHv9Y3QnUM|             vspirus|      People & Blogs|  0.479067956445885|     142|    248|\n""""
  },
  {
    "{": ""      ""|my56yxZiRfw|   TheVampireLucinda|              Sports| 0.6398047499457364|      82|    129|\n""""
  },
  {
    "{": ""      ""|naZF48ItHLU|          0ooGummies|      People & Blogs| 0.4000617511645886|      28|     24|\n""""
  },
  {
    "{": ""      ""|nj3iiATN2cU|       legacyofhonor|       Entertainment| 0.4133905018377269|      12|      8|\n""""
  },
  {
    "{": ""      ""|qyUjjKFQMI4|           Phenom770|       Entertainment| 0.6293791194404512|      23|     37|\n""""
  },
  {
    "{": ""      ""|rkGHI06xsPA|            Fendataw|      People & Blogs|  2.241452859567836|      58|     10|\n""""
  },
  {
    "{": ""      ""|rkNZiNbSNtA|       lildramaqueen|       Entertainment|  2.106642836263653|     332|    374|\n""""
  },
  {
    "{": ""      ""|sohIFKt4Alk|          jcleshaker|               Music|0.38827454282573026|       1|      2|\n""""
  },
  {
    "{": ""      ""|svADNRH6j3U|            mcsteveo|      People & Blogs| 1.3801732472101675|      38|     73|\n""""
  },
  {
    "{": ""      ""|szezav9F1zM|     skydiveelsinore|      People & Blogs| 0.4775031847089981|       4|      0|\n""""
  },
  {
    "{": ""      ""|tBqL0RKkyKU|             BlankTV|               Music|  5.583916278756918|     325|    550|\n""""
  },
  {
    "{": ""      ""|umaTLREgTqE|            TurboTax|       Entertainment| 0.6033182581819789|     343|   1995|\n""""
  },
  {
    "{": ""      ""|v3cdLhlF628|           feelmeerq|      People & Blogs| 0.5906798595178038|       4|     10|\n""""
  },
  {
    "{": ""      ""|v8HZAC8LF7Y|             dralter|      Pets & Animals|  4.556571889192998|     582|    854|\n""""
  },
  {
    "{": ""      ""|vEDnTyZdt-g|        darthphysics|Science & Technology| 0.3848189260105806|       4|      3|\n""""
  },
  {
    "{": ""      ""|vSCGGKCEHsE|   XRatedRMattitudeX|              Sports|  1.532241949013695|      85|    103|\n""""
  },
  {
    "{": ""      ""|w_zwt6jRJao|           MarkMan23|      People & Blogs| 0.5704966375221443|      19|     13|\n""""
  },
  {
    "{": ""      ""|xo2wRvJ04ss|             Dasyati|    Film & Animation|  1.910695525361163|     200|    185|\n""""
  },
  {
    "{": ""      ""|yBqPCrZTqDw|         bennyjammin|       Entertainment|  0.378963254449864|       1|      0|\n""""
  },
  {
    "{": ""      ""|yJPzcy37bA8|        ultracowlord|               Music| 0.6896728829925497|     122|    220|\n""""
  },
  {
    "{": ""      ""|yTCfTvZpBSY|     anastasiaxkiddo|               Music| 0.4179018679654799|       4|      2|\n""""
  },
  {
    "{": ""      ""|yY1t1dOzFfk|           JustA11en|              Comedy| 0.8685711890785794|     256|    302|\n""""
  },
  {
    "{": ""      ""|z-nK8eOPFf8|            moonvakk|               Music| 1.6600072859426374|     176|    382|\n""""
  },
  {
    "{": ""      ""|z1IgEn_5hpQ|           ruxpinexe|      People & Blogs|0.42512701304146366|       4|      4|\n""""
  },
  {
    "{": ""      ""|zHOyrOK8Y04|        camdacarizma|               Music| 0.3561932267597994|       0|      1|\n""""
  },
  {
    "{": ""      ""|-WTHgrusTpI|        CraigBrockie|     News & Politics|  4.517345918671409|     181|    120|\n""""
  },
  {
    "{": ""      ""|09PIhtBaPSg|       hayleyghoover|              Comedy| 1.3281386312418941|     181|    233|\n""""
  },
  {
    "{": ""      ""|0GAUnuuBkW4|      crunchysaviour|Science & Technology|  2.096397773476296|     342|    655|\n""""
  },
  {
    "{": ""      ""|0Z4CwpBYbeM|     ClenchedFISTpro|               Music| 1.1954761327571612|      66|    101|\n""""
  },
  {
    "{": ""      ""|1LVc8JDGawA|         aybaybay222|               Music| 0.3961641049503549|       6|      4|\n""""
  },
  {
    "{": ""      ""|1cKvHEUMN1w|          UserName89|       Howto & Style| 1.2017907169324529|     357|    108|\n""""
  },
  {
    "{": ""      ""|24bdkthgUyc|           Glorykins|       Entertainment| 2.1625596407843206|     135|    127|\n""""
  },
  {
    "{": ""      ""|25ssefYFxiw|               Ocio2|       Entertainment|0.36421650642936154|       0|      0|\n""""
  },
  {
    "{": ""      ""|3NjxBNjSnA4|    TmaxxPianoplayer|               Music| 1.3459301298433541|      37|     22|\n""""
  },
  {
    "{": ""      ""|4iOzqOU2bQA|           TSlay1974|      People & Blogs| 0.3644626816855104|     147|    146|\n""""
  },
  {
    "{": ""      ""|4ncOf09-Bmg|            TRANE200|       Entertainment| 1.4484640662139532|      45|     36|\n""""
  },
  {
    "{": ""      ""|5Vv4jPexww8|    LeonaLewisOnline|               Music|  1.373744703369431|     278|    546|\n""""
  },
  {
    "{": ""      ""|5jBcLRXc91E|             yamicin|       Entertainment|0.42720433520453216|       3|      3|\n""""
  },
  {
    "{": ""      ""|63o_OM3dAqk|        eltoncantoni|       Entertainment|  3.374913360927866|     185|    171|\n""""
  },
  {
    "{": ""      ""|8MDnkNMgYZA|          DoGyMoLiNa|       Entertainment| 0.7110061377323447|     133|    166|\n""""
  },
  {
    "{": ""      ""|8QJKC2WmEds|          narutomas1|    Film & Animation|  0.355430596425427|       3|      3|\n""""
  },
  {
    "{": ""      ""|9YtXDK2Lrc8|           hypnofun3|       Entertainment|0.39779406300462966|       0|      4|\n""""
  },
  {
    "{": ""      ""|A3WcC8HcfDI|      musicvideoswhd|               Music|0.37746341046896376|      39|     35|\n""""
  },
  {
    "{": ""      ""|AiTwQUFjrgU|             wuttkea|     News & Politics|  2.191739670506503|      31|   1261|\n""""
  },
  {
    "{": ""      ""|B-Kzc_m3m2o|           chiligoyo|      People & Blogs|  1.005882785351277|      15|     57|\n""""
  },
  {
    "{": ""      ""|BUV9pdFajPo|           eMePeSeiS|              Sports|  3.898706086654775|     116|    295|\n""""
  },
  {
    "{": ""      ""|Ba8QkYOFG-c|            poshbabi|      People & Blogs|  0.355430596425427|       0|      1|\n""""
  },
  {
    "{": ""      ""|BrMOBHdQfjc|          lolabobble|              Comedy| 1.6962954146014884|      56|    106|\n""""
  },
  {
    "{": ""      ""|CjC3Y4KZTto|          leviscouse|               Music| 0.8685754931487449|      43|     71|\n""""
  },
  {
    "{": ""      ""|CpRz6XV5LrY|           pester900|              Comedy|0.48831018752704924|      18|     41|\n""""
  },
  {
    "{": ""      ""|D0_n1DhnBZE|             kpalleh|              Sports|0.37068320311287434|       0|      0|\n""""
  },
  {
    "{": ""      ""|D1ImXRI3qww|             tao7671|       Entertainment| 0.7872370380066346|      11|     30|\n""""
  },
  {
    "{": ""      ""|D8JE_p6Rlqs|         stevechippy|Science & Technology| 1.3381033314055815|       8|     11|\n""""
  },
  {
    "{": ""      ""|DPZkOhcFYZY|       goldminevideo|       Howto & Style| 0.6521343405369022|      21|     23|\n""""
  },
  {
    "{": ""      ""|DkKNyv-URM8|     dominiodemuerte|      People & Blogs| 1.0113015830526928|      28|     26|\n""""
  },
  {
    "{": ""      ""|EBT_nowM-Mo|         lilvilan816|              Sports| 0.3888646597610435|      63|     28|\n""""
  },
  {
    "{": ""      ""|EVZbt3WjMJs|             NovaXlp|               Music|0.36992057277850204|       0|      0|\n""""
  },
  {
    "{": ""      ""|Ekr80_78Fyg|             laupong|      People & Blogs|0.38154162214842424|      24|     39|\n""""
  },
  {
    "{": ""      ""|F-RQS_ATv5k|         lewisjankel|               Music| 1.5529549184781206|     130|    119|\n""""
  },
  {
    "{": ""      ""|F0FvG9GO8Qs|                MadV|      People & Blogs|  1.706021588090082|    3977|   7757|\n""""
  },
  {
    "{": ""      ""|FI5SSlQ3F7c|         ZelenaVrana|      People & Blogs| 1.7660776393507336|      85|    194|\n""""
  },
  {
    "{": ""      ""|FXtrY8Yet9k|      likefattybelly|                 UNA| 0.6340320674092509|      76|    156|\n""""
  },
  {
    "{": ""      ""|Fgz0d8vlSqw|        grantseifers|              Comedy| 0.5073674859719349|      76|     40|\n""""
  },
  {
    "{": ""      ""|GWYuXncckjU|            denysa25|    Film & Animation|  1.169059659453404|      41|     83|\n""""
  },
  {
    "{": ""      ""|HPPj6viIBmU|             raze7ds|       Entertainment| 15.075074777948759|   22567|  13314|\n""""
  },
  {
    "{": ""      ""|H_O6y9bd8pg|            oXXoLiNe|      People & Blogs| 0.7546612283868969|      12|      8|\n""""
  },
  {
    "{": ""      ""|Hg47-CwiP-I|              AsikTV|       Entertainment| 1.0196034057532344|       3|     25|\n""""
  },
  {
    "{": ""      ""|Hn-F6H6RNEo|             magic17|    Autos & Vehicles| 1.0385410548542537|     524|    160|\n""""
  },
  {
    "{": ""      ""|HnmBxII-a44|         markcrilley|       Howto & Style| 0.7981349585768158|     204|    230|\n""""
  },
  {
    "{": ""      ""|HzSIP83FwZU|             Setyman|       Entertainment| 0.7597021200833998|      63|     40|\n""""
  },
  {
    "{": ""      ""|IrkaRTwItL0|            Odenized|              Sports| 0.5264834469238262|      67|     24|\n""""
  },
  {
    "{": ""      ""|KX1oUqtFlJ0|                IxJa|               Music| 0.6203423999705162|      18|     15|\n""""
  },
  {
    "{": ""      ""|Lm1wx1iJhe8|         blueangelak|               Music| 0.3880718786881113|       1|      1|\n""""
  },
  {
    "{": ""      ""|Lw1H_fiWUDM|    jonoogletree2008|              Comedy| 0.5355063887662062|       5|      4|\n""""
  },
  {
    "{": ""      ""|LwgvVZoKCb8|             lburgos|       Howto & Style| 0.6903710089996306|       4|      5|\n""""
  },
  {
    "{": ""      ""|M0OmzPiD8uM|       nitratedmafia|              Sports| 0.5303063428998352|       1|      2|\n""""
  },
  {
    "{": ""      ""|N-nS0ylhkKU|         Willie41288|       Entertainment| 0.3701314900580615|      13|     71|\n""""
  },
  {
    "{": ""      ""|N6WhI9JNVrs| universalmusicgroup|               Music|   5.82565566358038|     613|   1230|\n""""
  },
  {
    "{": ""      ""|NIrpNDte-vU|          bizonsuper|    Autos & Vehicles|   1.35617586528396|     103|     21|\n""""
  },
  {
    "{": ""      ""|NrK0MbBR1Lg|          visioncael|      People & Blogs| 0.7362284781490506|       1|      5|\n""""
  },
  {
    "{": ""      ""|NseRfdfQ0Dg|     TurtlesTheClown|       Entertainment| 0.5472452500327764|      25|     19|\n""""
  },
  {
    "{": ""      ""|O77jktR02LQ|  karakartal19032003|      People & Blogs| 0.4473801465056698|       2|     16|\n""""
  },
  {
    "{": ""      ""|O9MIkgdZZYU| thelebronjamesblitz|              Sports| 0.4285540848524981|       0|      2|\n""""
  },
  {
    "{": ""      ""|OdLLkoORF-k|       andrewcrowden|       Entertainment| 0.5216962685043135|       1|      3|\n""""
  },
  {
    "{": ""      ""|OsAsW06C1nY|         CarlosSlimm|       Entertainment| 1.9559843153132257|      27|     28|\n""""
  },
  {
    "{": ""      ""|PR8gDi72jaw|mileycyrusrockssuppo|               Music|  0.355430596425427|       0|      1|\n""""
  },
  {
    "{": ""      ""|P__dftbPsyc|            davedays|              Sports|  3.998422009536565|    2065|   3258|\n""""
  },
  {
    "{": ""      ""|PfofGgAF-pk| MixtapeMessiahJr619|    Film & Animation| 0.4278804781908019|       2|      1|\n""""
  },
  {
    "{": ""      ""|PjCPrvne97w|            juhilove|               Music| 0.5159312344963207|      11|     11|\n""""
  },
  {
    "{": ""      ""|Q4B8Opd7K98|   imgilmoregirl1984|               Music| 0.8175706958591568|      26|     16|\n""""
  },
  {
    "{": ""      ""|Qz6EBChGsI4|            candre23|    Film & Animation| 0.6314072482218132|      31|     51|\n""""
  },
  {
    "{": ""      ""|R4k0vZ1RZI4|        VelocityCrew|       Entertainment|0.36534243024980423|       5|      2|\n""""
  },
  {
    "{": ""      ""|RM-WQUziAIc|          mchlcooper|       Entertainment| 0.5903540652795932|       1|      8|\n""""
  },
  {
    "{": ""      ""|S65xsy_bwqA|           Tigraskal|              Sports| 0.5479295010267317|       0|      0|\n""""
  },
  {
    "{": ""      ""|SoFEaLbn9O0|         ljalenjka77|              Comedy| 0.5080553529572237|       2|      4|\n""""
  },
  {
    "{": ""      ""|T-6m9KwipWo|             JonnyJM|              Comedy|  5.786399027655937|    2893|   1403|\n""""
  },
  {
    "{": ""      ""|T1ZxJLgdQbM|              rayadv|       Howto & Style| 0.8133255297610665|       5|      7|\n""""
  },
  {
    "{": ""      ""|TLUV4I795O4|          yemenfelix|               Music| 1.3013293910943153|       9|     13|\n""""
  },
  {
    "{": ""      ""|UB76nUJWW2Q|     Xemnashumanform|               Music| 0.5508781719229787|      11|     16|\n""""
  },
  {
    "{": ""      ""|V-B_fw5m3lo|     renatademetrioo|              Sports|  0.628097573416098|       0|      0|\n""""
  },
  {
    "{": ""      ""|VOvogBtvd2M|            IMiRoKuI|       Entertainment| 1.8941806866759754|      52|     17|\n""""
  },
  {
    "{": ""      ""|VRG_Y0jpaEw|         grahamdavid|    Film & Animation|  0.378699945950999|       1|      3|\n""""
  },
  {
    "{": ""      ""|VVkRHQBR_7I|            denmay88|               Music|  4.271100584156209|    1609|   4091|\n""""
  },
  {
    "{": ""      ""|Vm8A8Fty-bo|       IIIREDSTARIII|               Music| 1.0956475752584927|      30|     68|\n""""
  },
  {
    "{": ""      ""|W-zA6kll_0A|            dermblue|               Music|  1.048080387270405|       9|     36|\n""""
  },
  {
    "{": ""      ""|W6m79OCjR8Y|          SonGoten17|       Entertainment| 0.4661068344184073|      14|     28|\n""""
  },
  {
    "{": ""      ""|WU4lNOY3nLM|     TigerDirectBlog|       Entertainment|  0.824171402836741|      39|     50|\n""""
  },
  {
    "{": ""      ""|XVC-EhO0qqs|            andy3027|               Music| 1.4607415286824577|      69|     80|\n""""
  },
  {
    "{": ""      ""|Xln1YQCFYsI|            riephile|              Sports| 1.3594245386801636|      28|    103|\n""""
  },
  {
    "{": ""      ""|Xxblwo4z8F4|              m4rkos|       Entertainment| 1.0038286192419101|      10|     12|\n""""
  },
  {
    "{": ""      ""|YH1hQVOE2Es|           Mayorka10|       Entertainment|  0.355430596425427|       0|      1|\n""""
  },
  {
    "{": ""      ""|Yqm3JIL56Dw|             omocoro|       Entertainment| 0.3630844089347834|       0|      9|\n""""
  },
  {
    "{": ""      ""|ZJC-LUito-k|       shanehardcore|       Entertainment| 0.3658116294840943|       0|      0|\n""""
  },
  {
    "{": ""      ""|_ODC5e3AEa8|        doglover5353|      Pets & Animals| 1.5558982227797293|     353|    254|\n""""
  },
  {
    "{": ""      ""|ahHM7ZQkx4w|            sfonsek1|               Music|0.46717710948765284|       0|      0|\n""""
  },
  {
    "{": ""      ""|b0ehZ2LBU6A|          sebapidgey|               Music|0.41419539597872485|       2|      2|\n""""
  },
  {
    "{": ""      ""|bIkL8yf4zro|        interbartolo|Science & Technology|0.37073132145540016|       0|      0|\n""""
  },
  {
    "{": ""      ""|biIKpegx7h4|      gokoreapodcast|       Howto & Style| 0.7454140850703341|      20|     18|\n""""
  },
  {
    "{": ""      ""|cAwbxzoYSFc|        siannyshoo92|      People & Blogs|  0.355430596425427|       1|      0|\n""""
  },
  {
    "{": ""      ""|cXPSgK4_Z24|          SceneXster|               Music| 1.4290507686678795|      95|     60|\n""""
  },
  {
    "{": ""      ""|cw7W4QsJp88|            jontweet|               Music| 0.6678801038454046|     124|    620|\n""""
  },
  {
    "{": ""      ""|d4VBwB7wp70|            soel2007|     Travel & Events| 1.1388765463687298|      31|     23|\n""""
  },
  {
    "{": ""      ""|dyJe0wUdqZo|          pranavrulz|    Film & Animation|  0.355430596425427|       1|      1|\n""""
  },
  {
    "{": ""      ""|e51zLt_ZwS8|            bannerdb|       Entertainment| 0.4718584537929728|       6|      7|\n""""
  },
  {
    "{": ""      ""|e66Og0lOCcE|    forbiddenkingdom|       Entertainment| 2.1781313531635336|    4119|   6484|\n""""
  },
  {
    "{": ""      ""|eJPhl02ZI8E|         JCfenderman|               Music|0.39890145338938765|       5|      7|\n""""
  },
  {
    "{": ""      ""|eVNULpZJzmU|         GROUNDEDMAG|               Music| 1.1131192235666265|     294|     71|\n""""
  },
  {
    "{": ""      ""|foBc_4LAWN0|           Kruszakus|              Sports|0.38288429369824317|      22|     22|\n""""
  },
  {
    "{": ""      ""|fzMWC_rD1YY|     renegaderealtor|       Howto & Style| 1.8433960875252084|      47|     30|\n""""
  },
  {
    "{": ""      ""|gTRfGZjPrrk|hillaryclintondotcom|     News & Politics| 1.2439825018059043|       0|    690|\n""""
  },
  {
    "{": ""      ""|ggV8-F-NDEk|         kateydid514|       Entertainment|  0.478401025638871|       6|     11|\n""""
  },
  {
    "{": ""      ""|gsAJJQMx7mk|            dufrene9|              Comedy|  0.355430596425427|       1|      1|\n""""
  },
  {
    "{": ""      ""|gtGZ0dANmps|       XtrmL1AB1L1TY|              Comedy| 0.5771190539590063|       0|      2|\n""""
  },
  {
    "{": ""      ""|gy6MT_wnu9U|           rockermad|               Music| 0.4840814226852709|       8|     21|\n""""
  },
  {
    "{": ""      ""|h6_1eoyJqtc|      sevenbluespots|               Music|0.37123674563057296|       1|      5|\n""""
  },
  {
    "{": ""      ""|hAhlCWO_duo|        chazangel127|       Entertainment| 0.3610809815224597|       2|      2|\n""""
  },
  {
    "{": ""      ""|hPMU2fhINEs|          BIGMEL1981|     News & Politics|  0.355430596425427|       2|      1|\n""""
  },
  {
    "{": ""      ""|hpL-l9RXO-Y|              Pikori|    Film & Animation| 0.3900647480001184|       9|     19|\n""""
  },
  {
    "{": ""      ""|iKTBlQsxmN0|             SGT4EVA|Science & Technology| 0.9507884010715121|      99|     26|\n""""
  },
  {
    "{": ""      ""|kfe8yShfbeU|           AriaElysa|               Music|  0.374931689600607|       1|      0|\n""""
  },
  {
    "{": ""      ""|kupBnU-JjJw|          xJoJOannax|    Film & Animation| 0.3689787243155521|       5|      6|\n""""
  },
  {
    "{": ""      ""|lQyepIhggHE| crapidycrapcrapcrap|       Entertainment|  0.706733723012082|      26|     18|\n""""
  },
  {
    "{": ""      ""|mPgqpk8VaFw|          oxviastral|       Entertainment| 0.9183682352322111|       0|      1|\n""""
  },
  {
    "{": ""      ""|mkzj9wURYkc|         tennantfan1|       Entertainment| 1.5420407439030963|      45|     28|\n""""
  },
  {
    "{": ""      ""|mmzQnAO0QGw|            keroll85|       Entertainment| 0.6010857069577804|      48|     39|\n""""
  },
  {
    "{": ""      ""|n6PdE54NCGE|         hotforwords|       Entertainment| 2.4783907574405593|     477|   1763|\n""""
  },
  {
    "{": ""      ""|n8F1AWYoklQ|     kingofchaos1994|    Film & Animation| 0.5731281048986525|      11|      6|\n""""
  },
  {
    "{": ""      ""|-3JOdQc__Mo|            bobbiex2|       Entertainment|0.44858216940666523|      14|     22|\n""""
  },
  {
    "{": ""      ""|neZymKLzFAU|     afilmspalestine|     News & Politics|  1.017275052042282|       0|     10|\n""""
  },
  {
    "{": ""      ""|nq2aqXPOcQA|              efonts|               Music| 0.6363255869965756|      39|     29|\n""""
  },
  {
    "{": ""      ""|-GaEsupNvlM|           stupidgsa|              Comedy| 2.3285183885964997|     165|    181|\n""""
  },
  {
    "{": ""      ""|nwLV1t_ho8s|          donaldsonb|     News & Politics| 0.5226687488170922|       6|     24|\n""""
  },
  {
    "{": ""      ""|o9vxIfgMjwQ|          ultraforos|              Sports|0.45661395523234666|      12|     20|\n""""
  },
  {
    "{": ""      ""|0_N1KbTSwfA|           13mordeth|      Pets & Animals|  0.509265844569844|      43|     56|\n""""
  },
  {
    "{": ""      ""|oaWjEARrxPA|         stealthtrev|      People & Blogs| 0.5655158582363691|       6|      5|\n""""
  },
  {
    "{": ""      ""|0nUI3TUdFCk|  freedom4expression|      People & Blogs| 2.1204538832914497|    3174|    469|\n""""
  },
  {
    "{": ""      ""|pNKd06j9mm4| BlinkAndAirwaves182|               Music|  0.355430596425427|      19|     14|\n""""
  },
  {
    "{": ""      ""|11F3RRcPbFg|    JohnsonBrand2000|    Film & Animation|0.47657557503537806|      28|     39|\n""""
  },
  {
    "{": ""      ""|pXhIlh2PCwU|       bananalickers|       Entertainment| 0.8793767285637156|       0|      1|\n""""
  },
  {
    "{": ""      ""|1SuBFWsHX_U|           pacificoz|               Music| 1.4122675989600977|      28|     66|\n""""
  },
  {
    "{": ""      ""|1mYs6gW4b1w|    GoogleEarthHacks|Science & Technology|  0.355430596425427|      12|     21|\n""""
  },
  {
    "{": ""      ""|plfJQOzt1jM|            Pylom748|       Entertainment|  2.082572957111787|      85|     86|\n""""
  },
  {
    "{": ""      ""|2F13vYKvaOY|          dexlab2323|                 UNA| 1.1286684060215422|       8|     34|\n""""
  },
  {
    "{": ""      ""|qX4gJLypggU|           Jenny8886|               Music| 0.3923298254130715|      13|     32|\n""""
  },
  {
    "{": ""      ""|2ONggv7_-B8|            djodaman|      People & Blogs|  1.721408464118553|       9|      7|\n""""
  },
  {
    "{": ""      ""|qZBs0N8ofMU|            yonnie86|      People & Blogs|  0.694133080592874|       2|     11|\n""""
  },
  {
    "{": ""      ""|3WikvT-80FA|        dubbedlakorn|    Film & Animation| 0.9440576907828162|       6|      2|\n""""
  },
  {
    "{": ""      ""|rsDd1irot3s|           caritoval|    Film & Animation| 0.5685894353931646|      25|     45|\n""""
  },
  {
    "{": ""      ""|3XvqlJNPCB4|         cherrycoke8|              Comedy| 0.3954458946891477|       0|      5|\n""""
  },
  {
    "{": ""      ""|rxl8qSKJblE|       LiLBrklynBrat|    Film & Animation|  0.355430596425427|      23|     14|\n""""
  },
  {
    "{": ""      ""|3pnrWNmnlZY|    elisabethstjjeed|              Comedy| 0.5893424106226627|       2|      1|\n""""
  },
  {
    "{": ""      ""|s5qChE2tdSI|         moonbeam001|               Music| 1.3262995016801609|      70|     66|\n""""
  },
  {
    "{": ""      ""|4AqPRcF7ZC0|              xflash|               Music|  1.354011194009465|    1126|    865|\n""""
  },
  {
    "{": ""      ""|sKK2lC8m670|            PhilipHK|       Entertainment| 0.7842934053511801|      76|     56|\n""""
  },
  {
    "{": ""      ""|4hd0iBmBhrA|         XxshinhwaxX|       Entertainment| 1.8889497894349825|       7|     24|\n""""
  },
  {
    "{": ""      ""|slD99VJ7_mI|          jxsxnheadz|               Music| 1.9429637635247936|      34|     71|\n""""
  },
  {
    "{": ""      ""|5De9tpD_bPU|         serchswitch|               Music| 1.1084567234319376|      38|     89|\n""""
  },
  {
    "{": ""      ""|szZh6vDjmC0|           mlbgamer3|              Comedy|  1.691989694814908|     455|    190|\n""""
  },
  {
    "{": ""      ""|5rAPvarfeTI|     xlilmizzbiatchx|       Entertainment| 3.2423618183768212|      39|     11|\n""""
  },
  {
    "{": ""      ""|t5R2-r-cPgg|          tiga131313|      People & Blogs| 1.6985761066295584|     133|     37|\n""""
  },
  {
    "{": ""      ""|6NhA4kM8hxA|           atoslucas|               Music| 0.3635731581371689|       8|      6|\n""""
  },
  {
    "{": ""      ""|tBuHP1P_p2c|         kaylleigh73|               Music| 0.7147784330167214|      15|     24|\n""""
  },
  {
    "{": ""      ""|72fNcSUuP60|   SteinbergSoftware|               Music|  0.520578676822748|       2|     15|\n""""
  },
  {
    "{": ""      ""|tLxz_dgBQkQ|        billzerosion|              Sports|  1.024134334145202|      39|     37|\n""""
  },
  {
    "{": ""      ""|73lb5_U_o6I|       TrueSpeeder55|       Entertainment| 0.8940267818393364|      67|     42|\n""""
  },
  {
    "{": ""      ""|t_mWE-WvIFA|           diasbneto|      People & Blogs| 0.6158657034959386|      17|     23|\n""""
  },
  {
    "{": ""      ""|8dmLP6pr3JM|        GangstaMelli|      People & Blogs| 1.3817996567222717|      11|     17|\n""""
  },
  {
    "{": ""      ""|u3hjWmnL_ws|        rcbgreengirl|       Howto & Style| 0.5525914105244951|      38|     23|\n""""
  },
  {
    "{": ""      ""|8gb51BanPjc|           AllieRX87|       Entertainment| 1.1442262045620823|     200|    127|\n""""
  },
  {
    "{": ""      ""|uaB0S_s5pG0|      NihilistZealot|      People & Blogs|  0.355430596425427|      20|     15|\n""""
  },
  {
    "{": ""      ""|98smlDOK5iM|             vansegg|      People & Blogs|  0.673247459508439|       2|      1|\n""""
  },
  {
    "{": ""      ""|uosLJnPE2AI|    Jimmymcjimthejim|       Entertainment|   0.56503449230337|      51|     18|\n""""
  },
  {
    "{": ""      ""|9XH1b0xHJGQ|    anonymousexposed|Nonprofits & Acti...| 0.6572631280762141|      54|    109|\n""""
  },
  {
    "{": ""      ""|uvichPfJVlI|          sfscorpio1|              Comedy|  2.090100670699918|      35|     60|\n""""
  },
  {
    "{": ""      ""|9oS1JHIYm8k|        XabyFerreyra|    Autos & Vehicles| 2.5176553065257377|      46|     27|\n""""
  },
  {
    "{": ""      ""|vABIMRxnNGY|      sexisallexpect|       Entertainment|  0.355430596425427|       1|      1|\n""""
  },
  {
    "{": ""      ""|A44AT5li-BI|         fred123aaa1|    Film & Animation| 1.1239383442518032|      10|     60|\n""""
  },
  {
    "{": ""      ""|vnGb44iktpA|          DanGeRouS1|       Entertainment| 0.4892871267182667|       2|      6|\n""""
  },
  {
    "{": ""      ""|A7Du3UbCCEI|            sturch88|              Comedy| 1.5646123136331014|       4|     29|\n""""
  },
  {
    "{": ""      ""|wmHGM0Hwuzo|      QuantumPetshop|       Entertainment| 0.3628204843654953|       8|     12|\n""""
  },
  {
    "{": ""      ""|AaD9CPiL6As|          supposedcp|      People & Blogs| 1.5262295458584225|     133|     42|\n""""
  },
  {
    "{": ""      ""|xcNSQ-VNEDY|         Novatorm2k3|       Entertainment| 0.5180971214721438|      17|      5|\n""""
  },
  {
    "{": ""      ""|z1d2Mu-xBnk|xxStephanieMcMahonxx|       Entertainment| 0.5567618655900222|       3|     16|\n""""
  },
  {
    "{": ""      ""|Acg4WncxvAE| universalmusicgroup|               Music| 3.7370221344437318|    1092|   1632|\n""""
  },
  {
    "{": ""      ""|zCA79Du-WqY|             daftboy|       Entertainment|0.43425976895377466|      17|     10|\n""""
  },
  {
    "{": ""      ""|B9Vsq-v1_3M|            arnone95|       Entertainment|0.40659214182009934|       0|      1|\n""""
  },
  {
    "{": ""      ""|zMTndhA21O0|     CommonSenseAnon|     News & Politics| 0.6424889218330362|      68|     41|\n""""
  },
  {
    "{": ""      ""|BSqir9m7RC8|               CCTD6|               Music| 0.6701047883276731|     159|    185|\n""""
  },
  {
    "{": ""      ""|zUph68zfA2Q|         pocastriped|      People & Blogs| 0.4162735343298895|       7|     11|\n""""
  },
  {
    "{": ""      ""|CNBOfikCSOw|                simF|       Entertainment| 0.5657802153560156|      22|     11|\n""""
  },
  {
    "{": ""      ""|-c-JIFcEzkM|           dmitry199|    Autos & Vehicles| 1.0123769399840925|      38|     36|\n""""
  },
  {
    "{": ""      ""|COS3HQDrH5E|            hermanrc|              Sports| 1.2460220056344247|       8|     21|\n""""
  },
  {
    "{": ""      ""|0LW9Bl5sfUk|    labaxuricantonai|               Music|0.41009230722021744|       0|      0|\n""""
  },
  {
    "{": ""      ""|DHD60KDGGKU|         gensing7000|      People & Blogs| 0.5609117135777776|       0|      0|\n""""
  },
  {
    "{": ""      ""|0elvz-77lB0|        AngeLuciferk|      People & Blogs| 1.0026005395016986|       8|     16|\n""""
  },
  {
    "{": ""      ""|DJ0fO5pXOxM| TheSofaKingCoolVids|              Comedy| 0.6815685022544737|      26|     28|\n""""
  },
  {
    "{": ""      ""|0qVrj0yhCzg|            MLucouch|      People & Blogs| 1.2920666310666469|     547|    750|\n""""
  },
  {
    "{": ""      ""|DMBcyt_CRM4|             three3v|               Music| 1.5973169203876296|     140|    280|\n""""
  },
  {
    "{": ""      ""|1-eE3Cdw4oM|         CrossAddict|       Howto & Style|0.36180921783401404|       7|      5|\n""""
  },
  {
    "{": ""      ""|Dax-UEN9Q24|            Paulopes|     News & Politics| 0.8684417751819532|       0|      1|\n""""
  },
  {
    "{": ""      ""|35tCcY-Dpzc|       wwwerihitscom|              Comedy| 0.7287077492759158|       0|      1|\n""""
  },
  {
    "{": ""      ""|-8E02ubcogo|         gokufighter|       Entertainment| 1.4657497855618278|      21|     25|\n""""
  },
  {
    "{": ""      ""|-F7MKfl2Tc4|        ShoujoShadow|       Entertainment| 0.5896575805435668|      18|     31|\n""""
  },
  {
    "{": ""      ""|3Vcya2QKj3Y|           Kariodude|       Entertainment| 0.3846989242900578|      70|     49|\n""""
  },
  {
    "{": ""      ""|-sw9RnNRrjU|            feverfew|               Music|  2.594579561349018|    1335|   1729|\n""""
  },
  {
    "{": ""      ""|0DHe47-vWNE|          Faithville|              Comedy| 0.3616405862910306|       0|      0|\n""""
  },
  {
    "{": ""      ""|3YDb1mZxQRk|              ruihsj|               Music| 0.5280146262794639|      29|     81|\n""""
  },
  {
    "{": ""      ""|0KGzTwbKkUw|           charfue02|    Autos & Vehicles|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|4LpXUe8nwjk|         kadykole445|       Entertainment| 0.3633312272819881|       1|      0|\n""""
  },
  {
    "{": ""      ""|0Z3nndaU92c|         4chewnahdoe|    Film & Animation| 0.5662182217486255|      10|      4|\n""""
  },
  {
    "{": ""      ""|4XPSIijgx-c|        HotGiseleXXX|      People & Blogs| 0.8171648512894237|       0|      4|\n""""
  },
  {
    "{": ""      ""|0f55LjG_2ko|            DJaws971|              Sports| 1.2130023749470218|      22|      6|\n""""
  },
  {
    "{": ""      ""|4jNn45YZYuA|           0verspeed|              Sports|0.42199133780158776|       1|      2|\n""""
  },
  {
    "{": ""      ""|1-XoqAKGNL4|          amishfella|              Comedy|0.45742459343780484|       0|      6|\n""""
  },
  {
    "{": ""      ""|5P3YlqVlIds|    michaelangelo911|      People & Blogs| 0.6720491379133802|     454|    106|\n""""
  },
  {
    "{": ""      ""|1slzAFFDHhw| entertainmentvideos|               Music|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|62qQYsMw_mA| KurdishKalaschnikow|               Music| 0.5148203363092516|      59|     39|\n""""
  },
  {
    "{": ""      ""|2Z_Szh5nVVU|           MMDreamer|      Pets & Animals|0.47854100376861824|       0|      1|\n""""
  },
  {
    "{": ""      ""|6SJ7HuOYmvo|     GotLoversToKill|               Music| 0.9927823212782518|     118|    334|\n""""
  },
  {
    "{": ""      ""|2vMLY4PTNd8|         JumanaElena|              Comedy|  0.557029460987595|      15|      7|\n""""
  },
  {
    "{": ""      ""|6_MApk1h8Ko|       Michealang3lo|      People & Blogs| 0.4185232454028555|       0|      0|\n""""
  },
  {
    "{": ""      ""|36KJKURUR1c|       xxplasticplue|    Film & Animation|0.48457645352291595|      10|     15|\n""""
  },
  {
    "{": ""      ""|71n2NDgt4Zc|             osiethe|    Autos & Vehicles|  4.196169100416973|      68|    216|\n""""
  },
  {
    "{": ""      ""|4Fxt2yLn06I|          rafaking29|    Film & Animation|   0.51503708186011|      11|     27|\n""""
  },
  {
    "{": ""      ""|71rmYy_sWh8|          rajatonnet|       Entertainment| 0.4342295955537531|       0|      3|\n""""
  },
  {
    "{": ""      ""|4QAlt4Sfl7Q|            peewee64|              Comedy|  7.552458864874045|    6219|  11028|\n""""
  },
  {
    "{": ""      ""|7GgSOHwouGo|             xavxlab|               Music| 0.4001357121147217|       1|      0|\n""""
  },
  {
    "{": ""      ""|4S67utI_rqI|         redindian32|      People & Blogs| 0.6026985940676397|      18|     20|\n""""
  },
  {
    "{": ""      ""|7XM4G8VV9HM|         jdub1234813|              Comedy| 1.1515010950741023|       9|    183|\n""""
  },
  {
    "{": ""      ""|4VsZxcFKpc0|               mad77|      People & Blogs| 0.7256050169402858|      13|     16|\n""""
  },
  {
    "{": ""      ""|8C1b59VlxcM|               jpb68|               Music| 0.7180433333875145|       1|      1|\n""""
  },
  {
    "{": ""      ""|55kLEqopRX4|        simuyuki1214|       Entertainment|0.38667884958513565|       9|      5|\n""""
  },
  {
    "{": ""      ""|8MbH_z7s_uM|          amoremusik|       Entertainment| 1.2580806019436104|     248|    148|\n""""
  },
  {
    "{": ""      ""|5JlNGLhoQ9c|         MagixReborn|           Education| 1.1501064641760308|      32|     35|\n""""
  },
  {
    "{": ""      ""|9aq4g30_OcA|            Reniweed|              Sports| 0.5631658947661231|       0|      0|\n""""
  },
  {
    "{": ""      ""|5lsFxFhN1xI|      CampaignOfPain|       Entertainment|0.39795867702170207|       0|      0|\n""""
  },
  {
    "{": ""      ""|AcuzL7qqIeo|            chiwiiii|              Comedy| 0.7468354465866365|       8|     39|\n""""
  },
  {
    "{": ""      ""|At7XSLpzp5Y|           rohstyles|              Sports|  0.737647566591084|      51|     52|\n""""
  },
  {
    "{": ""      ""|5vCRevl-nNs|           carmeta10|       Entertainment| 0.6010631283557333|       1|      1|\n""""
  },
  {
    "{": ""      ""|C_G2Mcw738E|      Crazystntman03|              Sports| 0.7104519900740939|       2|     14|\n""""
  },
  {
    "{": ""      ""|64GlixyOSYM|        detroitaaron|              Comedy| 1.1529739164972477|      38|    109|\n""""
  },
  {
    "{": ""      ""|-1q6T_mysHk|          sakaryabjk|       Entertainment|  0.546925983914422|      13|      8|\n""""
  },
  {
    "{": ""      ""|C_oXFsuWEg8|            verocubs|              Sports|0.39914869353046495|       9|      2|\n""""
  },
  {
    "{": ""      ""|6HTip2fGXxo|              theaob|              Comedy|  1.180783780786494|      95|    194|\n""""
  },
  {
    "{": ""      ""|CjrGhN3PAZ8|          YuKariGuYa|       Entertainment| 0.6448174798641937|       7|      7|\n""""
  },
  {
    "{": ""      ""|6LcFWNBfv0c|           tebanrhcp|       Entertainment| 0.4254554265081494|       1|      2|\n""""
  },
  {
    "{": ""      ""|D-C0G_RNcEc|         UnleashedTV|       Entertainment| 0.4255183101707433|      18|     32|\n""""
  },
  {
    "{": ""      ""|78nTRrTeYE4|          sylvia1144|      People & Blogs| 1.1629952840988778|      20|     27|\n""""
  },
  {
    "{": ""      ""|0JsTIVQKBfk|             dyloner|               Music| 0.8420415797353014|      33|     81|\n""""
  },
  {
    "{": ""      ""|D6z5gB5TAmg|           usm943550|    Film & Animation| 2.5050213488298847|       1|      2|\n""""
  },
  {
    "{": ""      ""|7wQbGDmaKZc|    HealthyHerbalist|           Education|  0.355430596425427|       4|      7|\n""""
  },
  {
    "{": ""      ""|DQt4bPuyDoU|      standard07et08|              Sports|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|22yA37j6gWA|             Floaded|       Entertainment| 1.7049174128414986|      31|     67|\n""""
  },
  {
    "{": ""      ""|81TeiLDW_YQ|           astridkok|       Entertainment| 0.3617330173901876|       0|      0|\n""""
  },
  {
    "{": ""      ""|DS0Y1mGiSUg|             arpegix|               Music|  0.929560157231996|      76|    195|\n""""
  },
  {
    "{": ""      ""|28vqNLRTNyg|            Rapshite|               Music|  2.419680501726048|      58|     68|\n""""
  },
  {
    "{": ""      ""|8E4uyzYaZ0A|            TheDetoX|    Film & Animation| 0.4465739786983645|      14|     17|\n""""
  },
  {
    "{": ""      ""|DnvxA4m8ogs|           leffler85|              Comedy|  0.355430596425427|       2|      6|\n""""
  },
  {
    "{": ""      ""|2mbHOzUnvoA|            carrics3|              Sports| 0.7111844107985926|      67|     85|\n""""
  },
  {
    "{": ""      ""|8EGEbgiNxHo|           EliteOps1|       Entertainment| 0.4367707317180619|      23|     13|\n""""
  },
  {
    "{": ""      ""|E3BWSTAN21w|         activevideo|     News & Politics| 0.3927401292881139|      54|    155|\n""""
  },
  {
    "{": ""      ""|39YzWStKXeA|        robertageile|       Entertainment| 0.5075385135817225|       0|      0|\n""""
  },
  {
    "{": ""      ""|8mViVOg0xOk|          femdomlite|       Entertainment| 1.2688703433844037|       1|      7|\n""""
  },
  {
    "{": ""      ""|E8Q2irptevU|         copronymous|     News & Politics| 0.8854774517820682|      59|     26|\n""""
  },
  {
    "{": ""      ""|3I2qm20260o|    djsandrothompson|               Music| 0.3687295893654847|       6|      7|\n""""
  },
  {
    "{": ""      ""|9iS97D0Rkko|             raayz0r|      People & Blogs| 1.2241859416205407|     479|    748|\n""""
  },
  {
    "{": ""      ""|ECiMchfOuXs|              rfeejk|              Sports|0.36274153257126374|       1|      3|\n""""
  },
  {
    "{": ""      ""|EcKybqktI4w|          Dirkovic80|               Music| 1.2651518733226081|       6|      9|\n""""
  },
  {
    "{": ""      ""|9idRM8J2KPg|     travelersdigest|     Travel & Events|  1.285923476696796|       9|     12|\n""""
  },
  {
    "{": ""      ""|EmR99DTYv_s|              jleb22|              Comedy|0.37254139839654904|       2|      4|\n""""
  },
  {
    "{": ""      ""|EEQJIsC1Ty0|  boxheadproductions|    Film & Animation| 0.7414716244721191|      54|     88|\n""""
  },
  {
    "{": ""      ""|AlF9WuNwiRo|     Nimothenicefish|              Comedy|  3.017799725835571|     128|    301|\n""""
  },
  {
    "{": ""      ""|F2GeKErfsi0|     iPodTouchGuru21|       Howto & Style| 0.6685884253934008|      24|      4|\n""""
  },
  {
    "{": ""      ""|Ed9CYDt99tA|           gfarrell3|               Music| 1.6968885605777195|      16|     48|\n""""
  },
  {
    "{": ""      ""|ApzMAkUtqfY|           borsuknr1|                 UNA|   1.67941343969831|     245|    321|\n""""
  },
  {
    "{": ""      ""|FOoTbkZdQOY|           KokoKaina|               Music|  1.365657374379215|     284|    418|\n""""
  },
  {
    "{": ""      ""|G9XSCTJZEVc|     KatieLovesYou99|       Entertainment|0.37165000841964746|       5|      8|\n""""
  },
  {
    "{": ""      ""|Bizjbag0Em0|            elena019|                 UNA| 0.4047850658813729|      10|     99|\n""""
  },
  {
    "{": ""      ""|GZhPxoHs1AU|        Currypan4101|       Entertainment|0.42954013477769104|       3|      4|\n""""
  },
  {
    "{": ""      ""|GJJf6-LI9WU|             michouu|               Music| 2.8296562413584185|     193|    329|\n""""
  },
  {
    "{": ""      ""|Bmd_ZY4kI-0|         latexisgood|       Entertainment| 0.6994948600757968|      16|     60|\n""""
  },
  {
    "{": ""      ""|GhcgCWI3Ntc|             giolaus|       Entertainment|0.38265692257007966|       0|      0|\n""""
  },
  {
    "{": ""      ""|GsJ3plHXVsc|        TenaciousJDD|       Entertainment| 1.2859656500032364|     364|    473|\n""""
  },
  {
    "{": ""      ""|By4hgPlNQ9I|          shannyfish|       Entertainment| 2.3957548817678678|      52|    122|\n""""
  },
  {
    "{": ""      ""|GheAd59anbU|          Goldentusk|              Comedy| 2.2721830322583756|    1253|   2177|\n""""
  },
  {
    "{": ""      ""|I2sozCXog8E|        ubertuberman|               Music|0.40373051760234363|       5|      3|\n""""
  },
  {
    "{": ""      ""|C-4uhrfsnw4|       twotonearmy22|               Music| 0.4563812027244731|       0|      7|\n""""
  },
  {
    "{": ""      ""|H7J7Rs66VRs|        godsholyword|      People & Blogs| 0.6992386174724111|      23|      9|\n""""
  },
  {
    "{": ""      ""|Ig4OibqO_pg|           BellaHart|      People & Blogs|  0.355430596425427|       4|      8|\n""""
  },
  {
    "{": ""      ""|EIgB2dfKluM|          LamarOdom1|               Music| 0.3762731962117447|     225|    422|\n""""
  },
  {
    "{": ""      ""|H7dU3HRA3gg|       ArnaudDelonge|               Music| 1.7325833352507967|     415|    645|\n""""
  },
  {
    "{": ""      ""|3vESWPgv_Fk|          TitanSpace|               Music|   0.73003881166221|       5|     15|\n""""
  },
  {
    "{": ""      ""|IuyfPdjR0EY|               BKJFK|               Music| 2.8304802084881806|     905|   1755|\n""""
  },
  {
    "{": ""      ""|F0O7hC0pe8k|            KandyCSN|       Entertainment| 1.2131993993062336|      15|     39|\n""""
  },
  {
    "{": ""      ""|HOh0UC2XIKY|      SyntheticRhyme|              Comedy|  2.093558582355411|     142|    109|\n""""
  },
  {
    "{": ""      ""|JPkOfcPecvg|             phxsns1|               Music| 0.8711796028169355|     209|     74|\n""""
  },
  {
    "{": ""      ""|4HyZsroCvrg|              Chhusu|               Music| 1.7319142266059298|     322|    285|\n""""
  },
  {
    "{": ""      ""|FZDAu0pDdxY|         Elcorillove|               Music|  1.479114591384564|      12|      9|\n""""
  },
  {
    "{": ""      ""|IIuvxHNq3y4|    YGOUploaderFreak|      People & Blogs| 0.7548581896993742|      26|     33|\n""""
  },
  {
    "{": ""      ""|JlexbYQb1hk|        SilverGirl30|               Music| 1.1703496414627317|      17|     20|\n""""
  },
  {
    "{": ""      ""|4cOppo4TTEs|            riveruno|     Travel & Events| 0.3743480636352428|       0|      3|\n""""
  },
  {
    "{": ""      ""|G1aCIo3uea8|             ggisser|      People & Blogs| 0.8942328080592113|     306|    192|\n""""
  },
  {
    "{": ""      ""|Ig9ZEXIUKiU|          INDOMABLES|               Music|  2.493014177300194|     445|    937|\n""""
  },
  {
    "{": ""      ""|KNoADBb8_ac|              goreo2|      People & Blogs| 0.7209645624714487|       8|     24|\n""""
  },
  {
    "{": ""      ""|5KhbTj7iiuQ|     hotpuppylvr2123|    Film & Animation|  2.015400126235618|     386|    872|\n""""
  },
  {
    "{": ""      ""|KPj2HSPBo18|            Stannecy|    Film & Animation| 0.3602692135290431|       2|      9|\n""""
  },
  {
    "{": ""      ""|GGFj3gkutnY|         jewelspoint|       Entertainment| 0.4278804781908019|      15|     11|\n""""
  },
  {
    "{": ""      ""|JO7BFuyA2oA|      EternalLight93|       Entertainment| 0.5733096683843355|       7|      4|\n""""
  },
  {
    "{": ""      ""|6COgQag3kog|           jwb012335|      People & Blogs| 0.3409406200723521|       0|      0|\n""""
  },
  {
    "{": ""      ""|K_OEeH8PkiU|         Goonerboy23|              Sports|0.49825065359053927|       1|      8|\n""""
  },
  {
    "{": ""      ""|G_McLZOfE9Q|       murdamuzik007|               Music|0.41794496010755544|       2|      1|\n""""
  },
  {
    "{": ""      ""|6F2y80RA2us|            msquare6|      People & Blogs|  0.532957125435065|       6|      9|\n""""
  },
  {
    "{": ""      ""|LnrTgc1neMc|       BuTTerBLume22|       Entertainment|0.36323103369549903|       6|      4|\n""""
  },
  {
    "{": ""      ""|6IazeOJeg30|      CrescentKnight|       Entertainment| 0.6419238788825541|      97|    176|\n""""
  },
  {
    "{": ""      ""|Goi7YBVqvtM|           rockfan37|       Entertainment| 0.4099661384067964|       1|      2|\n""""
  },
  {
    "{": ""      ""|LtYXYFHzcxM|        dragondedalo|    Film & Animation| 1.8351538615221186|      65|    253|\n""""
  },
  {
    "{": ""      ""|76Ep30M9wUU|          focus200hp|    Autos & Vehicles| 0.8576736333465669|     103|     26|\n""""
  },
  {
    "{": ""      ""|HCWOjh7v1rE|            DjDiddyD|              Sports| 0.4133905018377269|     184|     45|\n""""
  },
  {
    "{": ""      ""|LwgV8wd1L6E|            tijolin2|               Music| 0.4942077829825632|       2|     15|\n""""
  },
  {
    "{": ""      ""|7BfuR7yoIz8|             mattd28|              Comedy| 0.8587694685200393|      47|    150|\n""""
  },
  {
    "{": ""      ""|HEsOVDqiybo|             welshcs|               Music| 0.4175925848846056|      36|     56|\n""""
  },
  {
    "{": ""      ""|7F79m4ouMkA|           oscuro648|       Entertainment| 0.3676737639451829|       4|      9|\n""""
  },
  {
    "{": ""      ""|HZ2ej6ZDAoA|              bakazn|               Music|  3.016894074392318|     601|    815|\n""""
  },
  {
    "{": ""      ""|7SwF9GrZ8Og|       sexybabes2010|       Entertainment|0.44050615309122965|       3|      9|\n""""
  },
  {
    "{": ""      ""|HZjq-oPWok0|         qwertysonic|       Entertainment| 0.7309019263305583|      98|     59|\n""""
  },
  {
    "{": ""      ""|KNz3qrDdM2w|           ggemini17|                 UNA|  0.976199949653021|     146|    111|\n""""
  },
  {
    "{": ""      ""|7oxh5roiK54|          Jakkel1971|    Autos & Vehicles| 0.4784111294511172|       0|      0|\n""""
  },
  {
    "{": ""      ""|He144vw4X_c|       asturianica18|               Music| 1.0433460751715409|      11|     37|\n""""
  },
  {
    "{": ""      ""|MXDqWN-8pPU|          Danielgc90|       Entertainment|0.37328949228059194|       1|      1|\n""""
  },
  {
    "{": ""      ""|9SxZAQTetF8|        punisherusac|              Comedy| 0.4455904492890046|       4|      2|\n""""
  },
  {
    "{": ""      ""|Ip5SggQN4yo|           ioachabal|               Music| 0.3783566099874552|       3|      3|\n""""
  },
  {
    "{": ""      ""|MgIRHG9Yn4I|          mannie1952|       Howto & Style| 1.3169104729463337|      13|      8|\n""""
  },
  {
    "{": ""      ""|KX4ZryzA6YU|              nimano|               Music|  0.400281944747732|       1|      2|\n""""
  },
  {
    "{": ""      ""|A6JXFFEuFOM|              nelopo|              Sports| 0.5698351861504353|       3|      1|\n""""
  },
  {
    "{": ""      ""|MrNmYIwmz18|         ultimatekai|      People & Blogs| 0.5426893908283325|     137|     31|\n""""
  },
  {
    "{": ""      ""|JtmEx9SBbus|            espana36|    Film & Animation| 0.3958279918625113|       0|      5|\n""""
  },
  {
    "{": ""      ""|K_i0DkmmEW4|    ChrisBenoit12321|              Sports| 1.4134350663591906|     528|    327|\n""""
  },
  {
    "{": ""      ""|ADUMNWjywIE|          YTwatchdog|           Education|  2.196337756283802|    4255|   3750|\n""""
  },
  {
    "{": ""      ""|NRbehdvofoA|         fullmoon251|               Music| 1.7652227721600129|      12|     17|\n""""
  },
  {
    "{": ""      ""|KF1R1PuOi6w|    Blondegurlybritt|              Comedy|0.49746747411011455|       3|      5|\n""""
  },
  {
    "{": ""      ""|Kj8MpszNics|      dancingladyboy|               Music| 1.1876702844215061|     192|    227|\n""""
  },
  {
    "{": ""      ""|AIaTovCf1Jc|           mikylinux|       Entertainment| 2.4258161713062485|      86|    444|\n""""
  },
  {
    "{": ""      ""|NaruxWr-w2M|         ivanjelical|      People & Blogs|0.41778046835772903|       1|      0|\n""""
  },
  {
    "{": ""      ""|KJIcE0wKYlQ|           timmyboyy|      People & Blogs|  1.332809957487943|      90|     51|\n""""
  },
  {
    "{": ""      ""|KnboMWGpawA|          jogryg1990|               Music| 1.2019721881166934|     101|     72|\n""""
  },
  {
    "{": ""      ""|AKr0J_TibcU|      wejusthitaboat|              Comedy| 0.6692600902323369|       1|      4|\n""""
  },
  {
    "{": ""      ""|NqLO7xKUrwQ|        metallimacca|      Pets & Animals|  0.368495583510264|       4|      2|\n""""
  },
  {
    "{": ""      ""|KkSjJ-pih8g|            BKirby23|       Entertainment|  0.355430596425427|       0|      4|\n""""
  },
  {
    "{": ""      ""|KoOcKSJhO0U|          lesbic2008|      People & Blogs| 0.3914623550412952|       3|      3|\n""""
  },
  {
    "{": ""      ""|ASOzDFyuE7I|          blinkdrums|              Sports| 3.2690439889605205|      89|     33|\n""""
  },
  {
    "{": ""      ""|OHkmzlVmWL8|        suckerlove23|      People & Blogs|  1.481939517876162|     299|    130|\n""""
  },
  {
    "{": ""      ""|L-_47CrFZ8A|             filopou|       Entertainment| 0.7910099115809426|       0|      3|\n""""
  },
  {
    "{": ""      ""|M37PzM1iUQc|   UNDERTAKERULEZ102|      People & Blogs|0.36036322587561964|       0|      0|\n""""
  },
  {
    "{": ""      ""|B1fIoGTvQEE|         IGNthespike|               Music| 0.5948382436809453|      29|     23|\n""""
  },
  {
    "{": ""      ""|P9lbiVm6UJA|            redearth|      People & Blogs|  0.574963079191757|      60|     83|\n""""
  },
  {
    "{": ""      ""|LkOqQ84lXOA|           xrockxerx|       Entertainment|0.43615160204630143|      11|     36|\n""""
  },
  {
    "{": ""      ""|MSqXKp-00hM|           360comedy|              Comedy| 2.1931358490220942|      36|    280|\n""""
  },
  {
    "{": ""      ""|PHLmbD_dLh4|               R2oor|       Entertainment| 20.161248092985655|    1748|   1231|\n""""
  },
  {
    "{": ""      ""|BBiLYEArZMI|              xataan|              Sports| 0.7379495279702623|       4|      5|\n""""
  },
  {
    "{": ""      ""|MefjovJJr-0|              adam02|               Music|  1.854254140534959|    1071|   2585|\n""""
  },
  {
    "{": ""      ""|MZogFCT0K7g|            Toxxic88|       Entertainment| 0.7883100746523847|     701|    781|\n""""
  },
  {
    "{": ""      ""|Pa9w6KD4Ubk|            funero14|      Pets & Animals| 1.5209623013270617|       1|      5|\n""""
  },
  {
    "{": ""      ""|Bi5W_VelJuo|           ludwig222|      People & Blogs| 0.5151853206103123|      38|     71|\n""""
  },
  {
    "{": ""      ""|Mow_1bfkwvs|              bu5ter|              Comedy| 0.3818083908781706|      35|     42|\n""""
  },
  {
    "{": ""      ""|MpoaHq0k9hs|         monclovitas|     News & Politics| 1.1125882926359814|     439|    389|\n""""
  },
  {
    "{": ""      ""|PgeqzJoCslI|          SDAVIS6399|    Autos & Vehicles| 1.6765422062086237|      13|     12|\n""""
  },
  {
    "{": ""      ""|CPmzOqiEHVY|        scopescanner|      People & Blogs| 0.6071652324987392|       1|      2|\n""""
  },
  {
    "{": ""      ""|Mqwdkt90bME|          rudygal333|     News & Politics|  1.744990244735628|     219|      1|\n""""
  },
  {
    "{": ""      ""|NcMMkp8F7HQ|          Miaorisuda|      People & Blogs|0.45058778027804564|       1|      2|\n""""
  },
  {
    "{": ""      ""|Po8rG4nXpUs|               Zxcen|               Music|  2.196863217930293|      95|    246|\n""""
  },
  {
    "{": ""      ""|N9-g21nqo8s|        Shibiusa1305|    Film & Animation| 0.5664272138813914|      34|     46|\n""""
  },
  {
    "{": ""      ""|D2NCi7gLnAM|    troubledbubble15|       Entertainment| 0.3983916513151094|       0|      2|\n""""
  },
  {
    "{": ""      ""|NtouIccPNd0|         billyq11492|       Entertainment| 0.5527722218411333|       3|      2|\n""""
  },
  {
    "{": ""      ""|QVCKBl0L8Uk|       NameNotNeeded|      People & Blogs| 1.2520000119752879|      74|     42|\n""""
  },
  {
    "{": ""      ""|Oc-fbhD_dQI|      gilmoregirl129|               Music| 0.4203075046520844|      10|     11|\n""""
  },
  {
    "{": ""      ""|E2S9mZhnmxM|            machu300|               Music|0.46543257819473494|       8|      9|\n""""
  },
  {
    "{": ""      ""|NvpnR13QbcM|             JBar387|     Travel & Events|0.49016502995458355|       7|      1|\n""""
  },
  {
    "{": ""      ""|RBhhl0MBKgk|            ABVA1974|      People & Blogs| 0.4038528355845449|       0|      0|\n""""
  },
  {
    "{": ""      ""|EIkqkHh24Es|   XOXOXOcutieXOXOXO|              Comedy| 0.4202889093298669|      54|     37|\n""""
  },
  {
    "{": ""      ""|OKbr7NGIR24|           bleach885|    Film & Animation| 0.6450588787411681|       5|      9|\n""""
  },
  {
    "{": ""      ""|RLbNs73RU00|           jherald19|               Music| 0.6215771553095698|      12|      9|\n""""
  },
  {
    "{": ""      ""|EXkcYul1LRo|          hell666xxx|              Sports|  1.929783382161759|     456|    175|\n""""
  },
  {
    "{": ""      ""|OTVMVreWTwU|         lilronaldoo|              Sports| 0.8381668033259017|       6|      9|\n""""
  },
  {
    "{": ""      ""|ROjCS9P94aA|      samedifference|       Entertainment| 1.0543480700095418|     115|    125|\n""""
  },
  {
    "{": ""      ""|SHgtE5rwEac| universalmusicgroup|               Music|  4.505204843364811|    1672|   3330|\n""""
  },
  {
    "{": ""      ""|Q2nc8NJ1hz8|                rxd5|    Autos & Vehicles| 0.7652783707239009|      11|     29|\n""""
  },
  {
    "{": ""      ""|SPaX620sfzc|          1996connor|       Entertainment| 0.6498442536577294|      13|      2|\n""""
  },
  {
    "{": ""      ""|Q9ISi6C0DpQ|  polloziggy92263299|       Entertainment| 0.6100829518525132|       0|      0|\n""""
  },
  {
    "{": ""      ""|Sau1qzWpxFI|              dnc101|              Comedy| 1.3402172274821502|      28|     61|\n""""
  },
  {
    "{": ""      ""|QLxusjpv27A|           RBPing999|       Entertainment| 1.6208317374087065|     253|    100|\n""""
  },
  {
    "{": ""      ""|Sluaw3EVdFQ|             peron75|       Entertainment| 3.8481921568455983|    2439|   2632|\n""""
  },
  {
    "{": ""      ""|QTsDgvgEkpw|       pastalover113|    Autos & Vehicles|  2.398390868235125|      12|     11|\n""""
  },
  {
    "{": ""      ""|TItVP3dyKCs|      petstylist1111|      Pets & Animals| 0.3740079536080985|       0|      0|\n""""
  },
  {
    "{": ""      ""|ExlzzZ0-R44|           yurbd2007|      People & Blogs| 0.6470638472003193|       3|     23|\n""""
  },
  {
    "{": ""      ""|Oor8Szi3U-c|            amyla516|      Pets & Animals| 0.4783693449502293|       7|      3|\n""""
  },
  {
    "{": ""      ""|QaQw9V4Upj4|            CLIPADAY|              Comedy| 1.9287418012687634|     238|    446|\n""""
  },
  {
    "{": ""      ""|TJSC2a4KjSA|   travisandjonathan|     News & Politics| 0.6576084771872964|     138|    167|\n""""
  },
  {
    "{": ""      ""|EzeoyrnYui0|      justkevinjonas|               Music| 0.7151346526734778|      20|     16|\n""""
  },
  {
    "{": ""      ""|RNcvHlbh_t8|               trboh|      People & Blogs| 1.0856858162943863|      19|     12|\n""""
  },
  {
    "{": ""      ""|OpQLHktcoqA|            SHOWTIME|      People & Blogs|  4.438117548791393|      43|    139|\n""""
  },
  {
    "{": ""      ""|Tk5bMZWgN1U|            marimori|      People & Blogs| 0.5382485757041925|       1|      1|\n""""
  },
  {
    "{": ""      ""|Rv6erqN3DW0|  unioncityapartment|      People & Blogs|  0.355430596425427|       0|      0|\n""""
  },
  {
    "{": ""      ""|FORwJu-WyfE|             3ivind3|       Entertainment| 1.0116654261964408|      21|     36|\n""""
  },
  {
    "{": ""      ""|PddSG55aANQ|      Yappakoredesho|              Sports| 0.8092349363141267|      15|     10|\n""""
  },
  {
    "{": ""      ""|Txrfq62emgY| AshiieCookieMonster|       Entertainment|  0.535071419927151|       0|      0|\n""""
  },
  {
    "{": ""      ""|Rvlsw6tx6_8|        DarthHendrix|               Music|  0.366965077601724|       0|    127|\n""""
  },
  {
    "{": ""      ""|FRQNre51P8I|        Thomas868686|              Sports|   2.79575126598247|     855|    447|\n""""
  },
  {
    "{": ""      ""|Q5wZY2Qx0bQ|          xdeexxdeex|              Sports| 0.4897409414167592|       1|      0|\n""""
  },
  {
    "{": ""      ""|U8V2qEOj678|    THEREALHARDYSHOW|       Entertainment|  1.238822238770487|      65|     77|\n""""
  },
  {
    "{": ""      ""|Rw5Kb1uzm2c|         eliteballer|              Comedy| 0.5325626205436819|       9|     11|\n""""
  },
  {
    "{": ""      ""|QO9gPbcJaN0|            TaiShoCK|              Sports| 1.0517490087837311|      31|     85|\n""""
  },
  {
    "{": ""      ""|Fj9XrdcNTBU|          sinedizitv|    Film & Animation| 1.3867139907346633|      85|     67|\n""""
  },
  {
    "{": ""      ""|UGtQ2ENOk1U|          mooglepimp|              Comedy| 0.5647741397618435|       5|     15|\n""""
  },
  {
    "{": ""      ""|Sl0XcIvFY6w|            alexanth|              Comedy|  0.604110467827991|       1|     19|\n""""
  },
  {
    "{": ""      ""|QStm3ZyzgY0|            MrTickle|               Music| 1.2555509060189154|     115|    299|\n""""
  },
  {
    "{": ""      ""|HEAje2KOKGE|               Kat35|              Comedy| 0.6829477245512464|     542|   1132|\n""""
  },
  {
    "{": ""      ""|UQD8MPz28Ck|           huhux1989|              Sports| 0.6707371149110004|      41|     85|\n""""
  },
  {
    "{": ""      ""|TPpU5azjCB8|             Lordi79|    Autos & Vehicles| 2.7042117660409253|     804|    392|\n""""
  },
  {
    "{": ""      ""|QtqOMvMFXg4|        shadowkid485|               Music|0.47066127043732114|      41|     63|\n""""
  },
  {
    "{": ""      ""|HYAkylLFMHM|               SALPT|       Entertainment| 1.5012625239079356|      47|     13|\n""""
  },
  {
    "{": ""      ""|UQJafN63_N4|             bim1002|       Entertainment| 0.7054434740301782|       1|      3|\n""""
  },
  {
    "{": ""      ""|UFlsJcZjwzc|         luisbriseno|    Autos & Vehicles|  1.272028307343577|     134|    136|\n""""
  },
  {
    "{": ""      ""|RilaxU045Nw|             g3m1n1z|    Film & Animation| 2.6329547530237147|      88|    123|\n""""
  },
  {
    "{": ""      ""|HYFeXwwVkao|           lovefromm|                 UNA| 0.5242466165313835|      22|     27|\n""""
  },
  {
    "{": ""      ""|UuE6cI0MsUI|           cchannahl|       Entertainment| 0.6689489497712162|      13|     16|\n""""
  },
  {
    "{": ""      ""+-----------+--------------------+--------------------+-------------------+--------+-------+\n""""
  },
  {
    "{": ""      ""only showing top 1000 rows\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 17""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""81c55cf201afb13c""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:50.560154Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:47.101746Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# Get top 10 videos with the lowest PageRank scores\n""""
  },
  {
    "{": ""    ""lowest_pagerank_videos = (pagerank_results\n""""
  },
  {
    "{": ""    ""                              .select(\""id\""""
  },
  {
    "{": ""    ""                              .orderBy(col(\""pagerank\"").asc())\n""""
  },
  {
    "{": ""    ""                              .limit(10))\n""""
  },
  {
    "{": ""    ""print(\""Top 10 videos with the lowest PageRank scores:\"")\n""""
  },
  {
    "{": ""    ""lowest_pagerank_videos.show()""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Top 10 videos with the lowest PageRank scores:\n""""
  },
  {
    "{": ""      ""+-----------+----------------+--------------+------------------+--------+-------+-----+\n""""
  },
  {
    "{": ""      ""|         id|        uploader|      category|          pagerank|comments|ratings|views|\n""""
  },
  {
    "{": ""      ""+-----------+----------------+--------------+------------------+--------+-------+-----+\n""""
  },
  {
    "{": ""      ""|ypGHqfSVagQ|        SHOWTIME|           UNA|0.3409406200723521|     157|    186|37456|\n""""
  },
  {
    "{": ""      ""|6COgQag3kog|       jwb012335|People & Blogs|0.3409406200723521|       0|      0|  222|\n""""
  },
  {
    "{": ""      ""|5-2I5w1n4rQ|        ArTaNize|     Education|0.3409406200723521|       0|      0|    0|\n""""
  },
  {
    "{": ""      ""|igZdpMlGbWI|     iloveyou312| Entertainment|0.3409406200723521|       0|      0|    0|\n""""
  },
  {
    "{": ""      ""|Ie6Q9Z44X8w|  resolinofagolo| Entertainment|0.3409406200723521|       0|      1|  209|\n""""
  },
  {
    "{": ""      ""|8MXUBkuSqqE|  surfenwolf2000|         Music|0.3409406200723521|       0|      0|    0|\n""""
  },
  {
    "{": ""      ""|1r4hBa8haeQ|  Misterpangloss|         Music|0.3409406200723521|       0|      1|   92|\n""""
  },
  {
    "{": ""      ""|al91lTz9n6A|CarlyMueller9852|         Music|0.3409406200723521|       8|   1041| 2781|\n""""
  },
  {
    "{": ""      ""|3zesnNdverg| fiveawesomeguys|People & Blogs|0.3409406200723521|     278|    614| 7470|\n""""
  },
  {
    "{": ""      ""|WSYnvO5mgIQ|      slimcarrot|People & Blogs|0.3409406200723521|       0|      0|   18|\n""""
  },
  {
    "{": ""      ""+-----------+----------------+--------------+------------------+--------+-------+-----+\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 18""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""markdown""""
  },
  {
    "{": ""   ""id"": ""bcc99ca3b810bc49""""
  },
  {
    "{": ""   ""metadata"": {}""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""As we can see from the output above""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""ca266c52d705eaca""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:52.892035Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:50.608368Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""# Get top 10 videos with highest PageRank scores\n""""
  },
  {
    "{": ""    ""highest_pagerank_videos = (pagerank_results\n""""
  },
  {
    "{": ""    ""                              .select(\""id\""""
  },
  {
    "{": ""    ""                              .orderBy(col(\""pagerank\"").desc())\n""""
  },
  {
    "{": ""    ""                              .limit(10))\n""""
  },
  {
    "{": ""    ""print(\""Top 10 videos with the highest PageRank scores:\"")\n""""
  },
  {
    "{": ""    ""highest_pagerank_videos.show()\n""""
  },
  {
    "{": ""    ""# spark.stop()""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Top 10 videos with the highest PageRank scores:\n""""
  },
  {
    "{": ""      ""+-----------+-------------------+--------------+------------------+--------+-------+--------+\n""""
  },
  {
    "{": ""      ""|         id|           uploader|      category|          pagerank|comments|ratings|   views|\n""""
  },
  {
    "{": ""      ""+-----------+-------------------+--------------+------------------+--------+-------+--------+\n""""
  },
  {
    "{": ""      ""|xsRWpK4pf90|universalmusicgroup|         Music|113.02774950255144|   53441|  99373|44614530|\n""""
  },
  {
    "{": ""      ""|v3ARyAb_1Bs|          MastaBest|People & Blogs|107.50032978132789|   31065|  51806|31812447|\n""""
  },
  {
    "{": ""      ""|ktUSIJEiOug|         aliciakeys|         Music|106.46650417260115|   59672| 103074|43583367|\n""""
  },
  {
    "{": ""      ""|FIUv3dOBbCk|universalmusicgroup|         Music| 83.90051418663451|   23048|  45905|21384501|\n""""
  },
  {
    "{": ""      ""|a4X7eFbP3u4|universalmusicgroup|         Music| 78.47204558511518|   40906|  75369|34118063|\n""""
  },
  {
    "{": ""      ""|sLGLum5SyKQ|          SouljaBoy| Howto & Style| 74.75516607901349|   37301|  48094|31121122|\n""""
  },
  {
    "{": ""      ""|8JUvbJekM88| JonasBrothersMusic|         Music| 74.36513282443553|   73747|  45480|14540049|\n""""
  },
  {
    "{": ""      ""|LpocrqvP2Yg|universalmusicgroup|         Music| 68.75769644942268|   52948|  59911|20336357|\n""""
  },
  {
    "{": ""      ""|89oS4SN4mNg|          BritneyTV|         Music| 65.11915307009798|  108937|  72620|31484375|\n""""
  },
  {
    "{": ""      ""|sF84pIhP5UM|         leonalewis|         Music| 64.60549062567767|   50894|  72929|36537340|\n""""
  },
  {
    "{": ""      ""+-----------+-------------------+--------------+------------------+--------+-------+--------+\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 19""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""23ed56ce""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:53.657375Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:52.920651Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""from pymongo import MongoClient\n""""
  },
  {
    "{": ""    ""from collections import Counter\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# client = MongoClient(\""mongodb://localhost:27018/\"")\n""""
  },
  {
    "{": ""    ""client = MongoClient(\""mongodb://localhost:27017/\"")\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""db = client[\""youtubedb\""]\n""""
  },
  {
    "{": ""    ""collection = db[\""youtube_vids\""]\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""k = 10\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""def top_k_categories(collection""
  },
  {
    "{": ""    ""    pipeline = [\n""""
  },
  {
    "{": ""    ""        {\""$group\"": {\""_id\"": \""$category\""""
  },
  {
    "{": ""    ""        {\""$sort\"": {\""count\"": -1}}""
  },
  {
    "{": ""    ""        {\""$limit\"": k}\n""""
  },
  {
    "{": ""    ""    ]\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""    top_categories = list(collection.aggregate(pipeline))\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""    print(\""Top categories:\"")\n""""
  },
  {
    "{": ""    ""    for entry in top_categories:\n""""
  },
  {
    "{": ""    ""        print(f\""{entry['_id']}: {entry['count']}\"")\n""""
  },
  {
    "{": ""    ""    print(\""\\n\"")\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""top_k_categories(collection""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Top categories:\n""""
  },
  {
    "{": ""    ""# Entertainment 162044\n""""
  },
  {
    "{": ""    ""# Music 156208\n""""
  },
  {
    "{": ""    ""# Comedy 61113\n""""
  },
  {
    "{": ""    ""# People & Blogs 56036\n""""
  },
  {
    "{": ""    ""# Film & Animation 51459\n""""
  },
  {
    "{": ""    ""# Sports 48265\n""""
  },
  {
    "{": ""    ""# News & Politics 30913\n""""
  },
  {
    "{": ""    ""# Autos & Vehicles 19237\n""""
  },
  {
    "{": ""    ""# Howto & Style 18031\n""""
  },
  {
    "{": ""    ""# Pets & Animals 11325\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""def top_k_categories_gui(collection""
  },
  {
    "{": ""    ""    pipeline = [\n""""
  },
  {
    "{": ""    ""        {\""$group\"": {\""_id\"": \""$category\""""
  },
  {
    "{": ""    ""        {\""$sort\"": {\""count\"": -1}}""
  },
  {
    "{": ""    ""        {\""$limit\"": k}\n""""
  },
  {
    "{": ""    ""    ]\n""""
  },
  {
    "{": ""    ""    top_categories = list(collection.aggregate(pipeline))\n""""
  },
  {
    "{": ""    ""    return top_categories""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Top categories:\n""""
  },
  {
    "{": ""      ""Entertainment: 162044\n""""
  },
  {
    "{": ""      ""Music: 156208\n""""
  },
  {
    "{": ""      ""Comedy: 61113\n""""
  },
  {
    "{": ""      ""People & Blogs: 56036\n""""
  },
  {
    "{": ""      ""Film & Animation: 51459\n""""
  },
  {
    "{": ""      ""Sports: 48265\n""""
  },
  {
    "{": ""      ""News & Politics: 30913\n""""
  },
  {
    "{": ""      ""Autos & Vehicles: 19237\n""""
  },
  {
    "{": ""      ""Howto & Style: 18031\n""""
  },
  {
    "{": ""      ""Pets & Animals: 11325\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 20""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""507293d0""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:54.233658Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:53.709332Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""#Top k rated videos\n""""
  },
  {
    "{": ""    ""def top_k_rated_videos(collection""
  },
  {
    "{": ""    ""    print(\""Top rated videos:\"")\n""""
  },
  {
    "{": ""    ""    top_rated_videos = collection.find().sort(\""rate\""""
  },
  {
    "{": ""    ""    for video in top_rated_videos:\n""""
  },
  {
    "{": ""    ""        print(video[\""videoID\""]""
  },
  {
    "{": ""    ""    print(\""\\n\"")\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""top_k_rated_videos(collection""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""def top_k_rated_videos_gui(collection""
  },
  {
    "{": ""    ""    top_rated_videos = collection.find().sort(\""rate\""""
  },
  {
    "{": ""    ""    return top_rated_videos""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Top rated videos:\n""""
  },
  {
    "{": ""      ""DV9DxJ2lhnw 5.0\n""""
  },
  {
    "{": ""      ""ZXyGmpE7MW8 5.0\n""""
  },
  {
    "{": ""      ""YZev1imoxX8 5.0\n""""
  },
  {
    "{": ""      ""NzVDm9sZWGI 5.0\n""""
  },
  {
    "{": ""      ""cvyWz0itTiM 5.0\n""""
  },
  {
    "{": ""      ""3TYqkBJ9YRk 5.0\n""""
  },
  {
    "{": ""      ""gP0jnBrVEpI 5.0\n""""
  },
  {
    "{": ""      ""dh6dF1XY3uI 5.0\n""""
  },
  {
    "{": ""      ""ZZpZOI-QBQU 5.0\n""""
  },
  {
    "{": ""      ""haOxt1wpWQA 5.0\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 21""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""efab2439""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:54.789601Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:54.288362Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""#Top k viewed videos\n""""
  },
  {
    "{": ""    ""def top_k_viewed_videos(collection""
  },
  {
    "{": ""    ""    print(\""Top viewed videos:\"")\n""""
  },
  {
    "{": ""    ""    top_viewed_videos = collection.find().sort(\""views\""""
  },
  {
    "{": ""    ""    for video in top_viewed_videos:\n""""
  },
  {
    "{": ""    ""        print(video[\""videoID\""]""
  },
  {
    "{": ""    ""    print(\""\\n\"")\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""top_k_viewed_videos(collection""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""def top_k_viewed_videos_gui(collection""
  },
  {
    "{": ""    ""    top_viewed_videos = collection.find().sort(\""views\""""
  },
  {
    "{": ""    ""    return top_viewed_videos""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Top viewed videos:\n""""
  },
  {
    "{": ""      ""dMH0bHeiRNg 79897120\n""""
  },
  {
    "{": ""      ""cQ25-glGRzI 77674728\n""""
  },
  {
    "{": ""      ""12Z3J1uzd0Q 65341925\n""""
  },
  {
    "{": ""      ""244qR7SvvX0 57790943\n""""
  },
  {
    "{": ""      ""ePyRrb2-fzs 45984219\n""""
  },
  {
    "{": ""      ""xsRWpK4pf90 44614530\n""""
  },
  {
    "{": ""      ""ktUSIJEiOug 43583367\n""""
  },
  {
    "{": ""      ""b3u65f4CRLk 43511791\n""""
  },
  {
    "{": ""      ""iWg3IMN_rhU 43323757\n""""
  },
  {
    "{": ""      ""5P6UU6m3cqk 42525795\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 22""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""1bb8e356""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:55.029043Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:54.822058Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""#Range queries\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""# Find videos in specific category with a duration between t1 and t2 seconds\n""""
  },
  {
    "{": ""    ""category = \""Comedy\"" \n""""
  },
  {
    "{": ""    ""t1 = 700 \n""""
  },
  {
    "{": ""    ""t2 = 1000 \n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""def videos_in_length_range_by_category(category""
  },
  {
    "{": ""    ""    category_query = {\n""""
  },
  {
    "{": ""    ""    \""category\"": category""
  },
  {
    "{": ""    ""    \""length\"": {\""$gte\"": t1""
  },
  {
    "{": ""    ""}\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""    print(f\""Videos in category {category} with duration between {t1} and {t2} seconds:\"")\n""""
  },
  {
    "{": ""    ""    result = collection.find(category_query)\n""""
  },
  {
    "{": ""    ""    for video in result:\n""""
  },
  {
    "{": ""    ""        print(f\""Video ID: {video['videoID']}""
  },
  {
    "{": ""    ""    print(\""\\n\"")\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""videos_in_length_range_by_category(category""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""def videos_in_length_range_by_category_gui(collection""
  },
  {
    "{": ""    ""    category_query = {\n""""
  },
  {
    "{": ""    ""        \""category\"": category""
  },
  {
    "{": ""    ""        \""length\"": {\""$gte\"": t1""
  },
  {
    "{": ""    ""    }\n""""
  },
  {
    "{": ""    ""    result = collection.find(category_query)\n""""
  },
  {
    "{": ""    ""    return list(result)""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""Videos in category Comedy with duration between 700 and 1000 seconds:\n""""
  },
  {
    "{": ""      ""Video ID: qkrvYnNpQm4""
  },
  {
    "{": ""      ""Video ID: E7OKDwX4Auw""
  },
  {
    "{": ""      ""Video ID: nqU2obMOz0M""
  },
  {
    "{": ""      ""Video ID: w8QzcS7g52g""
  },
  {
    "{": ""      ""Video ID: wWW8R58R8qs""
  },
  {
    "{": ""      ""Video ID: qJXYN3wFhgo""
  },
  {
    "{": ""      ""Video ID: nJ-xoIziMmQ""
  },
  {
    "{": ""      ""Video ID: G1l4hQM_d1w""
  },
  {
    "{": ""      ""Video ID: RQz5kcwgtl0""
  },
  {
    "{": ""      ""Video ID: ccIJ39u1fTI""
  },
  {
    "{": ""      ""Video ID: TUU3M442H1k""
  },
  {
    "{": ""      ""Video ID: Pdtb6yxolSw""
  },
  {
    "{": ""      ""Video ID: mGAuXid4FYU""
  },
  {
    "{": ""      ""Video ID: myB_8UPTGBQ""
  },
  {
    "{": ""      ""Video ID: 4Pp0VqblMPA""
  },
  {
    "{": ""      ""Video ID: op4byt-DtsI""
  },
  {
    "{": ""      ""Video ID: NrewpOyt5KE""
  },
  {
    "{": ""      ""Video ID: IUiNFzzF-ZI""
  },
  {
    "{": ""      ""Video ID: ICAfNYith5M""
  },
  {
    "{": ""      ""Video ID: 5l_c7MH-auA""
  },
  {
    "{": ""      ""Video ID: CXs8OSex56w""
  },
  {
    "{": ""      ""Video ID: SMrrdfOUNxs""
  },
  {
    "{": ""      ""Video ID: c4kxMiP6pmg""
  },
  {
    "{": ""      ""Video ID: X3t8XKtFMlI""
  },
  {
    "{": ""      ""Video ID: l9ijLulwUTY""
  },
  {
    "{": ""      ""Video ID: tWaKcvuh1os""
  },
  {
    "{": ""      ""Video ID: EzA7RnLxoQY""
  },
  {
    "{": ""      ""Video ID: 5vYs3n9mMuA""
  },
  {
    "{": ""      ""Video ID: 8X5qxBh3UC8""
  },
  {
    "{": ""      ""Video ID: qYPDKMYDiZ4""
  },
  {
    "{": ""      ""Video ID: JYQNcuFbjoU""
  },
  {
    "{": ""      ""Video ID: fQFs33fWzxo""
  },
  {
    "{": ""      ""Video ID: _hC-7mhg5x8""
  },
  {
    "{": ""      ""Video ID: X0IV_ZB9CDs""
  },
  {
    "{": ""      ""Video ID: k-sfM_bt5i8""
  },
  {
    "{": ""      ""Video ID: UlEGZmduSdE""
  },
  {
    "{": ""      ""Video ID: zzkJbWl45kU""
  },
  {
    "{": ""      ""Video ID: -FVSNDb09ho""
  },
  {
    "{": ""      ""Video ID: Go_VtqtxCHY""
  },
  {
    "{": ""      ""Video ID: wC-KAefuWxs""
  },
  {
    "{": ""      ""Video ID: JmN5mrnPVJU""
  },
  {
    "{": ""      ""Video ID: lQBYHXlH61g""
  },
  {
    "{": ""      ""Video ID: WvnbGoW0ZBQ""
  },
  {
    "{": ""      ""Video ID: Y6UzDbtImo4""
  },
  {
    "{": ""      ""Video ID: f3_CYdYDDpk""
  },
  {
    "{": ""      ""Video ID: 8oaD8AfEc7Y""
  },
  {
    "{": ""      ""Video ID: muImlz21cV8""
  },
  {
    "{": ""      ""Video ID: cGSOwVeGllo""
  },
  {
    "{": ""      ""Video ID: 0SIEKaCYPCY""
  },
  {
    "{": ""      ""Video ID: 0lcA5fQa_ak""
  },
  {
    "{": ""      ""Video ID: Sn0iosJVSIQ""
  },
  {
    "{": ""      ""Video ID: PLvqM1xl6u8""
  },
  {
    "{": ""      ""Video ID: deME6ND4qsA""
  },
  {
    "{": ""      ""Video ID: qHNns5n5sWg""
  },
  {
    "{": ""      ""Video ID: oKdbVwJ1Qps""
  },
  {
    "{": ""      ""Video ID: UBVEk3zMYN0""
  },
  {
    "{": ""      ""Video ID: 0kF2srw4Bks""
  },
  {
    "{": ""      ""Video ID: 7rk1OIOnfwM""
  },
  {
    "{": ""      ""Video ID: E0zn5xkLIjE""
  },
  {
    "{": ""      ""Video ID: 1HLb3uH1p3Q""
  },
  {
    "{": ""      ""Video ID: bGkVpY9t3qw""
  },
  {
    "{": ""      ""Video ID: xxuVCrMNC4Q""
  },
  {
    "{": ""      ""Video ID: 10vLOqVPgZM""
  },
  {
    "{": ""      ""Video ID: pF9OiNVlnNI""
  },
  {
    "{": ""      ""Video ID: IWbbfebhygA""
  },
  {
    "{": ""      ""Video ID: PAdG0Kvpq5k""
  },
  {
    "{": ""      ""Video ID: st823ae7ZgI""
  },
  {
    "{": ""      ""Video ID: 0YgWQdfq4so""
  },
  {
    "{": ""      ""Video ID: zDXAJH3LvJg""
  },
  {
    "{": ""      ""Video ID: GzWK12vSP6o""
  },
  {
    "{": ""      ""Video ID: Dwal6mL73xU""
  },
  {
    "{": ""      ""Video ID: y53Bfol4zao""
  },
  {
    "{": ""      ""Video ID: 7cC5HG3QnBw""
  },
  {
    "{": ""      ""Video ID: XYgjOIWXsu4""
  },
  {
    "{": ""      ""Video ID: LocGRt7GQ-E""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""      ""\n""""
  },
  {
    "{": ""     ]""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""execution_count"": 23""
  },
  {
    "{": ""  }""
  },
  {
    "{": ""  {""
  },
  {
    "{": ""   ""cell_type"": ""code""""
  },
  {
    "{": ""   ""id"": ""8f6a53d6""""
  },
  {
    "{": ""   ""metadata"": {""
  },
  {
    "{": ""    ""ExecuteTime"": {""
  },
  {
    "{": ""     ""end_time"": ""2024-12-07T01:10:56.245406Z""""
  },
  {
    "{": ""     ""start_time"": ""2024-12-07T01:10:55.074483Z""""
  },
  {
    "{": ""    }""
  },
  {
    "{": ""   }""
  },
  {
    "{": ""   ""source"": [""
  },
  {
    "{": ""    ""t1 = 500\n""""
  },
  {
    "{": ""    ""t2 = 1000 \n""""
  },
  {
    "{": ""    ""def get_videos_in_length_range(t1""
  },
  {
    "{": ""    ""    general_query = {\n""""
  },
  {
    "{": ""    "" \""length\"": {\""$gte\"": t1""
  },
  {
    "{": ""    ""}\n""""
  },
  {
    "{": ""    ""    print(f\""All videos with duration between {t1} and {t2} seconds:\"")\n""""
  },
  {
    "{": ""    ""    result = collection.find(general_query)\n""""
  },
  {
    "{": ""    ""    for video in result:\n""""
  },
  {
    "{": ""    ""        print(f\""Video ID: {video['videoID']}""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""get_videos_in_length_range(t1""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""def get_videos_in_length_range_gui(collection""
  },
  {
    "{": ""    ""    general_query = {\n""""
  },
  {
    "{": ""    "" \""length\"": {\""$gte\"": t1""
  },
  {
    "{": ""    ""}\n""""
  },
  {
    "{": ""    ""    result = collection.find(general_query)\n""""
  },
  {
    "{": ""    ""    return list(result)\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""    ""\n""""
  },
  {
    "{": ""   ]""
  },
  {
    "{": ""   ""outputs"": [""
  },
  {
    "{": ""    {""
  },
  {
    "{": ""     ""name"": ""stdout""""
  },
  {
    "{": ""     ""output_type"": ""stream""""
  },
  {
    "{": ""     ""text"": [""
  },
  {
    "{": ""      ""All videos with duration between 500 and 1000 seconds:\n""""
  },
  {
    "{": ""      ""Video ID: MhHfemP1GqU""
  },
  {
    "{": ""      ""Video ID: Rb_HXgPlgEs""
  },
  {
    "{": ""      ""Video ID: kmvcP71A-Wk""
  },
  {
    "{": ""      ""Video ID: QOdlnzkeoyQ""
  },
  {
    "{": ""      ""Video ID: AY5tM_U5VVw""
  },
  {
    "{": ""      ""Video ID: oi5dBnMZwdU""
  },
  {
    "{": ""      ""Video ID: jhyZGkGO4ZM""
  },
  {
    "{": ""      ""Video ID: IVY-LDL7A3M""
  },
  {
    "{": ""      ""Video ID: aIiRFSCgGu4""
  },
  {
    "{": ""      ""Video ID: eRqZfts4ClU""
  },
  {
    "{": ""      ""Video ID: G6SGwzsMZlw""
  },
  {
    "{": ""      ""Video ID: 3nQINA-UQ-g""
  },
  {
    "{": ""      ""Video ID: rtVbNdMHr60""
  },
  {
    "{": ""      ""Video ID: X5THlVnLFaA""
  },
  {
    "{": ""      ""Video ID: cvyWz0itTiM""
  },
  {
    "{": ""      ""Video ID: ITkCUj1zPw0""
  },
  {
    "{": ""      ""Video ID: 5-2I5w1n4rQ""
  },
  {
    "{": ""      ""Video ID: oOzBvdOtt5Y""
  },
  {
    "{": ""      ""Video ID: Pfn7L51e5Is""
  },
  {
    "{": ""      ""Video ID: 17IMWyNVOIg""
  },
  {
    "{": ""      ""Video ID: OshpuI9BGVU""
  },
  {
    "{": ""      ""Video ID: McZ3lP8lb6E""
  },
  {
    "{": ""      ""Video ID: aYHBqH_xbCw""
  },
  {
    "{": ""      ""Video ID: 13YOGHzzoMA""
  },
  {
    "{": ""      ""Video ID: qkrvYnNpQm4""
  },
  {
    "{": ""      ""Video ID: p3KqyCDaH28""
  },
  {
    "{": ""      ""Video ID: cRT3tV9VdbU""
  },
  {
    "{": ""      ""Video ID: S-6sdlftpv8""
  },
  {
    "{": ""      ""Video ID: E7OKDwX4Auw""
  },
  {
    "{": ""      ""Video ID: muaTrM7Ouxw""
  },
  {
    "{": ""      ""Video ID: oG21V-JwWYs""
  },
  {
    "{": ""      ""Video ID: xwGX5Fx7o8E""
  },
  {
    "{": ""      ""Video ID: R08Nxax_jsM""
  },
  {
    "{": ""      ""Video ID: HLAdLQ78LjU""
  },
  {
    "{": ""      ""Video ID: L4DICgyB6JE""
  },
  {
    "{": ""      ""Video ID: nqU2obMOz0M""
  },
  {
    "{": ""      ""Video ID: luB-JA8u8Fk""
  },
  {
    "{": ""      ""Video ID: 4Du5CNQuPhQ""
  },
  {
    "{": ""      ""Video ID: 3NgXUJJO8II""
  },
  {
    "{": ""      ""Video ID: wgXhN7lHXZs""
  },
  {
    "{": ""      ""Video ID: 3lj0uSB2Qs8""
  },
  {
    "{": ""      ""Video ID: 0pr7TkYVVAg""
  },
  {
    "{": ""      ""Video ID: Cgx0LnnXFO4""
  },
  {
    "{": ""      ""Video ID: 2h8nqVzP3j4""
  },
  {
    "{": ""      ""Video ID: tyfxM1WImb8""
  },
  {
    "{": ""      ""Video ID: BmpZ1ztfVqg""
  },
  {
    "{": ""      ""Video ID: hYkuhfsoX6M""
  },
  {
    "{": ""      ""Video ID: lyto3AubZFw""
  },
  {
    "{": ""      ""Video ID: kb8rdc-0OpQ""
  },
  {
    "{": ""      ""Video ID: LbbRpN2FNmw""
  },
  {
    "{": ""      ""Video ID: iyjLnvI4yE0""
  },
  {
    "{": ""      ""Video ID: 3IWY5MIlhiY""
  },
  {
    "{": ""      ""Video ID: tcfgvsCScsA""
  },
  {
    "{": ""      ""Video ID: JqoKuW0NS8g""
  },
  {
    "{": ""      ""Video ID: ZXptgNiUgw0""
  },
  {
    "{": ""      ""Video ID: 1RMc-HLMh4c""
  },
  {
    "{": ""      ""Video ID: zhES-GCD72c""
  },
  {
    "{": ""      ""Video ID: lVo88qqkkPQ""
  },
  {
    "{": ""      ""Video ID: jY0v32LAe9M""
  },
  {
    "{": ""      ""Video ID: OfsoIFDUyao""
  },
  {
    "{": ""      ""Video ID: 2qlOLmaoYzw""
  },
  {
    "{": ""      ""Video ID: wXPT48Irs4M""
  },
  {
    "{": ""      ""Video ID: uOwhdkJcz-c""
  },
  {
    "{": ""      ""Video ID: IirmETYJOw0""
  },
  {
    "{": ""      ""Video ID: jTpTOGljpLY""
  },
  {
    "{": ""      ""Video ID: k3NU5WZXCKU""
  },
  {
    "{": ""      ""Video ID: mSgwvL4Gdyw""
  },
  {
    "{": ""      ""Video ID: WW68Yx-_VZA""
  },
  {
    "{": ""      ""Video ID: -W2PeiA2JnY""
  },
  {
    "{": ""      ""Video ID: tjfzBfqp1UA""
  },
  {
    "{": ""      ""Video ID: twhcvq5JIUY""
  },
  {
    "{": ""      ""Video ID: NmgQHYChrPw""
  },
  {
    "{": ""      ""Video ID: ixRhRI5eXyU""
  },
  {
    "{": ""      ""Video ID: Z4A26YUsPgI""
  },
  {
    "{": ""      ""Video ID: DnmO7U92DrY""
  },
  {
    "{": ""      ""Video ID: 4dK-9jLPGqc""
  },
  {
    "{": ""      ""Video ID: V6ZYgDrzvZU""
  },
  {
    "{": ""      ""Video ID: ZRjPxVrm0VM""
  },
  {
    "{": ""      ""Video ID: _kjGOt4xdso""
  },
  {
    "{": ""      ""Video ID: 265li8v9m1k""
  },
  {
    "{": ""      ""Video ID: OMe5lb8kQWQ""
  },
  {
    "{": ""      ""Video ID: o2omZSr6a88""
  },
  {
    "{": ""      ""Video ID: iQ1_lN8I2_c""
  },
  {
    "{": ""      ""Video ID: m1Iqq081wVw""
  },
  {
    "{": ""      ""Video ID: b0hqh_yRIiA""
  },
  {
    "{": ""      ""Video ID: m0UjE32EF1Q""
  },
  {
    "{": ""      ""Video ID: LZMcAsNnvl4""
  },
  {
    "{": ""      ""Video ID: Aqvs3988wbU""
  },
  {
    "{": ""      ""Video ID: FpKmmCxOcGQ""
  },
  {
    "{": ""      ""Video ID: TvlUpoffohM""
  },
  {
    "{": ""      ""Video ID: 12Z3J1uzd0Q""
  },
  {
    "{": ""      ""Video ID: KGBE0c2OJKI""
  },
  {
    "{": ""      ""Video ID: 7Z12pSrZ-fU""
  },
  {
    "{": ""      ""Video ID: pjak4ByHnco""
  },
  {
    "{": ""      ""Video ID: 5R5oh8AIguE""
  },
  {
    "{": ""      ""Video ID: k67oCuyNQCw""
  },
  {
    "{": ""      ""Video ID: AJ9kRIgbMW8""
  },
  {
    "{": ""      ""Video ID: FQRRPM8pVJI""
  },
  {
    "{": ""      ""Video ID: ZE3QS_02R_s""
  },
  {
    "{": ""      ""Video ID: 28jgpGsmQjU""
  },
  {
    "{": ""      ""Video ID: 1LxOL9m254k""
  },
  {
    "{": ""      ""Video ID: 04ERBsim9rc""
  },
  {
    "{": ""      ""Video ID: I1c0uS5wkto""
  },
  {
    "{": ""      ""Video ID: Xz5amzknTSY""
  },
  {
    "{": ""      ""Video ID: rR4r5OPmTf0""
  },
  {
    "{": ""      ""Video ID: Oe5IKgKKjJw""
  },
  {
    "{": ""      ""Video ID: rvsWvMqBW6E""
  },
  {
    "{": ""      ""Video ID: C4wZf9Y66rM""
  },
  {
    "{": ""      ""Video ID: 2drgIjrFkto""
  },
  {
    "{": ""      ""Video ID: UIbyUOfz-9w""
  },
  {
    "{": ""      ""Video ID: _Le9DB9NXzU""
  },
  {
    "{": ""      ""Video ID: kjT-Ia4sDYw""
  },
  {
    "{": ""      ""Video ID: RLeLtDIdTuY""
  },
  {
    "{": ""      ""Video ID: RScKvEwKzZs""
  },
  {
    "{": ""      ""Video ID: QWASKqQ7EKk""
  },
  {
    "{": ""      ""Video ID: DgEoY4X0m1Q""
  },
  {
    "{": ""      ""Video ID: EHsfm7hqdIA""
  },
  {
    "{": ""      ""Video ID: PpQ2iDD0nuM""
  },
  {
    "{": ""      ""Video ID: 8_oNJgrQWbE""
  },
  {
    "{": ""      ""Video ID: VoHFXWiYQ8o""
  },
  {
    "{": ""      ""Video ID: CUBy19PMsmU""
  },
  {
    "{": ""      ""Video ID: OOVEWiXZZlw""
  },
  {
    "{": ""      ""Video ID: hCJv1iLF8HA""
  },
  {
    "{": ""      ""Video ID: 5wNzG4S6wKk""
  },
  {
    "{": ""      ""Video ID: AfDnOePoE00""
  },
  {
    "{": ""      ""Video ID: Qz7LIVE9dQE""
  },
  {
    "{": ""      ""Video ID: 0wu1i6GooQY""
  },
  {
    "{": ""      ""Video ID: UmkMj73FAQY""
  },
  {
    "{": ""      ""Video ID: bgyHqXcyxNk""
  },
  {
    "{": ""      ""Video ID: PfiQKUZPc1E""
  },
  {
    "{": ""      ""Video ID: 7xpLD8Zv5L4""
  },
  {
    "{": ""      ""Video ID: vyia7e7g01o""
  },
  {
    "{": ""      ""Video ID: YSDCdz9zgN0""
  },
  {
    "{": ""      ""Video ID: 6cEQnrd94Mc""
  },
  {
    "{": ""      ""Video ID: Lsu7ziGf5JY""
  },
  {
    "{": ""      ""Video ID: NCbsHPjevEU""
  },
  {
    "{": ""      ""Video ID: nxtseSG3vqo""
  },
  {
    "{": ""      ""Video ID: 3raQGf3ilEA""
  },
  {
    "{": ""      ""Video ID: srHT9H7cb0I""
  },
  {
    "{": ""      ""Video ID: KGpY2hw7ao8""
  },
  {
    "{": ""      ""Video ID: Lbi-I-BbBTw""
  },
  {
    "{": ""      ""Video ID: rHFmE3WbVCc""
  },
  {
    "{": ""      ""Video ID: gWp2Oj3Oiek""
  },
  {
    "{": ""      ""Video ID: D-VNVqtcywU""
  },
  {
    "{": ""      ""Video ID: 4mc07JtpzS4""
  },
  {
    "{": ""      ""Video ID: voGD_rriZPA""
  },
  {
    "{": ""      ""Video ID: ji_G0MqAqq8""
  },
  {
    "{": ""      ""Video ID: EYAVd9mvQM0""
  },
  {
    "{": ""      ""Video ID: VzZuKrS0hO8""
  },
  {
    "{": ""      ""Video ID: uqmO5CDMcN0""
  },
  {
    "{": ""      ""Video ID: zsHil7IAMWc""
  },
  {
    "{": ""      ""Video ID: QBE2RO5vj2Y""
  },
  {
    "{": ""      ""Video ID: -JREuvxyviQ""
  },
  {
    "{": ""      ""Video ID: xmJoRnBE1OM""
  },
  {
    "{": ""      ""Video ID: WzJS-2QZVzU""
  },
  {
    "{": ""      ""Video ID: e6KyyNKwHdA""
  },
  {
    "{": ""      ""Video ID: XHCQYUvWgTw""
  },
  {
    "{": ""      ""Video ID: yCkYsC20rys""
  },
  {
    "{": ""      ""Video ID: CyoGq79AYRA""
  },
  {
    "{": ""      ""Video ID: IuyVxVWLhgk""
  },
  {
    "{": ""      ""Video ID: 8WFqg4ULAks""
  },
  {
    "{": ""      ""Video ID: evc3AVDFjno""
  },
  {
    "{": ""      ""Video ID: m8RQN7mBQh8""
  },
  {
    "{": ""      ""Video ID: 8o72MzrgFiU""
  },
  {
    "{": ""      ""Video ID: 4RSnOiMVfHk""
  },
  {
    "{": ""      ""Video ID: c6xjsaCmmd0""
  },
  {
    "{": ""      ""Video ID: TA9BSkQgrGs""
  },
  {
    "{": ""      ""Video ID: STrX0yRl9Is""
  },
  {
    "{": ""      ""Video ID: MKovL4iKiAY""
  },
  {
    "{": ""      ""Video ID: nUDksaQp3IA""
  },
  {
    "{": ""      ""Video ID: 08hU_p48YBI""
  },
  {
    "{": ""      ""Video ID: NojLmuup_eM""
  },
  {
    "{": ""      ""Video ID: 3KCgCfy6xBk""
  },
  {
    "{": ""      ""Video ID: gE7Bm1KNpcg""
  },
  {
    "{": ""      ""Video ID: 1J4PKztKHCY""
  },
  {
    "{": ""      ""Video ID: fbnJ4KnFaCw""
  },
  {
    "{": ""      ""Video ID: C4Df-WD0dkU""
  },
  {
    "{": ""      ""Video ID: Ejb8QOyjz-E""
  },
  {
    "{": ""      ""Video ID: 4xL7yveZA_o""
  },
  {
    "{": ""      ""Video ID: JR43BD6K7jg""
  },
  {
    "{": ""      ""Video ID: TL6r9TTR7CY""
  },
  {
    "{": ""      ""Video ID: t-7HJye6EMo""
  },
  {
    "{": ""      ""Video ID: jzdPydR3goE""
  },
  {
    "{": ""      ""Video ID: KkzZya36g3Y""
  },
  {
    "{": ""      ""Video ID: bVR288WbDXc""
  },
  {
    "{": ""      ""Video ID: 0V0DgKArOqI""
  },
  {
    "{": ""      ""Video ID: q1O4bZi705U""
  },
  {
    "{": ""      ""Video ID: mRf48RkyXoY""
  },
  {
    "{": ""      ""Video ID: xrUchGucJvU""
  },
  {
    "{": ""      ""Video ID: IvzQ92HXohU""
  },
  {
    "{": ""      ""Video ID: Few1w-KogfI""
  },
  {
    "{": ""      ""Video ID: QqzEmQcVGFQ""
  },
  {
    "{": ""      ""Video ID: Z1WxUC5oxSA""
  },
  {
    "{": ""      ""Video ID: 9v02quhKY2s""
  },
  {
    "{": ""      ""Video ID: RZQJyBJKr6U""
  },
  {
    "{": ""      ""Video ID: p6h-Li0pJBI""
  },
  {
    "{": ""      ""Video ID: Mo8dVabH1Qs""
  },
  {
    "{": ""      ""Video ID: APzV_YjJBcQ""
  },
  {
    "{": ""      ""Video ID: zOEBWQg2wGM""
  },
  {
    "{": ""      ""Video ID: Xkhr8v2FBoE""
  },
  {
    "{": ""      ""Video ID: xueEtKYnvb8""
  },
  {
    "{": ""      ""Video ID: ZTtCdrn1uw0""
  },
  {
    "{": ""      ""Video ID: uRBTqoohv8k""
  },
  {
    "{": ""      ""Video ID: p4Aei7nV5xg""
  },
  {
    "{": ""      ""Video ID: PvvZ0Es-IEo""
  },
  {
    "{": ""      ""Video ID: Kz1PgbI8TrM""
  },
  {
    "{": ""      ""Video ID: E40Ni6oGpsE""
  },
  {
    "{": ""      ""Video ID: nRLDwc5w3o4""
  },
  {
    "{": ""      ""Video ID: kq57yClwJeA""
  },
  {
    "{": ""      ""Video ID: 9n_k4GKCUdU""
  },
  {
    "{": ""      ""Video ID: pljZszV4XU4""
  },
  {
    "{": ""      ""Video ID: wvUfMcZ_e-I""
  },
  {
    "{": ""      ""Video ID: c-a-uK82RWM""
  },
  {
    "{": ""      ""Video ID: avxMS18WsGg""
  },
  {
    "{": ""      ""Video ID: ALCH1l2_n1c""
  },
  {
    "{": ""      ""Video ID: kvf7XRM5kkI""
  },
  {
    "{": ""      ""Video ID: 6Vaa6Iuvs5g""
  },
  {
    "{": ""      ""Video ID: jCahODOQ16A""
  },
  {
    "{": ""      ""Video ID: SbZ4SFXkKRM""
  },
  {
    "{": ""      ""Video ID: n4GpwCrFWYM""
  },
  {
    "{": ""      ""Video ID: RN-CQVhgRDc""
  },
  {
    "{": ""      ""Video ID: 32LRkwbO7nE""
  },
  {
    "{": ""      ""Video ID: dXIr646yKqs""
  },
  {
    "{": ""      ""Video ID: 7QSv3sKwGNk""
  },
  {
    "{": ""      ""Video ID: oNyk5Yynwbg""
  },
  {
    "{": ""      ""Video ID: 6l6c66PjDuQ""
  },
  {
    "{": ""      ""Video ID: EFfEMYRDPwo""
  },
  {
    "{": ""      ""Video ID: thm-Kusrmcw""
  },
  {
    "{": ""      ""Video ID: Yx2iza6EfZo""
  },
  {
    "{": ""      ""Video ID: dDpmCRjx_k8""
  },
  {
    "{": ""      ""Video ID: MdTW4uU1uWk""
  },
  {
    "{": ""      ""Video ID: BqUG4DcqYFc""
  },
  {
    "{": ""      ""Video ID: m2eMFdKlihM""
  },
  {
    "{": ""      ""Video ID: gWVEGLJBjbU""
  },
  {
    "{": ""      ""Video ID: bm54Y3CR5KM""
  },
  {
    "{": ""      ""Video ID: Wm_gQVAJLjQ""
  },
  {
    "{": ""      ""Video ID: RUxY0-NthTI""
  },
  {
    "{": ""      ""Video ID: uuH0YvZfObQ""
  },
  {
    "{": ""      ""Video ID: tOUSGaUrHxc""
  },
  {
    "{": ""      ""Video ID: UZBEnCN4TdQ""
  },
  {
    "{": ""      ""Video ID: vB3VkKfilQI""
  },
  {
    "{": ""      ""Video ID: xZVdm-CnqW4""
  },
  {
    "{": ""      ""Video ID: mXbC14UnL7w""
  },
  {
    "{": ""      ""Video ID: nwODzscXKt8""
  },
  {
    "{": ""      ""Video ID: KTAq370HrXM""
  },
  {
    "{": ""      ""Video ID: hbttGbTMKK0""
  },
  {
    "{": ""      ""Video ID: nWr6ec2zEyE""
  },
  {
    "{": ""      ""Video ID: ENr9CCc3qiU""
  },
  {
    "{": ""      ""Video ID: kaPK5xoLZb4""
  },
  {
    "{": ""      ""Video ID: NZs5OmG17_8""
  },
  {
    "{": ""      ""Video ID: kU8kCA1CILQ""
  },
  {
    "{": ""      ""Video ID: XoLU6u6IJ9E""
  },
  {
    "{": ""      ""Video ID: DjSO5nAK6wE""
  },
  {
    "{": ""      ""Video ID: qosypvvEBrE""
  },
  {
    "{": ""      ""Video ID: F76JasttBOs""
  },
  {
    "{": ""      ""Video ID: ubBmyWR1Nwc""
  },
  {
    "{": ""      ""Video ID: xLzLwRmgIC4""
  },
  {
    "{": ""      ""Video ID: Gzj723LkRJY""
  },
  {
    "{": ""      ""Video ID: Bu3DSxqyZA8""
  },
  {
    "{": ""      ""Video ID: -FDJ8x3ZKQE""
  },
  {
    "{": ""      ""Video ID: PeM_5DSItGU""
  },
  {
    "{": ""      ""Video ID: qL8T2IQHy8M""
  },
  {
    "{": ""      ""Video ID: 9E85xwVDrc8""
  },
  {
    "{": ""      ""Video ID: yZaWojSz9es""
  },
  {
    "{": ""      ""Video ID: cWXBe3MrqJA""
  },
  {
    "{": ""      ""Video ID: cvd-OyHm9lE""
  },
  {
    "{": ""      ""Video ID: _Wb_EYe41I8""
  },
  {
    "{": ""      ""Video ID: HgGEwMX_npw""
  },
  {
    "{": ""      ""Video ID: 1suivhh78jE""
  },
  {
    "{": ""      ""Video ID: 6ZkMyOOfOPI""
  },
  {
    "{": ""      ""Video ID: 8BuL8pkFRn8""
  },
  {
    "{": ""      ""Video ID: YY-Plvg0PQA""
  },
  {
    "{": ""      ""Video ID: JzXIAzLGNj4""
  },
  {
    "{": ""      ""Video ID: H5kUjIIgNgc""
  },
  {
    "{": ""      ""Video ID: 7GZC_qeC400""
  },
  {
    "{": ""      ""Video ID: XyssPBoU9Bs""
  },
  {
    "{": ""      ""Video ID: w8QzcS7g52g""
  },
  {
    "{": ""      ""Video ID: I_pkKIdJWCU""
  },
  {
    "{": ""      ""Video ID: rx_tnPEv5VU""
  },
  {
    "{": ""      ""Video ID: KD2Ymtu_maY""
  },
  {
    "{": ""      ""Video ID: vYBbXJCOgOs""
  },
  {
    "{": ""      ""Video ID: MCky91H2VQI""
  },
  {
    "{": ""      ""Video ID: rn0oQIArLOY""
  },
  {
    "{": ""      ""Video ID: GKicLv8tfwE""
  },
  {
    "{": ""      ""Video ID: Zzz4qdWc8_A""
  },
  {
    "{": ""      ""Video ID: sicRqLkjN28""
  },
  {
    "{": ""      ""Video ID: mIWNN2bnYto""
  },
  {
    "{": ""      ""Video ID: tpp3PP3m8Bk""
  },
  {
    "{": ""      ""Video ID: mFXlnEYyym0""
  },
  {
    "{": ""      ""Video ID: S0Dleg40d0g""
  },
  {
    "{": ""      ""Video ID: QdzN9Ncdo78""
  },
  {
    "{": ""      ""Video ID: wDKaX0xkUmE""
  },
  {
    "{": ""      ""Video ID: 48Qe37cImnw""
  },
  {
    "{": ""      ""Video ID: Gx4LenxHGEg""
  },
  {
    "{": ""      ""Video ID: 9Teedv9zMzY""
  },
  {
    "{": ""      ""Video ID: TJLq2WZiBBs""
  },
  {
    "{": ""      ""Video ID: k_7LAqDjhq8""
  },
  {
    "{": ""      ""Video ID: igY8jzcEO0A""
  },
  {
    "{": ""      ""Video ID: BSbvedMd6FA""
  },
  {
    "{": ""      ""Video ID: FIPiVGEUTRA""
  },
  {
    "{": ""      ""Video ID: QDkPdRtr310""
  },
  {
    "{": ""      ""Video ID: lKhekAtQmX0""
  },
  {
    "{": ""      ""Video ID: Kj7LkIXS4dw""
  },
  {
    "{": ""      ""Video ID: cz2UM7uL_1c""
  },
  {
    "{": ""      ""Video ID: CYUc4H6_L5k""
  },
  {
    "{": ""      ""Video ID: vdM2Ti2YYXQ""
  },
  {
    "{": ""      ""Video ID: h34UUJnjj4I""
  },
  {
    "{": ""      ""Video ID: rG-5n7iSMPM""
  },
  {
    "{": ""      ""Video ID: wEQ54SUxtiI""
  },
  {
    "{": ""      ""Video ID: BRx0s0uHeNk""
  },
  {
    "{": ""      ""Video ID: eN6JCfKtLDk""
  },
  {
    "{": ""      ""Video ID: uZTCPTpWZUY""
  },
  {
    "{": ""      ""Video ID: asl6zQexKFI""
  },
  {
    "{": ""      ""Video ID: fLzC02FaQ0g""
  },
  {
    "{": ""      ""Video ID: xqv2U_dpdf0""
  },
  {
    "{": ""      ""Video ID: Ob3AzZhmIeU""
  },
  {
    "{": ""      ""Video ID: Bvuj6AX-Dok""
  },
  {
    "{": ""      ""Video ID: QXi02GoU6mo""
  },
  {
    "{": ""      ""Video ID: d2vFJsJsmJQ""
  },
  {
    "{": ""      ""Video ID: G4YUCUmmXms""
  },
  {
    "{": ""      ""Video ID: Upjmsu_Q97c""
  },
  {
    "{": ""      ""Video ID: hXc-0Wi2J4U""
  },
  {
    "{": ""      ""Video ID: ppFq7HCZw3o""
  },
  {
    "{": ""      ""Video ID: K0mdqYq0GQM""
  },
  {
    "{": ""      ""Video ID: _KVr7VOTwTQ""
  },
  {
    "{": ""      ""Video ID: qBeWdYmratU""
  },
  {
    "{": ""      ""Video ID: H3qvKE52J6I""
  },
  {
    "{": ""      ""Video ID: -JFusrlsKAs""
  },
  {
    "{": ""      ""Video ID: k0fiwlPOZTA""
  },
  {
    "{": ""      ""Video ID: XGSg5s41uiM""
  },
  {
    "{": ""      ""Video ID: Bcp_dPVfxVY""
  },
  {
    "{": ""      ""Video ID: 3M3JntKL4ag""
  },
  {
    "{": ""      ""Video ID: qOeto6Cy3ws""
  },
  {
    "{": ""      ""Video ID: Dz2fUGxH_vI""
  },
  {
    "{": ""      ""Video ID: eLzpEsF88Qo""
  },
  {
    "{": ""      ""Video ID: WNg1BX_QooY""
  },
  {
    "{": ""      ""Video ID: YImiFk3dd98""
  },
  {
    "{": ""      ""Video ID: Rf5z2UBH4Qk""
  },
  {
    "{": ""      ""Video ID: RSFeaU17Q8Y""
  },
  {
    "{": ""      ""Video ID: 8d5N2eRa1ZE""
  },
  {
    "{": ""      ""Video ID: AajECl0D4uk""
  },
  {
    "{": ""      ""Video ID: ly78vqKqioo""
  },
  {
    "{": ""      ""Video ID: 2UIvuyy7czk""
  },
  {
    "{": ""      ""Video ID: fw6cTt0ptjs""
  },
  {
    "{": ""      ""Video ID: kco_5DT7ppA""
  },
  {
    "{": ""      ""Video ID: dyfDISCKC5M""
  },
  {
    "{": ""      ""Video ID: sNSxUqe91tA""
  },
  {
    "{": ""      ""Video ID: kZ79IUl1I4E""
  },
  {
    "{": ""      ""Video ID: dLxWIlxDiRY""
  },
  {
    "{": ""      ""Video ID: ZPyq_6c5tZc""
  },
  {
    "{": ""      ""Video ID: dXHNK6vA8Ck""
  },
  {
    "{": ""      ""Video ID: adwXTA5weFs""
  },
  {
    "{": ""      ""Video ID: BWb5AP8YCBk""
  },
  {
    "{": ""      ""Video ID: cW4Ey9vTllY""
  },
  {
    "{": ""      ""Video ID: RB9zuq2jJ9A""
  },
  {
    "{": ""      ""Video ID: dgHCFoCOYxA""
  },
  {
    "{": ""      ""Video ID: 1-OKwxH9H2k""
  },
  {
    "{": ""      ""Video ID: X8LMuZUEzIs""
  },
  {
    "{": ""      ""Video ID: 0kcXttxWyi8""
  },
  {
    "{": ""      ""Video ID: S2gYL4gbGCs""
  },
  {
    "{": ""      ""Video ID: gVvQfu_uC4c""
  },
  {
    "{": ""      ""Video ID: EaAISRSFk3s""
  },
  {
    "{": ""      ""Video ID: x-BpOl5ps0I""
  },
  {
    "{": ""      ""Video ID: LU8DDYz68kM""
  },
  {
    "{": ""      ""Video ID: 9TLsV4dz_pk""
  },
  {
    "{": ""      ""Video ID: cnwEglBufdE""
  },
  {
    "{": ""      ""Video ID: iQfKPbfdp5s""
  },
  {
    "{": ""      ""Video ID: mtC5AAGB1y0""
  },
  {
    "{": ""      ""Video ID: 7t3TK_qLgUI""
  },
  {
    "{": ""      ""Video ID: z-g1ScRlQdM""
  },
  {
    "{": ""      ""Video ID: hFSUfKIA--U""
  },
  {
    "{": ""      ""Video ID: iorDbX0ar5g""
  },
  {
    "{": ""      ""Video ID: rvS-hZNRRuY""
  },
  {
    "{": ""      ""Video ID: h-t_qOr8ofI""
  },
  {
    "{": ""      ""Video ID: Ei3ZJJ9zqOY""
  },
  {
    "{": ""      ""Video ID: kj45UQiNKMw""
  },
  {
    "{": ""      ""Video ID: mHCxioPKIXY""
  },
  {
    "{": ""      ""Video ID: G_M1U8HibqI""
  },
  {
    "{": ""      ""Video ID: UnoHk7sOnMw""
  },
  {
    "{": ""      ""Video ID: S-SstLK7lh4""
  },
  {
    "{": ""      ""Video ID: Pq9wAvicuuM""
  },
  {
    "{": ""      ""Video ID: Or-PajUn1c4""
  },
  {
    "{": ""      ""Video ID: EcpYQDTmZis""
  },
  {
    "{": ""      ""Video ID: JHItJsz2k78""
  },
  {
    "{": ""      ""Video ID: HjgeoVTYUr0""
  },
  {
    "{": ""      ""Video ID: p1W75X2G5jQ""
  },
  {
    "{": ""      ""Video ID: otK5ODcSu4o""
  },
  {
    "{": ""      ""Video ID: -Vsg_qoig7s""
  },
  {
    "{": ""      ""Video ID: iJrfR4sGtAU""
  },
  {
    "{": ""      ""Video ID: 42g44MeIRfw""
  },
  {
    "{": ""      ""Video ID: 1H9drPDG68k""
  },
  {
    "{": ""      ""Video ID: C8KMnVcsXHc""
  },
  {
    "{": ""      ""Video ID: ca9-j0SPa0M""
  },
  {
    "{": ""      ""Video ID: ZVY5j_v_K64""
  },
  {
    "{": ""      ""Video ID: vqiiwjGjAfg""
  },
  {
    "{": ""      ""Video ID: gZuMHrjrd1U""
  },
  {
    "{": ""      ""Video ID: Hg47-CwiP-I""
  },
  {
    "{": ""      ""Video ID: mGE6diUx2IE""
  },
  {
    "{": ""      ""Video ID: dDJaP5QyvSA""
  },
  {
    "{": ""      ""Video ID: MAsqrigKYK0""
  },
  {
    "{": ""      ""Video ID: 8IlzSWMMKAk""
  },
  {
    "{": ""      ""Video ID: EWLy53jXPCI""
  },
  {
    "{": ""      ""Video ID: LrUde8vjYyw""
  },
  {
    "{": ""      ""Video ID: 6KPmW3yt1aI""
  },
  {
    "{": ""      ""Video ID: Efu1jp7fIoo""
  },
  {
    "{": ""      ""Video ID: BDJ-qAQ4t1o""
  },
  {
    "{": ""      ""Video ID: wWW8R58R8qs""
  },
  {
    "{": ""      ""Video ID: i0LDaOFPoYU""
  },
  {
    "{": ""      ""Video ID: u0Qq88DIFHc""
  },
  {
    "{": ""      ""Video ID: mE9dlVrkSFE""
  },
  {
    "{": ""      ""Video ID: bNEdkACBNR8""
  },
  {
    "{": ""      ""Video ID: DGQVX8iGbgk""
  },
  {
    "{": ""      ""Video ID: E4VMntSUskg""
  },
  {
    "{": ""      ""Video ID: 5-reBn0gUkg""
  },
  {
    "{": ""      ""Video ID: THM3FYUNyr8""
  },
  {
    "{": ""      ""Video ID: Ydnc_c4Afj0""
  },
  {
    "{": ""      ""Video ID: HFaCubSrqdQ""
  },
  {
    "{": ""      ""Video ID: -mQH9DloKD8""
  },
  {
    "{": ""      ""Video ID: vDuIB8Gv9GQ""
  },
  {
    "{": ""      ""Video ID: 3kITDVTeo-c""
  },
  {
    "{": ""      ""Video ID: vOAYUoiPkzA""
  },
  {
    "{": ""      ""Video ID: 8n-nT-luFIw""
  },
  {
    "{": ""      ""Video ID: q8XToX7aSdg""
  },
  {
    "{": ""      ""Video ID: dzUNvEfYDEQ""
  },
  {
    "{": ""      ""Video ID: LNsSn6D3CP4""
  },
  {
    "{": ""      ""Video ID: qJXYN3wFhgo""
  },
  {
    "{": ""      ""Video ID: xq8aopATYyw""
  },
  {
    "{": ""      ""Video ID: AK9_-sLF5M0""
  },
  {
    "{": ""      ""Video ID: ED6YaRl93CE""
  },
  {
    "{": ""      ""Video ID: 2iPKsuQ3RIM""
  },
  {
    "{": ""      ""Video ID: 6W5x8kuHvHk""
  },
  {
    "{": ""      ""Video ID: FmBFO25f2X4""
  },
  {
    "{": ""      ""Video ID: g9VETho5KzU""
  },
  {
    "{": ""      ""Video ID: kzy3G8uGnqo""
  },
  {
    "{": ""      ""Video ID: iL_K5BhPs1c""
  },
  {
    "{": ""      ""Video ID: 0oLMy5wWn30""
  },
  {
    "{": ""      ""Video ID: XBDOGE1sWuk""
  },
  {
    "{": ""      ""Video ID: gYt2kNJZCN8""
  },
  {
    "{": ""      ""Video ID: MM7_l-MEqmw""
  },
  {
    "{": ""      ""Video ID: n_vKNvy2ngs""
  },
  {
    "{": ""      ""Video ID: cF2vaT49Nh4""
  },
  {
    "{": ""      ""Video ID: bPuIj0Pc0IQ""
  },
  {
    "{": ""      ""Video ID: 1X9KIK1GOic""
  },
  {
    "{": ""      ""Video ID: hQTNBWIdLeI""
  },
  {
    "{": ""      ""Video ID: ZmCsoZJTl1A""
  },
  {
    "{": ""      ""Video ID: NOHAPxldtI4""
  },
  {
    "{": ""      ""Video ID: Bgzgj25CmKg""
  },
  {
    "{": ""      ""Video ID: 0hsONibA28I""
  },
  {
    "{": ""      ""Video ID: 00mxUwvzkfg""
  },
  {
    "{": ""      ""Video ID: 9VGYYRLbFSk""
  },
  {
    "{": ""      ""Video ID: tStMvo0ZI7M""
  },
  {
    "{": ""      ""Video ID: bsYB701ukq4""
  },
  {
    "{": ""      ""Video ID: SmLh8WGDbRE""
  },
  {
    "{": ""      ""Video ID: H4COk8BNCDI""
  },
  {
    "{": ""      ""Video ID: TILOpb1CcUw""
  },
  {
    "{": ""      ""Video ID: Vh3BgMbqdDM""
  },
  {
    "{": ""      ""Video ID: D01Wa2PLquU""
  },
  {
    "{": ""      ""Video ID: 3bayIXAaPm0""
  },
  {
    "{": ""      ""Video ID: 9fKr2qAg72E""
  },
  {
    "{": ""      ""Video ID: Fv7UVCPt6mQ""
  },
  {
    "{": ""      ""Video ID: L2P0sGcy1LE""
  },
  {
    "{": ""      ""Video ID: WAChj379yS8""
  },
  {
    "{": ""      ""Video ID: aKmNmrDsJHY""
  },
  {
    "{": ""      ""Video ID: 7h8abJUidwA""
  },
  {
    "{": ""      ""Video ID: sJ35xy2wM1o""
  },
  {
    "{": ""      ""Video ID: dbg5egUrc8M""
  },
  {
    "{": ""      ""Video ID: 4ZXEsu2XbKw""
  },
  {
    "{": ""      ""Video ID: KMO8v6c1VNw""
  },
  {
    "{": ""      ""Video ID: MHTim22_e04""
  },
  {
    "{": ""      ""Video ID: 5d0vzbL7J44""
  },
  {
    "{": ""      ""Video ID: UQaEBDA-Y_M""
  },
  {
    "{": ""      ""Video ID: NF0S_N-F-cQ""
  },
  {
    "{": ""      ""Video ID: zU2ZPRn9ENo""
  },
  {
    "{": ""      ""Video ID: o-srOj1KIkg""
  },
  {
    "{": ""      ""Video ID: 4S6F26Mfv8I""
  },
  {
    "{": ""      ""Video ID: vUiLjtPtcmQ""
  },
  {
    "{": ""      ""Video ID: 76bQDCwJ318""
  },
  {
    "{": ""      ""Video ID: EM7sMHXQM08""
  },
  {
    "{": ""      ""Video ID: wqEvEr8xahg""
  },
  {
    "{": ""      ""Video ID: 9js0dD8Kbrw""
  },
  {
    "{": ""      ""Video ID: 1c98iG1dJB4""
  },
  {
    "{": ""      ""Video ID: fuElHB54o2U""
  },
  {
    "{": ""      ""Video ID: x5KQaO_actQ""
  },
  {
    "{": ""      ""Video ID: aDDP__JDWPA""
  },
  {
    "{": ""      ""Video ID: 3lB8V_CyOiA""
  },
  {
    "{": ""      ""Video ID: jwpO-nnFY9g""
  },
  {
    "{": ""      ""Video ID: _vzGovUij2k""
  },
  {
    "{": ""      ""Video ID: k1h6yie7uGs""
  },
  {
    "{": ""      ""Video ID: MYDuy7wM8Gk""
  },
  {
    "{": ""      ""Video ID: LzLdPYu3RLQ""
  },
  {
    "{": ""      ""Video ID: 6V-_kUYgtpc""
  },
  {
    "{": ""      ""Video ID: 44LOjtXzxyE""
  },
  {
    "{": ""      ""Video ID: HqKjEROuYSw""
  },
  {
    "{": ""      ""Video ID: IPUmAd50o5k""
  },
  {
    "{": ""      ""Video ID: 5JjoIGw-Pv0""
  },
  {
    "{": ""      ""Video ID: 0z4bEYbbEJ4""
  },
  {
    "{": ""      ""Video ID: szEEY3iLyUs""
  },
  {
    "{": ""      ""Video ID: YSJWn2RfJiU""
  },
  {
    "{": ""      ""Video ID: u0Fz7R0SE-Q""
  },
  {
    "{": ""      ""Video ID: 85GYp1FaXjM""
  },
  {
    "{": ""      ""Video ID: L69ilPRM7Xo""
  },
  {
    "{": ""      ""Video ID: HIH2PdDMrXg""
  },
  {
    "{": ""      ""Video ID: E532ORgkTZM""
  },
  {
    "{": ""      ""Video ID: dFwS6n9wCYY""
  },
  {
    "{": ""      ""Video ID: 2YLoftFufzM""
  },
  {
    "{": ""      ""Video ID: 0ZNB_fktW4k""
  },
  {
    "{": ""      ""Video ID: CjAsFkLInwY""
  },
  {
    "{": ""      ""Video ID: eQ6csbN16PQ""
  },
  {
    "{": ""      ""Video ID: Z7Bzn8FZWBc""
  },
  {
    "{": ""      ""Video ID: hjE8TlIu9fQ""
  },
  {
    "{": ""      ""Video ID: neAkmTSm8qo""
  },
  {
    "{": ""      ""Video ID: f6ZXH17ac8c""
  },
  {
    "{": ""      ""Video ID: 3p713bNaO4A""
  },
  {
    "{": ""      ""Video ID: sDymphHPJo0""
  },
  {
    "{": ""      ""Video ID: 5sy9vhtsXXM""
  },
  {
    "{": ""      ""Video ID: 8FTuI7N8TIU""
  },
  {
    "{": ""      ""Video ID: 1raUvGNbZFg""
  },
  {
    "{": ""      ""Video ID: V4we8iFk-fY""
  },
  {
    "{": ""      ""Video ID: lNYpu6Hmvbk""
  },
  {
    "{": ""      ""Video ID: FvWuy7p5mZE""
  },
  {
    "{": ""      ""Video ID: nLvdTL3kdtY""
  },
  {
    "{": ""      ""Video ID: EC6j6KiO8Ic""
  },
  {
    "{": ""      ""Video ID: FewCv5gHNDw""
  },
  {
    "{": ""      ""Video ID: QPlmKVScVGo""
  },
  {
    "{": ""      ""Video ID: V1_KuZVrXGc""
  },
  {
    "{": ""      ""Video ID: 2lf7RnsOiyw""
  },
  {
    "{": ""      ""Video ID: bjTH3Eaqrr0""
  },
  {
    "{": ""      ""Video ID: iiTTxaU3oAY""
  },
  {
    "{": ""      ""Video ID: FKi4MmGnWcY""
  },
  {
    "{": ""      ""Video ID: McWSJ0elzN8""
  },
  {
    "{": ""      ""Video ID: pJAx9CzIEac""
  },
  {
    "{": ""      ""Video ID: mmPFa0MART0""
  },
  {
    "{": ""      ""Video ID: TznqWdFUwS4""
  },
  {
    "{": ""      ""Video ID: sKmO55JGL78""
  },
  {
    "{": ""      ""Video ID: KTYwVy1fpHE""
  },
  {
    "{": ""      ""Video ID: m3LF-lyQ2OA""
  },
  {
    "{": ""      ""Video ID: vysHGJTU1fo""
  },
  {
    "{": ""      ""Video ID: ABMwT2b3jG0""
  },
  {
    "{": ""      ""Video ID: Y21z8OAY7Pg""
  },
  {
    "{": ""      ""Video ID: 5QTx8454zQw""
  },
  {
    "{": ""      ""Video ID: Yo0bbJs33ng""
  },
  {
    "{": ""      ""Video ID: tNSKB66ywkg""
  },
  {
    "{": ""      ""Video ID: 1_8MCiP21w4""
  },
  {
    "{": ""      ""Video ID: s6V9niJlWw0""
  },
  {
    "{": ""      ""Video ID: MzI5msTuqX0""
  },
  {
    "{": ""      ""Video ID: u3cgRDUmoyY""
  },
  {
    "{": ""      ""Video ID: fqEslRajbP4""
  },
  {
    "{": ""      ""Video ID: Ho83lT3hvKQ""
  },
  {
    "{": ""      ""Video ID: 7XvYWdRun6Y""
  },
  {
    "{": ""      ""Video ID: aoJiZOxuTfA""
  },
  {
    "{": ""      ""Video ID: sgo6XMLbq2k""
  },
  {
    "{": ""      ""Video ID: 97nQ3v8L1Gw""
  },
  {
    "{": ""      ""Video ID: 4jPAlsXt1I0""
  },
  {
    "{": ""      ""Video ID: FnaNd-8qASo""
  },
  {
    "{": ""      ""Video ID: zt1TrxPAPak""
  },
  {
    "{": ""      ""Video ID: 1mluYaMeMy4""
  },
  {
    "{": ""      ""Video ID: mIaFZ8yR66o""
  },
  {
    "{": ""      ""Video ID: _eSf1KunK8k""
  },
  {
    "{": ""      ""Video ID: joq2g-uNvhA""
  },
  {
    "{": ""      ""Video ID: R8xbMjIX25Y""
  },
  {
    "{": ""      ""Video ID: DMF_24cQqT0""
  },
  {
    "{": ""      ""Video ID: arfrDgt7Nis""
  },
  {
    "{": ""      ""Video ID: IzO1mCAVyMw""
  },
  {
    "{": ""      ""Video ID: r0eAn6tnqpg""
  },
  {
    "{": ""      ""Video ID: 0c10TGi3kC0""
  },
  {
    "{": ""      ""Video ID: DXLBhN5JCho""
  },
  {
    "{": ""      ""Video ID: iZqGULdkEvs""
  },
  {
    "{": ""      ""Video ID: 8VHLoO1k3qE""
  },
  {
    "{": ""      ""Video ID: atLn23xA7RM""
  },
  {
    "{": ""      ""Video ID: g0XzT_NPvfE""
  },
  {
    "{": ""      ""Video ID: moHVn0F57Cs""
  },
  {
    "{": ""      ""Video ID: YJkBF78vM5M""
  },
  {
    "{": ""      ""Video ID: He9TIK62bBY""
  },
  {
    "{": ""      ""Video ID: VdjYYFOGE3k""
  },
  {
    "{": ""      ""Video ID: TiKnLXvsGxM""
  },
  {
    "{": ""      ""Video ID: yzLnqxH3tBw""
  },
  {
    "{": ""      ""Video ID: itdjlfyFh9A""
  },
  {
    "{": ""      ""Video ID: k03vIjhTc-k""
  },
  {
    "{": ""      ""Video ID: 0rai0CF43Wk""
  },
  {
    "{": ""      ""Video ID: UpAfs3Im_jk""
  },
  {
    "{": ""      ""Video ID: G7jjHLu3RTI""
  },
  {
    "{": ""      ""Video ID: qdcI9mIjR9k""
  },
  {
    "{": ""      ""Video ID: Tb-EvS_RvLw""
  },
  {
    "{": ""      ""Video ID: 7MEVBMY_dlA""
  },
  {
    "{": ""      ""Video ID: zL3Q5XmQabo""
  },
  {
    "{": ""      ""Video ID: SHORd3UUt00""
  },
  {
    "{": ""      ""Video ID: G3juzO2tQ7U""
  },
  {
    "{": ""      ""Video ID: h4nJvXWGF5Y""
  },
  {
    "{": ""      ""Video ID: PnAYRqahpq4""
  },
  {
    "{": ""      ""Video ID: GRD6TxNLsds""
  },
  {
    "{": ""      ""Video ID: b131iN3hOyk""
  },
  {
    "{": ""      ""Video ID: n_8x1eUpTmo""
  },
  {
    "{": ""      ""Video ID: -EuDYGnWMiQ""
  },
  {
    "{": ""      ""Video ID: EH5U-BPJor4""
  },
  {
    "{": ""      ""Video ID: A6Ejuf1QeNg""
  },
  {
    "{": ""      ""Video ID: BkPevfpWDso""
  },
  {
    "{": ""      ""Video ID: eDFIeM-FRaw""
  },
  {
    "{": ""      ""Video ID: bAUJ_JP9hF8""
  },
  {
    "{": ""      ""Video ID: LCuiPm1gFSo""
  },
  {
    "{": ""      ""Video ID: 0A87kp_5SXw""
  },
  {
    "{": ""      ""Video ID: GNe02-G2GsQ""
  },
  {
    "{": ""      ""Video ID: n3bgS3I9o0Q""
  },
  {
    "{": ""      ""Video ID: T3yUNtQRaDE""
  },
  {
    "{": ""      ""Video ID: ZnyMFw4ep8M""
  },
  {
    "{": ""      ""Video ID: lFBVsrxbRFc""
  },
  {
    "{": ""      ""Video ID: HpnJveMeS80""
  },
  {
    "{": ""      ""Video ID: 1Lll9jrAy5Y""
  },
  {
    "{": ""      ""Video ID: uEY_b81F0Uo""
  },
  {
    "{": ""      ""Video ID: OrQllR5uA9U""
  },
  {
    "{": ""      ""Video ID: XP42AdHxBLc""
  },
  {
    "{": ""      ""Video ID: rh-8fq0EUc4""
  },
  {
    "{": ""      ""Video ID: JbK7PaQpLL4""
  },
  {
    "{": ""      ""Video ID: CFp-iPSPplE""
  },
  {
    "{": ""      ""Video ID: MulLAfffQoQ""
  },
  {
    "{": ""      ""Video ID: ietPjluX1xU""
  },
  {
    "{": ""      ""Video ID: iPgzqKm4tFE""
  },
  {
    "{": ""      ""Video ID: 1FZhO4G5hIo""
  },
  {
    "{": ""      ""Video ID: id-hFzMDkOM""
  },
  {
    "{": ""      ""Video ID: UA0gr8705kk""
  },
  {
    "{": ""      ""Video ID: G4S2v6rHn9M""
  },
  {
    "{": ""      ""Video ID: 3KGw5u2bcvw""
  },
  {
    "{": ""      ""Video ID: asB0fV95x2U""
  },
  {
    "{": ""      ""Video ID: jT4AGp3AsRg""
  },
  {
    "{": ""      ""Video ID: O_BcNEsEmKg""
  },
  {
    "{": ""      ""Video ID: 0qQCrKpPWm8""
  },
  {
    "{": ""      ""Video ID: _54sSYFMf88""
  },
  {
    "{": ""      ""Video ID: qYUwWKjtMrI""
  },
  {
    "{": ""      ""Video ID: XhXLgVBzeu4""
  },
  {
    "{": ""      ""Video ID: 7RVix2N2M2s""
  },
  {
    "{": ""      ""Video ID: AyK82eiwNjo""
  },
  {
    "{": ""      ""Video ID: 1WyBzZbNuJI""
  },
  {
    "{": ""      ""Video ID: TOCUezcKcRg""
  },
  {
    "{": ""      ""Video ID: ZQIQZHZWbOU""
  },
  {
    "{": ""      ""Video ID: UBW3Qh0uJb0""
  },
  {
    "{": ""      ""Video ID: BZmE3fUKU5U""
  },
  {
    "{": ""      ""Video ID: TvabW3XEU0w""
  },
  {
    "{": ""      ""Video ID: EkeQ3spX-GA""
  },
  {
    "{": ""      ""Video ID: HiGSupr9W2M""
  },
  {
    "{": ""      ""Video ID: VwDBsm6lURo""
  },
  {
    "{": ""      ""Video ID: VgCrV-6z7dU""
  },
  {
    "{": ""      ""Video ID: wxwyL8NnWDY""
  },
  {
    "{": ""      ""Video ID: W2yt7HO3QqQ""
  },
  {
    "{": ""      ""Video ID: M0i-O510eCc""
  },
  {
    "{": ""      ""Video ID: g71ZgMLRUDs""
  },
  {
    "{": ""      ""Video ID: 23_r3Y-OXok""
  },
  {
    "{": ""      ""Video ID: pjnUha7a4T4""
  },
  {
    "{": ""      ""Video ID: T_F5IqfHD78""
  },
  {
    "{": ""      ""Video ID: P9x-dlz3QkE""
  },
  {
    "{": ""      ""Video ID: RLWKTfqbeS0""
  },
  {
    "{": ""      ""Video ID: UFPXfaIRx7o""
  },
  {
    "{": ""      ""Video ID: 4HTGFKlhJ8g""
  },
  {
    "{": ""      ""Video ID: v_yCuEvqu5Q""
  },
  {
    "{": ""      ""Video ID: F3y09rxE9vQ""
  },
  {
    "{": ""      ""Video ID: Jr_DEgUJU0w""
  },
  {
    "{": ""      ""Video ID: bFiMQav3gVs""
  },
  {
    "{": ""      ""Video ID: QSyMjecmBuk""
  },
  {
    "{": ""      ""Video ID: 9cQbRYRDIWs""
  },
  {
    "{": ""      ""Video ID: 09a685d5izo""
  },
  {
    "{": ""      ""Video ID: -onupWPLeyc""
  },
  {
    "{": ""      ""Video ID: Zg0bJQHqOac""
  },
  {
    "{": ""      ""Video ID: pwGjnghUybg""
  },
  {
    "{": ""      ""Video ID: DpSiMzOoxyY""
  },
  {
    "{": ""      ""Video ID: U_6lhhdeTFE""
  },
  {
    "{": ""      ""Video ID: j4uLorQsSlQ""
  },
  {
    "{": ""      ""Video ID: Hgc4Z97A7oM""
  },
  {
    "{": ""      ""Video ID: kOo_meLVxeA""
  },
  {
    "{": ""      ""Video ID: GW5p5GIcPlg""
  },
  {
    "{": ""      ""Video ID: Q7y_JBwUtIo""
  },
  {
    "{": ""      ""Video ID: X0o-LMxrvI0""
  },
  {
    "{": ""      ""Video ID: oEtps_UIjNE""
  },
  {
    "{": ""      ""Video ID: jSgsSZVIzec""
  },
  {
    "{": ""      ""Video ID: otGQqO2TYMI""
  },
  {
    "{": ""      ""Video ID: 79YydBy6Nl8""
  },
  {
    "{": ""      ""Video ID: Kw7wtARPkRY""
  },
  {
    "{": ""      ""Video ID: xSP-E6ed9vc""
  },
  {
    "{": ""      ""Video ID: xnkT_akurv8""
  },
  {
    "{": ""      ""Video ID: VsA2Ky5qMp8""
  },
  {
    "{": ""      ""Video ID: XO4qvaNRyzo""
  },
  {
    "{": ""      ""Video ID: s1lUOziI2XE""
  },
  {
    "{": ""      ""Video ID: kj0UZjrSVLA""
  },
  {
    "{": ""      ""Video ID: 6OtL7ZaRZsE""
  },
  {
    "{": ""      ""Video ID: Rm7eeZAiSDE""
  },
  {
    "{": ""      ""Video ID: vUA0hUjix_E""
  },
  {
    "{": ""      ""Video ID: sYjJYfl51cg""
  },
  {
    "{": ""      ""Video ID: IGXlcxWjpiM""
  },
  {
    "{": ""      ""Video ID: ZHvHcSE8cr8""
  },
  {
    "{": ""      ""Video ID: FzppiXdG1ic""
  },
  {
    "{": ""      ""Video ID: g_M4fW0FCXY""
  },
  {
    "{": ""      ""Video ID: bonbsx14QCo""
  },
  {
    "{": ""      ""Video ID: trNFNqTx-kw""
  },
  {
    "{": ""      ""Video ID: w2R3Ja_-p1A""
  },
  {
    "{": ""      ""Video ID: WLLUZqGvR90""
  },
  {
    "{": ""      ""Video ID: 7Zh64glQFH0""
  },
  {
    "{": ""      ""Video ID: D8-qzRfuWXE""
  },
  {
    "{": ""      ""Video ID: BHGLsYXn5SQ""
  },
  {
    "{": ""      ""Video ID: dDHW9Q40sjo""
  },
  {
    "{": ""      ""Video ID: PNvEeCcb2pE""
  },
  {
    "{": ""      ""Video ID: a_nyNegymJw""
  },
  {
    "{": ""      ""Video ID: q5C1idUzcQQ""
  },
  {
    "{": ""      ""Video ID: ih--l4-mtNo""
  },
  {
    "{": ""      ""Video ID: iHgECsp0aM4""
  },
  {
    "{": ""      ""Video ID: 6dUsBhQrBbE""
  },
  {
    "{": ""      ""Video ID: X_vLIg7H30k""
  },
  {
    "{": ""      ""Video ID: nUiH6uw7-ZY""
  },
  {
    "{": ""      ""Video ID: CVmUR6zXNbo""
  },
  {
    "{": ""      ""Video ID: VJyoE5urybk""
  },
  {
    "{": ""      ""Video ID: trrJ8exH6OU""
  },
  {
    "{": ""      ""Video ID: u3OgoCuInyc""
  },
  {
    "{": ""      ""Video ID: zzFjdGcQNWk""
  },
  {
    "{": ""      ""Video ID: QvumWbByGxQ""
  },
  {
    "{": ""      ""Video ID: UyY5rkHbi90""
  },
  {
    "{": ""      ""Video ID: 8bMH-FH_X3w""
  },
  {
    "{": ""      ""Video ID: UHdEHsUHSi0""
  },
  {
    "{": ""      ""Video ID: dZoPh2JRoXE""
  },
  {
    "{": ""      ""Video ID: QTFBrjUNZd8""
  },
  {
    "{": ""      ""Video ID: gGbldsHpJcA""
  },
  {
    "{": ""      ""Video ID: Te3e07aT7DA""
  },
  {
    "{": ""      ""Video ID: dPYv2pyRIuA""
  },
  {
    "{": ""      ""Video ID: mcSXuGnopUM""
  },
  {
    "{": ""      ""Video ID: O1wg_aFPEKA""
  },
  {
    "{": ""      ""Video ID: I9BbwIPp0g0""
  },
  {
    "{": ""      ""Video ID: 0jLiqfolgyk""
  },
  {
    "{": ""      ""Video ID: bGx9IN1aW8g""
  },
  {
    "{": ""      ""Video ID: PHwoSMlf09M""
  },
  {
    "{": ""      ""Video ID: 1h6QJkNhuOI""
  },
  {
    "{": ""      ""Video ID: jsO1fJSH2gM""
  },
  {
    "{": ""      ""Video ID: D6tCvxrRwG8""
  },
  {
    "{": ""      ""Video ID: vWRGw6wd-Ok""
  },
  {
    "{": ""      ""Video ID: 3DwoWSPxiik""
  },
  {
    "{": ""      ""Video ID: MO4hTsHXV3Q""
  },
  {
    "{": ""      ""Video ID: zavKGm6To-w""
  },
  {
    "{": ""      ""Video ID: kZcNVYDh9bY""
  },
  {
    "{": ""      ""Video ID: _V-2NKUlzns""
  },
  {
    "{": ""      ""Video ID: VyqLl0XoMTI""
  },
  {
    "{": ""      ""Video ID: Bn6O42a5vl8""
  },
  {
    "{": ""      ""Video ID: wLd-0qpPNR4""
  },
  {
    "{": ""      ""Video ID: 6AjGrc452JM""
  },
  {
    "{": ""      ""Video ID: No6uG6yKZrs""
  },
  {
    "{": ""      ""Video ID: 4atXek9tHw8""
  },
  {
    "{": ""      ""Video ID: thuRxNizRJQ""
  },
  {
    "{": ""      ""Video ID: 2Poh6kMWu00""
  },
  {
    "{": ""      ""Video ID: nN_1WJkh7Cw""
  },
  {
    "{": ""      ""Video ID: OcNmyTOLNZY""
  },
  {
    "{": ""      ""Video ID: jkyhqE_VOEE""
  },
  {
    "{": ""      ""Video ID: 6SFhUAR7ynQ""
  },
  {
    "{": ""      ""Video ID: jvBjp30wYOY""
  },
  {
    "{": ""      ""Video ID: oSpjgM5J0ds""
  },
  {
    "{": ""      ""Video ID: p5fzMCPZlY4""
  },
  {
    "{": ""      ""Video ID: ybKSFRbxQ9E""
  },
  {
    "{": ""      ""Video ID: 4no7w01K5g8""
  },
  {
    "{": ""      ""Video ID: zj0IsvHXBo0""
  },
  {
    "{": ""      ""Video ID: TpXcMaBvadw""
  },
  {
    "{": ""      ""Video ID: 7wcn4GV-F0E""
  },
  {
    "{": ""      ""Video ID: -ozi3X9x5K8""
  },
  {
    "{": ""      ""Video ID: 2S1Khm46PPg""
  },
  {
    "{": ""      ""Video ID: M9XqZ_K9dvI""
  },
  {
    "{": ""      ""Video ID: CunJcv89wuk""
  },
  {
    "{": ""      ""Video ID: xXtpxVNia1w""
  },
  {
    "{": ""      ""Video ID: MM9Ug-9bLT4""
  },
  {
    "{": ""      ""Video ID: 63S3vacxI9c""
  },
  {
    "{": ""      ""Video ID: 0RWQ7R555i4""
  },
  {
    "{": ""      ""Video ID: DC02fl5OaRU""
  },
  {
    "{": ""      ""Video ID: f6cj8e1YGm4""
  },
  {
    "{": ""      ""Video ID: yKt799IcqOY""
  },
  {
    "{": ""      ""Video ID: g73y7YD8CSc""
  },
  {
    "{": ""      ""Video ID: S0R7bZLt2cY""
  },
  {
    "{": ""      ""Video ID: C9FFH5Xjt_4""
  },
  {
    "{": ""      ""Video ID: KPTTEU__llM""
  },
  {
    "{": ""      ""Video ID: Js9A4ZwRVQE""
  },
  {
    "{": ""      ""Video ID: Ax6tbVXHlvY""
  },
  {
    "{": ""      ""Video ID: STEErrJYaNM""
  },
  {
    "{": ""      ""Video ID: 3zCg3kMVi8o""
  },
  {
    "{": ""      ""Video ID: gShkT3m0XrY""
  },
  {
    "{": ""      ""Video ID: 346AoQpw7kM""
  },
  {
    "{": ""      ""Video ID: khuu-RhOBDU""
  },
  {
    "{": ""      ""Video ID: ygWExq7g2F0""
  },
  {
    "{": ""      ""Video ID: zQjQMnp9jvE""
  },
  {
    "{": ""      ""Video ID: Tw6JdSNPRlo""
  },
  {
    "{": ""      ""Video ID: XqTMWUk2inI""
  },
  {
    "{": ""      ""Video ID: 3dU1xxo4YQI""
  },
  {
    "{": ""      ""Video ID: TV2v37u39NY""
  },
  {
    "{": ""      ""Video ID: JVeK0JDPm8Y""
  },
  {
    "{": ""      ""Video ID: PFQAQVcn89A""
  },
  {
    "{": ""      ""Video ID: I_TRJysI5U0""
  },
  {
    "{": ""      ""Video ID: 9_v7ytDt3Lc""
  },
  {
    "{": ""      ""Video ID: TFgR7lC5LEY""
  },
  {
    "{": ""      ""Video ID: 0T6-O8GIylQ""
  },
  {
    "{": ""      ""Video ID: bejx7NllRlo""
  },
  {
    "{": ""      ""Video ID: FxoDfjvGXjo""
  },
  {
    "{": ""      ""Video ID: 4vXK_1iCF-g""
  },
  {
    "{": ""      ""Video ID: tuCY6g5pwfo""
  },
  {
    "{": ""      ""Video ID: JaTWTMxXjH0""
  },
  {
    "{": ""      ""Video ID: 28mfvbJk_os""
  },
  {
    "{": ""      ""Video ID: f1Pd2I4kd6I""
  },
  {
    "{": ""      ""Video ID: ZY5UfdT1XL8""
  },
  {
    "{": ""      ""Video ID: WXy0Vp9ZPcQ""
  },
  {
    "{": ""      ""Video ID: Xy-HW28UY7g""
  },
  {
    "{": ""      ""Video ID: b7d4QJqp7U8""
  },
  {
    "{": ""      ""Video ID: zr-4A_7LFt0""
  },
  {
    "{": ""      ""Video ID: Ppr7ULw-zS4""
  },
  {
    "{": ""      ""Video ID: qH4vUW7KuBQ""
  },
  {
    "{": ""      ""Video ID: agoJ2vSsjZY""
  },
  {
    "{": ""      ""Video ID: HrrnNM8dzvM""
  },
  {
    "{": ""      ""Video ID: 3rKKNnZJfjE""
  },
  {
    "{": ""      ""Video ID: omzVG87fzOY""
  },
  {
    "{": ""      ""Video ID: UFf3j8zo8l8""
  },
  {
    "{": ""      ""Video ID: _XleKEAHd5I""
  },
  {
    "{": ""      ""Video ID: fCqg520YI0M""
  },
  {
    "{": ""      ""Video ID: U2cKKqrmjWs""
  },
  {
    "{": ""      ""Video ID: 037gP3t_in4""
  },
  {
    "{": ""      ""Video ID: jpMDXqXMom0""
  },
  {
    "{": ""      ""Video ID: 6RmsyoYPz7E""
  },
  {
    "{": ""      ""Video ID: lkAAIbtrxM0""
  },
  {
    "{": ""      ""Video ID: y_z8lEQ3Cqw""
  },
  {
    "{": ""      ""Video ID: sc99aDmWGMo""
  },
  {
    "{": ""      ""Video ID: vxIFbhNp8cg""
  },
  {
    "{": ""      ""Video ID: SXLoCLUEBFI""
  },
  {
    "{": ""      ""Video ID: b6a-j53u1YQ""
  },
  {
    "{": ""      ""Video ID: XOFRbk46qpk""
  },
  {
    "{": ""      ""Video ID: zKE4Cikx3k0""
  },
  {
    "{": ""      ""Video ID: UUrFYsKCxAg""
  },
  {
    "{": ""      ""Video ID: V7o8mEbgBCc""
  },
  {
    "{": ""      ""Video ID: HGIXEWZx7gg""
  },
  {
    "{": ""      ""Video ID: muyDjlhNJkI""
  },
  {
    "{": ""      ""Video ID: ZMODLl2QHh4""
  },
  {
    "{": ""      ""Video ID: iilJljVcq_8""
  },
  {
    "{": ""      ""Video ID: OSbW19YfeLw""
  },
  {
    "{": ""      ""Video ID: mcs682bF7Ic""
  },
  {
    "{": ""      ""Video ID: FAzMuHyg8Eg""
  },
  {
    "{": ""      ""Video ID: pobxJVbc4-U""
  },
  {
    "{": ""      ""Video ID: Olke4JH8QI0""
  },
  {
    "{": ""      ""Video ID: mkGVQjFm2FU""
  },
  {
    "{": ""      ""Video ID: 0niFNfcLYEg""
  },
  {
    "{": ""      ""Video ID: 2OQw-ri1nMU""
  },
  {
    "{": ""      ""Video ID: 83Xb_cKtcHI""
  },
  {
    "{": ""      ""Video ID: 3wW3cx91F_8""
  },
  {
    "{": ""      ""Video ID: zB7fiLReAwE""
  },
  {
    "{": ""      ""Video ID: QxoP_9W6FC8""
  },
  {
    "{": ""      ""Video ID: BaS6bLQixkM""
  },
  {
    "{": ""      ""Video ID: -M9wfrz86Gg""
  },
  {
    "{": ""      ""Video ID: gw4ASWnJsto""
  },
  {
    "{": ""      ""Video ID: TdPOm1BxmGU""
  },
  {
    "{": ""      ""Video ID: FBrnfSe95cs""
  },
  {
    "{": ""      ""Video ID: Tzu0c6ZVnAg""
  },
  {
    "{": ""      ""Video ID: VCMwVFz9v70""
  },
  {
    "{": ""      ""Video ID: E0qDelTKy-0""
  },
  {
    "{": ""      ""Video ID: xqeQ2H_8azM""
  },
  {
    "{": ""      ""Video ID: R6_GJ09IOhA""
  },
  {
    "{": ""      ""Video ID: CIrGE3UYf7M""
  },
  {
    "{": ""      ""Video ID: nwvd9u76nMQ""
  },
  {
    "{": ""      ""Video ID: BMcBpwmLa7U""
  },
  {
    "{": ""      ""Video ID: 0rYatMHC0N4""
  },
  {
    "{": ""      ""Video ID: juqcREUGEAs""
  },
  {
    "{": ""      ""Video ID: rVhGT_eB03g""
  },
  {
    "{": ""      ""Video ID: VaDtbwkTlBI""
  },
  {
    "{": ""      ""Video ID: cLYrFR9RT_U""
  },
  {
    "{": ""      ""Video ID: brX1Op5qmAQ""
  },
  {
    "{": ""      ""Video ID: 2klDumsraM4""
  },
  {
    "{": ""      ""Video ID: EOkdSx6OPSQ""
  },
  {
    "{": ""      ""Video ID: KK38wzakz2k""
  },
  {
    "{": ""      ""Video ID: TK9DH-HyDWk""
  },
  {
    "{": ""      ""Video ID: wQHtOGp-zb8""
  },
  {
    "{": ""      ""Video ID: uydOmHAuxxg""
  },
  {
    "{": ""      ""Video ID: -iUO2dqYmqg""
  },
  {
    "{": ""      ""Video ID: 1pV0-_99fLk""
  },
  {
    "{": ""      ""Video ID: d1japIhKU9I""
  },
  {
    "{": ""      ""Video ID: -7qIKCG8Ims""
  },
  {
    "{": ""      ""Video ID: ze4iGtAIcwQ""
  },
  {
    "{": ""      ""Video ID: 0VuavuJPhP4""
  },
  {
    "{": ""      ""Video ID: LKvyF5A3ozw""
  },
  {
    "{": ""      ""Video ID: IyVJ5UYmx10""
  },
  {
    "{": ""      ""Video ID: pq8hdtirZ2I""
  },
  {
    "{": ""      ""Video ID: DOTfWrjYwdk""
  },
  {
    "{": ""      ""Video ID: hxUBtSnRzLo""
  },
  {
    "{": ""      ""Video ID: Y2dIAJFBVMM""
  },
  {
    "{": ""      ""Video ID: e3_x5_-6YH0""
  },
  {
    "{": ""      ""Video ID: IhVtwsJAhPU""
  },
  {
    "{": ""      ""Video ID: ncOxCxiBBrc""
  },
  {
    "{": ""      ""Video ID: -cTGZRtB8FY""
  },
  {
    "{": ""      ""Video ID: bxKsLtElxXc""
  },
  {
    "{": ""      ""Video ID: YgGLCbwhmq4""
  },
  {
    "{": ""      ""Video ID: i9i74snDv8c""
  },
  {
    "{": ""      ""Video ID: Fe751kMBwms""
  },
  {
    "{": ""      ""Video ID: 8a3DWUCGIqg""
  },
  {
    "{": ""      ""Video ID: t4oebxLUHTg""
  },
  {
    "{": ""      ""Video ID: 82e4U3H-VfQ""
  },
  {
    "{": ""      ""Video ID: a9lEV2pMWAo""
  },
  {
    "{": ""      ""Video ID: 3HtVe7T_Nf0""
  },
  {
    "{": ""      ""Video ID: C7xk_1jZ6dw""
  },
  {
    "{": ""      ""Video ID: HveqGQrcYU8""
  },
  {
    "{": ""      ""Video ID: Nn0ta8pmfgU""
  },
  {
    "{": ""      ""Video ID: hsS9IdHIZ-4""
  },
  {
    "{": ""      ""Video ID: OoomZSLB_8c""
  },
  {
    "{": ""      ""Video ID: lKKg3RLgA2o""
  },
  {
    "{": ""      ""Video ID: lzIHu2GmcW8""
  },
  {
    "{": ""      ""Video ID: Nsfe_iElFmk""
  },
  {
    "{": ""      ""Video ID: O_GOjOsGxjM""
  },
  {
    "{": ""      ""Video ID: xCewmndnJEY""
  },
  {
    "{": ""      ""Video ID: eBi9aE5jDbE""
  },
  {
    "{": ""      ""Video ID: 9k5sx1PLxkQ""
  },
  {
    "{": ""      ""Video ID: tSo05P5QGGY""
  },
  {
    "{": ""      ""Video ID: Xa-hX6soAgg""
  },
  {
    "{": ""      ""Video ID: dJezhqrz5zI""
  },
  {
    "{": ""      ""Video ID: sfKJHlr-xAQ""
  },
  {
    "{": ""      ""Video ID: _YTy2RmBhXk""
  },
  {
    "{": ""      ""Video ID: IKxbbwiyMaY""
  },
  {
    "{": ""      ""Video ID: lEfvXaFKkeU""
  },
  {
    "{": ""      ""Video ID: _xmEP5Qyh_g""
  },
  {
    "{": ""      ""Video ID: bIqobg9FdLE""
  },
  {
    "{": ""      ""Video ID: No-RGC20B_0""
  },
  {
    "{": ""      ""Video ID: IcmI6UnR4gg""
  },
  {
    "{": ""      ""Video ID: ssbz7HuzONI""
  },
  {
    "{": ""      ""Video ID: lss4rR8N8as""
  },
  {
    "{": ""      ""Video ID: 4eJ3gS7Cih8""
  },
  {
    "{": ""      ""Video ID: 1IIns3qbibc""
  },
  {
    "{": ""      ""Video ID: eKrAZpANoeM""
  },
  {
    "{": ""      ""Video ID: Rpfz3m11bsk""
  },
  {
    "{": ""      ""Video ID: LcJ-y39GzzQ""
  },
  {
    "{": ""      ""Video ID: EYJxmaaYglg""
  },
  {
    "{": ""      ""Video ID: LHFiZrVSGeA""
  },
  {
    "{": ""      ""Video ID: XKQnHZ_yYJ0""
  },
  {
    "{": ""      ""Video ID: 81ng6qGZGpE""
  },
  {
    "{": ""      ""Video ID: UxfDObpWTiU""
  },
  {
    "{": ""      ""Video ID: ClaDcfTpZqg""
  },
  {
    "{": ""      ""Video ID: FAPi3TYPS34""
  },
  {
    "{": ""      ""Video ID: bKSH74eIvEU""
  },
  {
    "{": ""      ""Video ID: zK7gikSuTNQ""
  },
  {
    "{": ""      ""Video ID: 2FIiLsY6cXs""
  },
  {
    "{": ""      ""Video ID: 4XPJQihTadM""
  },
  {
    "{": ""      ""Video ID: Wo0mwCtqSWs""
  },
  {
    "{": ""      ""Video ID: bVYwcXMyLEs""
  },
  {
    "{": ""      ""Video ID: 5x-ksLinRs4""
  },
  {
    "{": ""      ""Video ID: uBVU2k_Zq0Q""
  },
  {
    "{": ""      ""Video ID: T0nJH6zB9VM""
  },
  {
    "{": ""      ""Video ID: E_BMCqd8OC0""
  },
  {
    "{": ""      ""Video ID: WtzrqvPfnE0""
  },
  {
    "{": ""      ""Video ID: _a1WzIjjCg4""
  },
  {
    "{": ""      ""Video ID: 3qaBoDZXrb0""
  },
  {
    "{": ""      ""Video ID: REGaafCoPNM""
  },
  {
    "{": ""      ""Video ID: GDcQeNnD8f0""
  },
  {
    "{": ""      ""Video ID: NjA3lUDr8uI""
  },
  {
    "{": ""      ""Video ID: zCUDNRy03Hg""
  },
  {
    "{": ""      ""Video ID: Sdo7UQfQISk""
  },
  {
    "{": ""      ""Video ID: ZtX44XwN-nI""
  },
  {
    "{": ""      ""Video ID: Vxh_fxwXC_M""
  },
  {
    "{": ""      ""Video ID: jqzM36C3H7Q""
  },
  {
    "{": ""      ""Video ID: Gt9OLpX2I7g""
  },
  {
    "{": ""      ""Video ID: TiBUzbdHV4g""
  },
  {
    "{": ""      ""Video ID: vgadqzZlQF0""
  },
  {
    "{": ""      ""Video ID: NgyNLQe8qX0""
  },
  {
    "{": ""      ""Video ID: b-IRI1bA5jw""
  },
  {
    "{": ""      ""Video ID: e7xtcuSCWGk""
  },
  {
    "{": ""      ""Video ID: NzYh4CGAbCU""
  },
  {
    "{": ""      ""Video ID: KOkwUKn_gfc""
  },
  {
    "{": ""      ""Video ID: o9vOFx0q9x0""
  },
  {
    "{": ""      ""Video ID: 2JYSGXoNVM4""
  },
  {
    "{": ""      ""Video ID: weKaHQCjKz0""
  },
  {
    "{": ""      ""Video ID: jfYip0ukUXE""
  },
  {
    "{": ""      ""Video ID: 1Y4ErG1cmOo""
  },
  {
    "{": ""      ""Video ID: ATLS3IDTEHA""
  },
  {
    "{": ""      ""Video ID: ZlP2X7ybja8""
  },
  {
    "{": ""      ""Video ID: 8M4_IlbaZHA""
  },
  {
    "{": ""      ""Video ID: J_e8pmIoUMc""
  },
  {
    "{": ""      ""Video ID: BFMmB7C453c""
  },
  {
    "{": ""      ""Video ID: trMrCKZMZSE""
  },
  {
    "{": ""      ""Video ID: MIvYhuXogJk""
  },
  {
    "{": ""      ""Video ID: ieP97FqZo5U""
  },
  {
    "{": ""      ""Video ID: Ge2FHDf_L78""
  },
  {
    "{": ""      ""Video ID: OdW5zzjsWQ8""
  },
  {
    "{": ""      ""Video ID: UUCm5-6-b00""
  },
  {
    "{": ""      ""Video ID: qLUKuI44Aeo""
  },
  {
    "{": ""      ""Video ID: k4GRGvIK_qo""
  },
  {
    "{": ""      ""Video ID: ubEW0LArYpc""
  },
  {
    "{": ""      ""Video ID: Y4ZR1cTFFQ8""
  },
  {
    "{": ""      ""Video ID: ANCu6ZYjENo""
  },
  {
    "{": ""      ""Video ID: iNwTVbLsBik""
  },
  {
    "{": ""      ""Video ID: cDH4s9VaVcQ""
  },
  {
    "{": ""      ""Video ID: uW6bJBmGn7o""
  },
  {
    "{": ""      ""Video ID: ZshSyn-j1bI""
  },
  {
    "{": ""      ""Video ID: heoGLukn98k""
  },
  {
    "{": ""      ""Video ID: DAjORLWc__4""
  },
  {
    "{": ""      ""Video ID: f6B_7ZRSwWg""
  },
  {
    "{": ""      ""Video ID: T0SMkfnd2t8""
  },
  {
    "{": ""      ""Video ID: g8ectEBz3vQ""
  },
  {
    "{": ""      ""Video ID: cq6HTfOotGk""
  },
  {
    "{": ""      ""Video ID: _fIOM24grQo""
  },
  {
    "{": ""      ""Video ID: jNSmXdO7HJY""
  },
  {
    "{": ""      ""Video ID: LKrh7MI_02c""
  },
  {
    "{": ""      ""Video ID: iPWb7lXsQyY""
  },
  {
    "{": ""      ""Video ID: 4ZM5Q1zAKE4""
  },
  {
    "{": ""      ""Video ID: nvrHklGOLEM""
  },
  {
    "{": ""      ""Video ID: mxdKvj6jfIk""
  },
  {
    "{": ""      ""Video ID: 4buhnXMZGs8""
  },
  {
    "{": ""      ""Video ID: 2hj25d_V0NE""
  },
  {
    "{": ""      ""Video ID: XRHdV-PNQRo""
  },
  {
    "{": ""      ""Video ID: rf88xYgc8Js""
  },
  {
    "{": ""      ""Video ID: HT0wnbKelIg""
  },
  {
    "{": ""      ""Video ID: M6SelMkjXzE""
  },
  {
    "{": ""      ""Video ID: -f857CIi0cc""
  },
  {
    "{": ""      ""Video ID: heFA3wPulos""
  },
  {
    "{": ""      ""Video ID: QxySE-VkCsk""
  },
  {
    "{": ""      ""Video ID: qgGKJr1Elqc""
  },
  {
    "{": ""      ""Video ID: aMyOYqbQrhg""
  },
  {
    "{": ""      ""Video ID: gw2P_gim1Gc""
  },
  {
    "{": ""      ""Video ID: Mz_PsVlI9IA""
  },
  {
    "{": ""      ""Video ID: oxXAnpahZNg""
  },
  {
    "{": ""      ""Video ID: G2_ckAwJoBA""
  },
  {
    "{": ""      ""Video ID: 3Rq8dKd1Xy0""
  },
  {
    "{": ""      ""Video ID: 3KT1PHkBXeM""
  },
  {
    "{": ""      ""Video ID: IlUkfM-AJDk""
  },
  {
    "{": ""      ""Video ID: gplEaDRKKaw""
  },
  {
    "{": ""      ""Video ID: IVwuP-O9onk""
  },
  {
    "{": ""      ""Video ID: XrDyUzoysPo""
  },
  {
    "{": ""      ""Video ID: 3tdoQr3BQ1g""
  },
  {
    "{": ""      ""Video ID: Kak15GbiZTA""
  },
  {
    "{": ""      ""Video ID: Ytyx73NGyjI""
  },
  {
    "{": ""      ""Video ID: KvwaKMEiSjI""
  },
  {
    "{": ""      ""Video ID: hjP3vZ7PW6Q""
  },
  {
    "{": ""      ""Video ID: cNZaq-YKCnE""
  },
  {
    "{": ""      ""Video ID: t-1Q9amQp34""
  },
  {
    "{": ""      ""Video ID: 8rWyeRdgnp4""
  },
  {
    "{": ""      ""Video ID: v4hDJzbzoTw""
  },
  {
    "{": ""      ""Video ID: toez6IWu3Rg""
  },
  {
    "{": ""      ""Video ID: Rj0j5JGl4Qg""
  },
  {
    "{": ""      ""Video ID: DF38U5SWcIo""
  },
  {
    "{": ""      ""Video ID: NFgKWsYMD-c""
  },
  {
    "{": ""      ""Video ID: _Tqws3tgtZs""
  },
  {
    "{": ""      ""Video ID: VzRoDo804zo""
  },
  {
    "{": ""      ""Video ID: L3XhSgzAmAA""
  },
  {
    "{": ""      ""Video ID: 40mOZF5Fe_8""
  },
  {
    "{": ""      ""Video ID: fU6uvKixSro""
  },
  {
    "{": ""      ""Video ID: L7rboLvGIfo""
  },
  {
    "{": ""      ""Video ID: QEr92PtR_6Q""
  },
  {
    "{": ""      ""Video ID: ODX-jLguVSA""
  },
  {
    "{": ""      ""Video ID: xlTSMNhG_PA""
  },
  {
    "{": ""      ""Video ID: lLaitLVtY14""
  },
  {
    "{": ""      ""Video ID: JZKs8QsYS8w""
  },
  {
    "{": ""      ""Video ID: o7VfGxVvmxE""
  },
  {
    "{": ""      ""Video ID: pkMJIaVIM-s""
  },
  {
    "{": ""      ""Video ID: GzYCIbEpft4""
  },
  {
    "{": ""      ""Video ID: fyOivSl6Zxw""
  },
  {
    "{": ""      ""Video ID: -8BRtmzUilA""
  },
  {
    "{": ""      ""Video ID: 49KawcUjohY""
  },
  {
    "{": ""      ""Video ID: XFYGD9K7918""
  },
  {
    "{": ""      ""Video ID: 5GE82tqcYYQ""
  },
  {
    "{": ""      ""Video ID: MuOvqeABHvQ""
  },
  {
    "{": ""      ""Video ID: -2caf6KlSyw""
  },
  {
    "{": ""      ""Video ID: LLTF3IUKW0Q""
  },
  {
    "{": ""      ""Video ID: 22IPpCDW2LU""
  },
  {
    "{": ""      ""Video ID: nf-bK1_0epk""
  },
  {
    "{": ""      ""Video ID: Tbk4Ms2cnjE""
  },
  {
    "{": ""      ""Video ID: VhcjeZ3o5us""
  },
  {
    "{": ""      ""Video ID: PdLCR_KYD7s""
  },
  {
    "{": ""      ""Video ID: cI1EqjsFppY""
  },
  {
    "{": ""      ""Video ID: A9Zy3B9s0qc""
  },
  {
    "{": ""      ""Video ID: b3VrrIRwriE""
  },
  {
    "{": ""      ""Video ID: Yw7yAbTQ5IM""
  },
  {
    "{": ""      ""Video ID: Iwguu6DALfU""
  },
  {
    "{": ""      ""Video ID: lMDKYhUlZAg""
  },
  {
    "{": ""      ""Video ID: a84kyLLSDd8""
  },
  {
    "{": ""      ""Video ID: qWv3n1Q5JVA""
  },
  {
    "{": ""      ""Video ID: Ico7Ti6p96c""
  },
  {
    "{": ""      ""Video ID: OysY_GC06HI""
  },
  {
    "{": ""      ""Video ID: hauN64i1ydQ""
  },
  {
    "{": ""      ""Video ID: 1t7AGdEaBTY""
  },
  {
    "{": ""      ""Video ID: 5jl29CyHnH0""
  },
  {
    "{": ""      ""Video ID: _Rg14AGjJWQ""
  },
  {
    "{": ""      ""Video ID: 5BXX5UnNicA""
  },
  {
    "{": ""      ""Video ID: 7npT7bujCtg""
  },
  {
    "{": ""      ""Video ID: cB2wO806gZo""
  },
  {
    "{": ""      ""Video ID: um-GMygsRg4""
  },
  {
    "{": ""      ""Video ID: ZbGFvljO_VM""
  },
  {
    "{": ""      ""Video ID: KS0pSwdQfbY""
  },
  {
    "{": ""      ""Video ID: ge8zd1ZR-hc""
  },
  {
    "{": ""      ""Video ID: WrNt-x-5XK0""
  },
  {
    "{": ""      ""Video ID: Bdk5m5IT8NY""
  },
  {
    "{": ""      ""Video ID: A0j9qEUwUak""
  },
  {
    "{": ""      ""Video ID: Z3C0K0FBHmY""
  },
  {
    "{": ""      ""Video ID: OyXKGT0llzY""
  },
  {
    "{": ""      ""Video ID: vtYRc4t2EMU""
  },
  {
    "{": ""      ""Video ID: AwCuxD5rRZc""
  },
  {
    "{": ""      ""Video ID: XPfaF-N42Gk""
  },
  {
    "{": ""      ""Video ID: fBkDCv4mIqY""
  },
  {
    "{": ""      ""Video ID: hXqKagsGI0c""
  },
  {
    "{": ""      ""Video ID: DlvlMJUjpqo""
  },
  {
    "{": ""      ""Video ID: ipprfPxPFdI""
  },
  {
    "{": ""      ""Video ID: wNbkYukCsfk""
  },
  {
    "{": ""      ""Video ID: awqWWlwUzFs""
  },
  {
    "{": ""      ""Video ID: ftEpeU0UShQ""
  },
  {
    "{": ""      ""Video ID: caxyKvL44OY""
  },
  {
    "{": ""      ""Video ID: SELD4p184-E""
  },
  {
    "{": ""      ""Video ID: f7mOEI-cuFk""
  },
  {
    "{": ""      ""Video ID: gsy1QlM825A""
  },
  {
    "{": ""      ""Video ID: YH1uYYjQFsU""
  },
  {
    "{": ""      ""Video ID: UxpOAcUruKk""
  },
  {
    "{": ""      ""Video ID: oOo2hHu66oo""
  },
  {
    "{": ""      ""Video ID: nr_7cBEN1aU""
  },
  {
    "{": ""      ""Video ID: gJwktYxztVU""
  },
  {
    "{": ""      ""Video ID: coQYz-K52_w""
  },
  {
    "{": ""      ""Video ID: RBFYCz5iFu4""
  },
  {
    "{": ""      ""Video ID: qkvl374liGs""
  },
  {
    "{": ""      ""Video ID: _rqUsC2KsiI""
  },
  {
    "{": ""      ""Video ID: vjTZakAqSWo""
  },
  {
    "{": ""      ""Video ID: vuBo4E77ZXo""
  },
  {
    "{": ""      ""Video ID: 9kJEQeE8opA""
  },
  {
    "{": ""      ""Video ID: NRpEji5aUwQ""
  },
  {
    "{": ""      ""Video ID: OQbvWdOzFNQ""
  },
  {
    "{": ""      ""Video ID: 4ztmYLxbuy0""
  },
  {
    "{": ""      ""Video ID: HiQ-Fk9JTdM""
  },
  {
    "{": ""      ""Video ID: _cwh9hpp__k""
  },
  {
    "{": ""      ""Video ID: UbiU9hqDQRQ""
  },
  {
    "{": ""      ""Video ID: F8O3fx4iEGQ""
  },
  {
    "{": ""      ""Video ID: Ux63ReCApAE""
  },
  {
    "{": ""      ""Video ID: RAUfVpv2ngM""
  },
  {
    "{": ""      ""Video ID: XkgYQFWTtNU""
  },
  {
    "{": ""      ""Video ID: 0qOAEbkFkCk""
  },
  {
    "{": ""      ""Video ID: dwTw3SImkG0""
  },
  {
    "{": ""      ""Video ID: HUrhDa6v-04""
  },
  {
    "{": ""      ""Video ID: ctkxZ4vUmxI""
  },
  {
    "{": ""      ""Video ID: oidWzutLeVA""
  },
  {
    "{": ""      ""Video ID: GO753UnpICs""
  },
  {
    "{": ""      ""Video ID: QrUXLx2skHo""
  },
  {
    "{": ""      ""Video ID: 7tss3pvwUJ0""
  },
  {
    "{": ""      ""Video ID: nVzw52f7hgU""
  },
  {
    "{": ""      ""Video ID: gtLSeUe5ZoQ""
  },
  {
    "{": ""      ""Video ID: RfD1MGMGVKw""
  },
  {
    "{": ""      ""Video ID: Nle5RqYVQqU""
  },
  {
    "{": ""      ""Video ID: ElXL0uAbhxw""
  },
  {
    "{": ""      ""Video ID: B500sccyMog""
  },
  {
    "{": ""      ""Video ID: 30ochFAoCEI""
  },
  {
    "{": ""      ""Video ID: NN3x4l5fKS0""
  },
  {
    "{": ""      ""Video ID: 8KvUE-Vg6JI""
  },
  {
    "{": ""      ""Video ID: DCIgXYaKrkU""
  },
  {
    "{": ""      ""Video ID: TurL-MOsH18""
  },
  {
    "{": ""      ""Video ID: 0OKr3ImkcJs""
  },
  {
    "{": ""      ""Video ID: _TND61FAe2E""
  },
  {
    "{": ""      ""Video ID: KcbxHP75L2M""
  },
  {
    "{": ""      ""Video ID: 40SCjbSczEo""
  },
  {
    "{": ""      ""Video ID: OZopJClcGvo""
  },
  {
    "{": ""      ""Video ID: Q7TCSCzdftE""
  },
  {
    "{": ""      ""Video ID: XQDJlLL3WlQ""
  },
  {
    "{": ""      ""Video ID: -0eF7j645Tc""
  },
  {
    "{": ""      ""Video ID: NowRMPE_nI0""
  },
  {
    "{": ""      ""Video ID: vVRhWnHHPwI""
  },
  {
    "{": ""      ""Video ID: 7oezxBOD1bg""
  },
  {
    "{": ""      ""Video ID: 43UxC-9gp0o""
  },
  {
    "{": ""      ""Video ID: kmF0C1xBKC4""
  },
  {
    "{": ""      ""Video ID: dwKrnd9onD0""
  },
  {
    "{": ""      ""Video ID: Q-xSPY8q-5E""
  },
  {
    "{": ""      ""Video ID: Bvq0IUYCzgs""
  },
  {
    "{": ""      ""Video ID: hsX80SMo5Mg""
  },
  {
    "{": ""      ""Video ID: OflzgSHj0fY""
  },
  {
    "{": ""      ""Video ID: sBSniZoSoDI""
  },
  {
    "{": ""      ""Video ID: -AcsP2kHzyw""
  },
  {
    "{": ""      ""Video ID: w4Kb9SX8t6U""
  },
  {
    "{": ""      ""Video ID: oWXNC1Bu5Pg""
  },
  {
    "{": ""      ""Video ID: LLDQmRliy0A""
  },
  {
    "{": ""      ""Video ID: DdMbPn5Ns9A""
  },
  {
    "{": ""      ""Video ID: Z_Ob24qgYhU""
  },
  {
    "{": ""      ""Video ID: lzCwAs5kVXc""
  },
  {
    "{": ""      ""Video ID: 2N5yqS4vud0""
  },
  {
    "{": ""      ""Video ID: BbC4t-B-Vsg""
  },
  {
    "{": ""      ""Video ID: 8EBtv2xfqks""
  },
  {
    "{": ""      ""Video ID: opKNqaOr6so""
  },
  {
    "{": ""      ""Video ID: oYyKxFLWYLA""
  },
  {
    "{": ""      ""Video ID: uYDSUd-gOBY""
  },
  {
    "{": ""      ""Video ID: 9o8HSdtjI6Q""
  },
  {
    "{": ""      ""Video ID: fe66EodgWww""
  },
  {
    "{": ""      ""Video ID: Op0GF6O7o7w""
  },
  {
    "{": ""      ""Video ID: 0z_BBdUETkA""
  },
  {
    "{": ""      ""Video ID: sZn71ksLmYE""
  },
  {
    "{": ""      ""Video ID: USoDibfcLtQ""
  },
  {
    "{": ""      ""Video ID: WIYlDYK2rcM""
  },
  {
    "{": ""      ""Video ID: BXQdOsoM_nc""
  },
  {
    "{": ""      ""Video ID: RO-76YxtHpg""
  },
  {
    "{": ""      ""Video ID: vSSqYLGpjZA""
  },
  {
    "{": ""      ""Video ID: VuSErM6iEc4""
  },
  {
    "{": ""      ""Video ID: 7L355h3AhNQ""
  },
  {
    "{": ""      ""Video ID: -44RnGJGp2E""
  },
  {
    "{": ""      ""Video ID: QahWKgjBVG4""
  },
  {
    "{": ""      ""Video ID: 7S4hPryoPZ8""
  },
  {
    "{": ""      ""Video ID: Kci60TcQEZg""
  },
  {
    "{": ""      ""Video ID: eAPKDB36nOg""
  },
  {
    "{": ""      ""Video ID: _sWKVruPC5s""
  },
  {
    "{": ""      ""Video ID: 88I13Zyjexs""
  },
  {
    "{": ""      ""Video ID: wUlqwYExtq8""
  },
  {
    "{": ""      ""Video ID: ZmImYK-9Ej0""
  },
  {
    "{": ""      ""Video ID: aJ-EGXigxVg""
  },
  {
    "{": ""      ""Video ID: S2qveHJYZ9Y""
  },
  {
    "{": ""      ""Video ID: B_AnA9FLFd4""
  },
  {
    "{": ""      ""Video ID: vHPEvojmNQc""
  },
  {
    "{": ""      ""Video ID: hGWYhEWlXfM""
  },
  {
    "{": ""      ""Video ID: v0_C7_1ThrA""
  },
  {
    "{": ""      ""Video ID: rzDky8b-lec""
  },
  {
    "{": ""      ""Video ID: 0OvoKms9C1Q""
  },
  {
    "{": ""      ""Video ID: pZcU7rXef7Q""
  },
  {
    "{": ""      ""Video ID: RRyGvpGEegk""
  },
  {
    "{": ""      ""Video ID: EquhhU0HE8s""
  },
  {
    "{": ""      ""Video ID: W3rAxG7wgyo""
  },
  {
    "{": ""      ""Video ID: _UIOMSs9JRY""
  },
  {
    "{": ""      ""Video ID: nPhOu-3kcUc""
  },
  {
    "{": ""      ""Video ID: 3zub0B6d4HQ""
  },
  {
    "{": ""      ""Video ID: MURzf0jX93w""
  },
  {
    "{": ""      ""Video ID: ecSmEZcyYWE""
  },
  {
    "{": ""      ""Video ID: gXb9p6nZmmA""
  },
  {
    "{": ""      ""Video ID: IA5mG5BCGXk""
  },
  {
    "{": ""      ""Video ID: XL7xbK92YFc""
  },
  {
    "{": ""      ""Video ID: hHaspYZrGZQ""
  },
  {
    "{": ""      ""Video ID: PC2RqhIWl4I""
  },
  {
    "{": ""      ""Video ID: PIK_UPvecHw""
  },
  {
    "{": ""      ""Video ID: Q7BC6uU3_Cs""
  },
  {
    "{": ""      ""Video ID: EmExheyGwKs""
  },
  {
    "{": ""      ""Video ID: b_wdviISt3I""
  },
  {
    "{": ""      ""Video ID: laDx5tiRIDk""
  },
  {
    "{": ""      ""Video ID: lafqGX86QLc""
  },
  {
    "{": ""      ""Video ID: mXtP_TBQAx0""
  },
  {
    "{": ""      ""Video ID: iTacfULKIC4""
  },
  {
    "{": ""      ""Video ID: rk7inOaLGOg""
  },
  {
    "{": ""      ""Video ID: g_kOggbsIWE""
  },
  {
    "{": ""      ""Video ID: ziUjIdeJVLI""
  },
  {
    "{": ""      ""Video ID: oD5nSBciggA""
  },
  {
    "{": ""      ""Video ID: tFLBM_yVBNg""
  },
  {
    "{": ""      ""Video ID: 6S1s1Tox0tM""
  },
  {
    "{": ""      ""Video ID: v70n9MacS8c""
  },
  {
    "{": ""      ""Video ID: a3Geam9JzJM""
  },
  {
    "{": ""      ""Video ID: MNX6XpqWVR0""
  },
  {
    "{": ""      ""Video ID: bOkyTZsWKNs""
  },
  {
    "{": ""      ""Video ID: ePCFwaw6Rqw""
  },
  {
    "{": ""      ""Video ID: C98_wJvTh9g""
  },
  {
    "{": ""      ""Video ID: idgtcUCXbEg""
  },
  {
    "{": ""      ""Video ID: ItzdSFTZmyk""
  },
  {
    "{": ""      ""Video ID: VHahWen89Ck""
  },
  {
    "{": ""      ""Video ID: gFXk-4E4-BE""
  },
  {
    "{": ""      ""Video ID: PLlNES0NhIE""
  },
  {
    "{": ""      ""Video ID: Ze-CPjQ5qXE""
  },
  {
    "{": ""      ""Video ID: EQnT3jxYBxo""
  },
  {
    "{": ""      ""Video ID: dg2vL_JFzpQ""
  },
  {
    "{": ""      ""Video ID: iz3W98wdQsU""
  },
  {
    "{": ""      ""Video ID: L7fHPjhLpPU""
  },
  {
    "{": ""      ""Video ID: SJrx4-RGSns""
  },
  {
    "{": ""      ""Video ID: s_ZkJPgWW4k""
  },
  {
    "{": ""      ""Video ID: Zoea8X49FpY""
  },
  {
    "{": ""      ""Video ID: z6cAwvtdcMg""
  },
  {
    "{": ""      ""Video ID: WrFieuyrDak""
  },
  {
    "{": ""      ""Video ID: fHHoG-2mEPA""
  },
  {
    "{": ""      ""Video ID: z3ApKNhSzSg""
  },
  {
    "{": ""      ""Video ID: TP9Y4gI3s7E""
  },
  {
    "{": ""      ""Video ID: NMczRJh_OeI""
  },
  {
    "{": ""      ""Video ID: fiYNCUXKAy0""
  },
  {
    "{": ""      ""Video ID: R_2n2Y7cyEU""
  },
  {
    "{": ""      ""Video ID: Soh_2RYa9OA""
  },
  {
    "{": ""      ""Video ID: DvZHTFTGSIc""
  },
  {
    "{": ""      ""Video ID: lU03HRQx_3s""
  },
  {
    "{": ""      ""Video ID: Jcy3JbGjQwo""
  },
  {
    "{": ""      ""Video ID: 1KlQ9957kR0""
  },
  {
    "{": ""      ""Video ID: rAC9uPaO94Y""
  },
  {
    "{": ""      ""Video ID: HdJvHYfvudU""
  },
  {
    "{": ""      ""Video ID: lp4M4eatl68""
  },
  {
    "{": ""      ""Video ID: 6K7wZ07FKp4""
  },
  {
    "{": ""      ""Video ID: -dPhymHlcwU""
  },
  {
    "{": ""      ""Video ID: qkHK_EFfTCM""
  },
  {
    "{": ""      ""Video ID: SNw2CnPLYc8""
  },
  {
    "{": ""      ""Video ID: lBfZIjplmVc""
  },
  {
    "{": ""      ""Video ID: L_zs3GgOVv4""
  },
  {
    "{": ""      ""Video ID: kRJWmAS7z2I""
  },
  {
    "{": ""      ""Video ID: qXBXD2zizIY""
  },
  {
    "{": ""      ""Video ID: a0-HkVcMOSw""
  },
  {
    "{": ""      ""Video ID: oQlgJQgoytk""
  },
  {
    "{": ""      ""Video ID: 16hGGvRB2mI""
  },
  {
    "{": ""      ""Video ID: M8QblC51ojA""
  },
  {
    "{": ""      ""Video ID: SJjxv31GcJ4""
  },
  {
    "{": ""      ""Video ID: t3TUuvwC0II""
  },
  {
    "{": ""      ""Video ID: AmMG_JSLsPE""
  },
  {
    "{": ""      ""Video ID: -B8tbd_4ACQ""
  },
  {
    "{": ""      ""Video ID: JCre0fiAOAA""
  },
  {
    "{": ""      ""Video ID: EYrf5KbVaY0""
  },
  {
    "{": ""      ""Video ID: ZjIFYyCWS3g""
  },
  {
    "{": ""      ""Video ID: Z4eCih5QE1w""
  },
  {
    "{": ""      ""Video ID: -uuavmmS2Sk""
  },
  {
    "{": ""      ""Video ID: 1dpiwxrkXpo""
  },
  {
    "{": ""      ""Video ID: 7hjJUZ85nHw""
  },
  {
    "{": ""      ""Video ID: kfT2q-BODSs""
  },
  {
    "{": ""      ""Video ID: UkEJPULyBdw""
  },
  {
    "{": ""      ""Video ID: s81OipUilOo""
  },
  {
    "{": ""      ""Video ID: yXWNLq-gQNA""
  },
  {
    "{": ""      ""Video ID: HiywUJnJmrc""
  },
  {
    "{": ""      ""Video ID: yjBoAQw7bgo""
  },
  {
    "{": ""      ""Video ID: W6Fgcu_4EEY""
  },
  {
    "{": ""      ""Video ID: 9wJsovPRTEM""
  },
  {
    "{": ""      ""Video ID: n150E0LewC4""
  },
  {
    "{": ""      ""Video ID: Qxnr7tfKlgw""
  },
  {
    "{": ""      ""Video ID: if11PeyuZEI""
  },
  {
    "{": ""      ""Video ID: loaJUu6REGs""
  },
  {
    "{": ""      ""Video ID: Gx19TPrtW28""
  },
  {
    "{": ""      ""Video ID: 8IBIK2bAiSM""
  },
  {
    "{": ""      ""Video ID: zNJ98ewaz1A""
  },
  {
    "{": ""      ""Video ID: XgVrbzQobqM""
  },
  {
    "{": ""      ""Video ID: 8fCnolZivPw""
  },
  {
    "{": ""      ""Video ID: 2mr-FmucoEk""
  },
  {
    "{": ""      ""Video ID: MK3trTqAKg0""
  },
  {
    "{": ""      ""Video ID: W-pGwwj9Tdk""
  },
  {
    "{": ""      ""Video ID: 0p-vt7UiFfk""
  },
  {
    "{": ""      ""Video ID: cNfUX_r7aAI""
  },
  {
    "{": ""      ""Video ID: Mf0Blp79v5o""
  },
  {
    "{": ""      ""Video ID: Z1sLo18QHOU""
  },
  {
    "{": ""      ""Video ID: tLRo55a4k3E""
  },
  {
    "{": ""      ""Video ID: zP318FK-QR8""
  },
  {
    "{": ""      ""Video ID: wF9yyHLY0qA""
  },
  {
    "{": ""      ""Video ID: LoSRNce9_MY""
  },
  {
    "{": ""      ""Video ID: zDLi-3Bf8ko""
  },
  {
    "{": ""      ""Video ID: CJlDEP_U1AU""
  },
  {
    "{": ""      ""Video ID: 20HvHgBKV5M""
  },
  {
    "{": ""      ""Video ID: ndbgJcdeNPU""
  },
  {
    "{": ""      ""Video ID: CrpErGBLYRg""
  },
  {
    "{": ""      ""Video ID: kw6pWNA-kZ4""
  },
  {
    "{": ""      ""Video ID: peklYRHeRDA""
  },
  {
    "{": ""      ""Video ID: vhCLiy9D7W0""
  },
  {
    "{": ""      ""Video ID: cNoS7UN9_7g""
  },
  {
    "{": ""      ""Video ID: qDQGvTYk1U4""
  },
  {
    "{": ""      ""Video ID: 8KMRZokvHsQ""
  },
  {
    "{": ""      ""Video ID: FVnsuLFJW1o""
  },
  {
    "{": ""      ""Video ID: CQUhNbjquIo""
  },
  {
    "{": ""      ""Video ID: OzhvWCXeA-Q""
  },
  {
    "{": ""      ""Video ID: R0LEM85Zf0c""
  },
  {
    "{": ""      ""Video ID: ei9YEy4D7g8""
  },
  {
    "{": ""      ""Video ID: EDMVHLg4rR8""
  },
  {
    "{": ""      ""Video ID: TYdGYZ2ARUc""
  },
  {
    "{": ""      ""Video ID: NsdQWKIrsvk""
  },
  {
    "{": ""      ""Video ID: -H8hZxdVcZY""
  },
  {
    "{": ""      ""Video ID: hl5X3NGKt00""
  },
  {
    "{": ""      ""Video ID: fXjAYE3DSTQ""
  },
  {
    "{": ""      ""Video ID: Ra9h3SO2DVI""
  },
  {
    "{": ""      ""Video ID: wShPwkSi6ms""
  },
  {
    "{": ""      ""Video ID: p_gqq-Hg1BI""
  },
  {
    "{": ""      ""Video ID: Gf_KF3VVSXY""
  },
  {
    "{": ""      ""Video ID: yvsqsXiMBrA""
  },
  {
    "{": ""      ""Video ID: qx4qPbck-nk""
  },
  {
    "{": ""      ""Video ID: Y4NklDuDW0g""
  },
  {
    "{": ""      ""Video ID: DvhmuY-AaI4""
  },
  {
    "{": ""      ""Video ID: nbUo-uHTJm0""
  },
  {
    "{": ""      ""Video ID: e-MJOJc6wNY""
  },
  {
    "{": ""      ""Video ID: PSZeRRABSfE""
  },
  {
    "{": ""      ""Video ID: x3a0WB9zXbk""
  },
  {
    "{": ""      ""Video ID: FFjThvUDX54""
  },
  {
    "{": ""      ""Video ID: umWx44NL2T8""
  },
  {
    "{": ""      ""Video ID: LgwcP3RE4pM""
  },
  {
    "{": ""      ""Video ID: Hh6Bg3Rx2u8""
  },
  {
    "{": ""      ""Video ID: tP5O4qnfK5k""
  },
  {
    "{": ""      ""Video ID: HGM3epTX8V8""
  },
  {
    "{": ""      ""Video ID: kFxx5bliNvQ""
  },
  {
    "{": ""      ""Video ID: xrYFzU6KHAw""
  },
  {
    "{": ""      ""Video ID: dlzoy8agbMQ""
  },
  {
    "{": ""      ""Video ID: 8iHBQfP2tus""
  },
  {
    "{": ""      ""Video ID: yaAfYdOb6Ks""
  },
  {
    "{": ""      ""Video ID: CYCIgH504Bk""
  },
  {
    "{": ""      ""Video ID: Bk8pU6l-dws""
  },
  {
    "{": ""      ""Video ID: HWZ7rvDUm54""
  },
  {
    "{": ""      ""Video ID: RUcq7mGZ6Og""
  },
  {
    "{": ""      ""Video ID: qw_644oGgso""
  },
  {
    "{": ""      ""Video ID: JpzJySI5W_4""
  },
  {
    "{": ""      ""Video ID: 5HER8GZTGu4""
  },
  {
    "{": ""      ""Video ID: lyrUElIGSPI""
  },
  {
    "{": ""      ""Video ID: a69qj74Pc8Q""
  },
  {
    "{": ""      ""Video ID: kju-R2nPTU8""
  },
  {
    "{": ""      ""Video ID: PsAvt1ls7ZA""
  },
  {
    "{": ""      ""Video ID: 2gjEJAASf8c""
  },
  {
    "{": ""      ""Video ID: aUrlRWRxVww""
  },
  {
    "{": ""      ""Video ID: 4n2TTLe5aE0""
  },
  {
    "{": ""      ""Video ID: sEny47bVuv8""
  },
  {
    "{": ""      ""Video ID: tY8XsdzpeL0""
  },
  {
    "{": ""      ""Video ID: HQQo0gfBHq0""
  },
  {
    "{": ""      ""Video ID: 4vhtKlHVViI""
  },
  {
    "{": ""      ""Video ID: VrkgC6yFG0k""
  },
  {
    "{": ""      ""Video ID: KHx-V8l4bS4""
  },
  {
    "{": ""      ""Video ID: DrhtnuLYnNk""
  },
  {
    "{": ""      ""Video ID: CvtAvGvn8gk""
  },
  {
    "{": ""      ""Video ID: tt0q4C10YqY""
  },
  {
    "{": ""      ""Video ID: gJ5uGXpDiz0""
  },
  {
    "{": ""      ""Video ID: Fw_ZGjgS0W4""
  },
  {
    "{": ""      ""Video ID: W13Wj34Lpto""
  },
  {
    "{": ""      ""Video ID: Zi9GOvR3Ynw""
  },
  {
    "{": ""      ""Video ID: MOEUgbiBXMc""
  },
  {
    "{": ""      ""Video ID: 1FMqo_udPh4""
  },
  {
    "{": ""      ""Video ID: kYjBpJJCAjY""
  },
  {
    "{": ""      ""Video ID: LuaomKOim_M""
  },
  {
    "{": ""      ""Video ID: vBjsBLP1S5I""
  },
  {
    "{": ""      ""Video ID: yUTUgXJadDU""
  },
  {
    "{": ""      ""Video ID: 2KjeVu4nBJM""
  },
  {
    "{": ""      ""Video ID: vYCMIZOGHJA""
  },
  {
    "{": ""      ""Video ID: UJz9NDbM_y4""
  },
  {
    "{": ""      ""Video ID: e1FY4XSTLOs""
  },
  {
    "{": ""      ""Video ID: W6cC-R96ErI""
  },
  {
    "{": ""      ""Video ID: dqgSDf3OpqU""
  },
  {
    "{": ""      ""Video ID: Za4tA2ZXL-I""
  },
  {
    "{": ""      ""Video ID: t9NGMIBoF3w""
  },
  {
    "{": ""      ""Video ID: JCl3FuOh7J0""
  },
  {
    "{": ""      ""Video ID: qEUl5ZYZlys""
  },
  {
    "{": ""      ""Video ID: sV8qP0HUc4k""
  },
  {
    "{": ""      ""Video ID: f7bmF-VOt3s""
  },
  {
    "{": ""      ""Video ID: KSUIG0x9ReU""
  },
  {
    "{": ""      ""Video ID: V0AV27KXp94""
  },
  {
    "{": ""      ""Video ID: FWVuYqGx65U""
  },
  {
    "{": ""      ""Video ID: TwoioULjIhA""
  },
  {
    "{": ""      ""Video ID: 6FNhwHLCiG0""
  },
  {
    "{": ""      ""Video ID: L3rb_PBGUIk""
  },
  {
    "{": ""      ""Video ID: MEvjJJvGd0M""
  },
  {
    "{": ""      ""Video ID: AmN0U5s_fF8""
  },
  {
    "{": ""      ""Video ID: sef5kTbU9gE""
  },
  {
    "{": ""      ""Video ID: ek3wmlGB_yY""
  },
  {
    "{": ""      ""Video ID: bmS61uN4QpM""
  },
  {
    "{": ""      ""Video ID: YwgxiUbDGws""
  },
  {
    "{": ""      ""Video ID: MNB0QKLDubg""
  },
  {
    "{": ""      ""Video ID: hRTo-dtMAvQ""
  },
  {
    "{": ""      ""Video ID: YJCLsci2XHU""
  },
  {
    "{": ""      ""Video ID: 63bWYFGBTuE""
  },
  {
    "{": ""      ""Video ID: NbYl2SHdAq8""
  },
  {
    "{": ""      ""Video ID: NlbJ2q3MO-M""
  },
  {
    "{": ""      ""Video ID: 2lhlyErhre4""
  },
  {
    "{": ""      ""Video ID: yud34TCaI-s""
  },
  {
    "{": ""      ""Video ID: rYvZQSydQMM""
  },
  {
    "{": ""      ""Video ID: 0v2Z6IXIpLQ""
  },
  {
    "{": ""      ""Video ID: sJN-gPkB3b8""
  },
  {
    "{": ""      ""Video ID: K3LoN4r5kuo""
  },
  {
    "{": ""      ""Video ID: yqoFwZUp5vc""
  },
  {
    "{": ""      ""Video ID: hwqDxLJNucg""
  },
  {
    "{": ""      ""Video ID: gVs0BfCBuRg""
  },
  {
    "{": ""      ""Video ID: awQkJNVsgKM""
  },
  {
    "{": ""      ""Video ID: 370IOtsIJkQ""
  },
  {
    "{": ""      ""Video ID: us4jbRlrAaA""
  },
  {
    "{": ""      ""Video ID: GsfvWJoiNFg""
  },
  {
    "{": ""      ""Video ID: cIUej6VJzII""
  },
  {
    "{": ""      ""Video ID: F9wtAqXq7Sg""
  },
  {
    "{": ""      ""Video ID: vwX_ba8h-oc""
  },
  {
    "{": ""      ""Video ID: Ng81kIYgoro""
  },
  {
    "{": ""      ""Video ID: DILspQ82AK0""
  },
  {
    "{": ""      ""Video ID: UbVzb0yqZuk""
  },
  {
    "{": ""      ""Video ID: OCTVpPB7hEM""
  },
  {
    "{": ""      ""Video ID: dfrnoujs1gA""
  },
  {
    "{": ""      ""Video ID: hiPRGSZdITk""
  },
  {
    "{": ""      ""Video ID: 6DrXRIUlqaY""
  },
  {
    "{": ""      ""Video ID: 0bCODt_fi9I""
  },
  {
    "{": ""      ""Video ID: JSkd0xrhcQ8""
  },
  {
    "{": ""      ""Video ID: M79oFa5a-W4""
  },
  {
    "{": ""      ""Video ID: WrlWqnWd-sY""
  },
  {
    "{": ""      ""Video ID: 2lP1gbKe4Sk""
  },
  {
    "{": ""      ""Video ID: iPYIEu_mink""
  },
  {
    "{": ""      ""Video ID: ErOmu7VdVO4""
  },
  {
    "{": ""      ""Video ID: HeaMsmVms6c""
  },
  {
    "{": ""      ""Video ID: 3gWgQh5oq74""
  },
  {
    "{": ""      ""Video ID: DRPRzDWSL5w""
  },
  {
    "{": ""      ""Video ID: LLZ0WpqHNSk""
  },
  {
    "{": ""      ""Video ID: 7UL1_Xv_5_Q""
  },
  {
    "{": ""      ""Video ID: SEJLYFKJ9oI""
  },
  {
    "{": ""      ""Video ID: XqzdPG2V5ns""
  },
  {
    "{": ""      ""Video ID: 8kq-_1iYduk""
  },
  {
    "{": ""      ""Video ID: RrmtO_JIf0Q""
  },
  {
    "{": ""      ""Video ID: xNAMzDy3rSQ""
  },
  {
    "{": ""      ""Video ID: 9L50shyUoQU""
  },
  {
    "{": ""      ""Video ID: 8Im697880oo""
  },
  {
    "{": ""      ""Video ID: IQR--GFNPQo""
  },
  {
    "{": ""      ""Video ID: OVHKZxfKkMY""
  },
  {
    "{": ""      ""Video ID: 6TMnApn8LIM""
  },
  {
    "{": ""      ""Video ID: BVYdtuxqePk""
  },
  {
    "{": ""      ""Video ID: IemaxWMuOdA""
  },
  {
    "{": ""      ""Video ID: WpgGCeB2Hi4""
  },
  {
    "{": ""      ""Video ID: 3w2VKDurLV0""
  },
  {
    "{": ""      ""Video ID: uRooGK5qAWw""
  },
  {
    "{": ""      ""Video ID: 6NeQ1h6lzLI""
  },
  {
    "{": ""      ""Video ID: ix4HUiKvKJY""
  },
  {
    "{": ""      ""Video ID: FeBhGYQFXkQ""
  },
  {
    "{": ""      ""Video ID: 64rlAC1X5Y4""
  },
  {
    "{": ""      ""Video ID: zFWuVYpOi1c""
  },
  {
    "{": ""      ""Video ID: 39BlxD96gXw""
  },
  {
    "{": ""      ""Video ID: 16RJ_M7yiB8""
  },
  {
    "{": ""      ""Video ID: lmoL2NRSzvQ""
  },
  {
    "{": ""      ""Video ID: dsy3K20gr58""
  },
  {
    "{": ""      ""Video ID: FnYykWL5HJ0""
  },
  {
    "{": ""      ""Video ID: eZcwU4659Cc""
  },
  {
    "{": ""      ""Video ID: eMbFcOW6KYc""
  },
  {
    "{": ""      ""Video ID: -YofhJs-c9M""
  },
  {
    "{": ""      ""Video ID: njo7QI0ySAU""
  },
  {
    "{": ""      ""Video ID: i454htsPDik""
  },
  {
    "{": ""      ""Video ID: EDCji_2TF40""
  },
  {
    "{": ""      ""Video ID: kZscxAZs8c8""
  },
  {
    "{": ""      ""Video ID: It2uwV3X_Yc""
  },
  {
    "{": ""      ""Video ID: VLO-90w-6kM""
  },
  {
    "{": ""      ""Video ID: rwCwtmnD_zc""
  },
  {
    "{": ""      ""Video ID: b3pEYpXeAS4""
  },
  {
    "{": ""      ""Video ID: s7-ixwkzfNs""
  },
  {
    "{": ""      ""Video ID: TY51MmZ6NaM""
  },
  {
    "{": ""      ""Video ID: qBB5n5Ikryc""
  },
  {
    "{": ""      ""Video ID: JKcCKeGf0AY""
  },
  {
    "{": ""      ""Video ID: nNnLhnqGZ0A""
  },
  {
    "{": ""      ""Video ID: DJhbshFkUiU""
  },
  {
    "{": ""      ""Video ID: GSxiPpEmEaA""
  },
  {
    "{": ""      ""Video ID: 6k0Lcb4sk6c""
  },
  {
    "{": ""      ""Video ID: KNkNJU5Uj7s""
  },
  {
    "{": ""      ""Video ID: aeG8rHuCIDQ""
  },
  {
    "{": ""      ""Video ID: QPX7H9NPwIQ""
  },
  {
    "{": ""      ""Video ID: yDZfKxjK-g0""
  },
  {
    "{": ""      ""Video ID: EwaBKIHHR14""
  },
  {
    "{": ""      ""Video ID: P3DjThC3Nuk""
  },
  {
    "{": ""      ""Video ID: CSmo_AJR-i4""
  },
  {
    "{": ""      ""Video ID: phbZ6SdI2kY""
  },
  {
    "{": ""      ""Video ID: v1d0DE-UCTA""
  },
  {
    "{": ""      ""Video ID: FgyHea6Vd0Q""
  },
  {
    "{": ""      ""Video ID: cWz-BXHDfjc""
  },
  {
    "{": ""      ""Video ID: UEqAlCV29no""
  },
  {
    "{": ""      ""Video ID: itU8VcAm3II""
  },
  {
    "{": ""      ""Video ID: kArNs8JUMiA""
  },
  {
    "{": ""      ""Video ID: HYWLRo1oxzc""
  },
  {
    "{": ""      ""Video ID: 65QXPZfIQco""
  },
  {
    "{": ""      ""Video ID: 0iQAUKR2j54""
  },
  {
    "{": ""      ""Video ID: q0ufQh2Btic""
  },
  {
    "{": ""      ""Video ID: XvPU-QiN9F8""
  },
  {
    "{": ""      ""Video ID: Yf2Ysz4b9dQ""
  },
  {
    "{": ""      ""Video ID: bWmqrId3Q3k""
  },
  {
    "{": ""      ""Video ID: 2DnKvfIykDg""
  },
  {
    "{": ""      ""Video ID: G_2nbKRk318""
  },
  {
    "{": ""      ""Video ID: wtLHpVWdErY""
  },
  {
    "{": ""      ""Video ID: Z37ozVt_XvA""
  },
  {
    "{": ""      ""Video ID: IzjR_rgR7KE""
  },
  {
    "{": ""      ""Video ID: XuZPqiJN9h4""
  },
  {
    "{": ""      ""Video ID: S8rDntTstjs""
  },
  {
    "{": ""      ""Video ID: mXO6YCzZ4Ss""
  },
  {
    "{": ""      ""Video ID: 7A3Bjfyxk7k""
  },
  {
    "{": ""      ""Video ID: Y47r6gBUv80""
  },
  {
    "{": ""      ""Video ID: Ru345-PnEaY""
  },
  {
    "{": ""      ""Video ID: flQNoq3kkrI""
  },
  {
    "{": ""      ""Video ID: Bbt3DjmN--4""
  },
  {
    "{": ""      ""Video ID: 3_JKYEa0keg""
  },
  {
    "{": ""      ""Video ID: 2d_oDuNcjDg""
  },
  {
    "{": ""      ""Video ID: eEzv7F8op54""
  },
  {
    "{": ""      ""Video ID: qSc_n2jTSp8""
  },
  {
    "{": ""      ""Video ID: o72GSjLZyAg""
  },
  {
    "{": ""      ""Video ID: AB30Z79Ka-0""
  },
  {
    "{": ""      ""Video ID: p-wkVuQNhMA""
  },
  {
    "{": ""      ""Video ID: wMF7CrK6kVQ""
  },
  {
    "{": ""      ""Video ID: AIxcdhG2mpU""
  },
  {
    "{": ""      ""Video ID: 3lC7MPZYFBI""
  },
  {
    "{": ""      ""Video ID: bcdin5kjdOw""
  },
  {
    "{": ""      ""Video ID: ED2_y78k4G0""
  },
  {
    "{": ""      ""Video ID: pgjFqCD-EMM""
  },
  {
    "{": ""      ""Video ID: -lox96iS7hU""
  },
  {
    "{": ""      ""Video ID: 4hd0iBmBhrA""
  },
  {
    "{": ""      ""Video ID: IWfIhFhelm8""
  },
  {
    "{": ""      ""Video ID: MaK1YBiYrSE""
  },
  {
    "{": ""      ""Video ID: wFncKFaNAB8""
  },
  {
    "{": ""      ""Video ID: G7d_e9lrcZ8""
  },
  {
    "{": ""      ""Video ID: BD8z4q2lMCU""
  },
  {
    "{": ""      ""Video ID: FG2PUZoukfA""
  },
  {
    "{": ""      ""Video ID: cziN3gt-hic""
  },
  {
    "{": ""      ""Video ID: Tts2uTWt6e8""
  },
  {
    "{": ""      ""Video ID: IQUMCGXq4yM""
  },
  {
    "{": ""      ""Video ID: XaxdUPNYj2s""
  },
  {
    "{": ""      ""Video ID: JsFevx_2U5E""
  },
  {
    "{": ""      ""Video ID: 75kAWaLPEKg""
  },
  {
    "{": ""      ""Video ID: nPyrcrVGL4o""
  },
  {
    "{": ""      ""Video ID: CA7jHaowNME""
  },
  {
    "{": ""      ""Video ID: ENA0vxLwoq4""
  },
  {
    "{": ""      ""Video ID: ld_TGAq3NF8""
  },
  {
    "{": ""      ""Video ID: ZHqxLrbTwVA""
  },
  {
    "{": ""      ""Video ID: yY6u-sXKGSo""
  },
  {
    "{": ""      ""Video ID: ivREYgodK4I""
  },
  {
    "{": ""      ""Video ID: zsjcxM8O5_g""
  },
  {
    "{": ""      ""Video ID: 8GzRWSof8uQ""
  },
  {
    "{": ""      ""Video ID: nWyygiyPbdA""
  },
  {
    "{": ""      ""Video ID: PoxlzPGIPt4""
  },
  {
    "{": ""      ""Video ID: HXkVJtz0bNI""
  },
  {
    "{": ""      ""Video ID: 44hNHiVPTUI""
  },
  {
    "{": ""      ""Video ID: K_F48oaOskI""
  },
  {
    "{": ""      ""Video ID: ur4hKqTikqM""
  },
  {
    "{": ""      ""Video ID: xUG8T0ceeRs""
  },
  {
    "{": ""      ""Video ID: AdlWmQbjxuE""
  },
  {
    "{": ""      ""Video ID: UydCZJeQPPQ""
  },
  {
    "{": ""      ""Video ID: d5YQlxJoEPY""
  },
  {
    "{": ""      ""Video ID: jBvD4VVaGZI""
  },
  {
    "{": ""      ""Video ID: RuqNWG9sbuE""
  },
  {
    "{": ""      ""Video ID: IGI0eUwPTZ0""
  },
  {
    "{": ""      ""Video ID: cSMECBE0Rzk""
  },
  {
    "{": ""      ""Video ID: X9-NqDyhnAs""
  },
  {
    "{": ""      ""Video ID: kRhzU-ZNvVM""
  },
  {
    "{": ""      ""Video ID: bg08RnRhXpw""
  },
  {
    "{": ""      ""Video ID: BPU8w7Bxc0A""
  },
  {
    "{": ""      ""Video ID: cy-fD78zyvI""
  },
  {
    "{": ""      ""Video ID: yGGOiv7sA4w""
  },
  {
    "{": ""      ""Video ID: -DNWIBhmYPg""
  },
  {
    "{": ""      ""Video ID: iHjAnesrbu8""
  },
  {
    "{": ""      ""Video ID: WmcC_QAzI_4""
  },
  {
    "{": ""      ""Video ID: ZfX4c3jQj5I""
  },
  {
    "{": ""      ""Video ID: c2CQfRai6yo""
  },
  {
    "{": ""      ""Video ID: ZlcETXgCvC4""
  },
  {
    "{": ""      ""Video ID: AaXG402Kejg""
  },
  {
    "{": ""      ""Video ID: XQWqGpxWgus""
  },
  {
    "{": ""      ""Video ID: PhZzh83C0iM""
  },
  {
    "{": ""      ""Video ID: qocBtcQ1g5Q""
  },
  {
    "{": ""      ""Video ID: Njceup3ojTw""
  },
  {
    "{": ""      ""Video ID: _RArK7yT69E""
  },
  {
    "{": ""      ""Video ID: bFVsSowgm9I""
  },
  {
    "{": ""      ""Video ID: yYvNFmMr9qs""
  },
  {
    "{": ""      ""Video ID: jjQfn8QN0G8""
  },
  {
    "{": ""      ""Video ID: HUYNQbkTagM""
  },
  {
    "{": ""      ""Video ID: URHs6nl5T8g""
  },
  {
    "{": ""      ""Video ID: Y7WI5sdGnhk""
  },
  {
    "{": ""      ""Video ID: 4tdNxTV9i2c""
  },
  {
    "{": ""      ""Video ID: QT2PtRGYehA""
  },
  {
    "{": ""      ""Video ID: MYDWfUkcnmc""
  },
  {
    "{": ""      ""Video ID: sGH7L-Z8Wzo""
  },
  {
    "{": ""      ""Video ID: x8h-5bqEWMI""
  },
  {
    "{": ""      ""Video ID: Jk05NZUqVZo""
  },
  {
    "{": ""      ""Video ID: x1xzOIbuiQg""
  },
  {
    "{": ""      ""Video ID: CevekZU7130""
  },
  {
    "{": ""      ""Video ID: UqwzPAHXSXg""
  },
  {
    "{": ""      ""Video ID: mXQFqlVMrrc""
  },
  {
    "{": ""      ""Video ID: CZLGsTmB3sk""
  },
  {
    "{": ""      ""Video ID: 7gjbxyaOOTM""
  },
  {
    "{": ""      ""Video ID: bZWUSCkXK2o""
  },
  {
    "{": ""      ""Video ID: Z8OXwfBxGU0""
  },
  {
    "{": ""      ""Video ID: 5sJLRVDIn3M""
  },
  {
    "{": ""      ""Video ID: 5sZcTjOmsAA""
  },
  {
    "{": ""      ""Video ID: JswiiGk8u2k""
  },
  {
    "{": ""      ""Video ID: OoEp0zTLVhs""
  },
  {
    "{": ""      ""Video ID: xeoxxpVUQgs""
  },
  {
    "{": ""      ""Video ID: gaBjdLQ0LJ0""
  },
  {
    "{": ""      ""Video ID: TW0Auzgamhs""
  },
  {
    "{": ""      ""Video ID: PPsDO0Qc1-M""
  },
  {
    "{": ""      ""Video ID: yXCxzzXv5OI""
  },
  {
    "{": ""      ""Video ID: Zvlffu1cess""
  },
  {
    "{": ""      ""Video ID: jLYzg1w2hKE""
  },
  {
    "{": ""      ""Video ID: G6Shlxf0LHM""
  },
  {
    "{": ""      ""Video ID: j0ZmwrfPTlg""
  },
  {
    "{": ""      ""Video ID: 8Owco8RovDA""
  },
  {
    "{": ""      ""Video ID: BxUq_zzvAaA""
  },
  {
    "{": ""      ""Video ID: gLeDXvcwW9c""
  },
  {
    "{": ""      ""Video ID: uxj8ypD7pdA""
  },
  {
    "{": ""      ""Video ID: -_hVDqIwQRs""
  },
  {
    "{": ""      ""Video ID: JTzLg9QKyPg""
  },
  {
    "{": ""      ""Video ID: GprUu55Z17Q""
  },
  {
    "{": ""      ""Video ID: 7wvAiwdgbXw""
  },
  {
    "{": ""      ""Video ID: Pht5ZNjQJPc""
  },
  {
    "{": ""      ""Video ID: _aCmWoVrHDc""
  },
  {
    "{": ""      ""Video ID: bBpQ3hctd2w""
  },
  {
    "{": ""      ""Video ID: N1_S7Orp_9M""
  },
  {
    "{": ""      ""Video ID: hL2znOJ3q7c""
  },
  {
    "{": ""      ""Video ID: GyQPaj5FHRg""
  },
  {
    "{": ""      ""Video ID: xvIi2phQWXI""
  },
  {
    "{": ""      ""Video ID: OTE4JYzea7s""
  },
  {
    "{": ""      ""Video ID: HUdClEsWxUg""
  },
  {
    "{": ""      ""Video ID: Ot4EaeDgyxo""
  },
  {
    "{": ""      ""Video ID: QY9iTUaS97g""
  },
  {
    "{": ""      ""Video ID: anLFNY1hfyE""
  },
  {
    "{": ""      ""Video ID: EN7KfJ7ZKXc""
  },
  {
    "{": ""      ""Video ID: pkXPbEb4NyI""
  },
  {
    "{": ""      ""Video ID: oMaTZFCLbq0""
  },
  {
    "{": ""      ""Video ID: 5bqpIlZhhYQ""
  },
  {
    "{": ""      ""Video ID: 7j-C7hsEmz8""
  },
  {
    "{": ""      ""Video ID: iABEgqlRm20""
  },
  {
    "{": ""      ""Video ID: McWg54PIsE8""
  },
  {
    "{": ""      ""Video ID: sXNFV7x1_28""
  },
  {
    "{": ""      ""Video ID: 1PrEcJLiUtE""
  },
  {
    "{": ""      ""Video ID: Avs43Ky7mCw""
  },
  {
    "{": ""      ""Video ID: n1MNLr5AoJU""
  },
  {
    "{": ""      ""Video ID: 4LDab7f_8NE""
  },
  {
    "{": ""      ""Video ID: zh0abDcrXas""
  },
  {
    "{": ""      ""Video ID: jf0BLuSeOWU""
  },
  {
    "{": ""      ""Video ID: S55E-8RP8X4""
  },
  {
    "{": ""      ""Video ID: Z5SxgNnNA18""
  },
  {
    "{": ""      ""Video ID: xpt_TEfN2RE""
  },
  {
    "{": ""      ""Video ID: DbYOH7v1gdA""
  },
  {
    "{": ""      ""Video ID: TGvDYKtHyMw""
  },
  {
    "{": ""      ""Video ID: rUVRTgCY99w""
  },
  {
    "{": ""      ""Video ID: wQbnBru0JU0""
  },
  {
    "{": ""      ""Video ID: anYryOIooF4""
  },
  {
    "{": ""      ""Video ID: cy5eAFAIcGk""
  },
  {
    "{": ""      ""Video ID: UW9J0KEP4uQ""
  },
  {
    "{": ""      ""Video ID: 0245oE7vPVM""
  },
  {
    "{": ""      ""Video ID: _Jql8XB7zno""
  },
  {
    "{": ""      ""Video ID: QgSj5Wt1Ap4""
  },
  {
    "{": ""      ""Video ID: oR2IZa7xeXk""
  },
  {
    "{": ""      ""Video ID: acJuET8IY40""
  },
  {
    "{": ""      ""Video ID: FhGEmoIZi8M""
  },
  {
    "{": ""      ""Video ID: QX6CyIwGYoM""
  },
  {
    "{": ""      ""Video ID: na3iCSTtM8k""
  },
  {
    "{": ""      ""Video ID: qTPNECnEHbs""
  },
  {
    "{": ""      ""Video ID: PqAjIb7QZtY""
  },
  {
    "{": ""      ""Video ID: FFLTCG9oNA4""
  },
  {
    "{": ""      ""Video ID: RsYi8OPX2X4""
  },
  {
    "{": ""      ""Video ID: 3xwesSyqnJU""
  },
  {
    "{": ""      ""Video ID: dQI5q1zAeIY""
  },
  {
    "{": ""      ""Video ID: 72c8YUNusEo""
  },
  {
    "{": ""      ""Video ID: vB1pwmGMie4""
  },
  {
    "{": ""      ""Video ID: fRphSZKeAgc""
  },
  {
    "{": ""      ""Video ID: NdpHX1qNk7E""
  },
  {
    "{": ""      ""Video ID: NNavV4I1f9o""
  },
  {
    "{": ""      ""Video ID: ikzD08m_ccs""
  },
  {
    "{": ""      ""Video ID: arW3TFrAL3A""
  },
  {
    "{": ""      ""Video ID: RzxLFZVQI4I""
  },
  {
    "{": ""      ""Video ID: DwjPgvNnZsM""
  },
  {
    "{": ""      ""Video ID: JoyG5EXh0cI""
  },
  {
    "{": ""      ""Video ID: t8-Y2uKlDo4""
  },
  {
    "{": ""      ""Video ID: kjWIz698kks""
  },
  {
    "{": ""      ""Video ID: RmMI-abhyi8""
  },
  {
    "{": ""      ""Video ID: 9yyPvr9MgOM""
  },
  {
    "{": ""      ""Video ID: SuasarblOO0""
  },
  {
    "{": ""      ""Video ID: aAOzrisckBE""
  },
  {
    "{": ""      ""Video ID: U4tGK-kfTRc""
  },
  {
    "{": ""      ""Video ID: T6yCF5XW6JE""
  },
  {
    "{": ""      ""Video ID: sbMCAbC4Klo""
  },
  {
    "{": ""      ""Video ID: VWYuV82PMAk""
  },
  {
    "{": ""      ""Video ID: ax0JxKeCJEk""
  },
  {
    "{": ""      ""Video ID: Bsxerdftpik""
  },
  {
    "{": ""      ""Video ID: nHhfhdLdIsY""
  },
  {
    "{": ""      ""Video ID: NpKS8JlrfdI""
  },
  {
    "{": ""      ""Video ID: EOzWVnkn24U""
  },
  {
    "{": ""      ""Video ID: kn2bA7a2eE4""
  },
  {
    "{": ""      ""Video ID: rHo7BHo3CJQ""
  },
  {
    "{": ""      ""Video ID: lYdBN9M8lDE""
  },
  {
    "{": ""      ""Video ID: psDEy7dxTO4""
  },
  {
    "{": ""      ""Video ID: 6Ga1_SjxQgI""
  },
  {
    "{": ""      ""Video ID: CwVYncsjeqg""
  },
  {
    "{": ""      ""Video ID: JKD46KkurfU""
  },
  {
    "{": ""      ""Video ID: viIra7FQiAQ""
  },
  {
    "{": ""      ""Video ID: DvmtbH6W8UM""
  },
  {
    "{": ""      ""Video ID: o85pu9efjj0""
  },
  {
    "{": ""      ""Video ID: zB5LB0xAPoo""
  },
  {
    "{": ""      ""Video ID: PBIpmvQCeE4""
  },
  {
    "{": ""      ""Video ID: kxKzIfzUmqI""
  },
  {
    "{": ""      ""Video ID: 02BXFHaVuaA""
  },
  {
    "{": ""      ""Video ID: xUvGTobmofQ""
  },
  {
    "{": ""      ""Video ID: 6IXGRvPBZ9E""
  },
  {
    "{": ""      ""Video ID: E0LbW96UXZw""
  },
  {
    "{": ""      ""Video ID: J-_Tr0l9F-Y""
  },
  {
    "{": ""      ""Video ID: c-i-Gbhdr10""
  },
  {
    "{": ""      ""Video ID: wcetyPoe_T0""
  },
  {
    "{": ""      ""Video ID: mySDeYuJn2M""
  },
  {
    "{": ""      ""Video ID: BxmFTmX1CIs""
  },
  {
    "{": ""      ""Video ID: xB4GXdoA9Qk""
  },
  {
    "{": ""      ""Video ID: ZTQolymKmDA""
  },
  {
    "{": ""      ""Video ID: RjpElpEKIuA""
  },
  {
    "{": ""      ""Video ID: ph4YXz3-aXU""
  },
  {
    "{": ""      ""Video ID: Pp4eEwmFsmc""
  },
  {
    "{": ""      ""Video ID: U8HRPDMiTMU""
  },
  {
    "{": ""      ""Video ID: Go2GTKsjFtg""
  },
  {
    "{": ""      ""Video ID: Dp2dYy9NHtU""
  },
  {
    "{": ""      ""Video ID: 4dQpZaggJD8""
  },
  {
    "{": ""      ""Video ID: jhb5o3tfwv0""
  },
  {
    "{": ""      ""Video ID: PaQISfBteCc""
  },
  {
    "{": ""      ""Video ID: 0RLJ40Kj7xY""
  },
  {
    "{": ""      ""Video ID: 9Zwh4G3t-vI""
  },
  {
    "{": ""      ""Video ID: 6CRFHuJg6Ao""
  },
  {
    "{": ""      ""Video ID: KqQik47Upg0""
  },
  {
    "{": ""      ""Video ID: gwj3yoXa5aU""
  },
  {
    "{": ""      ""Video ID: SvuWvAy5eaM""
  },
  {
    "{": ""      ""Video ID: SXo4qmgF-nY""
  },
  {
    "{": ""      ""Video ID: THy0r3_2suE""
  },
  {
    "{": ""      ""Video ID: NAcyCv2AMys""
  },
  {
    "{": ""      ""Video ID: m_bsRFYog-k""
  },
  {
    "{": ""      ""Video ID: WOHwjsxV3C4""
  },
  {
    "{": ""      ""Video ID: IJIdjGI9Ys8""
  },
  {
    "{": ""      ""Video ID: _zqr6zOfTFo""
  },
  {
    "{": ""      ""Video ID: cn6St6DKq88""
  },
  {
    "{": ""      ""Video ID: 7JXNQqyinDI""
  },
  {
    "{": ""      ""Video ID: n5RfFIai-Qo""
  },
  {
    "{": ""      ""Video ID: vAai8P48eyo""
  },
  {
    "{": ""      ""Video ID: W3jAK3r9vLc""
  },
  {
    "{": ""      ""Video ID: _-6TdlvsYP4""
  },
  {
    "{": ""      ""Video ID: 0of-P_ETVVw""
  },
  {
    "{": ""      ""Video ID: Q2KUjVOGp7g""
  },
  {
    "{": ""      ""Video ID: WR7KSwjJajw""
  },
  {
    "{": ""      ""Video ID: Zf-e5ZDfxfU""
  },
  {
    "{": ""      ""Video ID: rOjLn9Y5NMg""
  },
  {
    "{": ""      ""Video ID: 7RBelz8BgX0""
  },
  {
    "{": ""      ""Video ID: L4PthyDuFbk""
  },
  {
    "{": ""      ""Video ID: bsGEWHNJ3s8""
  },
  {
    "{": ""      ""Video ID: P5GaKLDOKZI""
  },
  {
    "{": ""      ""Video ID: rRR8lqlpU68""
  },
  {
    "{": ""      ""Video ID: lCgZ5uXi9z4""
  },
  {
    "{": ""      ""Video ID: bG_Vbh8arNM""
  },
  {
    "{": ""      ""Video ID: wt-x2cNcfNs""
  },
  {
    "{": ""      ""Video ID: V35BNwfeDos""
  },
  {
    "{": ""      ""Video ID: OcjkX8fB4MI""
  },
  {
    "{": ""      ""Video ID: bIZTl5536RU""
  },
  {
    "{": ""      ""Video ID: W3FRB0YX3nc""
  },
  {
    "{": ""      ""Video ID: oWjypof2Q5c""
  },
  {
    "{": ""      ""Video ID: GXVGWiVn1XU""
  },
  {
    "{": ""      ""Video ID: 2K1Dhyh9jgU""
  },
  {
    "{": ""      ""Video ID: h_-CRSHurq4""
  },
  {
    "{": ""      ""Video ID: YgB6mFmYEcM""
  },
  {
    "{": ""      ""Video ID: 9pj81ICUr3M""
  },
  {
    "{": ""      ""Video ID: APTBYQWsnrA""
  },
  {
    "{": ""      ""Video ID: NsN_JJ6aT-0""
  },
  {
    "{": ""      ""Video ID: 4FzgdJ2dMas""
  },
  {
    "{": ""      ""Video ID: PCHh1Z1BK9o""
  },
  {
    "{": ""      ""Video ID: v1NTbtAHv-s""
  },
  {
    "{": ""      ""Video ID: v3mSVMXqMCw""
  },
  {
    "{": ""      ""Video ID: r7ultFR_YSE""
  },
  {
    "{": ""      ""Video ID: PPMfnik0nHk""
  },
  {
    "{": ""      ""Video ID: gYjaBf3oeNw""
  },
  {
    "{": ""      ""Video ID: L9tlQEEyYOU""
  },
  {
    "{": ""      ""Video ID: PZWtC0OUu_g""
  },
  {
    "{": ""      ""Video ID: bAL51BvuPzM""
  },
  {
    "{": ""      ""Video ID: CLlJ8AtHoek""
  },
  {
    "{": ""      ""Video ID: SzaitnlSx7w""
  },
  {
    "{": ""      ""Video ID: __r0gwxzeVE""
  },
  {
    "{": ""      ""Video ID: SOseVKDZi7c""
  },
  {
    "{": ""      ""Video ID: uqiadqN5tSQ""
  },
  {
    "{": ""      ""Video ID: sok6hFCWHgU""
  },
  {
    "{": ""      ""Video ID: uc9nUi2IMQs""
  },
  {
    "{": ""      ""Video ID: SVo4Xiz8hjA""
  },
  {
    "{": ""      ""Video ID: NEq2jpgDIF4""
  },
  {
    "{": ""      ""Video ID: NZG6U51AQ70""
  },
  {
    "{": ""      ""Video ID: NoGDFOebAsw""
  },
  {
    "{": ""      ""Video ID: Z8NLbRL860U""
  },
  {
    "{": ""      ""Video ID: XfPAjUvvnIc""
  },
  {
    "{": ""      ""Video ID: L0iQoPzCkYo""
  },
  {
    "{": ""      ""Video ID: 33RmcuajnCk""
  },
  {
    "{": ""      ""Video ID: X6-cf69q_OI""
  },
  {
    "{": ""      ""Video ID: qQkqCCRAa38""
  },
  {
    "{": ""      ""Video ID: xZA6g29tivo""
  },
  {
    "{": ""      ""Video ID: Va8fA8BYEYk""
  },
  {
    "{": ""      ""Video ID: zMCuRkGA9hg""
  },
  {
    "{": ""      ""Video ID: z-7EKSGPaAU""
  },
  {
    "{": ""      ""Video ID: wif-fHG-Ej0""
  },
  {
    "{": ""      ""Video ID: iwfsFtpACFw""
  },
  {
    "{": ""      ""Video ID: Lz28kJZFU40""
  },
  {
    "{": ""      ""Video ID: 8dxl2qXPPms""
  },
  {
    "{": ""      ""Video ID: mdHkpJIkXUg""
  },
  {
    "{": ""      ""Video ID: A0mXGy539Rg""
  },
  {
    "{": ""      ""Video ID: cWJWb1MnA7c""
  },
  {
    "{": ""      ""Video ID: xlWcnWj8cxQ""
  },
  {
    "{": ""      ""Video ID: ic99s47DnSw""
  },
  {
    "{": ""      ""Video ID: eIyXsdJuvrs""
  },
  {
    "{": ""      ""Video ID: 78ChatsRe6Y""
  },
  {
    "{": ""      ""Video ID: fNmHXx0KX5g""
  },
  {
    "{": ""      ""Video ID: tURJAK3qz4o""
  },
  {
    "{": ""      ""Video ID: vdWVF_xzqWc""
  },
  {
    "{": ""      ""Video ID: N8HONbE7q58""
  },
  {
    "{": ""      ""Video ID: 2BSlRYeVPWc""
  },
  {
    "{": ""      ""Video ID: fjP5rdXvlIg""
  },
  {
    "{": ""      ""Video ID: IGvxT12WWgA""
  },
  {
    "{": ""      ""Video ID: eZX_IKOBiwo""
  },
  {
    "{": ""      ""Video ID: S8sc3c_WyMg""
  },
  {
    "{": ""      ""Video ID: 7a2PaTECVSk""
  },
  {
    "{": ""      ""Video ID: _yd5WreHxPg""
  },
  {
    "{": ""      ""Video ID: r_J9_oMl3VM""
  },
  {
    "{": ""      ""Video ID: UFUd4G9DiK0""
  },
  {
    "{": ""      ""Video ID: Etx7HXOuvBI""
  },
  {
    "{": ""      ""Video ID: GKxOmJV0rwQ""
  },
  {
    "{": ""      ""Video ID: U29uxfI15VA""
  },
  {
    "{": ""      ""Video ID: M59vV9HFJ_Y""
  },
  {
    "{": ""      ""Video ID: k8pDe2sire0""
  },
  {
    "{": ""      ""Video ID: U3bEzBAreRg""
  },
  {
    "{": ""      ""Video ID: ygqoRt3Rosk""
  },
  {
    "{": ""      ""Video ID: 6XjMQjzhtMU""
  },
  {
    "{": ""      ""Video ID: SIFr4Gx2pMU""
  },
  {
    "{": ""      ""Video ID: jBFxRXziy44""
  },
  {
    "{": ""      ""Video ID: KaX7DGSO31s""
  },
  {
    "{": ""      ""Video ID: wDYSL8EGEDk""
  },
  {
    "{": ""      ""Video ID: UshThfrrJ5o""
  },
  {
    "{": ""      ""Video ID: KbWpOROU5js""
  },
  {
    "{": ""      ""Video ID: cfkrohugBR4""
  },
  {
    "{": ""      ""Video ID: 7DD-Ctn1p5U""
  },
  {
    "{": ""      ""Video ID: 0F3lt9hlnOY""
  },
  {
    "{": ""      ""Video ID: CCobegwdt3o""
  },
  {
    "{": ""      ""Video ID: ZJSN5V72w7s""
  },
  {
    "{": ""      ""Video ID: RZS7cMbxkFs""
  },
  {
    "{": ""      ""Video ID: sygw0l_FcsQ""
  },
  {
    "{": ""      ""Video ID: OF0EMnruqzY""
  },
  {
    "{": ""      ""Video ID: GkrWqpymXLY""
  },
  {
    "{": ""      ""Video ID: 93ubRaUm2J0""
  },
  {
    "{": ""      ""Video ID: ZiOuHnbd8xc""
  },
  {
    "{": ""      ""Video ID: Bj4owyUqoIg""
  },
  {
    "{": ""      ""Video ID: BmuFY52arhM""
  },
  {
    "{": ""      ""Video ID: JDYI7-tp5GY""
  },
  {
    "{": ""      ""Video ID: D1vjbtzhqUE""
  },
  {
    "{": ""      ""Video ID: ld6FTy9c7ho""
  },
  {
    "{": ""      ""Video ID: _OpgJ2uNTck""
  },
  {
    "{": ""      ""Video ID: NcdNV1pWdT8""
  },
  {
    "{": ""      ""Video ID: Y9KC7uhMY9s""
  },
  {
    "{": ""      ""Video ID: rx_Wl-bTM9U""
  },
  {
    "{": ""      ""Video ID: 7BcbrtVQyzk""
  },
  {
    "{": ""      ""Video ID: jGoyUxgwNr4""
  },
  {
    "{": ""      ""Video ID: B0Ydzn8RrEA""
  },
  {
    "{": ""      ""Video ID: K51JAN_dpbM""
  },
  {
    "{": ""      ""Video ID: deoJUBW9CI8""
  },
  {
    "{": ""      ""Video ID: 9_QWEKRV9Nc""
  },
  {
    "{": ""      ""Video ID: CLuyIPfNGKk""
  },
  {
    "{": ""      ""Video ID: 9uSyEhP9Zuw""
  },
  {
    "{": ""      ""Video ID: wp0eCsI3Krg""
  },
  {
    "{": ""      ""Video ID: KEEi8LKNcqo""
  },
  {
    "{": ""      ""Video ID: jbJzdBLkDxY""
  },
  {
    "{": ""      ""Video ID: wLOGVpfSBtk""
  },
  {
    "{": ""      ""Video ID: TUUe2AalOq8""
  },
  {
    "{": ""      ""Video ID: s4FYXqhAFaM""
  },
  {
    "{": ""      ""Video ID: bV2IGo1KS2Q""
  },
  {
    "{": ""      ""Video ID: kOdgaiMRxVo""
  },
  {
    "{": ""      ""Video ID: IihISRIgdfI""
  },
  {
    "{": ""      ""Video ID: pw9uM80mVBI""
  },
  {
    "{": ""      ""Video ID: M-3QMYxDD1M""
  },
  {
    "{": ""      ""Video ID: 9kiiBkrHtvs""
  },
  {
    "{": ""      ""Video ID: wgft_Mts6B0""
  },
  {
    "{": ""      ""Video ID: vy2LI6y5rDI""
  },
  {
    "{": ""      ""Video ID: stEwegih5rM""
  },
  {
    "{": ""      ""Video ID: MmPL6mh6-Cg""
  },
  {
    "{": ""      ""Video ID: L_KlA133Vzg""
  },
  {
    "{": ""      ""Video ID: XowQ0Fu0jk4""
  },
  {
    "{": ""      ""Video ID: NmSJEJM3IYQ""
  },
  {
    "{": ""      ""Video ID: 8H709v1h4Os""
  },
  {
    "{": ""      ""Video ID: VTaU53lPPpM""
  },
  {
    "{": ""      ""Video ID: AKuCxcz1lUQ""
  },
  {
    "{": ""      ""Video ID: BjMt0V6Q6dU""
  },
  {
    "{": ""      ""Video ID: neZymKLzFAU""
  },
  {
    "{": ""      ""Video ID: ZrHpgOt19mA""
  },
  {
    "{": ""      ""Video ID: xOMRScN3Hlw""
  },
  {
    "{": ""      ""Video ID: STyEOzoUALI""
  },
  {
    "{": ""      ""Video ID: t09J35D2QD0""
  },
  {
    "{": ""      ""Video ID: WyEKh-C0-uE""
  },
  {
    "{": ""      ""Video ID: QEeT2NICKqY""
  },
  {
    "{": ""      ""Video ID: AeSRvpkY_dw""
  },
  {
    "{": ""      ""Video ID: NRj9r1OBBD4""
  },
  {
    "{": ""      ""Video ID: jQrTxdIRyU4""
  },
  {
    "{": ""      ""Video ID: pvKo_R_uM-A""
  },
  {
    "{": ""      ""Video ID: UJDHKI54v_g""
  },
  {
    "{": ""      ""Video ID: IJBmiKHm694""
  },
  {
    "{": ""      ""Video ID: o8DRICmFu0g""
  },
  {
    "{": ""      ""Video ID: 8c9ZWklRojo""
  },
  {
    "{": ""      ""Video ID: swb6mVWqnwY""
  },
  {
    "{": ""      ""Video ID: dk8BTkqYjBE""
  },
  {
    "{": ""      ""Video ID: QgZ3-MHEgHs""
  },
  {
    "{": ""      ""Video ID: oaOwRu_n9qc""
  },
  {
    "{": ""      ""Video ID: sbVHmPK6hSo""
  },
  {
    "{": ""      ""Video ID: W4BaD-f8590""
  },
  {
    "{": ""      ""Video ID: nzcb-xMz9n0""
  },
  {
    "{": ""      ""Video ID: 5k8R-kSsQ0s""
  },
  {
    "{": ""      ""Video ID: OHL4T1WqlHw""
  },
  {
    "{": ""      ""Video ID: nvsVRwxTwDs""
  },
  {
    "{": ""      ""Video ID: TLfo1X16Ps0""
  },
  {
    "{": ""      ""Video ID: WUPn-xWHUBg""
  },
  {
    "{": ""      ""Video ID: DzGj8rMbYVk""
  },
  {
    "{": ""      ""Video ID: uQ9FcFS3S40""
  },
  {
    "{": ""      ""Video ID: cE36c6VY3ew""
  },
  {
    "{": ""      ""Video ID: kJVz_GsP87I""
  },
  {
    "{": ""      ""Video ID: NKpTVuutzck""
  },
  {
    "{": ""      ""Video ID: PhS4DTODMr0""
  },
  {
    "{": ""      ""Video ID: xlrOHgLEZyM""
  },
  {
    "{": ""      ""Video ID: uJA6dDG7CbQ""
  },
  {
    "{": ""      ""Video ID: qWcYUe-0V5c""
  },
  {
    "{": ""      ""Video ID: xD8__J88LnI""
  },
  {
    "{": ""      ""Video ID: wiYqY2MNM54""
  },
  {
    "{": ""      ""Video ID: bbCREOCa0Ng""
  },
  {
    "{": ""      ""Video ID: -_kwPboJxi8""
  },
  {
    "{": ""      ""Video ID: RuI0OPavDn0""
  },
  {
    "{": ""      ""Video ID: Gyns3mf6BcY""
  },
  {
    "{": ""      ""Video ID: xmK9EfnGMf8""
  },
  {
    "{": ""      ""Video ID: s1ZWJjC648I""
  },
  {
    "{": ""      ""Video ID: jz0EEtJGeuw""
  },
  {
    "{": ""      ""Video ID: eLvZMPFLxzo""
  },
  {
    "{": ""      ""Video ID: mZujFLZlxyY""
  },
  {
    "{": ""      ""Video ID: JdgeVuxQCKk""
  },
  {
    "{": ""      ""Video ID: 7u0fgtaWR6g""
  },
  {
    "{": ""      ""Video ID: A7GvRAurmJc""
  },
  {
    "{": ""      ""Video ID: ii9iZ9Fw71U""
  },
  {
    "{": ""      ""Video ID: FrXPJuzYhsA""
  },
  {
    "{": ""      ""Video ID: MqQexsXYJeo""
  },
  {
    "{": ""      ""Video ID: z-Niur_FYRE""
  },
  {
    "{": ""      ""Video ID: 7S5kbS0JsAA""
  },
  {
    "{": ""      ""Video ID: -QXJIQO4Dps""
  },
  {
    "{": ""      ""Video ID: ao-9B8IV9_E""
  },
  {
    "{": ""      ""Video ID: ZpJL4aFQeu0""
  },
  {
    "{": ""      ""Video ID: MYfBTXiurDs""
  },
  {
    "{": ""      ""Video ID: jtuvXrTz8DY""
  },
  {
    "{": ""      ""Video ID: SQmvERfesSw""
  },
  {
    "{": ""      ""Video ID: nn5WXsgMIL8""
  },
  {
    "{": ""      ""Video ID: 5o-_UaLwTP8""
  },
  {
    "{": ""      ""Video ID: hKT8UXYMCt8""
  },
  {
    "{": ""      ""Video ID: 8Ftj6xU3MxI""
  },
  {
    "{": ""      ""Video ID: JLRdz9aXWJE""
  },
  {
    "{": ""      ""Video ID: u7yLJ9XVwJg""
  },
  {
    "{": ""      ""Video ID: G-vGpS1cDfo""
  },
  {
    "{": ""      ""Video ID: 2Zh__t8vBeQ""
  },
  {
    "{": ""      ""Video ID: GwaMHJzruDU""
  },
  {
    "{": ""      ""Video ID: uuuApoPa9r0""
  },
  {
    "{": ""      ""Video ID: 03UoK01NWEw""
  },
  {
    "{": ""      ""Video ID: TuXhJNUrkBk""
  },
  {
    "{": ""      ""Video ID: ZQtFpfzsckc""
  },
  {
    "{": ""      ""Video ID: RbiFbkC0O8w""
  },
  {
    "{": ""      ""Video ID: YGmxn83WyX4""
  },
  {
    "{": ""      ""Video ID: gPI2jj9-hiI""
  },
  {
    "{": ""      ""Video ID: UBBvJsNMxUE""
  },
  {
    "{": ""      ""Video ID: SpwFbJt8ZKg""
  },
  {
    "{": ""      ""Video ID: lkaGGs9gZzA""
  },
  {
    "{": ""      ""Video ID: vVBzO3OFJOc""
  },
  {
    "{": ""      ""Video ID: QtrwzDabMzk""
  },
  {
    "{": ""      ""Video ID: zYkz-Wlw4wk""
  },
  {
    "{": ""      ""Video ID: SLhPq8VJb0I""
  },
  {
    "{": ""      ""Video ID: KyWODmDHcGY""
  },
  {
    "{": ""      ""Video ID: BrbEnFtpXe4""
  },
  {
    "{": ""      ""Video ID: Fwvb3ovgeRw""
  },
  {
    "{": ""      ""Video ID: EjBjATDn9tU""
  },
  {
    "{": ""      ""Video ID: tZN66CQgHhg""
  },
  {
    "{": ""      ""Video ID: ckriO82nR1c""
  },
  {
    "{": ""      ""Video ID: wFkExD4mo_k""
  },
  {
    "{": ""      ""Video ID: r1QOWK518Ys""
  },
  {
    "{": ""      ""Video ID: u5CX_rJf8nA""
  },
  {
    "{": ""      ""Video ID: R8SANUJobgY""
  },
  {
    "{": ""      ""Video ID: edD-Wdbr5IE""
  },
  {
    "{": ""      ""Video ID: 5wgd08TfK2U""
  },
  {
    "{": ""      ""Video ID: zaMkAXqqoHQ""
  },
  {
    "{": ""      ""Video ID: 5nPi5FYKTZ4""
  },
  {
    "{": ""      ""Video ID: N2lRGbTkIws""
  },
  {
    "{": ""      ""Video ID: TJ8Ctdo3tA8""
  },
  {
    "{": ""      ""Video ID: xztwF_nUREs""
  },
  {
    "{": ""      ""Video ID: SJqQwNcwI-M""
  },
  {
    "{": ""      ""Video ID: hwyZd3L6mCo""
  },
  {
    "{": ""      ""Video ID: HW5ynj4Ko4w""
  },
  {
    "{": ""      ""Video ID: cPMxAjECdO0""
  },
  {
    "{": ""      ""Video ID: b_P2wF7BBzU""
  },
  {
    "{": ""      ""Video ID: l2m5mb4vVX0""
  },
  {
    "{": ""      ""Video ID: vrJD6SXX6Bo""
  },
  {
    "{": ""      ""Video ID: BrkihBLzwEk""
  },
  {
    "{": ""      ""Video ID: _3SoM5vp_TA""
  },
  {
    "{": ""      ""Video ID: U_5SjHTCUMg""
  },
  {
    "{": ""      ""Video ID: pgnUeVQd4kQ""
  },
  {
    "{": ""      ""Video ID: BK9JwGf40NU""
  },
  {
    "{": ""      ""Video ID: dMGmAcF6XAs""
  },
  {
    "{": ""      ""Video ID: UVyH4jGvHCw""
  },
  {
    "{": ""      ""Video ID: G9tC4Q9xjxk""
  },
  {
    "{": ""      ""Video ID: QlIp8-Ktk7I""
  },
  {
    "{": ""      ""Video ID: kPI3jsko48Q""
  },
  {
    "{": ""      ""Video ID: Tw9eGDxQJok""
  },
  {
    "{": ""      ""Video ID: 93cErAqdz98""
  },
  {
    "{": ""      ""Video ID: MhZcFJVGqq0""
  },
  {
    "{": ""      ""Video ID: 2CLkCs3Yk2g""
  },
  {
    "{": ""      ""Video ID: 7zA6TXHoWag""
  },
  {
    "{": ""      ""Video ID: gh2p0yZ1kgU""
  },
  {
    "{": ""      ""Video ID: bDsFBq7sZqo""
  },
  {
    "{": ""      ""Video ID: ZFKosNOegbc""
  },
  {
    "{": ""      ""Video ID: ZP_2Ha_HAgc""
  },
  {
    "{": ""      ""Video ID: SBfpYqrrzgQ""
  },
  {
    "{": ""      ""Video ID: mjwf7WvxoZY""
  },
  {
    "{": ""      ""Video ID: g-HSoEcV0Lg""
  },
  {
    "{": ""      ""Video ID: XeQ_7dvwhvs""
  },
  {
    "{": ""      ""Video ID: rhRUmOlrj-4""
  },
  {
    "{": ""      ""Video ID: QgJsoHBx91A""
  },
  {
    "{": ""      ""Video ID: h5IJNeHx0hY""
  },
  {
    "{": ""      ""Video ID: VbHyz4FWI8o""
  },
  {
    "{": ""      ""Video ID: NW6p8MFq9d4""
  },
  {
    "{": ""      ""Video ID: Z9Pv-gQas90""
  },
  {
    "{": ""      ""Video ID: 9gcvePANaog""
  },
  {
    "{": ""      ""Video ID: 9POoFxYNnfo""
  },
  {
    "{": ""      ""Video ID: CVcRwfThoo8""
  },
  {
    "{": ""      ""Video ID: lUvmPj9zU64""
  },
  {
    "{": ""      ""Video ID: PZbG9i1oGPA""
  },
  {
    "{": ""      ""Video ID: buUn7ZPlavs""
  },
  {
    "{": ""      ""Video ID: qPa6GbiXtTk""
  },
  {
    "{": ""      ""Video ID: PqR9g1OEuZg""
  },
  {
    "{": ""      ""Video ID: csNEjnfGsTM""
  },
  {
    "{": ""      ""Video ID: Q_Cn0RreVcg""
  },
  {
    "{": ""      ""Video ID: nOJ2K4GRx-c""
  },
  {
    "{": ""      ""Video ID: kFQrK77KwS8""
  },
  {
    "{": ""      ""Video ID: Uky7b3m9w_0""
  },
  {
    "{": ""      ""Video ID: TDD0UOKm8NA""
  },
  {
    "{": ""      ""Video ID: qNprGciFiy4""
  },
  {
    "{": ""      ""Video ID: QyVU1JuGewI""
  },
  {
    "{": ""      ""Video ID: E3OD57-Fm7Q""
  },
  {
    "{": ""      ""Video ID: ZYU0gsmivTk""
  },
  {
    "{": ""      ""Video ID: lWKpED72jFU""
  },
  {
    "{": ""      ""Video ID: 98WP39hb0vI""
  },
  {
    "{": ""      ""Video ID: _Xb9LXuROGI""
  },
  {
    "{": ""      ""Video ID: srf2EryyJb8""
  },
  {
    "{": ""      ""Video ID: MMUDS_cZtyg""
  },
  {
    "{": ""      ""Video ID: FLSAZQRZu6c""
  },
  {
    "{": ""      ""Video ID: Jlig-fZrHgs""
  },
  {
    "{": ""      ""Video ID: 9XPSfZ8f8Jw""
  },
  {
    "{": ""      ""Video ID: qXGiGKik0WM""
  },
  {
    "{": ""      ""Video ID: 9dadKfrguPE""
  },
  {
    "{": ""      ""Video ID: jjVbtFRlZFU""
  },
  {
    "{": ""      ""Video ID: Q8dlhrPdAco""
  },
  {
    "{": ""      ""Video ID: tTZm0XjW0RE""
  },
  {
    "{": ""      ""Video ID: rHi3HVQC_co""
  },
  {
    "{": ""      ""Video ID: Qkhye7ot4zI""
  },
  {
    "{": ""      ""Video ID: owMSXSo1gXg""
  },
  {
    "{": ""      ""Video ID: XoMrCTcK0TI""
  },
  {
    "{": ""      ""Video ID: 7oZfWkSzM28""
  },
  {
    "{": ""      ""Video ID: G7E_cKFEwzU""
  },
  {
    "{": ""      ""Video ID: rB6IJAArC9w""
  },
  {
    "{": ""      ""Video ID: CVWFBTNtqnw""
  },
  {
    "{": ""      ""Video ID: rRNd9MWVTEY""
  },
  {
    "{": ""      ""Video ID: Q64lhJd3_WU""
  },
  {
    "{": ""      ""Video ID: hqTwXQsWQ4c""
  },
  {
    "{": ""      ""Video ID: diSBTmDJ_do""
  },
  {
    "{": ""      ""Video ID: 8elBbiw4hIk""
  },
  {
    "{": ""      ""Video ID: kq15PpEwVsw""
  },
  {
    "{": ""      ""Video ID: brU-OSN3mQw""
  },
  {
    "{": ""      ""Video ID: ER70cFuCMYo""
  },
  {
    "{": ""      ""Video ID: gLQL8rTDChk""
  },
  {
    "{": ""      ""Video ID: lyMoMUoEf4g""
  },
  {
    "{": ""      ""Video ID: DTXzQg11xtA""
  },
  {
    "{": ""      ""Video ID: ti-LoGmusuU""
  },
  {
    "{": ""      ""Video ID: tFWIKSI00Vo""
  },
  {
    "{": ""      ""Video ID: -bQldU7mAI0""
  },
  {
    "{": ""      ""Video ID: JpelKBKa-qc""
  },
  {
    "{": ""      ""Video ID: FYeYb5whgE8""
  },
  {
    "{": ""      ""Video ID: DKxnw_46EVQ""
  },
  {
    "{": ""      ""Video ID: S5zc8LQIYLw""
  },
  {
    "{": ""      ""Video ID: ImA7KPy837Q""
  },
  {
    "{": ""      ""Video ID: wncB8rp-4e4""
  },
  {
    "{": ""      ""Video ID: CYoAHYkrOBw""
  },
  {
    "{": ""      ""Video ID: TJxjc38Aizc""
  },
  {
    "{": ""      ""Video ID: 7inNsXwoxoo""
  },
  {
    "{": ""      ""Video ID: 6efLvjvtns0""
  },
  {
    "{": ""      ""Video ID: P5yIzU2K3Fk""
  },
  {
    "{": ""      ""Video ID: IqVvu17cEY8""
  },
  {
    "{": ""      ""Video ID: RudZmeUooBM""
  },
  {
    "{": ""      ""Video ID: WLInj4gd0VE""
  },
  {
    "{": ""      ""Video ID: qPNqT2Ni83g""
  },
  {
    "{": ""      ""Video ID: kW-7fiEjjoQ""
  },
  {
    "{": ""      ""Video ID: e9XU0nEImxE""
  },
  {
    "{": ""      ""Video ID: ghpAv8716ck""
  },
  {
    "{": ""      ""Video ID: o7i7jYG7Kn4""
  },
  {
    "{": ""      ""Video ID: ouLKQEledy0""
  },
  {
    "{": ""      ""Video ID: -W0OfB-N1DE""
  },
  {
    "{": ""      ""Video ID: 45_U3uFaDI8""
  },
  {
    "{": ""      ""Video ID: 3bWH9T6jAmw""
  },
  {
    "{": ""      ""Video ID: SwsnPwYYEhs""
  },
  {
    "{": ""      ""Video ID: YokfhyrGHgc""
  },
  {
    "{": ""      ""Video ID: ZaUhEtlqZ94""
  },
  {
    "{": ""      ""Video ID: BWzI_Wn0ZwM""
  },
  {
    "{": ""      ""Video ID: mRxNePVWSQw""
  },
  {
    "{": ""      ""Video ID: 96kkjJC_Yp4""
  },
  {
    "{": ""      ""Video ID: P3EJTeoX6M8""
  },
  {
    "{": ""      ""Video ID: RfQBWq_vgt0""
  },
  {
    "{": ""      ""Video ID: SIRWufHkx18""
  },
  {
    "{": ""      ""Video ID: rWDnEKxXtD4""
  },
  {
    "{": ""      ""Video ID: hIojQQJG6LM""
  },
  {
    "{": ""      ""Video ID: fcB9JZkd8g4""
  },
  {
    "{": ""      ""Video ID: 7LLL1xtrB1w""
  },
  {
    "{": ""      ""Video ID: QjcC7y_oCow""
  },
  {
    "{": ""      ""Video ID: l340o_C27_w""
  },
  {
    "{": ""      ""Video ID: pLhf86WItdI""
  },
  {
    "{": ""      ""Video ID: 6KDeUZC9V6w""
  },
  {
    "{": ""      ""Video ID: qbsTbnuGxhQ""
  },
  {
    "{": ""      ""Video ID: yHcek3Ir6I4""
  },
  {
    "{": ""      ""Video ID: vSzbcBnq5yk""
  },
  {
    "{": ""      ""Video ID: uIYaFfZ9giE""
  },
  {
    "{": ""      ""Video ID: XxJI5e6zZKU""
  },
  {
    "{": ""      ""Video ID: SI2EuP7DzgE""
  },
  {
    "{": ""      ""Video ID: IDOfU3ZjkLY""
  },
  {
    "{": ""      ""Video ID: QKh4F-Mxv7w""
  },
  {
    "{": ""      ""Video ID: ZKsDPRutFw8""
  },
  {
    "{": ""      ""Video ID: -B5-n2ubi9k""
  },
  {
    "{": ""      ""Video ID: pyuShP-6qxY""
  },
  {
    "{": ""      ""Video ID: vUYE0xkEwuk""
  },
  {
    "{": ""      ""Video ID: V-gxvTLowes""
  },
  {
    "{": ""      ""Video ID: E9o4MTIhlqU""
  },
  {
    "{": ""      ""Video ID: D_JHtCO1wGo""
  },
  {
    "{": ""      ""Video ID: LHPdtgrmpx8""
  },
  {
    "{": ""      ""Video ID: csHN6qu0xr4""
  },
  {
    "{": ""      ""Video ID: 6JddsjELqiA""
  },
  {
    "{": ""      ""Video ID: C114FrqCaKk""
  },
  {
    "{": ""      ""Video ID: YU5kadUgbsM""
  },
  {
    "{": ""      ""Video ID: -HJVzkXwASc""
  },
  {
    "{": ""      ""Video ID: gAliZBxlfH0""
  },
  {
    "{": ""      ""Video ID: dXrvFLhoM5U""
  },
  {
    "{": ""      ""Video ID: FKD7Gfyikj0""
  },
  {
    "{": ""      ""Video ID: IOLcjYu-Q6g""
  },
  {
    "{": ""      ""Video ID: 4k4LsMbm0KE""
  },
  {
    "{": ""      ""Video ID: gHWlLX4ljoQ""
  },
  {
    "{": ""      ""Video ID: BGG_Q1ojq9U""
  },
  {
    "{": ""      ""Video ID: TddFnTB_7IM""
  },
  {
    "{": ""      ""Video ID: K23dcrh3X0k""
  },
  {
    "{": ""      ""Video ID: qoEiA5p0o7Y""
  },
  {
    "{": ""      ""Video ID: xnSzpHfiwNg""
  },
  {
    "{": ""      ""Video ID: URffupf0OWk""
  },
  {
    "{": ""      ""Video ID: vkWcEq9rmPo""
  },
  {
    "{": ""      ""Video ID: ZDoCuhzN_z8""
  },
  {
    "{": ""      ""Video ID: O8IFo4nn1z4""
  },
  {
    "{": ""      ""Video ID: RfoKFrNQ9Is""
  },
  {
    "{": ""      ""Video ID: SzMPjpYD2N0""
  },
  {
    "{": ""      ""Video ID: Z5uir3tE3Xw""
  },
  {
    "{": ""      ""Video ID: nMGv49aHnMQ""
  },
  {
    "{": ""      ""Video ID: HxytrUdFurg""
  },
  {
    "{": ""      ""Video ID: zORv8wwiadQ""
  },
  {
    "{": ""      ""Video ID: rXvnn4Gg2k0""
  },
  {
    "{": ""      ""Video ID: d597to4hg_k""
  },
  {
    "{": ""      ""Video ID: GdNMsTDRrRc""
  },
  {
    "{": ""      ""Video ID: 0UP1OU9uQ2k""
  },
  {
    "{": ""      ""Video ID: -jo_QNK4q0w""
  },
  {
    "{": ""      ""Video ID: Z4ASP3aKVj4""
  },
  {
    "{": ""      ""Video ID: gjQgqZ6eMP4""
  },
  {
    "{": ""      ""Video ID: KEkDzHCDTwo""
  },
  {
    "{": ""      ""Video ID: A4sQePBTMAU""
  },
  {
    "{": ""      ""Video ID: 7-02Q5kVZYk""
  },
  {
    "{": ""      ""Video ID: ny_Wfc7sjgk""
  },
  {
    "{": ""      ""Video ID: uOQNWRjTV4E""
  },
  {
    "{": ""      ""Video ID: es3EFI8QILM""
  },
  {
    "{": ""      ""Video ID: 9GNBqYlfpHs""
  },
  {
    "{": ""      ""Video ID: Ek8LE-LTu00""
  },
  {
    "{": ""      ""Video ID: gEgJw3kCVXE""
  },
  {
    "{": ""      ""Video ID: g5KUMHsWXCA""
  },
  {
    "{": ""      ""Video ID: cTC6VESN9LE""
  },
  {
    "{": ""      ""Video ID: HP_SMHbnHvw""
  },
  {
    "{": ""      ""Video ID: YRDTdAoXIdU""
  },
  {
    "{": ""      ""Video ID: NyNgEmIVKBM""
  },
  {
    "{": ""      ""Video ID: 9r39evoZUZU""
  },
  {
    "{": ""      ""Video ID: 6O0Q_HQ6FVk""
  },
  {
    "{": ""      ""Video ID: enLfxN_Hlm0""
  },
  {
    "{": ""      ""Video ID: 8e_M8rlTBWU""
  },
  {
    "{": ""      ""Video ID: Ent_sFWWNkA""
  },
  {
    "{": ""      ""Video ID: eE0UcJcR58g""
  },
  {
    "{": ""      ""Video ID: 8qZzEMoTlMI""
  },
  {
    "{": ""      ""Video ID: 4Fzrt3aSQUw""
  },
  {
    "{": ""      ""Video ID: gFt5nejKaEg""
  },
  {
    "{": ""      ""Video ID: fgxxclNQXjY""
  },
  {
    "{": ""      ""Video ID: qHUyMGGYRj4""
  },
  {
    "{": ""      ""Video ID: XKPCTJgpdgE""
  },
  {
    "{": ""      ""Video ID: n8OdbaNUz04""
  },
  {
    "{": ""      ""Video ID: WaWoo82zNUA""
  },
  {
    "{": ""      ""Video ID: ZKHrdL-rEuk""
  },
  {
    "{": ""      ""Video ID: 0C5UtH55BxM""
  },
  {
    "{": ""      ""Video ID: HAqAfZucdU0""
  },
  {
    "{": ""      ""Video ID: HeGI0E9hYhA""
  },
  {
    "{": ""      ""Video ID: p71d3qpypJU""
  },
  {
    "{": ""      ""Video ID: IyzQyPm0Rpw""
  },
  {
    "{": ""      ""Video ID: gpgqCPFMkwU""
  },
  {
    "{": ""      ""Video ID: I3V5XeuKPsk""
  },
  {
    "{": ""      ""Video ID: fMdN9FOrJTk""
  },
  {
    "{": ""      ""Video ID: N0QSTz9nBzQ""
  },
  {
    "{": ""      ""Video ID: ANG_XkdAH-8""
  },
  {
    "{": ""      ""Video ID: K00V-vi0lLY""
  },
  {
    "{": ""      ""Video ID: 20yG4i0eFgg""
  },
  {
    "{": ""      ""Video ID: sgKqSTi7FL8""
  },
  {
    "{": ""      ""Video ID: Cr2x6mdDJlc""
  },
  {
    "{": ""      ""Video ID: C4mcTAprYBw""
  },
  {
    "{": ""      ""Video ID: 2FjVJBAES7A""
  },
  {
    "{": ""      ""Video ID: obNzvEH3wvc""
  },
  {
    "{": ""      ""Video ID: soDdtiY08Zg""
  },
  {
    "{": ""      ""Video ID: 7bh9a_z8GzQ""
  },
  {
    "{": ""      ""Video ID: 0_zYd51eXBs""
  },
  {
    "{": ""      ""Video ID: XQ8m0T-ag9A""
  },
  {
    "{": ""      ""Video ID: u9tX3cRQNZ8""
  },
  {
    "{": ""      ""Video ID: UJqQJ4p_p4M""
  },
  {
    "{": ""      ""Video ID: FamSMoQE2DE""
  },
  {
    "{": ""      ""Video ID: 2alCpGhbReQ""
  },
  {
    "{": ""      ""Video ID: BazBdnkvpN4""
  },
  {
    "{": ""      ""Video ID: t0TdXM9Ez88""
  },
  {
    "{": ""      ""Video ID: b_S8k5pS0-E""
  },
  {
    "{": ""      ""Video ID: gNXqk1sTUvc""
  },
  {
    "{": ""      ""Video ID: _kfUsDe8slA""
  },
  {
    "{": ""      ""Video ID: vHvMt_oL-7M""
  },
  {
    "{": ""      ""Video ID: MhZAFRaGHDs""
  },
  {
    "{": ""      ""Video ID: RcESidDP0rY""
  },
  {
    "{": ""      ""Video ID: Eez3FVudwxA""
  },
  {
    "{": ""      ""Video ID: 8bAm7exQTrg""
  },
  {
    "{": ""      ""Video ID: DLCG54WX6Z8""
  },
  {
    "{": ""      ""Video ID: qw4RAG4z4JI""
  },
  {
    "{": ""      ""Video ID: 4t61q7nu3x0""
  },
  {
    "{": ""      ""Video ID: rIWL5uCyfmI""
  },
  {
    "{": ""      ""Video ID: 5uhV24R7Dd4""
  },
  {
    "{": ""      ""Video ID: mh4m-uvxXzc""
  },
  {
    "{": ""      ""Video ID: 5H7N4st6axQ""
  },
  {
    "{": ""      ""Video ID: sx-KP8K5P1w""
  },
  {
    "{": ""      ""Video ID: HP7HAvbib9Q""
  },
  {
    "{": ""      ""Video ID: Co2MnALkpU4""
  },
  {
    "{": ""      ""Video ID: tP-9UOvWaao""
  },
  {
    "{": ""      ""Video ID: B1iosBN0vSw""
  },
  {
    "{": ""      ""Video ID: Bs3zBzBSL28""
  },
  {
    "{": ""      ""Video ID: dTH58Mtce20""
  },
  {
    "{": ""      ""Video ID: LtvOkLd5jw4""
  },
  {
    "{": ""      ""Video ID: XehOwYef1DU""
  },
  {
    "{": ""      ""Video ID: vj5nxYShD4I""
  },
  {
    "{": ""      ""Video ID: ma9cdejCNxo""
  },
  {
    "{": ""      ""Video ID: h9NrJj_Bejw""
  },
  {
    "{": ""      ""Video ID: gyRSWSDnESI""
  },
  {
    "{": ""      ""Video ID: 0XZmZxV1E7o""
  },
  {
    "{": ""      ""Video ID: 6SeU-LM94cI""
  },
  {
    "{": ""      ""Video ID: VX-SqdVzV4A""
  },
  {
    "{": ""      ""Video ID: wf9nzqfZsPU""
  },
  {
    "{": ""      ""Video ID: ioNfK9692Zk""
  },
  {
    "{": ""      ""Video ID: hNHV4SZ73YE""
  },
  {
    "{": ""      ""Video ID: vs9LuHd1Ob0""
  },
  {
    "{": ""      ""Video ID: ztSz77-sAtw""
  },
  {
    "{": ""      ""Video ID: _hqxAvmjYU4""
  },
  {
    "{": ""      ""Video ID: HALVKNoHuqU""
  },
  {
    "{": ""      ""Video ID: RhCbTGMfa2I""
  },
  {
    "{": ""      ""Video ID: jil48TCMEQo""
  },
  {
    "{": ""      ""Video ID: DG1vHMqBZgg""
  },
  {
    "{": ""      ""Video ID: LGIHOsg17UQ""
  },
  {
    "{": ""      ""Video ID: SEt2nHju7bI""
  },
  {
    "{": ""      ""Video ID: PVrggHX5HSI""
  },
  {
    "{": ""      ""Video ID: m9g6zmObvac""
  },
  {
    "{": ""      ""Video ID: F2TDT7uXJ70""
  },
  {
    "{": ""      ""Video ID: gO6rqAJ3mGc""
  },
  {
    "{": ""      ""Video ID: TE7n25Qzcsc""
  },
  {
    "{": ""      ""Video ID: ngx0L8lnw3I""
  },
  {
    "{": ""      ""Video ID: wQH1ui1QS4Y""
  },
  {
    "{": ""      ""Video ID: -is63goeBgc""
  },
  {
    "{": ""      ""Video ID: GpuEMSH6zB4""
  },
  {
    "{": ""      ""Video ID: DASfcnxl7Dk""
  },
  {
    "{": ""      ""Video ID: dL1ZTLNC--U""
  },
  {
    "{": ""      ""Video ID: yGM6WChPj_k""
  },
  {
    "{": ""      ""Video ID: nJ-xoIziMmQ""
  },
  {
    "{": ""      ""Video ID: zFYO81F9MZ4""
  },
  {
    "{": ""      ""Video ID: gLlzNiRsF8g""
  },
  {
    "{": ""      ""Video ID: SPQsc0LDT20""
  },
  {
    "{": ""      ""Video ID: VgpvbHvAT3g""
  },
  {
    "{": ""      ""Video ID: C0tZYZ8o5x8""
  },
  {
    "{": ""      ""Video ID: 48RbpaWIzfQ""
  },
  {
    "{": ""      ""Video ID: QHllAtzMEdg""
  },
  {
    "{": ""      ""Video ID: ccD9zCBMeS0""
  },
  {
    "{": ""      ""Video ID: TQTlj8yrAco""
  },
  {
    "{": ""      ""Video ID: d9pO8WxNo-w""
  },
  {
    "{": ""      ""Video ID: auAaXNTVATk""
  },
  {
    "{": ""      ""Video ID: XBHOWcWWrYI""
  },
  {
    "{": ""      ""Video ID: VKEPPw5Jd2M""
  },
  {
    "{": ""      ""Video ID: eK8HaUl1IOQ""
  },
  {
    "{": ""      ""Video ID: NA62P-uGu6E""
  },
  {
    "{": ""      ""Video ID: wHku_43spsQ""
  },
  {
    "{": ""      ""Video ID: E5gwjzR1J8I""
  },
  {
    "{": ""      ""Video ID: lJQCpcrvyJY""
  },
  {
    "{": ""      ""Video ID: 3TxexltWdkQ""
  },
  {
    "{": ""      ""Video ID: gxNpJVabE8s""
  },
  {
    "{": ""      ""Video ID: 0Qw-ILskT5Q""
  },
  {
    "{": ""      ""Video ID: 8o2D7uokmV8""
  },
  {
    "{": ""      ""Video ID: qj7LJlYeTEc""
  },
  {
    "{": ""      ""Video ID: keyOQXbtepE""
  },
  {
    "{": ""      ""Video ID: xIeOlTkT_m0""
  },
  {
    "{": ""      ""Video ID: URF2sVQWuxU""
  },
  {
    "{": ""      ""Video ID: _G5Yxp6j6hY""
  },
  {
    "{": ""      ""Video ID: E79LSs_ZvCM""
  },
  {
    "{": ""      ""Video ID: e5t7njlvGdY""
  },
  {
    "{": ""      ""Video ID: 4hXVcCUoAH0""
  },
  {
    "{": ""      ""Video ID: ET4E2wyMKJo""
  },
  {
    "{": ""      ""Video ID: 0OrDEF0Q97I""
  },
  {
    "{": ""      ""Video ID: G0smntbxyJ8""
  },
  {
    "{": ""      ""Video ID: p2Clk5lNUdQ""
  },
  {
    "{": ""      ""Video ID: yw2EisVqKZ4""
  },
  {
    "{": ""      ""Video ID: N9zlNGOs7QM""
  },
  {
    "{": ""      ""Video ID: dyB5FTpymf8""
  },
  {
    "{": ""      ""Video ID: Y-TXJTj0hjo""
  },
  {
    "{": ""      ""Video ID: t8xGxi4q57Q""
  },
  {
    "{": ""      ""Video ID: 8lQaSi6J27M""
  },
  {
    "{": ""      ""Video ID: 8Q-O8yMSDWc""
  },
  {
    "{": ""      ""Video ID: HAc4FdOQJLY""
  },
  {
    "{": ""      ""Video ID: ZrnK-qPARYI""
  },
  {
    "{": ""      ""Video ID: mUN3zXi2QRA""
  },
  {
    "{": ""      ""Video ID: xmerfW3Xv08""
  },
  {
    "{": ""      ""Video ID: wF8joJaOVJw""
  },
  {
    "{": ""      ""Video ID: SLGJTAfyG44""
  },
  {
    "{": ""      ""Video ID: CVMghUjz6bc""
  },
  {
    "{": ""      ""Video ID: T6QH4AKhOFk""
  },
  {
    "{": ""      ""Video ID: W_KNtsAIf_U""
  },
  {
    "{": ""      ""Video ID: hbm8yRYPhXE""
  },
  {
    "{": ""      ""Video ID: 8EVYPFNcG-o""
  },
  {
    "{": ""      ""Video ID: zux_-QFpX9Q""
  },
  {
    "{": ""      ""Video ID: HPrW8WoR7nc""
  },
  {
    "{": ""      ""Video ID: RLKrWPxADU0""
  },
  {
    "{": ""      ""Video ID: ZO4u9e8Paiw""
  },
  {
    "{": ""      ""Video ID: b8dq5Vis8dk""
  },
  {
    "{": ""      ""Video ID: 39hOm0pCg-s""
  },
  {
    "{": ""      ""Video ID: fnlaXuuTqSY""
  },
  {
    "{": ""      ""Video ID: MqAsravUn-Y""
  },
  {
    "{": ""      ""Video ID: InLJmrK8xWw""
  },
  {
    "{": ""      ""Video ID: wskAinFClsE""
  },
  {
    "{": ""      ""Video ID: K6ohNo0a8yk""
  },
  {
    "{": ""      ""Video ID: -Mn-rdTY-DU""
  },
  {
    "{": ""      ""Video ID: hGWjXu1LpoE""
  },
  {
    "{": ""      ""Video ID: ocZntJTh7Ik""
  },
  {
    "{": ""      ""Video ID: 1v1KB83rOYs""
  },
  {
    "{": ""      ""Video ID: gb9VCfivwdM""
  },
  {
    "{": ""      ""Video ID: ZJOVr10rP1c""
  },
  {
    "{": ""      ""Video ID: PXpwC1o5AcI""
  },
  {
    "{": ""      ""Video ID: BZ5wVv26Hyc""
  },
  {
    "{": ""      ""Video ID: IABDVheq0LY""
  },
  {
    "{": ""      ""Video ID: _SmgCJSY8LE""
  },
  {
    "{": ""      ""Video ID: VApj0nz6g30""
  },
  {
    "{": ""      ""Video ID: QdId8McuRXc""
  },
  {
    "{": ""      ""Video ID: fEUTG1iQNYo""
  },
  {
    "{": ""      ""Video ID: iQwUpHA8iu8""
  },
  {
    "{": ""      ""Video ID: uZdzkD7scOc""
  },
  {
    "{": ""      ""Video ID: sTR81wuFP0g""
  },
  {
    "{": ""      ""Video ID: JYh4-1EncIk""
  },
  {
    "{": ""      ""Video ID: PCoppLO4sw8""
  },
  {
    "{": ""      ""Video ID: gGEzf9b5xBk""
  },
  {
    "{": ""      ""Video ID: VzqbEelzza4""
  },
  {
    "{": ""      ""Video ID: vZ4UwWJyUYc""
  },
  {
    "{": ""      ""Video ID: flzytOImbQU""
  },
  {
    "{": ""      ""Video ID: K-WOvlIEAoI""
  },
  {
    "{": ""      ""Video ID: iifNBOgWoGk""
  },
  {
    "{": ""      ""Video ID: gr-PrXEfu64""
  },
  {
    "{": ""      ""Video ID: _MvHzMZctPg""
  },
  {
    "{": ""      ""Video ID: KBmsE6atrVA""
  },
  {
    "{": ""      ""Video ID: mVqz0LKphws""
  },
  {
    "{": ""      ""Video ID: eBB12J2i-sg""
  },
  {
    "{": ""      ""Video ID: wIX5QmLAO7Q""
  },
  {
    "{": ""      ""Video ID: xd7D_qAT8ok""
  },
  {
    "{": ""      ""Video ID: Dtpei0-5kQk""
  },
  {
    "{": ""      ""Video ID: m0T9ZBKE22Y""
  },
  {
    "{": ""      ""Video ID: ziSBu3U0iLA""
  },
  {
    "{": ""      ""Video ID: YfgmcCh2EcA""
  },
  {
    "{": ""      ""Video ID: JQ4U7eEF0Rw""
  },
  {
    "{": ""      ""Video ID: TSutxh6NEgQ""
  },
  {
    "{": ""      ""Video ID: 8HDDsGZOYFI""
  },
  {
    "{": ""      ""Video ID: yUmKfm5OOmc""
  },
  {
    "{": ""      ""Video ID: hS7WtoooIuU""
  },
  {
    "{": ""      ""Video ID: ZfrztIFqiow""
  },
  {
    "{": ""      ""Video ID: fai3XKTfLxY""
  },
  {
    "{": ""      ""Video ID: EOWq2zXgdUc""
  },
  {
    "{": ""      ""Video ID: 4dQ_TG4ogRQ""
  },
  {
    "{": ""      ""Video ID: zqLnPE6UW-o""
  },
  {
    "{": ""      ""Video ID: B5u9fNc87sM""
  },
  {
    "{": ""      ""Video ID: 4zBJJZBkc90""
  },
  {
    "{": ""      ""Video ID: vt-N66rW7fs""
  },
  {
    "{": ""      ""Video ID: p0GhZXIPrPM""
  },
  {
    "{": ""      ""Video ID: pZ3aBCg1XE0""
  },
  {
    "{": ""      ""Video ID: Q6HH_6yHT5M""
  },
  {
    "{": ""      ""Video ID: jTPzk2uC_Os""
  },
  {
    "{": ""      ""Video ID: va-vclrTnEo""
  },
  {
    "{": ""      ""Video ID: VPOT0PhiAVk""
  },
  {
    "{": ""      ""Video ID: gP9G45LpgKA""
  },
  {
    "{": ""      ""Video ID: S9tf51ORELA""
  },
  {
    "{": ""      ""Video ID: DJSbQnDVr6c""
  },
  {
    "{": ""      ""Video ID: zuTtpR4Mwck""
  },
  {
    "{": ""      ""Video ID: 7jliszD5bzU""
  },
  {
    "{": ""      ""Video ID: QEYozHREQbA""
  },
  {
    "{": ""      ""Video ID: Do4XlSKs8W8""
  },
  {
    "{": ""      ""Video ID: hljK-E_e6uA""
  },
  {
    "{": ""      ""Video ID: cSw_fKtcYdo""
  },
  {
    "{": ""      ""Video ID: UH7ah0M5LLY""
  },
  {
    "{": ""      ""Video ID: sGOjnlLSwiU""
  },
  {
    "{": ""      ""Video ID: hZ-FxDufIC0""
  },
  {
    "{": ""      ""Video ID: r3Mdb2d3yUI""
  },
  {
    "{": ""      ""Video ID: 3g9CJdiXugs""
  },
  {
    "{": ""      ""Video ID: JnY8pLz8Oew""
  },
  {
    "{": ""      ""Video ID: AX-2JvqkAOM""
  },
  {
    "{": ""      ""Video ID: 6lSLgFC23IQ""
  },
  {
    "{": ""      ""Video ID: 3KixKoCX7Pk""
  },
  {
    "{": ""      ""Video ID: 0EPbRfu_Ztk""
  },
  {
    "{": ""      ""Video ID: ZRvRHsGQnjs""
  },
  {
    "{": ""      ""Video ID: m4vfO1oxjks""
  },
  {
    "{": ""      ""Video ID: FxDyaiPr5q0""
  },
  {
    "{": ""      ""Video ID: rWCQme1COIs""
  },
  {
    "{": ""      ""Video ID: JlTVwNkfY_A""
  },
  {
    "{": ""      ""Video ID: WiKFTwiGGh0""
  },
  {
    "{": ""      ""Video ID: 0xJP5rI7r1I""
  },
  {
    "{": ""      ""Video ID: FzZ9BI0zg9k""
  },
  {
    "{": ""      ""Video ID: CWurjlqnOp0""
  },
  {
    "{": ""      ""Video ID: jmUNkvuKHbo""
  },
  {
    "{": ""      ""Video ID: lgxU8UbQqy0""
  },
  {
    "{": ""      ""Video ID: sbLGa_brlvw""
  },
  {
    "{": ""      ""Video ID: -wYcBJiOe7I""
  },
  {
    "{": ""      ""Video ID: Re8spAF5wjA""
  },
  {
    "{": ""      ""Video ID: 6ssfB-TKXmE""
  },
  {
    "{": ""      ""Video ID: 3o1SSuWyUuc""
  },
  {
    "{": ""      ""Video ID: BRzjAvFlEhQ""
  },
  {
    "{": ""      ""Video ID: xwKC9a6BsQs""
  },
  {
    "{": ""      ""Video ID: AMweS0WLQ4Y""
  },
  {
    "{": ""      ""Video ID: 8LPZ_kmC5rc""
  },
  {
    "{": ""      ""Video ID: 29vDU-y82cE""
  },
  {
    "{": ""      ""Video ID: OlPePYJfwEc""
  },
  {
    "{": ""      ""Video ID: 1YZDyxP4zB0""
  },
  {
    "{": ""      ""Video ID: HOQzct-8Mo4""
  },
  {
    "{": ""      ""Video ID: BT30Y7J4WXM""
  },
  {
    "{": ""      ""Video ID: ryr-FgbrdHw""
  },
  {
    "{": ""      ""Video ID: ROXpXTYjzk4""
  },
  {
    "{": ""      ""Video ID: -ylKak2bvwk""
  },
  {
    "{": ""      ""Video ID: 4lr2oL5UjGU""
  },
  {
    "{": ""      ""Video ID: khjtrIkYU5I""
  },
  {
    "{": ""      ""Video ID: pW-IMXbcNjc""
  },
  {
    "{": ""      ""Video ID: IQE2v7fhvNg""
  },
  {
    "{": ""      ""Video ID: J_WpTk6y6EE""
  },
  {
    "{": ""      ""Video ID: _VjmquazhY4""
  },
  {
    "{": ""      ""Video ID: JyO0RfJx-Og""
  },
  {
    "{": ""      ""Video ID: iZVFMf1V0q8""
  },
  {
    "{": ""      ""Video ID: I2ZaiXFyiCI""
  },
  {
    "{": ""      ""Video ID: qLkhgfY8GTA""
  },
  {
    "{": ""      ""Video ID: S--yKbFGQTM""
  },
  {
    "{": ""      ""Video ID: 2UzN2r500IU""
  },
  {
    "{": ""      ""Video ID: CFRXqhC-Ycw""
  },
  {
    "{": ""      ""Video ID: gH2V211QDGo""
  },
  {
    "{": ""      ""Video ID: 7yrW9ZMowTo""
  },
  {
    "{": ""      ""Video ID: AOXkbDhpP5k""
  },
  {
    "{": ""      ""Video ID: hr-YJruHgIw""
  },
  {
    "{": ""      ""Video ID: lkCTpGCGLk4""
  },
  {
    "{": ""      ""Video ID: BRnUZmkYgro""
  },
  {
    "{": ""      ""Video ID: MY2lT5YcTT4""
  },
  {
    "{": ""      ""Video ID: gZEenRKY3nQ""
  },
  {
    "{": ""      ""Video ID: 5C-_bQsclRY""
  },
  {
    "{": ""      ""Video ID: 0TYRFrwsOTo""
  },
  {
    "{": ""      ""Video ID: 1nW0f2Ye9BU""
  },
  {
    "{": ""      ""Video ID: rQvCT-c5G1A""
  },
  {
    "{": ""      ""Video ID: YBL69kxp2gU""
  },
  {
    "{": ""      ""Video ID: 0w93q1p39xM""
  },
  {
    "{": ""      ""Video ID: 54XVOkJOoqM""
  },
  {
    "{": ""      ""Video ID: MD8pXp8e7K0""
  },
  {
    "{": ""      ""Video ID: wwRDZOmXMFU""
  },
  {
    "{": ""      ""Video ID: NCmzir1GXBk""
  },
  {
    "{": ""      ""Video ID: 79ha-zYcKRk""
  },
  {
    "{": ""      ""Video ID: o4v4uPll0Cg""
  },
  {
    "{": ""      ""Video ID: vgy6X_4DcfA""
  },
  {
    "{": ""      ""Video ID: HArwXOtGyfM""
  },
  {
    "{": ""      ""Video ID: DulkdcUdyjo""
  },
  {
    "{": ""      ""Video ID: qFCl3AESXPo""
  },
  {
    "{": ""      ""Video ID: cC4Lxos-zVM""
  },
  {
    "{": ""      ""Video ID: KjsgoSNJ6E8""
  },
  {
    "{": ""      ""Video ID: r5oI8LW_Q1w""
  },
  {
    "{": ""      ""Video ID: LRwQHHcy4mQ""
  },
  {
    "{": ""      ""Video ID: -zPMvpdlZbY""
  },
  {
    "{": ""      ""Video ID: Aq8ULisIpuw""
  },
  {
    "{": ""      ""Video ID: Gf0Uir8SCeg""
  },
  {
    "{": ""      ""Video ID: vshYcCAXvTY""
  },
  {
    "{": ""      ""Video ID: RZTFl-KLbM4""
  },
  {
    "{": ""      ""Video ID: EPOgqGdawak""
  },
  {
    "{": ""      ""Video ID: DEDqTBr0Yls""
  },
  {
    "{": ""      ""Video ID: 6A0rwG39Jzk""
  },
  {
    "{": ""      ""Video ID: qovo5CGikQI""
  },
  {
    "{": ""      ""Video ID: h_B2s7utGmc""
  },
  {
    "{": ""      ""Video ID: neDyIWRyiXQ""
  },
  {
    "{": ""      ""Video ID: ppAn0LNU_V8""
  },
  {
    "{": ""      ""Video ID: zv8d_ry-u-Q""
  },
  {
    "{": ""      ""Video ID: -3q-MDkmQCg""
  },
  {
    "{": ""      ""Video ID: MHNiG8ffQ4A""
  },
  {
    "{": ""      ""Video ID: gbJDiyHuBmw""
  },
  {
    "{": ""      ""Video ID: BvPdWcCHkxM""
  },
  {
    "{": ""      ""Video ID: tiLgi5p14ts""
  },
  {
    "{": ""      ""Video ID: yqDk3aJ7XOk""
  },
  {
    "{": ""      ""Video ID: _SrmeIF7Owo""
  },
  {
    "{": ""      ""Video ID: Lh-VKg_D92o""
  },
  {
    "{": ""      ""Video ID: KaJbHQBlgr0""
  },
  {
    "{": ""      ""Video ID: tkjpVp-1q5E""
  },
  {
    "{": ""      ""Video ID: bDdIgNw421k""
  },
  {
    "{": ""      ""Video ID: PNyuO0LpfVM""
  },
  {
    "{": ""      ""Video ID: WqIs25OH5sI""
  },
  {
    "{": ""      ""Video ID: 6VAaeMnA8Js""
  },
  {
    "{": ""      ""Video ID: 2nTbWR0dRRE""
  },
  {
    "{": ""      ""Video ID: 65eeLpy-YME""
  },
  {
    "{": ""      ""Video ID: eDjdNJlDr7o""
  },
  {
    "{": ""      ""Video ID: DRwHhSGXjXg""
  },
  {
    "{": ""      ""Video ID: sZU6nZO_Mso""
  },
  {
    "{": ""      ""Video ID: vdhNUiQnVv8""
  },
  {
    "{": ""      ""Video ID: p5XPcJA_3g0""
  },
  {
    "{": ""      ""Video ID: I1USw-nYVIw""
  },
  {
    "{": ""      ""Video ID: ThtO4V1DzT4""
  },
  {
    "{": ""      ""Video ID: G1l4hQM_d1w""
  },
  {
    "{": ""      ""Video ID: 9ZJoPpda5Ik""
  },
  {
    "{": ""      ""Video ID: El3hlf5BqYI""
  },
  {
    "{": ""      ""Video ID: -lo9QcOG9JM""
  },
  {
    "{": ""      ""Video ID: cmKXFZffIos""
  },
  {
    "{": ""      ""Video ID: VXiI9jN0vXc""
  },
  {
    "{": ""      ""Video ID: Wv8bLNuqz2A""
  },
  {
    "{": ""      ""Video ID: HYyA9EXCKDc""
  },
  {
    "{": ""      ""Video ID: hq9FChCTLtA""
  },
  {
    "{": ""      ""Video ID: 928W9niR0G0""
  },
  {
    "{": ""      ""Video ID: lg9_ZP99pcE""
  },
  {
    "{": ""      ""Video ID: Gn5zldAc6sE""
  },
  {
    "{": ""      ""Video ID: 5sLjSZCNZp4""
  },
  {
    "{": ""      ""Video ID: gDap3TTkXJg""
  },
  {
    "{": ""      ""Video ID: 9sUZA_sSBZQ""
  },
  {
    "{": ""      ""Video ID: JcBPVNccRIE""
  },
  {
    "{": ""      ""Video ID: tZ1n_h5kGF0""
  },
  {
    "{": ""      ""Video ID: TwKw7zGrebc""
  },
  {
    "{": ""      ""Video ID: HcSXbeYftsI""
  },
  {
    "{": ""      ""Video ID: s1uoshS_ILY""
  },
  {
    "{": ""      ""Video ID: 2sdPHPd88M0""
  },
  {
    "{": ""      ""Video ID: VTqW4QXt_ic""
  },
  {
    "{": ""      ""Video ID: T0-EIpflHgQ""
  },
  {
    "{": ""      ""Video ID: 7LX4ZfL-_U4""
  },
  {
    "{": ""      ""Video ID: St9OIm6IawM""
  },
  {
    "{": ""      ""Video ID: Mk3HQjCdqjY""
  },
  {
    "{": ""      ""Video ID: 0n1plrwQwrk""
  },
  {
    "{": ""      ""Video ID: fXgnbxnidoE""
  },
  {
    "{": ""      ""Video ID: QL-wCIjmmQw""
  },
  {
    "{": ""      ""Video ID: wK2PcZKDi7g""
  },
  {
    "{": ""      ""Video ID: _0fGcdik79M""
  },
  {
    "{": ""      ""Video ID: JS0_OwQzHjw""
  },
  {
    "{": ""      ""Video ID: AxHpTD7cEUs""
  },
  {
    "{": ""      ""Video ID: XZcg_cYXcSE""
  },
  {
    "{": ""      ""Video ID: WY2AeD0Tn4Y""
  },
  {
    "{": ""      ""Video ID: LKjTNUiK1sg""
  },
  {
    "{": ""      ""Video ID: nMh8Cjnzen8""
  },
  {
    "{": ""      ""Video ID: YkrF3rMCIDo""
  },
  {
    "{": ""      ""Video ID: rPmvncVL7xQ""
  },
  {
    "{": ""      ""Video ID: ELx2eX_kM-w""
  },
  {
    "{": ""      ""Video ID: cv1T_EJsVXc""
  },
  {
    "{": ""      ""Video ID: JS2Erv2Xqp4""
  },
  {
    "{": ""      ""Video ID: iGopjZTsw9c""
  },
  {
    "{": ""      ""Video ID: 10STpZ4NySA""
  },
  {
    "{": ""      ""Video ID: AtyJbIOZjS8""
  },
  {
    "{": ""      ""Video ID: 8Q_sSYiB1IY""
  },
  {
    "{": ""      ""Video ID: mzxOl0dsuR0""
  },
  {
    "{": ""      ""Video ID: sHIWCWDS1ls""
  },
  {
    "{": ""      ""Video ID: A859_-VtlNk""
  },
  {
    "{": ""      ""Video ID: 2ZFDPF7LNQ8""
  },
  {
    "{": ""      ""Video ID: -7aGgINbyDA""
  },
  {
    "{": ""      ""Video ID: wG0TScK42aU""
  },
  {
    "{": ""      ""Video ID: zX3XxD5TxRc""
  },
  {
    "{": ""      ""Video ID: LK5SFtLE-FE""
  },
  {
    "{": ""      ""Video ID: dhz_J-B04i0""
  },
  {
    "{": ""      ""Video ID: yR1KxRaMP0Q""
  },
  {
    "{": ""      ""Video ID: -73vLtvd8Qc""
  },
  {
    "{": ""      ""Video ID: mTrw15pkBfs""
  },
  {
    "{": ""      ""Video ID: 3UDO0gDg6-Y""
  },
  {
    "{": ""      ""Video ID: 81ZjkP5dXQA""
  },
  {
    "{": ""      ""Video ID: fYBbQJlswuk""
  },
  {
    "{": ""      ""Video ID: vSav7O8ZEow""
  },
  {
    "{": ""      ""Video ID: FG_HuFtP8w8""
  },
  {
    "{": ""      ""Video ID: 8DvBSM99eKQ""
  },
  {
    "{": ""      ""Video ID: aTyYM-dUgCI""
  },
  {
    "{": ""      ""Video ID: Tsi2JMGnVEQ""
  },
  {
    "{": ""      ""Video ID: sr2uR6QNkKE""
  },
  {
    "{": ""      ""Video ID: 3mbLnbxYXIU""
  },
  {
    "{": ""      ""Video ID: H57pizJcVtg""
  },
  {
    "{": ""      ""Video ID: ocWZWyd4NGs""
  },
  {
    "{": ""      ""Video ID: thtIO-HvAnc""
  },
  {
    "{": ""      ""Video ID: 2xpDxzrvmYY""
  },
  {
    "{": ""      ""Video ID: wRByVi482Sg""
  },
  {
    "{": ""      ""Video ID: uPkwSCcs2UE""
  },
  {
    "{": ""      ""Video ID: b0GTjbDVilA""
  },
  {
    "{": ""      ""Video ID: nSCVVLwUz_w""
  },
  {
    "{": ""      ""Video ID: 1at-rAsPk1c""
  },
  {
    "{": ""      ""Video ID: Pc0_5rmbIuY""
  },
  {
    "{": ""      ""Video ID: RgLMKoPn3go""
  },
  {
    "{": ""      ""Video ID: CZ6U5CR0dPU""
  },
  {
    "{": ""      ""Video ID: Fva3istAy8o""
  },
  {
    "{": ""      ""Video ID: oZwE1KHwhQM""
  },
  {
    "{": ""      ""Video ID: x1bJdhSOsZY""
  },
  {
    "{": ""      ""Video ID: MZCIHOCakgM""
  },
  {
    "{": ""      ""Video ID: OQI1cYptD1Y""
  },
  {
    "{": ""      ""Video ID: EkuZFmoHkP8""
  },
  {
    "{": ""      ""Video ID: Y6bAzkJDjVs""
  },
  {
    "{": ""      ""Video ID: doDoT9f5Vlc""
  },
  {
    "{": ""      ""Video ID: xzmxzaz14Aw""
  },
  {
    "{": ""      ""Video ID: Q4r5G6VT3ds""
  },
  {
    "{": ""      ""Video ID: XEu4K449CME""
  },
  {
    "{": ""      ""Video ID: Xvvg63jcC2o""
  },
  {
    "{": ""      ""Video ID: CYF7NjPK65w""
  },
  {
    "{": ""      ""Video ID: yv4hYBVZPYk""
  },
  {
    "{": ""      ""Video ID: s9sm4VzwA68""
  },
  {
    "{": ""      ""Video ID: 9pfIGXXAJVg""
  },
  {
    "{": ""      ""Video ID: GlFlRtdGA5Y""
  },
  {
    "{": ""      ""Video ID: QX2QLRk8IWA""
  },
  {
    "{": ""      ""Video ID: BAkeQOxQ-KU""
  },
  {
    "{": ""      ""Video ID: F6EMrF6uQrM""
  },
  {
    "{": ""      ""Video ID: 4dpKqDVRjCA""
  },
  {
    "{": ""      ""Video ID: xGWAsgcrpEk""
  },
  {
    "{": ""      ""Video ID: S309kHQkpYs""
  },
  {
    "{": ""      ""Video ID: fE4vdMs8iK4""
  },
  {
    "{": ""      ""Video ID: gvTprv1HF8M""
  },
  {
    "{": ""      ""Video ID: DpBJ0tHSDIc""
  },
  {
    "{": ""      ""Video ID: 6blqhtFvhL8""
  },
  {
    "{": ""      ""Video ID: 03Ti8572JRY""
  },
  {
    "{": ""      ""Video ID: ohC69Mm6AoU""
  },
  {
    "{": ""      ""Video ID: QZzaHl8Mu9M""
  },
  {
    "{": ""      ""Video ID: 71UDP2HVF0g""
  },
  {
    "{": ""      ""Video ID: SAGjfhFP9Xc""
  },
  {
    "{": ""      ""Video ID: qJ5DORBePes""
  },
  {
    "{": ""      ""Video ID: uHYjvVWQa5g""
  },
  {
    "{": ""      ""Video ID: 5mJk28v-NhM""
  },
  {
    "{": ""      ""Video ID: 3yffweMQHrI""
  },
  {
    "{": ""      ""Video ID: 7MFkOcJQUBk""
  },
  {
    "{": ""      ""Video ID: eh4TztMY0gU""
  },
  {
    "{": ""      ""Video ID: ajwBUhfyg7U""
  },
  {
    "{": ""      ""Video ID: SmkO9biZQlc""
  },
  {
    "{": ""      ""Video ID: kZ0T4yXc6HI""
  },
  {
    "{": ""      ""Video ID: TPUxDYvXvwY""
  },
  {
    "{": ""      ""Video ID: DBse5Cupocc""
  },
  {
    "{": ""      ""Video ID: ds-5Ud5KCHM""
  },
  {
    "{": ""      ""Video ID: cp_0XdEBcNc""
  },
  {
    "{": ""      ""Video ID: byl7_AcXO6g""
  },
  {
    "{": ""      ""Video ID: oivjkFNt9xo""
  },
  {
    "{": ""      ""Video ID: xR2bS2rKiQA""
  },
  {
    "{": ""      ""Video ID: s9ds_iGe2rU""
  },
  {
    "{": ""      ""Video ID: ZTCrm6iT2tU""
  },
  {
    "{": ""      ""Video ID: NKpr0qe8dS8""
  },
  {
    "{": ""      ""Video ID: c4n9SBULTN0""
  },
  {
    "{": ""      ""Video ID: vHZ1Z5pdXMA""
  },
  {
    "{": ""      ""Video ID: lNwpcmwAMB4""
  },
  {
    "{": ""      ""Video ID: XS7vJrosqZ0""
  },
  {
    "{": ""      ""Video ID: gmjjK2MYKDg""
  },
  {
    "{": ""      ""Video ID: yFqNy1iJEbg""
  },
  {
    "{": ""      ""Video ID: PNVnFeJ49Rg""
  },
  {
    "{": ""      ""Video ID: 5yHrn5addX8""
  },
  {
    "{": ""      ""Video ID: 4UQ5CHifqMs""
  },
  {
    "{": ""      ""Video ID: L9sDBiu56k0""
  },
  {
    "{": ""      ""Video ID: k5elUcG8zMQ""
  },
  {
    "{": ""      ""Video ID: rd2iL6ha59A""
  },
  {
    "{": ""      ""Video ID: HLROLbkfc5o""
  },
  {
    "{": ""      ""Video ID: tbgj7LCj1Mw""
  },
  {
    "{": ""      ""Video ID: VvfrrK98O10""
  },
  {
    "{": ""      ""Video ID: C5sc9fkraUM""
  },
  {
    "{": ""      ""Video ID: 9fSjNWWvM1I""
  },
  {
    "{": ""      ""Video ID: TpW1YnC-8SY""
  },
  {
    "{": ""      ""Video ID: AEuyGm6qSO4""
  },
  {
    "{": ""      ""Video ID: z4s65I-m32M""
  },
  {
    "{": ""      ""Video ID: oUXR9SmBKPM""
  },
  {
    "{": ""      ""Video ID: tlBZbpg_quY""
  },
  {
    "{": ""      ""Video ID: X-h1Fi2kkYM""
  },
  {
    "{": ""      ""Video ID: F-baNhCSQQ8""
  },
  {
    "{": ""      ""Video ID: RwwyIkhwD94""
  },
  {
    "{": ""      ""Video ID: HUdQgqEEbJs""
  },
  {
    "{": ""      ""Video ID: aphFkjw0jr4""
  },
  {
    "{": ""      ""Video ID: RiqhAi2ntyk""
  },
  {
    "{": ""      ""Video ID: CduoiYOcAYY""
  },
  {
    "{": ""      ""Video ID: -MKPo-WcHFw""
  },
  {
    "{": ""      ""Video ID: Aclvp7G53R8""
  },
  {
    "{": ""      ""Video ID: FVbAiPmRvnc""
  },
  {
    "{": ""      ""Video ID: If9emq1bWmw""
  },
  {
    "{": ""      ""Video ID: 93WhRPbh5Js""
  },
  {
    "{": ""      ""Video ID: uu4kUiXagcY""
  },
  {
    "{": ""      ""Video ID: 88h7A3B60t0""
  },
  {
    "{": ""      ""Video ID: Be9xWVIyu2g""
  },
  {
    "{": ""      ""Video ID: 9PIJgq3DRfg""
  },
  {
    "{": ""      ""Video ID: iMkgzo44Wzg""
  },
  {
    "{": ""      ""Video ID: QSAtTVCif20""
  },
  {
    "{": ""      ""Video ID: m_4dw5uLY3w""
  },
  {
    "{": ""      ""Video ID: sBAZlHiMN-E""
  },
  {
    "{": ""      ""Video ID: IedVRYUNWUU""
  },
  {
    "{": ""      ""Video ID: w7qS5c3WRJk""
  },
  {
    "{": ""      ""Video ID: _X6A8sTg2IE""
  },
  {
    "{": ""      ""Video ID: _U9KPHHNal0""
  },
  {
    "{": ""      ""Video ID: oqEpuTGc98s""
  },
  {
    "{": ""      ""Video ID: l0Zp3_m9mm0""
  },
  {
    "{": ""      ""Video ID: Hjz-n037mMo""
  },
  {
    "{": ""      ""Video ID: 4DJYsg53biY""
  },
  {
    "{": ""      ""Video ID: SYXKhBQDGZY""
  },
  {
    "{": ""      ""Video ID: ZqvJyj5zEzg""
  },
  {
    "{": ""      ""Video ID: AWQQmDaEUQ0""
  },
  {
    "{": ""      ""Video ID: VKHTthoNSpE""
  },
  {
    "{": ""      ""Video ID: 3_Ug3CRvkOc""
  },
  {
    "{": ""      ""Video ID: pk6tWh0oVGY""
  },
  {
    "{": ""      ""Video ID: kLpZEq1gDiE""
  },
  {
    "{": ""      ""Video ID: C9uzpvRzzYQ""
  },
  {
    "{": ""      ""Video ID: RZ5EXXyN_Us""
  },
  {
    "{": ""      ""Video ID: AU9607IVOiY""
  },
  {
    "{": ""      ""Video ID: EhMubEYIsX0""
  },
  {
    "{": ""      ""Video ID: gBJDmlCuzew""
  },
  {
    "{": ""      ""Video ID: uHP4OtIMeIU""
  },
  {
    "{": ""      ""Video ID: 2WO0i2oPLCc""
  },
  {
    "{": ""      ""Video ID: w9eIGMPgrxQ""
  },
  {
    "{": ""      ""Video ID: jfYyuRoeWig""
  },
  {
    "{": ""      ""Video ID: 0gCjWMtLRW4""
  },
  {
    "{": ""      ""Video ID: Zk9CNPu0kRQ""
  },
  {
    "{": ""      ""Video ID: etT5zOp5CW0""
  },
  {
    "{": ""      ""Video ID: NfCdjtoAfjQ""
  },
  {
    "{": ""      ""Video ID: uwt9Bgtylbw""
  },
  {
    "{": ""      ""Video ID: 8t_X-hHhDso""
  },
  {
    "{": ""      ""Video ID: gPWHNWFiLgE""
  },
  {
    "{": ""      ""Video ID: SsVLXUyPhhY""
  },
  {
    "{": ""      ""Video ID: ADbba57PDQk""
  },
  {
    "{": ""      ""Video ID: OlEV0sBUh8I""
  },
  {
    "{": ""      ""Video ID: tkbwWuybv0I""
  },
  {
    "{": ""      ""Video ID: LCw8o05uApk""
  },
  {
    "{": ""      ""Video ID: ZIGAwakixf8""
  },
  {
    "{": ""      ""Video ID: P271yYvmSbo""
  },
  {
    "{": ""      ""Video ID: h8LUkfFzL1s""
  },
  {
    "{": ""      ""Video ID: tXCAhKDZRlo""
  },
  {
    "{": ""      ""Video ID: ZYPgA_9EchA""
  },
  {
    "{": ""      ""Video ID: VrxyIQQR7uY""
  },
  {
    "{": ""      ""Video ID: ZQiihjpFYWg""
  },
  {
    "{": ""      ""Video ID: 98HrSDRvzq4""
  },
  {
    "{": ""      ""Video ID: e7vU8it2bgw""
  },
  {
    "{": ""      ""Video ID: wkqoEKqX_D0""
  },
  {
    "{": ""      ""Video ID: 0BaSm75QnPo""
  },
  {
    "{": ""      ""Video ID: b257WfXYiQE""
  },
  {
    "{": ""      ""Video ID: Fn1P_bwLiEw""
  },
  {
    "{": ""      ""Video ID: u_04LXZLMOE""
  },
  {
    "{": ""      ""Video ID: n7jnvpGACbw""
  },
  {
    "{": ""      ""Video ID: Mh1gcaKP5Bc""
  },
  {
    "{": ""      ""Video ID: wgIH3Ye2RW8""
  },
  {
    "{": ""      ""Video ID: HO4kzH6ZVsU""
  },
  {
    "{": ""      ""Video ID: aPqy8hF4buQ""
  },
  {
    "{": ""      ""Video ID: zqC8nl--g9A""
  },
  {
    "{": ""      ""Video ID: 8uTcd2wp6X8""
  },
  {
    "{": ""      ""Video ID: P_WkenzUj2E""
  },
  {
    "{": ""      ""Video ID: afkd-IbdWL8""
  },
  {
    "{": ""      ""Video ID: dyuFhEoTqSQ""
  },
  {
    "{": ""      ""Video ID: SCpSRClnpVY""
  },
  {
    "{": ""      ""Video ID: YWpdJoWfzXQ""
  },
  {
    "{": ""      ""Video ID: yUpzPnHsSIA""
  },
  {
    "{": ""      ""Video ID: NDAg9JsAt7M""
  },
  {
    "{": ""      ""Video ID: u4-NUozDNuk""
  },
  {
    "{": ""      ""Video ID: QDC5XLpaKZQ""
  },
  {
    "{": ""      ""Video ID: tlagQ4KW5t4""
  },
  {
    "{": ""      ""Video ID: sZQ5C5UU_lg""
  },
  {
    "{": ""      ""Video ID: RYYtTjNhPG4""
  },
  {
    "{": ""      ""Video ID: YW38AKMyNHk""
  },
  {
    "{": ""      ""Video ID: WOPL1EOMrfw""
  },
  {
    "{": ""      ""Video ID: oPtKqMmbtNA""
  },
  {
    "{": ""      ""Video ID: 7kotn1s80Gc""
  },
  {
    "{": ""      ""Video ID: sDRYy6kjqvc""
  },
  {
    "{": ""      ""Video ID: VuVkvpxkjZU""
  },
  {
    "{": ""      ""Video ID: stlZQq1Q1Pc""
  },
  {
    "{": ""      ""Video ID: 5nMvibQ3B98""
  },
  {
    "{": ""      ""Video ID: 68kziYudV8I""
  },
  {
    "{": ""      ""Video ID: AjOMGaPAlLo""
  },
  {
    "{": ""      ""Video ID: cPeH1ePxLYU""
  },
  {
    "{": ""      ""Video ID: stOpGTjVLH8""
  },
  {
    "{": ""      ""Video ID: ea1YXNBpZV8""
  },
  {
    "{": ""      ""Video ID: v5DvdlzLeg4""
  },
  {
    "{": ""      ""Video ID: PjHp6IW_B0g""
  },
  {
    "{": ""      ""Video ID: u8le6fOMZH0""
  },
  {
    "{": ""      ""Video ID: z8cArfOAK5U""
  },
  {
    "{": ""      ""Video ID: dIV8DlxAt6k""
  },
  {
    "{": ""      ""Video ID: tiwCclK3jSo""
  },
  {
    "{": ""      ""Video ID: DYWFWmJ4ols""
  },
  {
    "{": ""      ""Video ID: ud5MrVTKDgw""
  },
  {
    "{": ""      ""Video ID: OLZwiIZqZgk""
  },
  {
    "{": ""      ""Video ID: GCiCSuzv67c""
  },
  {
    "{": ""      ""Video ID: FHYGm8cgQZE""
  },
  {
    "{": ""      ""Video ID: hJcSAsATTl4""
  },
  {
    "{": ""      ""Video ID: JDjCVlDn0mE""
  },
  {
    "{": ""      ""Video ID: 0yJ4qSiy4bk""
  },
  {
    "{": ""      ""Video ID: Jjlng4dQr0A""
  },
  {
    "{": ""      ""Video ID: KV9jLz1Q8bs""
  },
  {
    "{": ""      ""Video ID: VxI_vXlWvvQ""
  },
  {
    "{": ""      ""Video ID: VOVtlX59f8g""
  },
  {
    "{": ""      ""Video ID: JMXgZyUwc_s""
  },
  {
    "{": ""      ""Video ID: 6IT_yRYXdcQ""
  },
  {
    "{": ""      ""Video ID: D-cI7tfTJbU""
  },
  {
    "{": ""      ""Video ID: RzVokmZK0Og""
  },
  {
    "{": ""      ""Video ID: QcCGW-xN5Co""
  },
  {
    "{": ""      ""Video ID: PfazEFd9_YQ""
  },
  {
    "{": ""      ""Video ID: UwlGzOn3S-4""
  },
  {
    "{": ""      ""Video ID: Swwe0TsJCTg""
  },
  {
    "{": ""      ""Video ID: NI5UhZZs1qE""
  },
  {
    "{": ""      ""Video ID: hMzkTDIWtRE""
  },
  {
    "{": ""      ""Video ID: rQjMh1Xwloc""
  },
  {
    "{": ""      ""Video ID: 1NP8uedUPnI""
  },
  {
    "{": ""      ""Video ID: vlfMiKI7DDE""
  },
  {
    "{": ""      ""Video ID: 4hYubrxvVOE""
  },
  {
    "{": ""      ""Video ID: hY3onJoS8c0""
  },
  {
    "{": ""      ""Video ID: DJwrPrq66Y0""
  },
  {
    "{": ""      ""Video ID: NPebFT-Wb50""
  },
  {
    "{": ""      ""Video ID: loKNPuE4ILA""
  },
  {
    "{": ""      ""Video ID: p5_HUpximAs""
  },
  {
    "{": ""      ""Video ID: PSTEyhf37gc""
  },
  {
    "{": ""      ""Video ID: LXx0qrasdTE""
  },
  {
    "{": ""      ""Video ID: TG7Vp_V3JKE""
  },
  {
    "{": ""      ""Video ID: Yx1X3kzH19I""
  },
  {
    "{": ""      ""Video ID: Ir2cQzrGeyE""
  },
  {
    "{": ""      ""Video ID: kGXSkdmi_Ys""
  },
  {
    "{": ""      ""Video ID: AyoMeGVxPwo""
  },
  {
    "{": ""      ""Video ID: iab76GJZMoQ""
  },
  {
    "{": ""      ""Video ID: iCk02Wu0xyk""
  },
  {
    "{": ""      ""Video ID: WZalTkFVTNY""
  },
  {
    "{": ""      ""Video ID: oc9X6gHq5UA""
  },
  {
    "{": ""      ""Video ID: 4sR6q-16iiI""
  },
  {
    "{": ""      ""Video ID: fm3glZtyj3M""
  },
  {
    "{": ""      ""Video ID: NJUfJAx41jc""
  },
  {
    "{": ""      ""Video ID: 2Dtk_SXxOpM""
  },
  {
    "{": ""      ""Video ID: Dmy8CwWJiLQ""
  },
  {
    "{": ""      ""Video ID: Z8RRJ0Q08rQ""
  },
  {
    "{": ""      ""Video ID: N1mZZfbUUuQ""
  },
  {
    "{": ""      ""Video ID: M5-KpqL8RMc""
  },
  {
    "{": ""      ""Video ID: iSJSguSs5_o""
  },
  {
    "{": ""      ""Video ID: oMlP33DPHOA""
  },
  {
    "{": ""      ""Video ID: cztsT9hDU0k""
  },
  {
    "{": ""      ""Video ID: n_V9JyhOyek""
  },
  {
    "{": ""      ""Video ID: 6nrOCYyw7Ck""
  },
  {
    "{": ""      ""Video ID: DSnAalqrUzs""
  },
  {
    "{": ""      ""Video ID: i5U171yzSa8""
  },
  {
    "{": ""      ""Video ID: tz8OKw_mRgw""
  },
  {
    "{": ""      ""Video ID: 7UN9axsc0U4""
  },
  {
    "{": ""      ""Video ID: uDg_bN2wxgo""
  },
  {
    "{": ""      ""Video ID: bw3eRZSvkH8""
  },
  {
    "{": ""      ""Video ID: ZTMMKak-NLI""
  },
  {
    "{": ""      ""Video ID: xqSLWMnc8-c""
  },
  {
    "{": ""      ""Video ID: 45k0Qr_4Hf4""
  },
  {
    "{": ""      ""Video ID: LvfPHt0IsS0""
  },
  {
    "{": ""      ""Video ID: VT9H5CK9thE""
  },
  {
    "{": ""      ""Video ID: lftV5-1Oh0A""
  },
  {
    "{": ""      ""Video ID: YJ7mQ6iRs8A""
  },
  {
    "{": ""      ""Video ID: wWYCnYZW3Zw""
  },
  {
    "{": ""      ""Video ID: fjVrQWilQVA""
  },
  {
    "{": ""      ""Video ID: qJdvDQqDp3E""
  },
  {
    "{": ""      ""Video ID: ggAZBX7QxWw""
  },
  {
    "{": ""      ""Video ID: 25yhygUkecE""
  },
  {
    "{": ""      ""Video ID: y9fUFF0YwPo""
  },
  {
    "{": ""      ""Video ID: CzzUz5APe2Y""
  },
  {
    "{": ""      ""Video ID: yJoIbPkRvig""
  },
  {
    "{": ""      ""Video ID: tQzp1aMhs-E""
  },
  {
    "{": ""      ""Video ID: ISW9sXP_Sik""
  },
  {
    "{": ""      ""Video ID: zQ27ucTdQaI""
  },
  {
    "{": ""      ""Video ID: HA6zNeM3I_M""
  },
  {
    "{": ""      ""Video ID: nzYd7Iq9xyM""
  },
  {
    "{": ""      ""Video ID: Vk064nSwPCI""
  },
  {
    "{": ""      ""Video ID: 54NV4w1yxu8""
  },
  {
    "{": ""      ""Video ID: SSKS9a9NuPc""
  },
  {
    "{": ""      ""Video ID: 8tHSrovtJF0""
  },
  {
    "{": ""      ""Video ID: no4luPP6t9c""
  },
  {
    "{": ""      ""Video ID: 7kmplpguPTs""
  },
  {
    "{": ""      ""Video ID: G2wiGCdYoYY""
  },
  {
    "{": ""      ""Video ID: c8PM8ZK-GBo""
  },
  {
    "{": ""      ""Video ID: -5nvARS2bus""
  },
  {
    "{": ""      ""Video ID: EFooJ1L2FbY""
  },
  {
    "{": ""      ""Video ID: DsqIr2bcX7w""
  },
  {
    "{": ""      ""Video ID: zEqrViynPwU""
  },
  {
    "{": ""      ""Video ID: YLSiArb3WVg""
  },
  {
    "{": ""      ""Video ID: wVDVH-2igbw""
  },
  {
    "{": ""      ""Video ID: VBbq6Sxpdjk""
  },
  {
    "{": ""      ""Video ID: 1i_YRZQAxAU""
  },
  {
    "{": ""      ""Video ID: 6Wcx2qM5C4g""
  },
  {
    "{": ""      ""Video ID: WzrCXHvNwFo""
  },
  {
    "{": ""      ""Video ID: tWQjB1oy6fA""
  },
  {
    "{": ""      ""Video ID: mS3H6Qjq0k8""
  },
  {
    "{": ""      ""Video ID: QV-j1YmxO6E""
  },
  {
    "{": ""      ""Video ID: Oweqs_KINvk""
  },
  {
    "{": ""      ""Video ID: YyyRufTXk_A""
  },
  {
    "{": ""      ""Video ID: JOC869ADF2U""
  },
  {
    "{": ""      ""Video ID: Aj0X8B05QxU""
  },
  {
    "{": ""      ""Video ID: LS4YWSdgCcQ""
  },
  {
    "{": ""      ""Video ID: kqVKO71uQ_Q""
  },
  {
    "{": ""      ""Video ID: CTeLISbb3e0""
  },
  {
    "{": ""      ""Video ID: yqOiGsUqkpc""
  },
  {
    "{": ""      ""Video ID: zPwAaG-PhYQ""
  },
  {
    "{": ""      ""Video ID: Aa5ygNips3M""
  },
  {
    "{": ""      ""Video ID: HFTFH4MlHDE""
  },
  {
    "{": ""      ""Video ID: N-3BudGLN7Q""
  },
  {
    "{": ""      ""Video ID: ptGbZUlYVD4""
  },
  {
    "{": ""      ""Video ID: TLvTUufDz5c""
  },
  {
    "{": ""      ""Video ID: Cne6UCRSOJk""
  },
  {
    "{": ""      ""Video ID: 3aWm5Nqu4R8""
  },
  {
    "{": ""      ""Video ID: yrgGp2jaafs""
  },
  {
    "{": ""      ""Video ID: 21dfilSok-A""
  },
  {
    "{": ""      ""Video ID: A2n-_FZhb3o""
  },
  {
    "{": ""      ""Video ID: CfJzyUivMS8""
  },
  {
    "{": ""      ""Video ID: El-EM1EGOb0""
  },
  {
    "{": ""      ""Video ID: 0J-WGDF2d1I""
  },
  {
    "{": ""      ""Video ID: WaavtzDNRzo""
  },
  {
    "{": ""      ""Video ID: h4UyJJsxfQ4""
  },
  {
    "{": ""      ""Video ID: U3dO-tDhIq4""
  },
  {
    "{": ""      ""Video ID: vmijkb4B7Xs""
  },
  {
    "{": ""      ""Video ID: 6TAJD6UV7WQ""
  },
  {
    "{": ""      ""Video ID: taCuSVodpnI""
  },
  {
    "{": ""      ""Video ID: 1RBVb1aVLDA""
  },
  {
    "{": ""      ""Video ID: JIySripTLio""
  },
  {
    "{": ""      ""Video ID: JI7o2Uq97P4""
  },
  {
    "{": ""      ""Video ID: McC__1mXojw""
  },
  {
    "{": ""      ""Video ID: OONNAO2hIoU""
  },
  {
    "{": ""      ""Video ID: xUoMVFVeTVY""
  },
  {
    "{": ""      ""Video ID: qFjgOa2xsY4""
  },
  {
    "{": ""      ""Video ID: HWQht5O71cM""
  },
  {
    "{": ""      ""Video ID: K7ZbtKbXE1s""
  },
  {
    "{": ""      ""Video ID: wCMXZBVP9io""
  },
  {
    "{": ""      ""Video ID: jTB6tnq__Ww""
  },
  {
    "{": ""      ""Video ID: xDZseim1_w0""
  },
  {
    "{": ""      ""Video ID: 3sbG1ML-hlE""
  },
  {
    "{": ""      ""Video ID: Lzrvf1SQ1CA""
  },
  {
    "{": ""      ""Video ID: _xy4qHXjFis""
  },
  {
    "{": ""      ""Video ID: 97ti0pcRp4E""
  },
  {
    "{": ""      ""Video ID: uNlqpZwtle8""
  },
  {
    "{": ""      ""Video ID: nPySVh4BI1w""
  },
  {
    "{": ""      ""Video ID: xoJ6tSKRkFo""
  },
  {
    "{": ""      ""Video ID: 7txo4EIpIJM""
  },
  {
    "{": ""      ""Video ID: bR24G_v3bXM""
  },
  {
    "{": ""      ""Video ID: e6PIzEeanNU""
  },
  {
    "{": ""      ""Video ID: _z-hEyVQDRA""
  },
  {
    "{": ""      ""Video ID: N3HJXTiY_ZY""
  },
  {
    "{": ""      ""Video ID: sJwZvuaNXIg""
  },
  {
    "{": ""      ""Video ID: dvX4i5dpogU""
  },
  {
    "{": ""      ""Video ID: 5XHtoFjnv4U""
  },
  {
    "{": ""      ""Video ID: BNszEHjmoK8""
  },
  {
    "{": ""      ""Video ID: YHJQ1gn4bDg""
  },
  {
    "{": ""      ""Video ID: eI6yOBw-x-o""
  },
  {
    "{": ""      ""Video ID: uAiRngXjo3U""
  },
  {
    "{": ""      ""Video ID: aol6Wx-ox6A""
  },
  {
    "{": ""      ""Video ID: uUDMUVSt79A""
  },
  {
    "{": ""      ""Video ID: UZiT2cEXkCo""
  },
  {
    "{": ""      ""Video ID: zCjvU3d6tQo""
  },
  {
    "{": ""      ""Video ID: Rnuk0BeSsmw""
  },
  {
    "{": ""      ""Video ID: kTBVm6xV_hc""
  },
  {
    "{": ""      ""Video ID: nqR5eLUg1qw""
  },
  {
    "{": ""      ""Video ID: Fwc34GPrGT0""
  },
  {
    "{": ""      ""Video ID: 3-b7NPtmwNA""
  },
  {
    "{": ""      ""Video ID: eSo30SfDBSM""
  },
  {
    "{": ""      ""Video ID: UevoqJ8A5RU""
  },
  {
    "{": ""      ""Video ID: uhB77FXpP1E""
  },
  {
    "{": ""      ""Video ID: oVOtyeOL5q8""
  },
  {
    "{": ""      ""Video ID: coZ3yonR3Kk""
  },
  {
    "{": ""      ""Video ID: bw70-pRryPY""
  },
  {
    "{": ""      ""Video ID: d8TqOZY3kn4""
  },
  {
    "{": ""      ""Video ID: edWJqev0eWY""
  },
  {
    "{": ""      ""Video ID: zCaD_EpPlQc""
  },
  {
    "{": ""      ""Video ID: iNQ497fvklI""
  },
  {
    "{": ""      ""Video ID: JqIJr5mMxo4""
  },
  {
    "{": ""      ""Video ID: GuEuGZhD1xA""
  },
  {
    "{": ""      ""Video ID: 5HN0jVfuyR4""
  },
  {
    "{": ""      ""Video ID: NMfISV7t5vU""
  },
  {
    "{": ""      ""Video ID: V0G6y_itBPQ""
  },
  {
    "{": ""      ""Video ID: 4Lm2li2of98""
  },
  {
    "{": ""      ""Video ID: FwwMLUULl5s""
  },
  {
    "{": ""      ""Video ID: Ft9QzpXu228""
  },
  {
    "{": ""      ""Video ID: -zrmNPGK8wI""
  },
  {
    "{": ""      ""Video ID: gHlRi28h0Ew""
  },
  {
    "{": ""      ""Video ID: grTLYl-LtBE""
  },
  {
    "{": ""      ""Video ID: 37x75USzFl4""
  },
  {
    "{": ""      ""Video ID: RfKZP_jRgQY""
  },
  {
    "{": ""      ""Video ID: v3W9bUFksc4""
  },
  {
    "{": ""      ""Video ID: POw2rDAtHcI""
  },
  {
    "{": ""      ""Video ID: 05xVcdg7HE4""
  },
  {
    "{": ""      ""Video ID: 513YC1s4cFA""
  },
  {
    "{": ""      ""Video ID: q3__DUte2hI""
  },
  {
    "{": ""      ""Video ID: 5ZKCA2azp8M""
  },
  {
    "{": ""      ""Video ID: yeXouB19Yr8""
  },
  {
    "{": ""      ""Video ID: E2hMw_iRoUQ""
  },
  {
    "{": ""      ""Video ID: 2fnX40CHsGk""
  },
  {
    "{": ""      ""Video ID: RQz5kcwgtl0""
  },
  {
    "{": ""      ""Video ID: 1lPHMdSI_RM""
  },
  {
    "{": ""      ""Video ID: NiznR1nRc1o""
  },
  {
    "{": ""      ""Video ID: bdxSuvoPXcc""
  },
  {
    "{": ""      ""Video ID: 2admL3roqSc""
  },
  {
    "{": ""      ""Video ID: zQ3cmoyiYaM""
  },
  {
    "{": ""      ""Video ID: 5shL7orMZ2o""
  },
  {
    "{": ""      ""Video ID: j-VWTAHOMWQ""
  },
  {
    "{": ""      ""Video ID: 9GecWl2x71s""
  },
  {
    "{": ""      ""Video ID: V3TFKEKB5NE""
  },
  {
    "{": ""      ""Video ID: hfHGPzEUJ0g""
  },
  {
    "{": ""      ""Video ID: aSxD4XbXn1o""
  },
  {
    "{": ""      ""Video ID: KPBe_MaZSPk""
  },
  {
    "{": ""      ""Video ID: 2F21MJsLeOc""
  },
  {
    "{": ""      ""Video ID: 9B6uzrGr7Yo""
  },
  {
    "{": ""      ""Video ID: T_Rzmdu3cFg""
  },
  {
    "{": ""      ""Video ID: FmpwI9Vq8es""
  },
  {
    "{": ""      ""Video ID: 95XbknUw7dQ""
  },
  {
    "{": ""      ""Video ID: i8m6Mn4-dl8""
  },
  {
    "{": ""      ""Video ID: yUsSBLscaEQ""
  },
  {
    "{": ""      ""Video ID: WLXgCoeB-QU""
  },
  {
    "{": ""      ""Video ID: f8kR8gBfozk""
  },
  {
    "{": ""      ""Video ID: AfpoxsXX8zQ""
  },
  {
    "{": ""      ""Video ID: 1BPD8FY00nw""
  },
  {
    "{": ""      ""Video ID: dzZbCqLYjqA""
  },
  {
    "{": ""      ""Video ID: iwuHVnmSW5g""
  },
  {
    "{": ""      ""Video ID: 7SX-jUyOzrc""
  },
  {
    "{": ""      ""Video ID: 1O4VF43h_lg""
  },
  {
    "{": ""      ""Video ID: fdvo4p4PHBU""
  },
  {
    "{": ""      ""Video ID: pNDyOyvr6jA""
  },
  {
    "{": ""      ""Video ID: bNKyrmZIhCU""
  },
  {
    "{": ""      ""Video ID: bSgEgeRzNck""
  },
  {
    "{": ""      ""Video ID: yWEmlungJK8""
  },
  {
    "{": ""      ""Video ID: uZ52sX2SVe4""
  },
  {
    "{": ""      ""Video ID: A3eReO7336w""
  },
  {
    "{": ""      ""Video ID: ZwZrgi3ZwZs""
  },
  {
    "{": ""      ""Video ID: BjEQf79O0AM""
  },
  {
    "{": ""      ""Video ID: XCsbBko6Q68""
  },
  {
    "{": ""      ""Video ID: qXOFWoXOAs0""
  },
  {
    "{": ""      ""Video ID: yrkNf5Y7KLg""
  },
  {
    "{": ""      ""Video ID: EDa865k_V38""
  },
  {
    "{": ""      ""Video ID: OlnE4K_krv0""
  },
  {
    "{": ""      ""Video ID: Fu3RpqZ5xCA""
  },
  {
    "{": ""      ""Video ID: TUcatA4t3EQ""
  },
  {
    "{": ""      ""Video ID: 0Z_gZahMHJ8""
  },
  {
    "{": ""      ""Video ID: HoMbn3WAfb0""
  },
  {
    "{": ""      ""Video ID: hAU_47vwJQM""
  },
  {
    "{": ""      ""Video ID: Ql1-ANoqINY""
  },
  {
    "{": ""      ""Video ID: kqFZEHgZMa0""
  },
  {
    "{": ""      ""Video ID: Vihf-CdxM-c""
  },
  {
    "{": ""      ""Video ID: l1iBOBi4lPE""
  },
  {
    "{": ""      ""Video ID: 9MAeyBwjxUA""
  },
  {
    "{": ""      ""Video ID: R99tlybH8cM""
  },
  {
    "{": ""      ""Video ID: -qOoyphMdjI""
  },
  {
    "{": ""      ""Video ID: OcC0o6OC-hk""
  },
  {
    "{": ""      ""Video ID: k8iIs1-Aeu4""
  },
  {
    "{": ""      ""Video ID: VIUfJnR0OzM""
  },
  {
    "{": ""      ""Video ID: MUyAo1xKP2w""
  },
  {
    "{": ""      ""Video ID: OcJ9vxxJq_g""
  },
  {
    "{": ""      ""Video ID: Frx9LBFZbOI""
  },
  {
    "{": ""      ""Video ID: YkHDCOqs_K0""
  },
  {
    "{": ""      ""Video ID: 4Kr2XiS_jts""
  },
  {
    "{": ""      ""Video ID: HxGrWLCB57k""
  },
  {
    "{": ""      ""Video ID: P8b1LpsYnBM""
  },
  {
    "{": ""      ""Video ID: 50AQcwGdH3c""
  },
  {
    "{": ""      ""Video ID: FmS9ga49IJc""
  },
  {
    "{": ""      ""Video ID: TjxeIRQE5eY""
  },
  {
    "{": ""      ""Video ID: Sf_mldqnQ-Q""
  },
  {
    "{": ""      ""Video ID: U_7JHrP8rKk""
  },
  {
    "{": ""      ""Video ID: lfIqdD_tV_E""
  },
  {
    "{": ""      ""Video ID: 7wRVeauOLSM""
  },
  {
    "{": ""      ""Video ID: bydd_7yDEVQ""
  },
  {
    "{": ""      ""Video ID: rJKCGC-86Qc""
  },
  {
    "{": ""      ""Video ID: T--tdydb_Us""
  },
  {
    "{": ""      ""Video ID: jPEJ1JYbecU""
  },
  {
    "{": ""      ""Video ID: K5r4_vttWmg""
  },
  {
    "{": ""      ""Video ID: 1vWldQSRi08""
  },
  {
    "{": ""      ""Video ID: 4G1_QfBt4-Y""
  },
  {
    "{": ""      ""Video ID: 11M1Xd0XOfs""
  },
  {
    "{": ""      ""Video ID: ZMbk9b559Bk""
  },
  {
    "{": ""      ""Video ID: I0q3ZWcEVVM""
  },
  {
    "{": ""      ""Video ID: kZRgdgkDI7U""
  },
  {
    "{": ""      ""Video ID: FAvhNcIRYi8""
  },
  {
    "{": ""      ""Video ID: eiNH6a3WKLA""
  },
  {
    "{": ""      ""Video ID: WsbIGArYTRw""
  },
  {
    "{": ""      ""Video ID: IJRfxW6OWzk""
  },
  {
    "{": ""      ""Video ID: Gq_IxOXTZU4""
  },
  {
    "{": ""      ""Video ID: qI1Qu5MLPt4""
  },
  {
    "{": ""      ""Video ID: on-nY3d8KUI""
  },
  {
    "{": ""      ""Video ID: BqIOdzdTUCY""
  },
  {
    "{": ""      ""Video ID: 7zXZIJyOhE4""
  },
  {
    "{": ""      ""Video ID: C22YGSOgaQk""
  },
  {
    "{": ""      ""Video ID: GwJ8HvMusJA""
  },
  {
    "{": ""      ""Video ID: nUdmw1cxRlk""
  },
  {
    "{": ""      ""Video ID: 3Wfol7ES_hY""
  },
  {
    "{": ""      ""Video ID: AyP2Y6Icu54""
  },
  {
    "{": ""      ""Video ID: iVtECrWTvlA""
  },
  {
    "{": ""      ""Video ID: swJ0zhVJ8DU""
  },
  {
    "{": ""      ""Video ID: BfyXDekObKI""
  },
  {
    "{": ""      ""Video ID: n72cCLjJ6mg""
  },
  {
    "{": ""      ""Video ID: YkidS0Wb_fA""
  },
  {
    "{": ""      ""Video ID: 4sj7aFovukY""
  },
  {
    "{": ""      ""Video ID: 0wG0fmYbhyk""
  },
  {
    "{": ""      ""Video ID: ZdawcKFz2Cw""
  },
  {
    "{": ""      ""Video ID: s1kXZkaWxrM""
  },
  {
    "{": ""      ""Video ID: W0pOPK0eN9E""
  },
  {
    "{": ""      ""Video ID: kc8x_iFHSIM""
  },
  {
    "{": ""      ""Video ID: 5GNzBFnUAdo""
  },
  {
    "{": ""      ""Video ID: xiMZAPIfZxI""
  },
  {
    "{": ""      ""Video ID: Zdj9vMH4BfQ""
  },
  {
    "{": ""      ""Video ID: 2XCyk6sXkJg""
  },
  {
    "{": ""      ""Video ID: XrSyWBd-exY""
  },
  {
    "{": ""      ""Video ID: ayzhJKy8H_A""
  },
  {
    "{": ""      ""Video ID: tTaOvzZKRxA""
  },
  {
    "{": ""      ""Video ID: 0rhERCJKMr4""
  },
  {
    "{": ""      ""Video ID: uRaCv4Njcnk""
  },
  {
    "{": ""      ""Video ID: o-HEEW7YVNM""
  },
  {
    "{": ""      ""Video ID: 22fSspZCA-c""
  },
  {
    "{": ""      ""Video ID: Mc_rid8O0cw""
  },
  {
    "{": ""      ""Video ID: 3dFp_5P6hzE""
  },
  {
    "{": ""      ""Video ID: P2BfzUIBy9A""
  },
  {
    "{": ""      ""Video ID: t8OAlj4WEI0""
  },
  {
    "{": ""      ""Video ID: e7QrBwANSDs""
  },
  {
    "{": ""      ""Video ID: bhLbFGVduTA""
  },
  {
    "{": ""      ""Video ID: DgGZL_rAR8U""
  },
  {
    "{": ""      ""Video ID: eLNY4hEcqpk""
  },
  {
    "{": ""      ""Video ID: ASVQFzJ47uA""
  },
  {
    "{": ""      ""Video ID: Q26UaEYTt2g""
  },
  {
    "{": ""      ""Video ID: e8N-h8anSuE""
  },
  {
    "{": ""      ""Video ID: 9SNhpY6gjLw""
  },
  {
    "{": ""      ""Video ID: rwo8ySt4qXo""
  },
  {
    "{": ""      ""Video ID: 45-30_dCo6E""
  },
  {
    "{": ""      ""Video ID: F4jq_sucA34""
  },
  {
    "{": ""      ""Video ID: pFj0HdW2iDs""
  },
  {
    "{": ""      ""Video ID: LRDQYbTbUzg""
  },
  {
    "{": ""      ""Video ID: c_WE-1sWfmk""
  },
  {
    "{": ""      ""Video ID: Mj7bevpgM80""
  },
  {
    "{": ""      ""Video ID: ruwF_fm1V-Y""
  },
  {
    "{": ""      ""Video ID: IremtcSrc1A""
  },
  {
    "{": ""      ""Video ID: Epa-BXFfXJs""
  },
  {
    "{": ""      ""Video ID: XN_Hcirqrmo""
  },
  {
    "{": ""      ""Video ID: pbzrBzPyVdw""
  },
  {
    "{": ""      ""Video ID: eagtTkBlX9M""
  },
  {
    "{": ""      ""Video ID: GRR1q0IJyIs""
  },
  {
    "{": ""      ""Video ID: EpamEiuzAVo""
  },
  {
    "{": ""      ""Video ID: NDfyh2eak0o""
  },
  {
    "{": ""      ""Video ID: 1jqHEnZhpmA""
  },
  {
    "{": ""      ""Video ID: opewE7wNlnc""
  },
  {
    "{": ""      ""Video ID: 87WMymeERaU""
  },
  {
    "{": ""      ""Video ID: vd_iqoStcYg""
  },
  {
    "{": ""      ""Video ID: k9CLsmA8lto""
  },
  {
    "{": ""      ""Video ID: MH52c46XYZQ""
  },
  {
    "{": ""      ""Video ID: vXvNYmm-ciQ""
  },
  {
    "{": ""      ""Video ID: jC-8mp1y25s""
  },
  {
    "{": ""      ""Video ID: G6G9aMZoNcU""
  },
  {
    "{": ""      ""Video ID: J4oPPApzGRk""
  },
  {
    "{": ""      ""Video ID: OpKZsYgOnLc""
  },
  {
    "{": ""      ""Video ID: qHHkfNCPAZc""
  },
  {
    "{": ""      ""Video ID: w4m7RIgm7O4""
  },
  {
    "{": ""      ""Video ID: 920Sfbhb-ps""
  },
  {
    "{": ""      ""Video ID: 8tFuDqRdGu0""
  },
  {
    "{": ""      ""Video ID: z2l8O1JUrRo""
  },
  {
    "{": ""      ""Video ID: vBGIdf0VjQ4""
  },
  {
    "{": ""      ""Video ID: 825hY4rjRQk""
  },
  {
    "{": ""      ""Video ID: 4WRhQVfp6VQ""
  },
  {
    "{": ""      ""Video ID: FnBYHhmxdvs""
  },
  {
    "{": ""      ""Video ID: EY0KKZoDWOg""
  },
  {
    "{": ""      ""Video ID: MztMk44i-P8""
  },
  {
    "{": ""      ""Video ID: n872GcUigKo""
  },
  {
    "{": ""      ""Video ID: 2eJHX7xlmVk""
  },
  {
    "{": ""      ""Video ID: ZbdrouHCWxQ""
  },
  {
    "{": ""      ""Video ID: y5o7UEKAVKI""
  },
  {
    "{": ""      ""Video ID: MFf9fyWHAkw""
  },
  {
    "{": ""      ""Video ID: zG5scsSdALg""
  },
  {
    "{": ""      ""Video ID: iIWobhtJe7Y""
  },
  {
    "{": ""      ""Video ID: KD5RAAXEHRw""
  },
  {
    "{": ""      ""Video ID: E0Sn1cjvp7s""
  },
  {
    "{": ""      ""Video ID: t_WKgfnf0dU""
  },
  {
    "{": ""      ""Video ID: 0RfzDSKAE5M""
  },
  {
    "{": ""      ""Video ID: T-IJKXylOTs""
  },
  {
    "{": ""      ""Video ID: qsWI96NxHpQ""
  },
  {
    "{": ""      ""Video ID: GTsM-X6soPw""
  },
  {
    "{": ""      ""Video ID: wpyj9oxZ5TE""
  },
  {
    "{": ""      ""Video ID: r0VUXLsBSjo""
  },
  {
    "{": ""      ""Video ID: z3RJr4Gq00Y""
  },
  {
    "{": ""      ""Video ID: lmPCDtrt_6Q""
  },
  {
    "{": ""      ""Video ID: YDbKuBEgWAQ""
  },
  {
    "{": ""      ""Video ID: em_XyTeNA1g""
  },
  {
    "{": ""      ""Video ID: yIgoXQWiSlM""
  },
  {
    "{": ""      ""Video ID: x9lwvImJqT0""
  },
  {
    "{": ""      ""Video ID: 2aW2N46vf4Q""
  },
  {
    "{": ""      ""Video ID: iEuJimaumW4""
  },
  {
    "{": ""      ""Video ID: EgJuHNfk7no""
  },
  {
    "{": ""      ""Video ID: nnnjIzamnJo""
  },
  {
    "{": ""      ""Video ID: 1kxE6lftTWU""
  },
  {
    "{": ""      ""Video ID: 9yTgbZSATTU""
  },
  {
    "{": ""      ""Video ID: e0d_KG7I6o8""
  },
  {
    "{": ""      ""Video ID: b5JVYTxjmdc""
  },
  {
    "{": ""      ""Video ID: iFqYf-ID5oY""
  },
  {
    "{": ""      ""Video ID: puWqNJI8Mjo""
  },
  {
    "{": ""      ""Video ID: QF4CQeK91bk""
  },
  {
    "{": ""      ""Video ID: uM3gisJiNkI""
  },
  {
    "{": ""      ""Video ID: O0_wrpgbIDE""
  },
  {
    "{": ""      ""Video ID: VrJX53n1eGk""
  },
  {
    "{": ""      ""Video ID: tvL9jG_vmNw""
  },
  {
    "{": ""      ""Video ID: mgiRtTxNp_o""
  },
  {
    "{": ""      ""Video ID: NHbI3EAf88k""
  },
  {
    "{": ""      ""Video ID: jj6FyqVwm98""
  },
  {
    "{": ""      ""Video ID: JNsZWLgHlSI""
  },
  {
    "{": ""      ""Video ID: ccIJ39u1fTI""
  },
  {
    "{": ""      ""Video ID: qWCruBWp-PQ""
  },
  {
    "{": ""      ""Video ID: ZJDK6ctRjqw""
  },
  {
    "{": ""      ""Video ID: LI_jWbfUKbo""
  },
  {
    "{": ""      ""Video ID: g1Qp-hY_Zsk""
  },
  {
    "{": ""      ""Video ID: gLQefJiE89o""
  },
  {
    "{": ""      ""Video ID: dGYqbAK36-4""
  },
  {
    "{": ""      ""Video ID: rnlPaSkTObY""
  },
  {
    "{": ""      ""Video ID: VRAh3Qse-Us""
  },
  {
    "{": ""      ""Video ID: VLCzta7BROE""
  },
  {
    "{": ""      ""Video ID: JZuMak6Ne6M""
  },
  {
    "{": ""      ""Video ID: a2-9lD4xvgo""
  },
  {
    "{": ""      ""Video ID: zT984NrRHEY""
  },
  {
    "{": ""      ""Video ID: 9JVv68C4e7w""
  },
  {
    "{": ""      ""Video ID: _-r_p2u39_I""
  },
  {
    "{": ""      ""Video ID: SIrhLdyeOh0""
  },
  {
    "{": ""      ""Video ID: KZZYZlvXO_o""
  },
  {
    "{": ""      ""Video ID: KzjMIcER4EU""
  },
  {
    "{": ""      ""Video ID: jKZuucQIlD8""
  },
  {
    "{": ""      ""Video ID: SFn7syPIbfM""
  },
  {
    "{": ""      ""Video ID: vmixsFpgD6A""
  },
  {
    "{": ""      ""Video ID: Moe5YEuZWwg""
  },
  {
    "{": ""      ""Video ID: Jfr8JQbCix0""
  },
  {
    "{": ""      ""Video ID: Xyqt185Y2BU""
  },
  {
    "{": ""      ""Video ID: 8PanH0HQMIQ""
  },
  {
    "{": ""      ""Video ID: YCyh87ivzc0""
  },
  {
    "{": ""      ""Video ID: uWhghph7FH8""
  },
  {
    "{": ""      ""Video ID: pLWZIUd8x6E""
  },
  {
    "{": ""      ""Video ID: TBIwr39CS8M""
  },
  {
    "{": ""      ""Video ID: SJ_qK4g6ntM""
  },
  {
    "{": ""      ""Video ID: msE6Mv5-5zw""
  },
  {
    "{": ""      ""Video ID: 6zgXWOG7qns""
  },
  {
    "{": ""      ""Video ID: JQL1nC8HpLc""
  },
  {
    "{": ""      ""Video ID: cXBdupZZMEM""
  },
  {
    "{": ""      ""Video ID: 6TO61nHlgBk""
  },
  {
    "{": ""      ""Video ID: xGH_OcRGkzo""
  },
  {
    "{": ""      ""Video ID: zc1JT5BIogg""
  },
  {
    "{": ""      ""Video ID: vweGmpo0r0w""
  },
  {
    "{": ""      ""Video ID: Jsdoko6bEbA""
  },
  {
    "{": ""      ""Video ID: ntmKX7xpqgc""
  },
  {
    "{": ""      ""Video ID: wqtGos5CT0o""
  },
  {
    "{": ""      ""Video ID: X5gdpPIdV5k""
  },
  {
    "{": ""      ""Video ID: WPcXqf1kjec""
  },
  {
    "{": ""      ""Video ID: TTEmnMtG4wI""
  },
  {
    "{": ""      ""Video ID: 3t7kfD6NVrc""
  },
  {
    "{": ""      ""Video ID: XG1oqPs_6jM""
  },
  {
    "{": ""      ""Video ID: -RBxoJuYFtE""
  },
  {
    "{": ""      ""Video ID: 2awrJWfiNks""
  },
  {
    "{": ""      ""Video ID: pUycenwpF-s""
  },
  {
    "{": ""      ""Video ID: UcHrs4MXuzQ""
  },
  {
    "{": ""      ""Video ID: Bh_bmav6SCI""
  },
  {
    "{": ""      ""Video ID: JWrNXYyKvz0""
  },
  {
    "{": ""      ""Video ID: z2fz04ARa60""
  },
  {
    "{": ""      ""Video ID: B5C2UCLpn6c""
  },
  {
    "{": ""      ""Video ID: NGADHZ20374""
  },
  {
    "{": ""      ""Video ID: Em2ga83nGnA""
  },
  {
    "{": ""      ""Video ID: av0JeNtDHfQ""
  },
  {
    "{": ""      ""Video ID: VprYtT2XYlE""
  },
  {
    "{": ""      ""Video ID: QQajt3lpIBw""
  },
  {
    "{": ""      ""Video ID: gQbgtOgARis""
  },
  {
    "{": ""      ""Video ID: 3wmfMR_tT4g""
  },
  {
    "{": ""      ""Video ID: RdnCvu_qMRY""
  },
  {
    "{": ""      ""Video ID: t8uiF-Ryfw0""
  },
  {
    "{": ""      ""Video ID: XMcbDQHavac""
  },
  {
    "{": ""      ""Video ID: K50sQHKeMR4""
  },
  {
    "{": ""      ""Video ID: vlSgXkh0J8I""
  },
  {
    "{": ""      ""Video ID: UUMytG9EGUA""
  },
  {
    "{": ""      ""Video ID: 1SAfVZ70-Cw""
  },
  {
    "{": ""      ""Video ID: 2HU_AJbx10Q""
  },
  {
    "{": ""      ""Video ID: FRcohIdp-9k""
  },
  {
    "{": ""      ""Video ID: cilZuY1av-o""
  },
  {
    "{": ""      ""Video ID: 1dMF3ZCoIdI""
  },
  {
    "{": ""      ""Video ID: oDEg88Lc_zM""
  },
  {
    "{": ""      ""Video ID: PalfzR8QtU0""
  },
  {
    "{": ""      ""Video ID: 6D1tKFhmlm8""
  },
  {
    "{": ""      ""Video ID: Ut4CkdpH7ww""
  },
  {
    "{": ""      ""Video ID: V8UD6o4-OLg""
  },
  {
    "{": ""      ""Video ID: 26UkxVNI1OI""
  },
  {
    "{": ""      ""Video ID: iluw2zBO17c""
  },
  {
    "{": ""      ""Video ID: 6_jMqriLTIA""
  },
  {
    "{": ""      ""Video ID: l6z7tiZLW14""
  },
  {
    "{": ""      ""Video ID: sJPJbhk2y1M""
  },
  {
    "{": ""      ""Video ID: -raUJXj4SIw""
  },
  {
    "{": ""      ""Video ID: cmYbTBEzL-g""
  },
  {
    "{": ""      ""Video ID: L0P_dc1Geao""
  },
  {
    "{": ""      ""Video ID: isns9TYWm-o""
  },
  {
    "{": ""      ""Video ID: XxOdFnTn0gQ""
  },
  {
    "{": ""      ""Video ID: nV7F6C9aBTU""
  },
  {
    "{": ""      ""Video ID: 9VGMs9sVuX8""
  },
  {
    "{": ""      ""Video ID: nxM-xg3Y33o""
  },
  {
    "{": ""      ""Video ID: eiqM75akZnM""
  },
  {
    "{": ""      ""Video ID: hUUXcr45OIA""
  },
  {
    "{": ""      ""Video ID: KIcbAjZX9FQ""
  },
  {
    "{": ""      ""Video ID: bIIXawbx1pQ""
  },
  {
    "{": ""      ""Video ID: 2C1x8nTGJac""
  },
  {
    "{": ""      ""Video ID: M0YEy0jwE_o""
  },
  {
    "{": ""      ""Video ID: lfxVMxKvs-8""
  },
  {
    "{": ""      ""Video ID: Uynrjc5ZuW8""
  },
  {
    "{": ""      ""Video ID: 2_353cKIvis""
  },
  {
    "{": ""      ""Video ID: rj26BZUDfLU""
  },
  {
    "{": ""      ""Video ID: oV39sQ46h28""
  },
  {
    "{": ""      ""Video ID: Eh3-X2jfFxE""
  },
  {
    "{": ""      ""Video ID: xPB7kM4Gbxg""
  },
  {
    "{": ""      ""Video ID: eEaX3h-PtsU""
  },
  {
    "{": ""      ""Video ID: _56r_Jwr6TI""
  },
  {
    "{": ""      ""Video ID: D6yR8DUJHu4""
  },
  {
    "{": ""      ""Video ID: DhPeRJ3o9Ng""
  },
  {
    "{": ""      ""Video ID: z-ZLwSVvKJI""
  },
  {
    "{": ""      ""Video ID: xKBDUDYFzWg""
  },
  {
    "{": ""      ""Video ID: iW3e9Vd8W34""
  },
  {
    "{": ""      ""Video ID: uLI6vA03d4Q""
  },
  {
    "{": ""      ""Video ID: sVvVcGSUvko""
  },
  {
    "{": ""      ""Video ID: 70zwUsm-EN4""
  },
  {
    "{": ""      ""Video ID: XDLKbkiNsck""
  },
  {
    "{": ""      ""Video ID: bViGU4JSCr0""
  },
  {
    "{": ""      ""Video ID: 2BuAiwcuC8o""
  },
  {
    "{": ""      ""Video ID: j3_W75Pa05s""
  },
  {
    "{": ""      ""Video ID: jnEPl8Ovf_c""
  },
  {
    "{": ""      ""Video ID: rfp7FbsnsbU""
  },
  {
    "{": ""      ""Video ID: fh8VfFH78jY""
  },
  {
    "{": ""      ""Video ID: lFRMWDt99JM""
  },
  {
    "{": ""      ""Video ID: VYDTDLHq25c""
  },
  {
    "{": ""      ""Video ID: KxEivB5sP2o""
  },
  {
    "{": ""      ""Video ID: Ps3ecPbdWyQ""
  },
  {
    "{": ""      ""Video ID: 1vsPbIszQYU""
  },
  {
    "{": ""      ""Video ID: McsZ1U20W0M""
  },
  {
    "{": ""      ""Video ID: l2-jYis-k8Y""
  },
  {
    "{": ""      ""Video ID: 5PpkVyTFmTA""
  },
  {
    "{": ""      ""Video ID: tdGnl2Vgimk""
  },
  {
    "{": ""      ""Video ID: NkspsoXdNZc""
  },
  {
    "{": ""      ""Video ID: LDqQ9CM9ZUk""
  },
  {
    "{": ""      ""Video ID: rzQn2HBRACQ""
  },
  {
    "{": ""      ""Video ID: 4F7pNLpwqDA""
  },
  {
    "{": ""      ""Video ID: wujsfGWd7SA""
  },
  {
    "{": ""      ""Video ID: Xkxtb6REaqI""
  },
  {
    "{": ""      ""Video ID: s-5fHYWpSqU""
  },
  {
    "{": ""      ""Video ID: YRx0cNZn_8A""
  },
  {
    "{": ""      ""Video ID: wg_j-2oEVxY""
  },
  {
    "{": ""      ""Video ID: iJYt-JtkEYE""
  },
  {
    "{": ""      ""Video ID: p_LfaAur17I""
  },
  {
    "{": ""      ""Video ID: FKXm3Qg7sBo""
  },
  {
    "{": ""      ""Video ID: HAVI7OaDF6Q""
  },
  {
    "{": ""      ""Video ID: 5RUYewnyREc""
  },
  {
    "{": ""      ""Video ID: OMvAXpq7Xj4""
  },
  {
    "{": ""      ""Video ID: BliMK_pbrGE""
  },
  {
    "{": ""      ""Video ID: DaOVPaYf780""
  },
  {
    "{": ""      ""Video ID: _UoHfCUBiEM""
  },
  {
    "{": ""      ""Video ID: S3-Y-Yq9A0g""
  },
  {
    "{": ""      ""Video ID: myRm6tfY8C4""
  },
  {
    "{": ""      ""Video ID: O9gZllZM_ZM""
  },
  {
    "{": ""      ""Video ID: TQcp5LR43iI""
  },
  {
    "{": ""      ""Video ID: 8-adj20R5LQ""
  },
  {
    "{": ""      ""Video ID: mgZHfY3a07c""
  },
  {
    "{": ""      ""Video ID: a39qbfsPwYU""
  },
  {
    "{": ""      ""Video ID: JiyJNUC6e70""
  },
  {
    "{": ""      ""Video ID: lDQ7GPicnx4""
  },
  {
    "{": ""      ""Video ID: HnmBxII-a44""
  },
  {
    "{": ""      ""Video ID: W_g4mq8t8LE""
  },
  {
    "{": ""      ""Video ID: JI3FrcA3t7I""
  },
  {
    "{": ""      ""Video ID: P-PiARew26Y""
  },
  {
    "{": ""      ""Video ID: svIvdA7Dx6U""
  },
  {
    "{": ""      ""Video ID: ZPcT3LT1zXY""
  },
  {
    "{": ""      ""Video ID: hhfruOUPNDQ""
  },
  {
    "{": ""      ""Video ID: EKsapdP9IbU""
  },
  {
    "{": ""      ""Video ID: MFIuH9jL-b0""
  },
  {
    "{": ""      ""Video ID: 8Q54IVUPoJ0""
  },
  {
    "{": ""      ""Video ID: dlQm0iQQJyk""
  },
  {
    "{": ""      ""Video ID: P709fD6b_nI""
  },
  {
    "{": ""      ""Video ID: XhWdJDMVHX8""
  },
  {
    "{": ""      ""Video ID: lCUEQF92QRc""
  },
  {
    "{": ""      ""Video ID: slTvPH_FIOU""
  },
  {
    "{": ""      ""Video ID: t9H6G_AyZL8""
  },
  {
    "{": ""      ""Video ID: Sjg1ctHtTH0""
  },
  {
    "{": ""      ""Video ID: W8XqvpMFUMg""
  },
  {
    "{": ""      ""Video ID: eVWJ2FxFq-Y""
  },
  {
    "{": ""      ""Video ID: EPWCRdee2RE""
  },
  {
    "{": ""      ""Video ID: RdMskQsHViE""
  },
  {
    "{": ""      ""Video ID: e6HizSrXBgw""
  },
  {
    "{": ""      ""Video ID: gITbKIOAwNs""
  },
  {
    "{": ""      ""Video ID: He9gO6I1_sg""
  },
  {
    "{": ""      ""Video ID: j1h5fq2AfNs""
  },
  {
    "{": ""      ""Video ID: L9LrZcLrCbo""
  },
  {
    "{": ""      ""Video ID: UuRQvViiLFA""
  },
  {
    "{": ""      ""Video ID: iw2skS_Yidw""
  },
  {
    "{": ""      ""Video ID: bo7vRy5JhtQ""
  },
  {
    "{": ""      ""Video ID: vbezoWJh9Cc""
  },
  {
    "{": ""      ""Video ID: ssDb_L9hwEo""
  },
  {
    "{": ""      ""Video ID: sx2K7Nm7Tv0""
  },
  {
    "{": ""      ""Video ID: adB6RzWDQ-Q""
  },
  {
    "{": ""      ""Video ID: JkItGwGzfM8""
  },
  {
    "{": ""      ""Video ID: u5Ua1yq8qAE""
  },
  {
    "{": ""      ""Video ID: d8wMZQeGIFE""
  },
  {
    "{": ""      ""Video ID: Dj4OXcO7Yj4""
  },
  {
    "{": ""      ""Video ID: ua9uCW2KHsc""
  },
  {
    "{": ""      ""Video ID: PmlrXsHNe3I""
  },
  {
    "{": ""      ""Video ID: y6iLJqLNik4""
  },
  {
    "{": ""      ""Video ID: pBumZvyMkSQ""
  },
  {
    "{": ""      ""Video ID: qg1Ru01ebRQ""
  },
  {
    "{": ""      ""Video ID: Usiw20Y7G4Y""
  },
  {
    "{": ""      ""Video ID: ZLUeSy7Qr1Y""
  },
  {
    "{": ""      ""Video ID: Ezdx9btkNu4""
  },
  {
    "{": ""      ""Video ID: MPYckOX0fsE""
  },
  {
    "{": ""      ""Video ID: x7K1gNUdlj4""
  },
  {
    "{": ""      ""Video ID: sPBQEbB9x1w""
  },
  {
    "{": ""      ""Video ID: 1DeiByyRlF0""
  },
  {
    "{": ""      ""Video ID: c5WrO63nHxc""
  },
  {
    "{": ""      ""Video ID: vZSfz1Akdc8""
  },
  {
    "{": ""      ""Video ID: 2qX2L1q19_U""
  },
  {
    "{": ""      ""Video ID: OlBY6iB5DJ4""
  },
  {
    "{": ""      ""Video ID: _89udGVjkG4""
  },
  {
    "{": ""      ""Video ID: UodVbi1o9hg""
  },
  {
    "{": ""      ""Video ID: Pr1cs60TFaU""
  },
  {
    "{": ""      ""Video ID: 37rfj9wtXSA""
  },
  {
    "{": ""      ""Video ID: lL5rsQNprf8""
  },
  {
    "{": ""      ""Video ID: SxX7bRhTkNA""
  },
  {
    "{": ""      ""Video ID: Aa6dCUWocbs""
  },
  {
    "{": ""      ""Video ID: AqQVyPkNJcQ""
  },
  {
    "{": ""      ""Video ID: PV1jq7xZYcI""
  },
  {
    "{": ""      ""Video ID: _UzhkP_f384""
  },
  {
    "{": ""      ""Video ID: 7BB4Vvgn_4k""
  },
  {
    "{": ""      ""Video ID: kCKsHJGmmAc""
  },
  {
    "{": ""      ""Video ID: tMdYI5yZuXM""
  },
  {
    "{": ""      ""Video ID: f_2dBInLvpI""
  },
  {
    "{": ""      ""Video ID: jd7LvJBIaNo""
  },
  {
    "{": ""      ""Video ID: E-CpdOH5wm4""
  },
  {
    "{": ""      ""Video ID: 2E_s_aSJBdY""
  },
  {
    "{": ""      ""Video ID: 924zvDkF2sg""
  },
  {
    "{": ""      ""Video ID: H_K4sc80nck""
  },
  {
    "{": ""      ""Video ID: 7lr19rotN2c""
  },
  {
    "{": ""      ""Video ID: TdvqruW1nkM""
  },
  {
    "{": ""      ""Video ID: bqO32KDfax0""
  },
  {
    "{": ""      ""Video ID: AXqGrMAKORE""
  },
  {
    "{": ""      ""Video ID: wfeGbk_y4LE""
  },
  {
    "{": ""      ""Video ID: ieQIY-7FXwY""
  },
  {
    "{": ""      ""Video ID: PicNJE_BTjs""
  },
  {
    "{": ""      ""Video ID: K_tUo6zazXs""
  },
  {
    "{": ""      ""Video ID: WXMkZsRQcH8""
  },
  {
    "{": ""      ""Video ID: AkKTJ4ur7Jg""
  },
  {
    "{": ""      ""Video ID: iYVrMA9PkKo""
  },
  {
    "{": ""      ""Video ID: X4TpkURZECs""
  },
  {
    "{": ""      ""Video ID: XisU0YXJK-Q""
  },
  {
    "{": ""      ""Video ID: OvMa8NZ3Krg""
  },
  {
    "{": ""      ""Video ID: dZevTVPlfJ4""
  },
  {
    "{": ""      ""Video ID: GHcTstXaIW8""
  },
  {
    "{": ""      ""Video ID: kPzauCmxqQc""
  },
  {
    "{": ""      ""Video ID: YqyxOFVvPeo""
  },
  {
    "{": ""      ""Video ID: 46REHGSwc_8""
  },
  {
    "{": ""      ""Video ID: c1r65Ok0SiE""
  },
  {
    "{": ""      ""Video ID: J1WHdViGycY""
  },
  {
    "{": ""      ""Video ID: -h674r2TFDU""
  },
  {
    "{": ""      ""Video ID: z6754vsWnOo""
  },
  {
    "{": ""      ""Video ID: CZVjurveVz8""
  },
  {
    "{": ""      ""Video ID: Mq7QyJ4_6EA""
  },
  {
    "{": ""      ""Video ID: vZTiZlTNpA4""
  },
  {
    "{": ""      ""Video ID: 43veym3rUX4""
  },
  {
    "{": ""      ""Video ID: T9QITFXiMOc""
  },
  {
    "{": ""      ""Video ID: 8xCMWPztz38""
  },
  {
    "{": ""      ""Video ID: 3DnLSurG69Q""
  },
  {
    "{": ""      ""Video ID: wGzW93YyI4U""
  },
  {
    "{": ""      ""Video ID: KrWm0sWbdg0""
  },
  {
    "{": ""      ""Video ID: cbIPQFs45lE""
  },
  {
    "{": ""      ""Video ID: ZEhA7HCeeeA""
  },
  {
    "{": ""      ""Video ID: 8xmnZ8o5sbc""
  },
  {
    "{": ""      ""Video ID: tSMc8yoM1_Q""
  },
  {
    "{": ""      ""Video ID: CPKG0NAfmYM""
  },
  {
    "{": ""      ""Video ID: yCd56yJk2sk""
  },
  {
    "{": ""      ""Video ID: Vo5CZvD3-QM""
  },
  {
    "{": ""      ""Video ID: SeLpEOjlUGE""
  },
  {
    "{": ""      ""Video ID: gMBybgHAfts""
  },
  {
    "{": ""      ""Video ID: X0zqbuSVqIU""
  },
  {
    "{": ""      ""Video ID: Yenlw4GyxqI""
  },
  {
    "{": ""      ""Video ID: o8M_It1aehw""
  },
  {
    "{": ""      ""Video ID: xtAja20kTCA""
  },
  {
    "{": ""      ""Video ID: kOLcg9hy3gA""
  },
  {
    "{": ""      ""Video ID: 0iLs-HI9I2k""
  },
  {
    "{": ""      ""Video ID: GQ2JtUmB3kc""
  },
  {
    "{": ""      ""Video ID: _l47DmiijcQ""
  },
  {
    "{": ""      ""Video ID: ebhA6mdVzIU""
  },
  {
    "{": ""      ""Video ID: dvJyRxCxNM8""
  },
  {
    "{": ""      ""Video ID: MlBNniTdMlQ""
  },
  {
    "{": ""      ""Video ID: Zhkly9xwDmY""
  },
  {
    "{": ""      ""Video ID: PzRlubt4pms""
  },
  {
    "{": ""      ""Video ID: qPMSeBXdbx4""
  },
  {
    "{": ""      ""Video ID: OZLYLufamV4""
  },
  {
    "{": ""      ""Video ID: 8mXMVYwD2oA""
  },
  {
    "{": ""      ""Video ID: gfF6tMoLSJI""
  },
  {
    "{": ""      ""Video ID: 4DEho2pkws8""
  },
  {
    "{": ""      ""Video ID: Zqnof0hGAcc""
  },
  {
    "{": ""      ""Video ID: m1W5uk3rqsY""
  },
  {
    "{": ""      ""Video ID: VYKdpWp_yU0""
  },
  {
    "{": ""      ""Video ID: FwviQlsScEw""
  },
  {
    "{": ""      ""Video ID: rxvSqSXs0io""
  },
  {
    "{": ""      ""Video ID: o1uJztFbOk8""
  },
  {
    "{": ""      ""Video ID: qxZACaelHr4""
  },
  {
    "{": ""      ""Video ID: F-EPJeTaaio""
  },
  {
    "{": ""      ""Video ID: Kw2QIaGR8bY""
  },
  {
    "{": ""      ""Video ID: LYGt9l4FdXo""
  },
  {
    "{": ""      ""Video ID: L8ztVQlTcGY""
  },
  {
    "{": ""      ""Video ID: GxmExtbcSoI""
  },
  {
    "{": ""      ""Video ID: ls55sIfGgPI""
  },
  {
    "{": ""      ""Video ID: ZFVhyGgwUWw""
  },
  {
    "{": ""      ""Video ID: 3TsSOTd0DsY""
  },
  {
    "{": ""      ""Video ID: TYuU6DXu-h0""
  },
  {
    "{": ""      ""Video ID: jw4oyxq_jZ8""
  },
  {
    "{": ""      ""Video ID: MC_vbA4vXSE""
  },
  {
    "{": ""      ""Video ID: i5k6kMLray0""
  },
  {
    "{": ""      ""Video ID: neib3y7mIDc""
  },
  {
    "{": ""      ""Video ID: E7gs_3UUInA""
  },
  {
    "{": ""      ""Video ID: tQkzs_ec4Nk""
  },
  {
    "{": ""      ""Video ID: QwD7t3pJVMA""
  },
  {
    "{": ""      ""Video ID: TFVY5gbT2VU""
  },
  {
    "{": ""      ""Video ID: touM-GoRRXs""
  },
  {
    "{": ""      ""Video ID: Qrcykw1nKMw""
  },
  {
    "{": ""      ""Video ID: AWwPF0dkCic""
  },
  {
    "{": ""      ""Video ID: oEH4sBsazGg""
  },
  {
    "{": ""      ""Video ID: _axNJ7QRPmw""
  },
  {
    "{": ""      ""Video ID: -X0J3OGX-u8""
  },
  {
    "{": ""      ""Video ID: fYOfn8a52h4""
  },
  {
    "{": ""      ""Video ID: kZk5s-IozwY""
  },
  {
    "{": ""      ""Video ID: TIcSHBspcTM""
  },
  {
    "{": ""      ""Video ID: bXZ1vNOPEgs""
  },
  {
    "{": ""      ""Video ID: rSeqmE7v9i0""
  },
  {
    "{": ""      ""Video ID: u2a6xIkX-RU""
  },
  {
    "{": ""      ""Video ID: JEJfmInpgDs""
  },
  {
    "{": ""      ""Video ID: TM7C9cNgkm8""
  },
  {
    "{": ""      ""Video ID: FDrfedv7XlQ""
  },
  {
    "{": ""      ""Video ID: zhIuIZKKj64""
  },
  {
    "{": ""      ""Video ID: L_1eY_w3wew""
  },
  {
    "{": ""      ""Video ID: BzwY5H044rk""
  },
  {
    "{": ""      ""Video ID: D_gJIPLC4yc""
  },
  {
    "{": ""      ""Video ID: gyjqD8JxAd8""
  },
  {
    "{": ""      ""Video ID: wzWBcxoHarc""
  },
  {
    "{": ""      ""Video ID: XoSY9Thtu_A""
  },
  {
    "{": ""      ""Video ID: twnnadukdFs""
  },
  {
    "{": ""      ""Video ID: eV1beUaggmM""
  },
  {
    "{": ""      ""Video ID: 3FeNuYjoQZc""
  },
  {
    "{": ""      ""Video ID: u714s7wPxAM""
  },
  {
    "{": ""      ""Video ID: EdwNTeQYSmk""
  },
  {
    "{": ""      ""Video ID: 7ub2vpitKfQ""
  },
  {
    "{": ""      ""Video ID: Gql9c9T-awI""
  },
  {
    "{": ""      ""Video ID: m7G7UsLK-X4""
  },
  {
    "{": ""      ""Video ID: ARVeBEHxnJo""
  },
  {
    "{": ""      ""Video ID: b6SLITNMDaI""
  },
  {
    "{": ""      ""Video ID: yOus7-l8qsw""
  },
  {
    "{": ""      ""Video ID: 4diFUePp0pA""
  },
  {
    "{": ""      ""Video ID: Hz4GYa_DAFE""
  },
  {
    "{": ""      ""Video ID: m9bTsClFABE""
  },
  {
    "{": ""      ""Video ID: rE4Rs5ICTbg""
  },
  {
    "{": ""      ""Video ID: CkkvhazIEQ0""
  },
  {
    "{": ""      ""Video ID: nxZv2P7yUsc""
  },
  {
    "{": ""      ""Video ID: SKAgdV0rFlQ""
  },
  {
    "{": ""      ""Video ID: z7clGDhkSIw""
  },
  {
    "{": ""      ""Video ID: U9a3y5z-RgE""
  },
  {
    "{": ""      ""Video ID: elwPF94wmSg""
  },
  {
    "{": ""      ""Video ID: A4GW1BxGCOE""
  },
  {
    "{": ""      ""Video ID: JUOnCVaxRs4""
  },
  {
    "{": ""      ""Video ID: hHxcGLGWF9M""
  },
  {
    "{": ""      ""Video ID: evcmQS0Cg-I""
  },
  {
    "{": ""      ""Video ID: jJwNrVTufpg""
  },
  {
    "{": ""      ""Video ID: 0lTYlJzK6GY""
  },
  {
    "{": ""      ""Video ID: RGRt-aTIB58""
  },
  {
    "{": ""      ""Video ID: cJ0s1isp2is""
  },
  {
    "{": ""      ""Video ID: JxdvOglnITM""
  },
  {
    "{": ""      ""Video ID: ulZezSmFp5Q""
  },
  {
    "{": ""      ""Video ID: _qtIu564k00""
  },
  {
    "{": ""      ""Video ID: BvaimgU9Mdo""
  },
  {
    "{": ""      ""Video ID: 6lAFfLy05_Y""
  },
  {
    "{": ""      ""Video ID: dU622DJ81e0""
  },
  {
    "{": ""      ""Video ID: v8frN4Rou_s""
  },
  {
    "{": ""      ""Video ID: 0dG3yrrAios""
  },
  {
    "{": ""      ""Video ID: aFQFB5YpDZE""
  },
  {
    "{": ""      ""Video ID: hJZ-xGngNpw""
  },
  {
    "{": ""      ""Video ID: oZdSO5et5xc""
  },
  {
    "{": ""      ""Video ID: UX1eYaqMPSE""
  },
  {
    "{": ""      ""Video ID: fl3H50JyLkk""
  },
  {
    "{": ""      ""Video ID: uDTkj4AMlSc""
  },
  {
    "{": ""      ""Video ID: BhsaxoXi1fU""
  },
  {
    "{": ""      ""Video ID: JlRJU0NkndI""
  },
  {
    "{": ""      ""Video ID: TlaSKpatlQw""
  },
  {
    "{": ""      ""Video ID: JxMVmdgvaNQ""
  },
  {
    "{": ""      ""Video ID: qja9mVy5u_0""
  },
  {
    "{": ""      ""Video ID: ewKF1NQ4MVg""
  },
  {
    "{": ""      ""Video ID: ICG4Ze8GzUU""
  },
  {
    "{": ""      ""Video ID: 7YhvL0CUiX4""
  },
  {
    "{": ""      ""Video ID: o1MgdpbEerU""
  },
  {
    "{": ""      ""Video ID: TavHQEZrGTs""
  },
  {
    "{": ""      ""Video ID: RIhut8jEgzE""
  },
  {
    "{": ""      ""Video ID: dAmleEgnomY""
  },
  {
    "{": ""      ""Video ID: 64Jd1SNPkyQ""
  },
  {
    "{": ""      ""Video ID: fVjWAyFdpbM""
  },
  {
    "{": ""      ""Video ID: Mz6_0BRsTWg""
  },
  {
    "{": ""      ""Video ID: okUkBtlhVuc""
  },
  {
    "{": ""      ""Video ID: OSCXH464aBg""
  },
  {
    "{": ""      ""Video ID: 7RxAlleN_Wo""
  },
  {
    "{": ""      ""Video ID: YmaDBFW2eWY""
  },
  {
    "{": ""      ""Video ID: SqhhALE5IrE""
  },
  {
    "{": ""      ""Video ID: OXW-qjAsj68""
  },
  {
    "{": ""      ""Video ID: lHGBYzmVXz0""
  },
  {
    "{": ""      ""Video ID: 5FUNxUCFMB4""
  },
  {
    "{": ""      ""Video ID: vCxEyVZJAHY""
  },
  {
    "{": ""      ""Video ID: kwmVixeY7p0""
  },
  {
    "{": ""      ""Video ID: RZ7IjnCvNjw""
  },
  {
    "{": ""      ""Video ID: XIUWBWChqS0""
  },
  {
    "{": ""      ""Video ID: FHKrZ0E6eTg""
  },
  {
    "{": ""      ""Video ID: 3bJ1Ydq0vZI""
  },
  {
    "{": ""      ""Video ID: g863DA5g2ss""
  },
  {
    "{": ""      ""Video ID: HAoEkeUhnGc""
  },
  {
    "{": ""      ""Video ID: baDJ-ZIvYy0""
  },
  {
    "{": ""      ""Video ID: uaAAmRDX4ok""
  },
  {
    "{": ""      ""Video ID: l9waiuxjDts""
  },
  {
    "{": ""      ""Video ID: R6yBhWLnvR0""
  },
  {
    "{": ""      ""Video ID: 9FfeXi5ymWk""
  },
  {
    "{": ""      ""Video ID: tdQzO5FGb0c""
  },
  {
    "{": ""      ""Video ID: -sDgj_IwJvE""
  },
  {
    "{": ""      ""Video ID: -x14RKiHpA4""
  },
  {
    "{": ""      ""Video ID: qIlC6H-bb4w""
  },
  {
    "{": ""      ""Video ID: b7zQhgz70f8""
  },
  {
    "{": ""      ""Video ID: 39lJpJgG9Ek""
  },
  {
    "{": ""      ""Video ID: vAkOti7pJJg""
  },
  {
    "{": ""      ""Video ID: vzdSYm1t28o""
  },
  {
    "{": ""      ""Video ID: fQjIRxTmBi4""
  },
  {
    "{": ""      ""Video ID: AseJMwYK2MU""
  },
  {
    "{": ""      ""Video ID: k8tIg-FJHXU""
  },
  {
    "{": ""      ""Video ID: toT7wJwDB1A""
  },
  {
    "{": ""      ""Video ID: n--QPAH4Prw""
  },
  {
    "{": ""      ""Video ID: reRB00bMVLg""
  },
  {
    "{": ""      ""Video ID: rcEI4TH3xFA""
  },
  {
    "{": ""      ""Video ID: 7TVl7_PvepM""
  },
  {
    "{": ""      ""Video ID: mNlnEM4H29c""
  },
  {
    "{": ""      ""Video ID: ILC-VTZ-XG4""
  },
  {
    "{": ""      ""Video ID: M1Vl8FNtbe8""
  },
  {
    "{": ""      ""Video ID: 7tasDPAGY8k""
  },
  {
    "{": ""      ""Video ID: fpLzZK6j_TA""
  },
  {
    "{": ""      ""Video ID: XJvOYOuG5nY""
  },
  {
    "{": ""      ""Video ID: S6xaUFQTf1U""
  },
  {
    "{": ""      ""Video ID: sHauA2RzHP4""
  },
  {
    "{": ""      ""Video ID: J2qiz4rS0xA""
  },
  {
    "{": ""      ""Video ID: mEpeBOl3qlE""
  },
  {
    "{": ""      ""Video ID: TK3CuyahKq0""
  },
  {
    "{": ""      ""Video ID: UZ8ovdJx5_s""
  },
  {
    "{": ""      ""Video ID: EL4btlSwe7k""
  },
  {
    "{": ""      ""Video ID: aVRKVetKyLM""
  },
  {
    "{": ""      ""Video ID: L5jhYom2iWQ""
  },
  {
    "{": ""      ""Video ID: YRWen6392yA""
  },
  {
    "{": ""      ""Video ID: Msx_Zeplo2w""
  },
  {
    "{": ""      ""Video ID: 8DT12aQxKZY""
  },
  {
    "{": ""      ""Video ID: AkharePeeQk""
  },
  {
    "{": ""      ""Video ID: txNiX09ZsBo""
  },
  {
    "{": ""      ""Video ID: UFBZ_uAbxS0""
  },
  {
    "{": ""      ""Video ID: 5u-20g7Bwdw""
  },
  {
    "{": ""      ""Video ID: 5UmRx4dEdRI""
  },
  {
    "{": ""      ""Video ID: 0WLUWNSQygg""
  },
  {
    "{": ""      ""Video ID: rYYBmEpNE0M""
  },
  {
    "{": ""      ""Video ID: NGNQGEdNOfw""
  },
  {
    "{": ""      ""Video ID: w4Uj9l_Ti8Y""
  },
  {
    "{": ""      ""Video ID: 36OPNTJGUMU""
  },
  {
    "{": ""      ""Video ID: TUU3M442H1k""
  },
  {
    "{": ""      ""Video ID: qpEombsYE48""
  },
  {
    "{": ""      ""Video ID: rhCMCbpPbbE""
  },
  {
    "{": ""      ""Video ID: 7Y3HHpVZcdQ""
  },
  {
    "{": ""      ""Video ID: eNZ1lOxsYYQ""
  },
  {
    "{": ""      ""Video ID: jTllN2jPKMU""
  },
  {
    "{": ""      ""Video ID: OEVzPCY2T-g""
  },
  {
    "{": ""      ""Video ID: t0lNyZ5aKXI""
  },
  {
    "{": ""      ""Video ID: luIgNPPh-io""
  },
  {
    "{": ""      ""Video ID: _5NpAoeQvpo""
  },
  {
    "{": ""      ""Video ID: YwA0z-QdC70""
  },
  {
    "{": ""      ""Video ID: helswqzTlX4""
  },
  {
    "{": ""      ""Video ID: gqB1e7MlWN8""
  },
  {
    "{": ""      ""Video ID: Gt5mmuBBP04""
  },
  {
    "{": ""      ""Video ID: AUVe9RAg3Js""
  },
  {
    "{": ""      ""Video ID: e32RDZZaeCw""
  },
  {
    "{": ""      ""Video ID: _AH0VE8SgyE""
  },
  {
    "{": ""      ""Video ID: ji2BCSYMOms""
  },
  {
    "{": ""      ""Video ID: 4nfMtShbay4""
  },
  {
    "{": ""      ""Video ID: boyOjNVbyvI""
  },
  {
    "{": ""      ""Video ID: pQ7RG4CxXCA""
  },
  {
    "{": ""      ""Video ID: IyigIbPCi98""
  },
  {
    "{": ""      ""Video ID: BmJAlSrzbM0""
  },
  {
    "{": ""      ""Video ID: nHIMovFp8lE""
  },
  {
    "{": ""      ""Video ID: YMlqLu_FVU4""
  },
  {
    "{": ""      ""Video ID: uGrsGDGVtm8""
  },
  {
    "{": ""      ""Video ID: ZKgSF0BNFrU""
  },
  {
    "{": ""      ""Video ID: UgizgOppVH8""
  },
  {
    "{": ""      ""Video ID: MsJFrsbsIjc""
  },
  {
    "{": ""      ""Video ID: 58MY1tPE5xk""
  },
  {
    "{": ""      ""Video ID: v-OZEofYzDM""
  },
  {
    "{": ""      ""Video ID: kPLtZ9MFPqE""
  },
  {
    "{": ""      ""Video ID: frG__JVHMYk""
  },
  {
    "{": ""      ""Video ID: isQmjhC8VuE""
  },
  {
    "{": ""      ""Video ID: WROtwUbU31k""
  },
  {
    "{": ""      ""Video ID: OEEN6X3JG3E""
  },
  {
    "{": ""      ""Video ID: dmy7MVqocaY""
  },
  {
    "{": ""      ""Video ID: uxz97WfYpAE""
  },
  {
    "{": ""      ""Video ID: lvcH0AHG7rg""
  },
  {
    "{": ""      ""Video ID: 3sGVNCE1_Aw""
  },
  {
    "{": ""      ""Video ID: iP5rD2JU2yo""
  },
  {
    "{": ""      ""Video ID: XXOC1qKehAM""
  },
  {
    "{": ""      ""Video ID: humuWpiy-pg""
  },
  {
    "{": ""      ""Video ID: R5os-qnhS9c""
  },
  {
    "{": ""      ""Video ID: JPWQ9TklkWA""
  },
  {
    "{": ""      ""Video ID: kthN9Xhd1w8""
  },
  {
    "{": ""      ""Video ID: syK0v1BB-O4""
  },
  {
    "{": ""      ""Video ID: NLGW414D2PU""
  },
  {
    "{": ""      ""Video ID: Lbto1neHWQA""
  },
  {
    "{": ""      ""Video ID: 08XJ79S_7sY""
  },
  {
    "{": ""      ""Video ID: StGVmeZYNIM""
  },
  {
    "{": ""      ""Video ID: D8BrLMy1XKg""
  },
  {
    "{": ""      ""Video ID: qR_Kb3ePe10""
  },
  {
    "{": ""      ""Video ID: 3-y7A_Hge6k""
  },
  {
    "{": ""      ""Video ID: 3t6IvjAEltE""
  },
  {
    "{": ""      ""Video ID: n8e-t311jug""
  },
  {
    "{": ""      ""Video ID: 7F49YS4lUL0""
  },
  {
    "{": ""      ""Video ID: GGJuO33ep5E""
  },
  {
    "{": ""      ""Video ID: w-wIxMPMH0k""
  },
  {
    "{": ""      ""Video ID: gXWsyXRMCQI""
  },
  {
    "{": ""      ""Video ID: Rnw1N5Z3iVg""
  },
  {
    "{": ""      ""Video ID: 5oPFyI9lHPk""
  },
  {
    "{": ""      ""Video ID: VCTqUZQ8HxI""
  },
  {
    "{": ""      ""Video ID: REUho-6O848""
  },
  {
    "{": ""      ""Video ID: HL0pgO2-wjA""
  },
  {
    "{": ""      ""Video ID: AavjCJlTTm0""
  },
  {
    "{": ""      ""Video ID: ea2o3L8tHGU""
  },
  {
    "{": ""      ""Video ID: WpGJPdFQOTA""
  },
  {
    "{": ""      ""Video ID: W5g8Morl4uw""
  },
  {
    "{": ""      ""Video ID: jrNb6LU11o4""
  },
  {
    "{": ""      ""Video ID: GFrTmLUj3KM""
  },
  {
    "{": ""      ""Video ID: WclLGX-90yg""
  },
  {
    "{": ""      ""Video ID: ptD6wxU6Ptk""
  },
  {
    "{": ""      ""Video ID: cLTGURGef-o""
  },
  {
    "{": ""      ""Video ID: VqQrIg90x5k""
  },
  {
    "{": ""      ""Video ID: mLLNpqaEFl8""
  },
  {
    "{": ""      ""Video ID: HVgJMssTVSY""
  },
  {
    "{": ""      ""Video ID: sDaN3WFD4nE""
  },
  {
    "{": ""      ""Video ID: S2C5SXPpgx8""
  },
  {
    "{": ""      ""Video ID: 1O52kQj6DOg""
  },
  {
    "{": ""      ""Video ID: ya-WiaWpIRo""
  },
  {
    "{": ""      ""Video ID: zhO6KWevirU""
  },
  {
    "{": ""      ""Video ID: iX6YvWxtrxw""
  },
  {
    "{": ""      ""Video ID: sUHzwdH3BqE""
  },
  {
    "{": ""      ""Video ID: vXMKfiK1vjE""
  },
  {
    "{": ""      ""Video ID: NyE475lyLY8""
  },
  {
    "{": ""      ""Video ID: 69637mM5-vM""
  },
  {
    "{": ""      ""Video ID: BWGaGcih5YU""
  },
  {
    "{": ""      ""Video ID: mTafNByyvTE""
  },
  {
    "{": ""      ""Video ID: v0WmFS0S-Ww""
  },
  {
    "{": ""      ""Video ID: tnpwfejnFo8""
  },
  {
    "{": ""      ""Video ID: hx-ReP1GRHA""
  },
  {
    "{": ""      ""Video ID: agun3rpnYPk""
  },
  {
    "{": ""      ""Video ID: CSzqaix-8d4""
  },
  {
    "{": ""      ""Video ID: DkTWJ-njS0Q""
  },
  {
    "{": ""      ""Video ID: uq1OMcY-fjc""
  },
  {
    "{": ""      ""Video ID: V4nCDyi3luQ""
  },
  {
    "{": ""      ""Video ID: 4X-PGVg1aiE""
  },
  {
    "{": ""      ""Video ID: 8yJ1nNGMaNU""
  },
  {
    "{": ""      ""Video ID: OL2UckDF7N4""
  },
  {
    "{": ""      ""Video ID: t9DbS1IcL1I""
  },
  {
    "{": ""      ""Video ID: TpLIMqOeNZE""
  },
  {
    "{": ""      ""Video ID: mFDHOvXKmZo""
  },
  {
    "{": ""      ""Video ID: _NH-_3B50ag""
  },
  {
    "{": ""      ""Video ID: iwtBFLznVnI""
  },
  {
    "{": ""      ""Video ID: qKljUWVY14c""
  },
  {
    "{": ""      ""Video ID: YiZViZct2Rc""
  },
  {
    "{": ""      ""Video ID: juOHg_wfv08""
  },
  {
    "{": ""      ""Video ID: uSua_VGeeRY""
  },
  {
    "{": ""      ""Video ID: FoJ2o8mAF0w""
  },
  {
    "{": ""      ""Video ID: AZNPgY5aizE""
  },
  {
    "{": ""      ""Video ID: n0_s4G8RkyU""
  },
  {
    "{": ""      ""Video ID: rx0mUdkrWM4""
  },
  {
    "{": ""      ""Video ID: C1z2_j-_nTQ""
  },
  {
    "{": ""      ""Video ID: R0FUtUkHZM0""
  },
  {
    "{": ""      ""Video ID: qRrYriAMmTs""
  },
  {
    "{": ""      ""Video ID: xiiMEBEG2TI""
  },
  {
    "{": ""      ""Video ID: EaELtepadmQ""
  },
  {
    "{": ""      ""Video ID: rykcRPiDzCE""
  },
  {
    "{": ""      ""Video ID: 541w5JncFQg""
  },
  {
    "{": ""      ""Video ID: JEg6aLHdXdo""
  },
  {
    "{": ""      ""Video ID: YdSFHCwlDRw""
  },
  {
    "{": ""      ""Video ID: y1cPakKLcGQ""
  },
  {
    "{": ""      ""Video ID: KzuxTP4LWts""
  },
  {
    "{": ""      ""Video ID: xIM2p9d_CVE""
  },
  {
    "{": ""      ""Video ID: dXeorF9L5lo""
  },
  {
    "{": ""      ""Video ID: 0pZ5rjU6_Jg""
  },
  {
    "{": ""      ""Video ID: aEYFn8RyO9M""
  },
  {
    "{": ""      ""Video ID: T0fWcQVu380""
  },
  {
    "{": ""      ""Video ID: ztLDYHVyPKs""
  },
  {
    "{": ""      ""Video ID: 1nmDBlvpQes""
  },
  {
    "{": ""      ""Video ID: GOPJVufYl-s""
  },
  {
    "{": ""      ""Video ID: RYjNFd1kvWE""
  },
  {
    "{": ""      ""Video ID: wCmvav1RslQ""
  },
  {
    "{": ""      ""Video ID: tF0U46KEQx4""
  },
  {
    "{": ""      ""Video ID: FrYlNNy929Y""
  },
  {
    "{": ""      ""Video ID: LyTwlJHvb60""
  },
  {
    "{": ""      ""Video ID: _gCa0QUePwg""
  },
  {
    "{": ""      ""Video ID: HaIt95pzHdQ""
  },
  {
    "{": ""      ""Video ID: YZoGaFGvg10""
  },
  {
    "{": ""      ""Video ID: sz4KdD0oVHs""
  },
  {
    "{": ""      ""Video ID: OTa-pQKD8Lo""
  },
  {
    "{": ""      ""Video ID: OqR-RCWj9GU""
  },
  {
    "{": ""      ""Video ID: FicDCtqSeiE""
  },
  {
    "{": ""      ""Video ID: 8qwUC0GLtw0""
  },
  {
    "{": ""      ""Video ID: thmbHs6512w""
  },
  {
    "{": ""      ""Video ID: 7J__HpNwGOo""
  },
  {
    "{": ""      ""Video ID: tOhDBo6x2ZY""
  },
  {
    "{": ""      ""Video ID: cFqNprSEOCA""
  },
  {
    "{": ""      ""Video ID: S5BmHFczKgA""
  },
  {
    "{": ""      ""Video ID: 4RUBqgltwq0""
  },
  {
    "{": ""      ""Video ID: YCg8xtyiqhs""
  },
  {
    "{": ""      ""Video ID: 1aXXP3spI9E""
  },
  {
    "{": ""      ""Video ID: RjDqufVKAMk""
  },
  {
    "{": ""      ""Video ID: o_lU1CKC1rc""
  },
  {
    "{": ""      ""Video ID: --JpoT82Vro""
  },
  {
    "{": ""      ""Video ID: Zz6eIEHzAEg""
  },
  {
    "{": ""      ""Video ID: XMs0e8-qW4w""
  },
  {
    "{": ""      ""Video ID: s_6YRPxYAts""
  },
  {
    "{": ""      ""Video ID: fQPv8RgsbSc""
  },
  {
    "{": ""      ""Video ID: BNnNIvjDqAs""
  },
  {
    "{": ""      ""Video ID: 62jLZdmTfR0""
  },
  {
    "{": ""      ""Video ID: tyqMgqToRLM""
  },
  {
    "{": ""      ""Video ID: wlVJ38z-8rs""
  },
  {
    "{": ""      ""Video ID: 0mHZBNQn6Po""
  },
  {
    "{": ""      ""Video ID: SPw-YAt69lw""
  },
  {
    "{": ""      ""Video ID: AGQyLBx4Hxs""
  },
  {
    "{": ""      ""Video ID: ZYiIYxifOps""
  },
  {
    "{": ""      ""Video ID: AAkiXOKzlaU""
  },
  {
    "{": ""      ""Video ID: jeeqYgEVPpY""
  },
  {
    "{": ""      ""Video ID: yzUQDhCN8to""
  },
  {
    "{": ""      ""Video ID: _lu-HXfZ184""
  },
  {
    "{": ""      ""Video ID: mGIa6RKgTOI""
  },
  {
    "{": ""      ""Video ID: joqi0LdeB1o""
  },
  {
    "{": ""      ""Video ID: CmNe8D32ONM""
  },
  {
    "{": ""      ""Video ID: IJewu2qX4Kg""
  },
  {
    "{": ""      ""Video ID: lPoDQ3-Hz7Q""
  },
  {
    "{": ""      ""Video ID: 0YPWC9pKsbY""
  },
  {
    "{": ""      ""Video ID: 8ifacnc5iQs""
  },
  {
    "{": ""      ""Video ID: b9LuMLSpgcE""
  },
  {
    "{": ""      ""Video ID: BlVqXSB3RXs""
  },
  {
    "{": ""      ""Video ID: tgkkNN3x4Ik""
  },
  {
    "{": ""      ""Video ID: psZwfXKTRBI""
  },
  {
    "{": ""      ""Video ID: 6bhO7m32AP8""
  },
  {
    "{": ""      ""Video ID: hirfIaVm0bM""
  },
  {
    "{": ""      ""Video ID: k3bZHZH8bRk""
  },
  {
    "{": ""      ""Video ID: baunYsQkkxQ""
  },
  {
    "{": ""      ""Video ID: NILt7-fvct8""
  },
  {
    "{": ""      ""Video ID: 9KlfxF6Jjis""
  },
  {
    "{": ""      ""Video ID: XDBriDq4LRI""
  },
  {
    "{": ""      ""Video ID: YSv0ttK14M0""
  },
  {
    "{": ""      ""Video ID: Pvr7HxIPce4""
  },
  {
    "{": ""      ""Video ID: cCaUujf3nKc""
  },
  {
    "{": ""      ""Video ID: CaHmAMapHb0""
  },
  {
    "{": ""      ""Video ID: W2DgwF2lJl4""
  },
  {
    "{": ""      ""Video ID: MAY2dzc1x-U""
  },
  {
    "{": ""      ""Video ID: oRn7DQIRbFU""
  },
  {
    "{": ""      ""Video ID: nNmnPWJfu3Q""
  },
  {
    "{": ""      ""Video ID: YZSN2K1wYD0""
  },
  {
    "{": ""      ""Video ID: t5WzgUMpGEI""
  },
  {
    "{": ""      ""Video ID: j-RbMT5DJpY""
  },
  {
    "{": ""      ""Video ID: pZ_-R-fKd0g""
  },
  {
    "{": ""      ""Video ID: jz9MTFYDgl0""
  },
  {
    "{": ""      ""Video ID: xTz9yyOz1OY""
  },
  {
    "{": ""      ""Video ID: R0y6q1pBbr4""
  },
  {
    "{": ""      ""Video ID: hONQ7Ygfyt0""
  },
  {
    "{": ""      ""Video ID: WDKa0HsW3Cw""
  },
  {
    "{": ""      ""Video ID: bCz8kOtvu5c""
  },
  {
    "{": ""      ""Video ID: 4yDraMy1nDg""
  },
  {
    "{": ""      ""Video ID: huVoznar0Rk""
  },
  {
    "{": ""      ""Video ID: LFgb1BdPBZo""
  },
  {
    "{": ""      ""Video ID: cceCy2flJKo""
  },
  {
    "{": ""      ""Video ID: AcFEm4Or9Hg""
  },
  {
    "{": ""      ""Video ID: kMd_NCMETp4""
  },
  {
    "{": ""      ""Video ID: Le5qcxgreOQ""
  },
  {
    "{": ""      ""Video ID: m5k8oXaG-bQ""
  },
  {
    "{": ""      ""Video ID: bEWhLZGpvPc""
  },
  {
    "{": ""      ""Video ID: yBXhhq9LDHA""
  },
  {
    "{": ""      ""Video ID: t-bwKCQy5iQ""
  },
  {
    "{": ""      ""Video ID: tTV0TGP9ACQ""
  },
  {
    "{": ""      ""Video ID: fL7d2meqNV4""
  },
  {
    "{": ""      ""Video ID: k7ZZB-RiJ9w""
  },
  {
    "{": ""      ""Video ID: f_bHEPvvsj8""
  },
  {
    "{": ""      ""Video ID: QJtrlrDkzLw""
  },
  {
    "{": ""      ""Video ID: 5JkhZhzOSFc""
  },
  {
    "{": ""      ""Video ID: N_CjN9v43ro""
  },
  {
    "{": ""      ""Video ID: AYrAu0cYCYw""
  },
  {
    "{": ""      ""Video ID: tReftR-6dyU""
  },
  {
    "{": ""      ""Video ID: hwfRsgyDjmE""
  },
  {
    "{": ""      ""Video ID: 8J8affWBGkw""
  },
  {
    "{": ""      ""Video ID: yDGCNuvEzJU""
  },
  {
    "{": ""      ""Video ID: CIgT0aTmMWw""
  },
  {
    "{": ""      ""Video ID: vor6840_A2Q""
  },
  {
    "{": ""      ""Video ID: plxOk6jyU4E""
  },
  {
    "{": ""      ""Video ID: 0cTylAfycRs""
  },
  {
    "{": ""      ""Video ID: 50PBYg8eqI0""
  },
  {
    "{": ""      ""Video ID: tnG_K-JdvPk""
  },
  {
    "{": ""      ""Video ID: 4obp6wAi9tU""
  },
  {
    "{": ""      ""Video ID: 1sJ0kFP2LKk""
  },
  {
    "{": ""      ""Video ID: sR5k8S4hLCg""
  },
  {
    "{": ""      ""Video ID: bwZQfGM8N0E""
  },
  {
    "{": ""      ""Video ID: vSb-nV8l2QY""
  },
  {
    "{": ""      ""Video ID: bTxkDWuJKC4""
  },
  {
    "{": ""      ""Video ID: LBcDZRWtFCU""
  },
  {
    "{": ""      ""Video ID: bxbIuDJTWFI""
  },
  {
    "{": ""      ""Video ID: kbgVW_dMMIM""
  },
  {
    "{": ""      ""Video ID: CcpXfJCxat8""
  },
  {
    "{": ""      ""Video ID: 6K5HiZZjtqc""
  },
  {
    "{": ""      ""Video ID: MEkHZOGXj-s""
  },
  {
    "{": ""      ""Video ID: IyhtYLT9Wyk""
  },
  {
    "{": ""      ""Video ID: vmLvT05uOf4""
  },
  {
    "{": ""      ""Video ID: PvH2oJ9x2A8""
  },
  {
    "{": ""      ""Video ID: sy7tYjsIzSk""
  },
  {
    "{": ""      ""Video ID: gRtcFbKK_us""
  },
  {
    "{": ""      ""Video ID: dhSBTI-txak""
  },
  {
    "{": ""      ""Video ID: X_rq_-dA9n0""
  },
  {
    "{": ""      ""Video ID: WQ3pYT6S2TI""
  },
  {
    "{": ""      ""Video ID: 7bVj0r1DcvY""
  },
  {
    "{": ""      ""Video ID: ztlnKZSPtcw""
  },
  {
    "{": ""      ""Video ID: z1LSEjmtwMw""
  },
  {
    "{": ""      ""Video ID: flX_evjtC4o""
  },
  {
    "{": ""      ""Video ID: T-VaQp31xwc""
  },
  {
    "{": ""      ""Video ID: JWLMir7yyCk""
  },
  {
    "{": ""      ""Video ID: U7njCaJGafI""
  },
  {
    "{": ""      ""Video ID: chJeKE2646U""
  },
  {
    "{": ""      ""Video ID: CnKINLUaFj4""
  },
  {
    "{": ""      ""Video ID: LACUT8RW6SI""
  },
  {
    "{": ""      ""Video ID: htSWwyrxUIA""
  },
  {
    "{": ""      ""Video ID: A7IZIRgzNEY""
  },
  {
    "{": ""      ""Video ID: sE8fgi_3iDI""
  },
  {
    "{": ""      ""Video ID: ludmllBDfEc""
  },
  {
    "{": ""      ""Video ID: GNe1e9gHsHI""
  },
  {
    "{": ""      ""Video ID: eJuHwgo61IA""
  },
  {
    "{": ""      ""Video ID: n3jeRkvfxlY""
  },
  {
    "{": ""      ""Video ID: VsREnYw6Afg""
  },
  {
    "{": ""      ""Video ID: lmOZmnTgtOs""
  },
  {
    "{": ""      ""Video ID: 4pc4TQWH4Gc""
  },
  {
    "{": ""      ""Video ID: D9BKx2HN8Ms""
  },
  {
    "{": ""      ""Video ID: aBBJDjM4jIw""
  },
  {
    "{": ""      ""Video ID: 9AMK0e8U87o""
  },
  {
    "{": ""      ""Video ID: YS30r1mjTdY""
  },
  {
    "{": ""      ""Video ID: qIFWcLvahiY""
  },
  {
    "{": ""      ""Video ID: O9eRYU7LMHA""
  },
  {
    "{": ""      ""Video ID: 5Z7hNb8lagM""
  },
  {
    "{": ""      ""Video ID: 8RZJGCCuC7E""
  },
  {
    "{": ""      ""Video ID: Xd61FTNQw9w""
  },
  {
    "{": ""      ""Video ID: Tfn1XapOq30""
  },
  {
    "{": ""      ""Video ID: awAmDAXlgDY""
  },
  {
    "{": ""      ""Video ID: FLuWThqAqJs""
  },
  {
    "{": ""      ""Video ID: YXoxFtXXW5M""
  },
  {
    "{": ""      ""Video ID: G2gZWZIK8us""
  },
  {
    "{": ""      ""Video ID: OB3Mkac7_Kk""
  },
  {
    "{": ""      ""Video ID: nP-Rm2atzU0""
  },
  {
    "{": ""      ""Video ID: C1f6mqtuDj8""
  },
  {
    "{": ""      ""Video ID: yDg3mFFpLrA""
  },
  {
    "{": ""      ""Video ID: FGznGVHo458""
  },
  {
    "{": ""      ""Video ID: 7ZXfyN1K_jY""
  },
  {
    "{": ""      ""Video ID: lYsMMs7asAU""
  },
  {
    "{": ""      ""Video ID: Pdtb6yxolSw""
  },
  {
    "{": ""      ""Video ID: s0iKvlWZHJM""
  },
  {
    "{": ""      ""Video ID: ioD9wzOKjls""
  },
  {
    "{": ""      ""Video ID: DYwVEOKRmLU""
  },
  {
    "{": ""      ""Video ID: JK2SAbNuC_o""
  },
  {
    "{": ""      ""Video ID: MHiqvzLhvn8""
  },
  {
    "{": ""      ""Video ID: 9HgsBn4kCaM""
  },
  {
    "{": ""      ""Video ID: I3dtPx9BZNs""
  },
  {
    "{": ""      ""Video ID: WTbYHKPZPIU""
  },
  {
    "{": ""      ""Video ID: _qY1nOuCN9c""
  },
  {
    "{": ""      ""Video ID: xYL5uLqtnqU""
  },
  {
    "{": ""      ""Video ID: F4BB8MgR8js""
  },
  {
    "{": ""      ""Video ID: foBmBF5Hxnc""
  },
  {
    "{": ""      ""Video ID: zfjOq441o3M""
  },
  {
    "{": ""      ""Video ID: 8tpPsLrXSv8""
  },
  {
    "{": ""      ""Video ID: MeME2b-yEyI""
  },
  {
    "{": ""      ""Video ID: 3Edu4nglddA""
  },
  {
    "{": ""      ""Video ID: SsiMU1_dIPQ""
  },
  {
    "{": ""      ""Video ID: _zDgjEYpEHM""
  },
  {
    "{": ""      ""Video ID: qSmTwuVkwJQ""
  },
  {
    "{": ""      ""Video ID: 2HpfOpVXkQc""
  },
  {
    "{": ""      ""Video ID: nZ0opsHwdP8""
  },
  {
    "{": ""      ""Video ID: Cc9xk33GasI""
  },
  {
    "{": ""      ""Video ID: cgXzhm-gsR4""
  },
  {
    "{": ""      ""Video ID: yhrplGb3SOI""
  },
  {
    "{": ""      ""Video ID: hem3heQdeiY""
  },
  {
    "{": ""      ""Video ID: t8RgtJfSBvw""
  },
  {
    "{": ""      ""Video ID: _0_UP2-odoA""
  },
  {
    "{": ""      ""Video ID: MZK-cxCJrEg""
  },
  {
    "{": ""      ""Video ID: 69jjcazxLcY""
  },
  {
    "{": ""      ""Video ID: Ce6u6vWbYmg""
  },
  {
    "{": ""      ""Video ID: J7owZu098Xg""
  },
  {
    "{": ""      ""Video ID: 5T6uwWfv2ow""
  },
  {
    "{": ""      ""Video ID: gsN3V56J478""
  },
  {
    "{": ""      ""Video ID: fPTp5SASPLg""
  },
  {
    "{": ""      ""Video ID: Yy1IxQ2w0_E""
  },
  {
    "{": ""      ""Video ID: e-5aqNttxxQ""
  },
  {
    "{": ""      ""Video ID: W_xV9SW1OrM""
  },
  {
    "{": ""      ""Video ID: E0uqFQ0y6w8""
  },
  {
    "{": ""      ""Video ID: MKcSr0HQhRA""
  },
  {
    "{": ""      ""Video ID: SSdd1gbHgag""
  },
  {
    "{": ""      ""Video ID: ED5no6oAQc4""
  },
  {
    "{": ""      ""Video ID: IKkrxNGODkc""
  },
  {
    "{": ""      ""Video ID: UF9Pahclz3Y""
  },
  {
    "{": ""      ""Video ID: e23DZBC5mx8""
  },
  {
    "{": ""      ""Video ID: 9hLcVUvBN3M""
  },
  {
    "{": ""      ""Video ID: WLU9BBCSy8Q""
  },
  {
    "{": ""      ""Video ID: x5s4Tm7cPTg""
  },
  {
    "{": ""      ""Video ID: P842Tmi6lrc""
  },
  {
    "{": ""      ""Video ID: Gjo9otIJxjE""
  },
  {
    "{": ""      ""Video ID: k0En-9sWawc""
  },
  {
    "{": ""      ""Video ID: xLKIUFo2mUA""
  },
  {
    "{": ""      ""Video ID: ccWMl4YgSAE""
  },
  {
    "{": ""      ""Video ID: iIG76nBQyfQ""
  },
  {
    "{": ""      ""Video ID: Gilppk_bku8""
  },
  {
    "{": ""      ""Video ID: Mb8jMldp6Jg""
  },
  {
    "{": ""      ""Video ID: ginSmD-VEeQ""
  },
  {
    "{": ""      ""Video ID: xrxXLKQIsJ0""
  },
  {
    "{": ""      ""Video ID: 2wmsGQxua_I""
  },
  {
    "{": ""      ""Video ID: SXgZhPjMQLQ""
  },
  {
    "{": ""      ""Video ID: _UzIRqnQhbw""
  },
  {
    "{": ""      ""Video ID: _ACrTzs4L78""
  },
  {
    "{": ""      ""Video ID: UHIKiN_mkHs""
  },
  {
    "{": ""      ""Video ID: za10AixYAcs""
  },
  {
    "{": ""      ""Video ID: SQV5KekF6Hc""
  },
  {
    "{": ""      ""Video ID: KczKw496JAg""
  },
  {
    "{": ""      ""Video ID: aDP0-k-bufU""
  },
  {
    "{": ""      ""Video ID: hwq-YOfPQu0""
  },
  {
    "{": ""      ""Video ID: ZM_RVi2ZoNE""
  },
  {
    "{": ""      ""Video ID: 82uEULONZhs""
  },
  {
    "{": ""      ""Video ID: nmH2nyPsz9Y""
  },
  {
    "{": ""      ""Video ID: DVUP0QV98Xk""
  },
  {
    "{": ""      ""Video ID: JY0UdmTzEEE""
  },
  {
    "{": ""      ""Video ID: 1Jatb8oFFpw""
  },
  {
    "{": ""      ""Video ID: 1l69MYGTKnc""
  },
  {
    "{": ""      ""Video ID: AJ2j8141jvU""
  },
  {
    "{": ""      ""Video ID: jX6AuL28m7I""
  },
  {
    "{": ""      ""Video ID: hSPlmIRNFoo""
  },
  {
    "{": ""      ""Video ID: JhZv5yPmlGw""
  },
  {
    "{": ""      ""Video ID: pqjdQFrZXco""
  },
  {
    "{": ""      ""Video ID: pt5lLyy3IkE""
  },
  {
    "{": ""      ""Video ID: BEn5MEjDW5M""
  },
  {
    "{": ""      ""Video ID: l4kXx2iQs1c""
  },
  {
    "{": ""      ""Video ID: euFKBgf_GqU""
  },
  {
    "{": ""      ""Video ID: c8cSyHDZwTs""
  },
  {
    "{": ""      ""Video ID: HDHliJ7wwiA""
  },
  {
    "{": ""      ""Video ID: wPYIba2R_FE""
  },
  {
    "{": ""      ""Video ID: 1AzRT-8AxKM""
  },
  {
    "{": ""      ""Video ID: eklIKnHl3cc""
  },
  {
    "{": ""      ""Video ID: sSeG2g0A6Ho""
  },
  {
    "{": ""      ""Video ID: x3H1BpSKbUA""
  },
  {
    "{": ""      ""Video ID: xUWJ8bf09BU""
  },
  {
    "{": ""      ""Video ID: -_qvhRMk2mM""
  },
  {
    "{": ""      ""Video ID: fRmad4_2Nbk""
  },
  {
    "{": ""      ""Video ID: fIu6WDa3dEI""
  },
  {
    "{": ""      ""Video ID: IXTlQHTuh3I""
  },
  {
    "{": ""      ""Video ID: XDPH0LF9hbY""
  },
  {
    "{": ""      ""Video ID: VF3oeDljW08""
  },
  {
    "{": ""      ""Video ID: 6djJbjcvsrg""
  },
  {
    "{": ""      ""Video ID: L-cs7QdPdtU""
  },
  {
    "{": ""      ""Video ID: tht3RwqVuhY""
  },
  {
    "{": ""      ""Video ID: 0vmduwfxnq4""
  },
  {
    "{": ""      ""Video ID: PKY8yHx63ew""
  },
  {
    "{": ""      ""Video ID: _m1uFE6o1Dw""
  },
  {
    "{": ""      ""Video ID: L63jZhVdYqM""
  },
  {
    "{": ""      ""Video ID: Q7JCyMb1UDA""
  },
  {
    "{": ""      ""Video ID: K0A4OYlPSG0""
  },
  {
    "{": ""      ""Video ID: yYFmuOBrds0""
  },
  {
    "{": ""      ""Video ID: NGfNzm3cP8U""
  },
  {
    "{": ""      ""Video ID: XrDl2HOWCAs""
  },
  {
    "{": ""      ""Video ID: 134o_5AGVIM""
  },
  {
    "{": ""      ""Video ID: XNVE5NSXlPU""
  },
  {
    "{": ""      ""Video ID: gNnkYzlVtMc""
  },
  {
    "{": ""      ""Video ID: oxKLVUj_5nw""
  },
  {
    "{": ""      ""Video ID: yWrUesy0_ys""
  },
  {
    "{": ""      ""Video ID: 4D-vxrE9MsQ""
  },
  {
    "{": ""      ""Video ID: A7vhZdi-InE""
  },
  {
    "{": ""      ""Video ID: VMqs-khH_yQ""
  },
  {
    "{": ""      ""Video ID: b8TPB9RHLaw""
  },
  {
    "{": ""      ""Video ID: Lk1WufusZIw""
  },
  {
    "{": ""      ""Video ID: jr5tqCccvw0""
  },
  {
    "{": ""      ""Video ID: VQ0QDANCRfk""
  },
  {
    "{": ""      ""Video ID: SJzDJZ-thiU""
  },
  {
    "{": ""      ""Video ID: 7hOdHTs9AVs""
  },
  {
    "{": ""      ""Video ID: GccfVr2RgBc""
  },
  {
    "{": ""      ""Video ID: iK6jIviuKYg""
  },
  {
    "{": ""      ""Video ID: -IiyFtYF10o""
  },
  {
    "{": ""      ""Video ID: WeVwhXv_nCY""
  },
  {
    "{": ""      ""Video ID: f0M7gVMJpxY""
  },
  {
    "{": ""      ""Video ID: -X_UDxF7t8U""
  },
  {
    "{": ""      ""Video ID: q4N3QD4RveA""
  },
  {
    "{": ""      ""Video ID: GPMYrJgM7Ho""
  },
  {
    "{": ""      ""Video ID: wz1LAICItlg""
  },
  {
    "{": ""      ""Video ID: ME-jisb45No""
  },
  {
    "{": ""      ""Video ID: wj2tW6igBis""
  },
  {
    "{": ""      ""Video ID: ByBdzaGobII""
  },
  {
    "{": ""      ""Video ID: jGb-MOBJPqQ""
  },
  {
    "{": ""      ""Video ID: gdH-mFlS0l0""
  },
  {
    "{": ""      ""Video ID: W6UMLiEZ1Vk""
  },
  {
    "{": ""      ""Video ID: ixMVUKV60kE""
  },
  {
    "{": ""      ""Video ID: iExSMI6hQDg""
  },
  {
    "{": ""      ""Video ID: v1aTWyF8oa8""
  },
  {
    "{": ""      ""Video ID: 7ThdoMC3azk""
  },
  {
    "{": ""      ""Video ID: teypasmbw6s""
  },
  {
    "{": ""      ""Video ID: 3xJY3Pnoots""
  },
  {
    "{": ""      ""Video ID: 67PiLOEufkM""
  },
  {
    "{": ""      ""Video ID: YrjFTKU273Y""
  },
  {
    "{": ""      ""Video ID: CICxH1cXvDM""
  },
  {
    "{": ""      ""Video ID: ZRxSGXxG-Jo""
  },
  {
    "{": ""      ""Video ID: IMaMYL_shxc""
  },
  {
    "{": ""      ""Video ID: tAa5RXHlXzs""
  },
  {
    "{": ""      ""Video ID: gPutYwiiE0o""
  },
  {
    "{": ""      ""Video ID: Qtti_A_HJbg""
  },
  {
    "{": ""      ""Video ID: qKdQe3gnr3Y""
  },
  {
    "{": ""      ""Video ID: K3ImVTE7rEg""
  },
  {
    "{": ""      ""Video ID: -g93NkI66_8""
  },
  {
    "{": ""      ""Video ID: sd6FJBfdqoY""
  },
  {
    "{": ""      ""Video ID: dRxw3eHsW3o""
  },
  {
    "{": ""      ""Video ID: XfySNucW0v0""
  },
  {
    "{": ""      ""Video ID: z6ME61qz9nE""
  },
  {
    "{": ""      ""Video ID: GCfE9UFCdto""
  },
  {
    "{": ""      ""Video ID: fJIZjAJJ4M4""
  },
  {
    "{": ""      ""Video ID: cfCLzX6BBBA""
  },
  {
    "{": ""      ""Video ID: veWn-aQQpuQ""
  },
  {
    "{": ""      ""Video ID: zKd8EEEREQY""
  },
  {
    "{": ""      ""Video ID: Jy9lyV-dqfc""
  },
  {
    "{": ""      ""Video ID: ebhe6WGncSE""
  },
  {
    "{": ""      ""Video ID: hEzcm8YWq2Y""
  },
  {
    "{": ""      ""Video ID: KkRXpcRkEPo""
  },
  {
    "{": ""      ""Video ID: lA-oY-zz2Fc""
  },
  {
    "{": ""      ""Video ID: B_FMyr8cB5E""
  },
  {
    "{": ""      ""Video ID: 2f8HSP3jwZ0""
  },
  {
    "{": ""      ""Video ID: eGEuHcOcTcE""
  },
  {
    "{": ""      ""Video ID: Y_MvC4FQVSs""
  },
  {
    "{": ""      ""Video ID: tB9bvR3VcRc""
  },
  {
    "{": ""      ""Video ID: xAePTWaobHw""
  },
  {
    "{": ""      ""Video ID: dyadOMnhqq0""
  },
  {
    "{": ""      ""Video ID: UIYUJKSPa34""
  },
  {
    "{": ""      ""Video ID: 34um-V4TXYc""
  },
  {
    "{": ""      ""Video ID: T959Zg3B6mI""
  },
  {
    "{": ""      ""Video ID: kAweSLHk7KE""
  },
  {
    "{": ""      ""Video ID: l29mZa0ilco""
  },
  {
    "{": ""      ""Video ID: LPMKSxBJGMM""
  },
  {
    "{": ""      ""Video ID: B9GogRZR4Yg""
  },
  {
    "{": ""      ""Video ID: PW0eMARI_Kw""
  },
  {
    "{": ""      ""Video ID: 9LkTdcXJy74""
  },
  {
    "{": ""      ""Video ID: 6HtcX91BAbo""
  },
  {
    "{": ""      ""Video ID: RbLh647x1fM""
  },
  {
    "{": ""      ""Video ID: OEnMaoNN9NM""
  },
  {
    "{": ""      ""Video ID: bD6fsFcdG4w""
  },
  {
    "{": ""      ""Video ID: ZMNSf1r42ew""
  },
  {
    "{": ""      ""Video ID: L3JBjGXO90M""
  },
  {
    "{": ""      ""Video ID: msbW5JBihXs""
  },
  {
    "{": ""      ""Video ID: mkkNT070GL4""
  },
  {
    "{": ""      ""Video ID: d66uXqC12Iw""
  },
  {
    "{": ""      ""Video ID: F7xBrobr9HQ""
  },
  {
    "{": ""      ""Video ID: SSBqllWXOiM""
  },
  {
    "{": ""      ""Video ID: qJ3ud5cWa4k""
  },
  {
    "{": ""      ""Video ID: 7WOBitDwESo""
  },
  {
    "{": ""      ""Video ID: mzh6rUgL2Cs""
  },
  {
    "{": ""      ""Video ID: FhrAakcFqYs""
  },
  {
    "{": ""      ""Video ID: OW6i1rMCt1A""
  },
  {
    "{": ""      ""Video ID: CYUvaQHx_zE""
  },
  {
    "{": ""      ""Video ID: 7JWd-mqzRE4""
  },
  {
    "{": ""      ""Video ID: L2WnEE2MwUI""
  },
  {
    "{": ""      ""Video ID: mDAh2HJFoDU""
  },
  {
    "{": ""      ""Video ID: NUBir53XEkY""
  },
  {
    "{": ""      ""Video ID: qBK1l2lrdyw""
  },
  {
    "{": ""      ""Video ID: n22iVddBx9w""
  },
  {
    "{": ""      ""Video ID: R6Vbwx4s7Vc""
  },
  {
    "{": ""      ""Video ID: nWc9XNpcoYk""
  },
  {
    "{": ""      ""Video ID: KyAfuN3-F3k""
  },
  {
    "{": ""      ""Video ID: 5bjMkSPDpMw""
  },
  {
    "{": ""      ""Video ID: tkHfTWkJvEE""
  },
  {
    "{": ""      ""Video ID: CWMhmtZx7fs""
  },
  {
    "{": ""      ""Video ID: R3BuU_RglCo""
  },
  {
    "{": ""      ""Video ID: 5r8JyfOGnPU""
  },
  {
    "{": ""      ""Video ID: Gj6iaVGAEIw""
  },
  {
    "{": ""      ""Video ID: YEFSWVnBL3A""
  },
  {
    "{": ""      ""Video ID: C8qOf0OO8YM""
  },
  {
    "{": ""      ""Video ID: HfGytXRpfho""
  },
  {
    "{": ""      ""Video ID: yK5vYhhm1uA""
  },
  {
    "{": ""      ""Video ID: UUAKT8uHAIQ""
  },
  {
    "{": ""      ""Video ID: ptO5m-_XTik""
  },
  {
    "{": ""      ""Video ID: dXa6-SJdRjI""
  },
  {
    "{": ""      ""Video ID: ivln9P76arM""
  },
  {
    "{": ""      ""Video ID: cLzbaisnEx4""
  },
  {
    "{": ""      ""Video ID: uQ9XLiMfBRo""
  },
  {
    "{": ""      ""Video ID: rKL3gNAtqOQ""
  },
  {
    "{": ""      ""Video ID: OPw6crS8lNg""
  },
  {
    "{": ""      ""Video ID: fFru_mlFMQM""
  },
  {
    "{": ""      ""Video ID: wGH1OJGvtdQ""
  },
  {
    "{": ""      ""Video ID: 63qIq9t9Gqs""
  },
  {
    "{": ""      ""Video ID: roM9qX-pMgI""
  },
  {
    "{": ""      ""Video ID: q6AlYBv77Oc""
  },
  {
    "{": ""      ""Video ID: H3k4UO4VTl0""
  },
  {
    "{": ""      ""Video ID: DRqMtVSY49M""
  },
  {
    "{": ""      ""Video ID: Wk7M0BEQGz0""
  },
  {
    "{": ""      ""Video ID: ktV15HtOKsk""
  },
  {
    "{": ""      ""Video ID: x2A-gOKlmIs""
  },
  {
    "{": ""      ""Video ID: J2zBaKLYeqQ""
  },
  {
    "{": ""      ""Video ID: 1xfUqSR80eo""
  },
  {
    "{": ""      ""Video ID: Xf2uLJze2WY""
  },
  {
    "{": ""      ""Video ID: HVAQI3u4PVc""
  },
  {
    "{": ""      ""Video ID: tAXaXuwc7ro""
  },
  {
    "{": ""      ""Video ID: x2udoNmQkR4""
  },
  {
    "{": ""      ""Video ID: kwOQf9KfDMs""
  },
  {
    "{": ""      ""Video ID: oMaZhB7IPJ0""
  },
  {
    "{": ""      ""Video ID: BbKPuabq8Wc""
  },
  {
    "{": ""      ""Video ID: 0CbjUNzBV6I""
  },
  {
    "{": ""      ""Video ID: L3Wi9MCMoDk""
  },
  {
    "{": ""      ""Video ID: gF2wFx3KLks""
  },
  {
    "{": ""      ""Video ID: j8PQ-QEpLOw""
  },
  {
    "{": ""      ""Video ID: KsLjRYTn_1U""
  },
  {
    "{": ""      ""Video ID: 6xxW7PLtwe4""
  },
  {
    "{": ""      ""Video ID: TNm2G3ev-X0""
  },
  {
    "{": ""      ""Video ID: kUtV4q138to""
  },
  {
    "{": ""      ""Video ID: sV761Orl6V4""
  },
  {
    "{": ""      ""Video ID: tzroG2qO1YQ""
  },
  {
    "{": ""      ""Video ID: DI2HEjQqW5A""
  },
  {
    "{": ""      ""Video ID: 2nwSaGv3Roo""
  },
  {
    "{": ""      ""Video ID: tBKBUCjsN-s""
  },
  {
    "{": ""      ""Video ID: 90QunGmEWyw""
  },
  {
    "{": ""      ""Video ID: BetFuPWknLI""
  },
  {
    "{": ""      ""Video ID: 8efmKImxz9k""
  },
  {
    "{": ""      ""Video ID: MficS-ToFR4""
  },
  {
    "{": ""      ""Video ID: bce8ElPkvys""
  },
  {
    "{": ""      ""Video ID: GKnGsj5QXJs""
  },
  {
    "{": ""      ""Video ID: TI3BHd0ovHg""
  },
  {
    "{": ""      ""Video ID: Zbr-uxLBSgM""
  },
  {
    "{": ""      ""Video ID: 3W3bBEC4R1Y""
  },
  {
    "{": ""      ""Video ID: uA1cyG5KGlA""
  },
  {
    "{": ""      ""Video ID: f18d7lzCNNU""
  },
  {
    "{": ""      ""Video ID: UZ61yGJETHs""
  },
  {
    "{": ""      ""Video ID: trY4NrYxDoo""
  },
  {
    "{": ""      ""Video ID: 5HxPYQlYRXk""
  },
  {
    "{": ""      ""Video ID: RE-JOQTXRmo""
  },
  {
    "{": ""      ""Video ID: U8Q3xDtm8F8""
  },
  {
    "{": ""      ""Video ID: Yvy-whqLNdo""
  },
  {
    "{": ""      ""Video ID: GlEGYWfO7XM""
  },
  {
    "{": ""      ""Video ID: 3lDFLo-dbOU""
  },
  {
    "{": ""      ""Video ID: Hv5KvdJuuds""
  },
  {
    "{": ""      ""Video ID: de20zjR5aw8""
  },
  {
    "{": ""      ""Video ID: 5bYrGQGsCjU""
  },
  {
    "{": ""      ""Video ID: JYuhxwa9n1s""
  },
  {
    "{": ""      ""Video ID: MOjDKfAU-k0""
  },
  {
    "{": ""      ""Video ID: 18joS1IP2oc""
  },
  {
    "{": ""      ""Video ID: nKr-6qYUKao""
  },
  {
    "{": ""      ""Video ID: m4hWQKeoPIE""
  },
  {
    "{": ""      ""Video ID: olKnAY44Y7o""
  },
  {
    "{": ""      ""Video ID: 79aTqcoYeOM""
  },
  {
    "{": ""      ""Video ID: l3_vkMWfYdI""
  },
  {
    "{": ""      ""Video ID: cR3Fy52iuAU""
  },
  {
    "{": ""      ""Video ID: IXAcZyrF584""
  },
  {
    "{": ""      ""Video ID: 8DINV9Uq8tA""
  },
  {
    "{": ""      ""Video ID: vRzTgfo2PsM""
  },
  {
    "{": ""      ""Video ID: H5F7fVwr--Y""
  },
  {
    "{": ""      ""Video ID: QlDG0Xx7qV8""
  },
  {
    "{": ""      ""Video ID: Yem3FxpDOeY""
  },
  {
    "{": ""      ""Video ID: pHpUoWhhYKA""
  },
  {
    "{": ""      ""Video ID: BBn9TbmWgVc""
  },
  {
    "{": ""      ""Video ID: eYfHytkRbqA""
  },
  {
    "{": ""      ""Video ID: nIpLn6Zq_90""
  },
  {
    "{": ""      ""Video ID: G4HMVkwZ8dQ""
  },
  {
    "{": ""      ""Video ID: 8aD1iWj9Pu0""
  },
  {
    "{": ""      ""Video ID: 7GooXQ-mPnc""
  },
  {
    "{": ""      ""Video ID: 2LDgGhYi8mk""
  },
  {
    "{": ""      ""Video ID: 9yRxQH4-T3M""
  },
  {
    "{": ""      ""Video ID: C1Q2J4QvJsQ""
  },
  {
    "{": ""      ""Video ID: JA9_eSlwuWE""
  },
  {
    "{": ""      ""Video ID: 6EWWJ_l9PNA""
  },
  {
    "{": ""      ""Video ID: t38uaj5udbU""
  },
  {
    "{": ""      ""Video ID: pvle1Chm8mU""
  },
  {
    "{": ""      ""Video ID: sgWM8AxNNAw""
  },
  {
    "{": ""      ""Video ID: windbIyKl7U""
  },
  {
    "{": ""      ""Video ID: ZsGilZ1gLwM""
  },
  {
    "{": ""      ""Video ID: AO6b8G0HjS0""
  },
  {
    "{": ""      ""Video ID: bSKHgOqQePg""
  },
  {
    "{": ""      ""Video ID: I5DTjED_4GI""
  },
  {
    "{": ""      ""Video ID: TsMmlu8corA""
  },
  {
    "{": ""      ""Video ID: t2WvClP-5ZQ""
  },
  {
    "{": ""      ""Video ID: l75WAsrlRNA""
  },
  {
    "{": ""      ""Video ID: 11FBCnUx40s""
  },
  {
    "{": ""      ""Video ID: QnBNTtgo2mY""
  },
  {
    "{": ""      ""Video ID: 6YqescOIED0""
  },
  {
    "{": ""      ""Video ID: lh2ukIibJiE""
  },
  {
    "{": ""      ""Video ID: f4MRLyLQSzA""
  },
  {
    "{": ""      ""Video ID: CF2foNejEQE""
  },
  {
    "{": ""      ""Video ID: sT8iIiwxPjg""
  },
  {
    "{": ""      ""Video ID: VE6qJxSVVmA""
  },
  {
    "{": ""      ""Video ID: GrL3Jc0isF0""
  },
  {
    "{": ""      ""Video ID: 70xKFih59EI""
  },
  {
    "{": ""      ""Video ID: MojFk_VmB7E""
  },
  {
    "{": ""      ""Video ID: Ntq3KtA8IGo""
  },
  {
    "{": ""      ""Video ID: 52RZkq040GU""
  },
  {
    "{": ""      ""Video ID: p63mH7d0S6I""
  },
  {
    "{": ""      ""Video ID: se3gL5yKzw4""
  },
  {
    "{": ""      ""Video ID: 2M1Ji9ZijGI""
  },
  {
    "{": ""      ""Video ID: ec8-KLsaFyc""
  },
  {
    "{": ""      ""Video ID: vwNHmcGgJ9k""
  },
  {
    "{": ""      ""Video ID: rQtU6Ydpkwo""
  },
  {
    "{": ""      ""Video ID: N44s8a-6vks""
  },
  {
    "{": ""      ""Video ID: cSZYgeSflNw""
  },
  {
    "{": ""      ""Video ID: x5iPJwZkr6E""
  },
  {
    "{": ""      ""Video ID: OIV6peKMj9M""
  },
  {
    "{": ""      ""Video ID: OP-UpM8Q-wc""
  },
  {
    "{": ""      ""Video ID: UmMXDeOrrxo""
  },
  {
    "{": ""      ""Video ID: eVquhkZpJFw""
  },
  {
    "{": ""      ""Video ID: X3fzoB_BScE""
  },
  {
    "{": ""      ""Video ID: miWNoAdGMiE""
  },
  {
    "{": ""      ""Video ID: LX6VKmHEGs0""
  },
  {
    "{": ""      ""Video ID: vcGvUi1cJRo""
  },
  {
    "{": ""      ""Video ID: sm5lB_GWZVc""
  },
  {
    "{": ""      ""Video ID: SGmwZS-UB34""
  },
  {
    "{": ""      ""Video ID: fTMRV5WQRaw""
  },
  {
    "{": ""      ""Video ID: Bz_Kgj4Kkd4""
  },
  {
    "{": ""      ""Video ID: plNjNNvQoUs""
  },
  {
    "{": ""      ""Video ID: OTV4TkqPhhA""
  },
  {
    "{": ""      ""Video ID: HUNT_kGIc1Q""
  },
  {
    "{": ""      ""Video ID: xG-vgB_ChNk""
  },
  {
    "{": ""      ""Video ID: da8h3cw6BNI""
  },
  {
    "{": ""      ""Video ID: nLHNfwQHV5Y""
  },
  {
    "{": ""      ""Video ID: Blgq2XxkkQk""
  },
  {
    "{": ""      ""Video ID: o7KdVd1kGcI""
  },
  {
    "{": ""      ""Video ID: G4DBWP9h184""
  },
  {
    "{": ""      ""Video ID: NjetZXbhzYQ""
  },
  {
    "{": ""      ""Video ID: zPdf8pzIuZk""
  },
  {
    "{": ""      ""Video ID: 3ZDphNrJ7N0""
  },
  {
    "{": ""      ""Video ID: UzIe4pcWHGw""
  },
  {
    "{": ""      ""Video ID: KYOVioYKOD0""
  },
  {
    "{": ""      ""Video ID: ogNiNPy6r34""
  },
  {
    "{": ""      ""Video ID: mGu5qXzZnBI""
  },
  {
    "{": ""      ""Video ID: W5DaCijBG0s""
  },
  {
    "{": ""      ""Video ID: EqmvglAcKfI""
  },
  {
    "{": ""      ""Video ID: PNfFBsV9pk8""
  },
  {
    "{": ""      ""Video ID: bNT1CaTTxME""
  },
  {
    "{": ""      ""Video ID: VBy8AGtUA2A""
  },
  {
    "{": ""      ""Video ID: ReNLvgzwJAQ""
  },
  {
    "{": ""      ""Video ID: I5CKw0s_154""
  },
  {
    "{": ""      ""Video ID: xcuflipV0eM""
  },
  {
    "{": ""      ""Video ID: ojzgwzU8T7g""
  },
  {
    "{": ""      ""Video ID: 8kwmEIctuUw""
  },
  {
    "{": ""      ""Video ID: ABh2WcmlLzQ""
  },
  {
    "{": ""      ""Video ID: vp1T5HI4Zrc""
  },
  {
    "{": ""      ""Video ID: O_P_EldT6WY""
  },
  {
    "{": ""      ""Video ID: s1UEqHNVJZU""
  },
  {
    "{": ""      ""Video ID: _R7PRqkdR84""
  },
  {
    "{": ""      ""Video ID: GYxXs584tC8""
  },
  {
    "{": ""      ""Video ID: 14yguC4H10I""
  },
  {
    "{": ""      ""Video ID: 6Ow6413kLSI""
  },
  {
    "{": ""      ""Video ID: FIoABv9szp8""
  },
  {
    "{": ""      ""Video ID: 8J5OwK719qU""
  },
  {
    "{": ""      ""Video ID: tF2DlgffnUI""
  },
  {
    "{": ""      ""Video ID: t4lzszmahx8""
  },
  {
    "{": ""      ""Video ID: 8otYlHeVNSY""
  },
  {
    "{": ""      ""Video ID: Ybq1JWR0WAM""
  },
  {
    "{": ""      ""Video ID: 6aJQ0BzJpDo""
  },
  {
    "{": ""      ""Video ID: AYS0-eNrj8g""
  },
  {
    "{": ""      ""Video ID: LQVHzLqz8Bg""
  },
  {
    "{": ""      ""Video ID: Y1MnqK3UIm4""
  },
  {
    "{": ""      ""Video ID: vJ0llQggevY""
  },
  {
    "{": ""      ""Video ID: u4R-8MUs4R8""
  },
  {
    "{": ""      ""Video ID: lzyZ11GMxzQ""
  },
  {
    "{": ""      ""Video ID: tjNpWpwY_8U""
  },
  {
    "{": ""      ""Video ID: S_rlQ6_rnWA""
  },
  {
    "{": ""      ""Video ID: Rc6jcOi39XQ""
  },
  {
    "{": ""      ""Video ID: 0GfMGamZxKw""
  },
  {
    "{": ""      ""Video ID: 76y5evHb3Bo""
  },
  {
    "{": ""      ""Video ID: EjE5FSsAy_0""
  },
  {
    "{": ""      ""Video ID: 8c2EIpEBD80""
  },
  {
    "{": ""      ""Video ID: hiTwqjefrUw""
  },
  {
    "{": ""      ""Video ID: Fuk9o76WtLU""
  },
  {
    "{": ""      ""Video ID: cnRCJm12W-s""
  },
  {
    "{": ""      ""Video ID: MFDFpCbc8P8""
  },
  {
    "{": ""      ""Video ID: mPEt7AxgU2I""
  },
  {
    "{": ""      ""Video ID: 2wYEMsxiBaY""
  },
  {
    "{": ""      ""Video ID: iR-vVflHG1g""
  },
  {
    "{": ""      ""Video ID: 6rXoxM8kBjI""
  },
  {
    "{": ""      ""Video ID: q2y69POjOZs""
  },
  {
    "{": ""      ""Video ID: 6kL6a0iv-Pw""
  },
  {
    "{": ""      ""Video ID: PrhcBZ_K300""
  },
  {
    "{": ""      ""Video ID: 8skI2QXdidY""
  },
  {
    "{": ""      ""Video ID: I27nVOqlzKE""
  },
  {
    "{": ""      ""Video ID: nhuYPWHjlHM""
  },
  {
    "{": ""      ""Video ID: fa0i7XZXu1s""
  },
  {
    "{": ""      ""Video ID: ghrf46V8LZI""
  },
  {
    "{": ""      ""Video ID: TssGenhau5Y""
  },
  {
    "{": ""      ""Video ID: ImM_ZrRBRWo""
  },
  {
    "{": ""      ""Video ID: b0SbaVq-wAE""
  },
  {
    "{": ""      ""Video ID: xYP3jhqUC3I""
  },
  {
    "{": ""      ""Video ID: nFD2NS-ebE0""
  },
  {
    "{": ""      ""Video ID: nL1yDqNvWwY""
  },
  {
    "{": ""      ""Video ID: jORj4D8-APE""
  },
  {
    "{": ""      ""Video ID: 9PqaNj26xLs""
  },
  {
    "{": ""      ""Video ID: GtJItd_ZsaY""
  },
  {
    "{": ""      ""Video ID: yCkgMKKtw4M""
  },
  {
    "{": ""      ""Video ID: 5h7V6VLGF_Q""
  },
  {
    "{": ""      ""Video ID: bplimaetOd0""
  },
  {
    "{": ""      ""Video ID: 3zLQ_zad0po""
  },
  {
    "{": ""      ""Video ID: 7fL4o2ps_vE""
  },
  {
    "{": ""      ""Video ID: TqUe6jLR9kM""
  },
  {
    "{": ""      ""Video ID: c5t2N4gwdqk""
  },
  {
    "{": ""      ""Video ID: VJ6Wl_BVfo0""
  },
  {
    "{": ""      ""Video ID: 5Deq7c8woQI""
  },
  {
    "{": ""      ""Video ID: Ju_10CzEjw0""
  },
  {
    "{": ""      ""Video ID: OyGf8VPoYyY""
  },
  {
    "{": ""      ""Video ID: 5HFlvOBEnU0""
  },
  {
    "{": ""      ""Video ID: bt6pa1WTS0A""
  },
  {
    "{": ""      ""Video ID: b9nrTO2pP-Q""
  },
  {
    "{": ""      ""Video ID: p_SsakPOVoQ""
  },
  {
    "{": ""      ""Video ID: Dup02i-O25g""
  },
  {
    "{": ""      ""Video ID: ac5hXVv8yVg""
  },
  {
    "{": ""      ""Video ID: TijCmhGJmCE""
  },
  {
    "{": ""      ""Video ID: I8eogIsr-Es""
  },
  {
    "{": ""      ""Video ID: 24e48AY0O2Y""
  },
  {
    "{": ""      ""Video ID: 1vI-QbPCOA8""
  },
  {
    "{": ""      ""Video ID: 1Xzh5bBdsuM""
  },
  {
    "{": ""      ""Video ID: RE4HKZaTMGE""
  },
  {
    "{": ""      ""Video ID: Sax2njDDLIE""
  },
  {
    "{": ""      ""Video ID: o3GKbqoSgcI""
  },
  {
    "{": ""      ""Video ID: TYUKZDlAyRk""
  },
  {
    "{": ""      ""Video ID: Bg9lY7_hCGA""
  },
  {
    "{": ""      ""Video ID: dyf38s4pjD0""
  },
  {
    "{": ""      ""Video ID: 5q0ads8wXIw""
  },
  {
    "{": ""      ""Video ID: xqUcrnCiEzM""
  },
  {
    "{": ""      ""Video ID: q7VxMxVR-Bs""
  },
  {
    "{": ""      ""Video ID: pkN1n5TMXl0""
  },
  {
    "{": ""      ""Video ID: 8UBh4krBbQs""
  },
  {
    "{": ""      ""Video ID: PmVpgLqV-LQ""
  },
  {
    "{": ""      ""Video ID: e1qc6i8ouzA""
  },
  {
    "{": ""      ""Video ID: lmRep5MXsB0""
  },
  {
    "{": ""      ""Video ID: _aRfjyoeJ9I""
  },
  {
    "{": ""      ""Video ID: fTMx3LFCuPE""
  },
  {
    "{": ""      ""Video ID: 12BhS22ZySA""
  },
  {
    "{": ""      ""Video ID: LpkrLqahToI""
  },
  {
    "{": ""      ""Video ID: m_2ZaT-26Z4""
  },
  {
    "{": ""      ""Video ID: JLMJAJp_w0U""
  },
  {
    "{": ""      ""Video ID: vDkZ79S5hVo""
  },
  {
    "{": ""      ""Video ID: HRQPy7NEt2s""
  },
  {
    "{": ""      ""Video ID: pOmXOMpZLR4""
  },
  {
    "{": ""      ""Video ID: 7bpN3EHDfZA""
  },
  {
    "{": ""      ""Video ID: TXd_WgFGT9E""
  },
  {
    "{": ""      ""Video ID: k0tByMkfZd0""
  },
  {
    "{": ""      ""Video ID: AIycg7besN4""
  },
  {
    "{": ""      ""Video ID: WjBVPo-AtOE""
  },
  {
    "{": ""      ""Video ID: V73o6Fc7PfI""
  },
  {
    "{": ""      ""Video ID: oHbBMAZn--c""
  },
  {
    "{": ""      ""Video ID: WNYEoSRWi_Y""
  },
  {
    "{": ""      ""Video ID: ZC45b3IJGYw""
  },
  {
    "{": ""      ""Video ID: n51sJMVwrEc""
  },
  {
    "{": ""      ""Video ID: iC57a2p4MwE""
  },
  {
    "{": ""      ""Video ID: 4sZCNlPwG8o""
  },
  {
    "{": ""      ""Video ID: T4rXx-xXeG8""
  },
  {
    "{": ""      ""Video ID: Yc7xrrZXdCM""
  },
  {
    "{": ""      ""Video ID: eL6lN1dERps""
  },
  {
    "{": ""      ""Video ID: 7fIshcSkP7Q""
  },
  {
    "{": ""      ""Video ID: Lr6CT85pkjs""
  },
  {
    "{": ""      ""Video ID: Eiu2mlO9Big""
  },
  {
    "{": ""      ""Video ID: E3Lia4J3UYU""
  },
  {
    "{": ""      ""Video ID: jitcb7srPgg""
  },
  {
    "{": ""      ""Video ID: iqJOIQWkfWA""
  },
  {
    "{": ""      ""Video ID: TjQ8xIEyQlI""
  },
  {
    "{": ""      ""Video ID: KknFEguhD5s""
  },
  {
    "{": ""      ""Video ID: uCf4OxC8fLM""
  },
  {
    "{": ""      ""Video ID: eJEZLqOzB6o""
  },
  {
    "{": ""      ""Video ID: cOyzsejQAnM""
  },
  {
    "{": ""      ""Video ID: TghWJVpTl90""
  },
  {
    "{": ""      ""Video ID: qhjDGqtLN3s""
  },
  {
    "{": ""      ""Video ID: F3rPOHZa4rY""
  },
  {
    "{": ""      ""Video ID: g8vTNpOl8B8""
  },
  {
    "{": ""      ""Video ID: Hjsugj9H-Ac""
  },
  {
    "{": ""      ""Video ID: unvARgBm0BY""
  },
  {
    "{": ""      ""Video ID: S4A-s532Yn4""
  },
  {
    "{": ""      ""Video ID: f0xmPTjPj5I""
  },
  {
    "{": ""      ""Video ID: pMa_66Z_HeY""
  },
  {
    "{": ""      ""Video ID: 4vLN7MN6m-k""
  },
  {
    "{": ""      ""Video ID: xTgU4l0dnGU""
  },
  {
    "{": ""      ""Video ID: SNXM4Sq-GIA""
  },
  {
    "{": ""      ""Video ID: fvIlhN0frdY""
  },
  {
    "{": ""      ""Video ID: XXM3Wye9iW0""
  },
  {
    "{": ""      ""Video ID: XnneFgVaCCI""
  },
  {
    "{": ""      ""Video ID: 0ipO_k-1u7I""
  },
  {
    "{": ""      ""Video ID: ZFRlTJkf0sY""
  },
  {
    "{": ""      ""Video ID: ON947EtxREg""
  },
  {
    "{": ""      ""Video ID: RUplk8JaavI""
  },
  {
    "{": ""      ""Video ID: xlUlP4JUx6Y""
  },
  {
    "{": ""      ""Video ID: xt9Bvc8s_d0""
  },
  {
    "{": ""      ""Video ID: 4CvNHlanW98""
  },
  {
    "{": ""      ""Video ID: HL-VEwAlMNY""
  },
  {
    "{": ""      ""Video ID: m0_m2-LIc2c""
  },
  {
    "{": ""      ""Video ID: Ftv8TJ3QIFc""
  },
  {
    "{": ""      ""Video ID: 4PYcM3vyQxI""
  },
  {
    "{": ""      ""Video ID: JkT_yp2MHuA""
  },
  {
    "{": ""      ""Video ID: sWuJ9knTMsw""
  },
  {
    "{": ""      ""Video ID: vYvijXS3dGs""
  },
  {
    "{": ""      ""Video ID: 9GB-DuVMPUk""
  },
  {
    "{": ""      ""Video ID: kF_nlpWq0t0""
  },
  {
    "{": ""      ""Video ID: 6-uyu_qQV1g""
  },
  {
    "{": ""      ""Video ID: SuvWADtC0Rk""
  },
  {
    "{": ""      ""Video ID: 6O8vVqUlaaM""
  },
  {
    "{": ""      ""Video ID: plDmH_aw6N0""
  },
  {
    "{": ""      ""Video ID: vTH-GS2x9Ng""
  },
  {
    "{": ""      ""Video ID: RgNcKhkctf8""
  },
  {
    "{": ""      ""Video ID: v6A80r2HBkw""
  },
  {
    "{": ""      ""Video ID: ceJzz_-GxN0""
  },
  {
    "{": ""      ""Video ID: YrCmt4WB6XA""
  },
  {
    "{": ""      ""Video ID: m2dP6boH6mI""
  },
  {
    "{": ""      ""Video ID: uqxmPjB0WSs""
  },
  {
    "{": ""      ""Video ID: k27mErPIJ6c""
  },
  {
    "{": ""      ""Video ID: aUMGOeBlRZc""
  },
  {
    "{": ""      ""Video ID: A0gGRS9ng9g""
  },
  {
    "{": ""      ""Video ID: YFIAE0soNWo""
  },
  {
    "{": ""      ""Video ID: n1W56x3Fb5U""
  },
  {
    "{": ""      ""Video ID: uJ8DH-MaB2s""
  },
  {
    "{": ""      ""Video ID: SbtTfiIOzFI""
  },
  {
    "{": ""      ""Video ID: NX_LM7WZc9A""
  },
  {
    "{": ""      ""Video ID: RM3BNy24rsg""
  },
  {
    "{": ""      ""Video ID: Ip2nw0NWUW4""
  },
  {
    "{": ""      ""Video ID: bAejscXAui4""
  },
  {
    "{": ""      ""Video ID: ObvjdJrDPkg""
  },
  {
    "{": ""      ""Video ID: n3vvqu2QWLQ""
  },
  {
    "{": ""      ""Video ID: bWt8a1aMkZ4""
  },
  {
    "{": ""      ""Video ID: qkcI-vP_J_U""
  },
  {
    "{": ""      ""Video ID: Z-YjSRsOSu0""
  },
  {
    "{": ""      ""Video ID: 3vadVvci0s0""
  },
  {
    "{": ""      ""Video ID: Tpfp1odRWAQ""
  },
  {
    "{": ""      ""Video ID: VlePSTjhZz8""
  },
  {
    "{": ""      ""Video ID: hcBEYcKBJmY""
  },
  {
    "{": ""      ""Video ID: wLlyLM0YEdk""
  },
  {
    "{": ""      ""Video ID: p4e7wRSy5SI""
  },
  {
    "{": ""      ""Video ID: v0CfJlkXFqg""
  },
  {
    "{": ""      ""Video ID: 3B9LhwPsTQc""
  },
  {
    "{": ""      ""Video ID: oC12EA1MvS4""
  },
  {
    "{": ""      ""Video ID: MKfK6tNbqUM""
  },
  {
    "{": ""      ""Video ID: exIrhLzLUFw""
  },
  {
    "{": ""      ""Video ID: AdCiElbEjho""
  },
  {
    "{": ""      ""Video ID: svzNZnJ3xKo""
  },
  {
    "{": ""      ""Video ID: R3JXkaQ75IY""
  },
  {
    "{": ""      ""Video ID: tCNj0DpCuBg""
  },
  {
    "{": ""      ""Video ID: W2qliFk8P3s""
  },
  {
    "{": ""      ""Video ID: g8RNmHkDDxE""
  },
  {
    "{": ""      ""Video ID: 11lRFvq8miQ""
  },
  {
    "{": ""      ""Video ID: V5TXEUiR1Xk""
  },
  {
    "{": ""      ""Video ID: i7SRjUNyBpM""
  },
  {
    "{": ""      ""Video ID: _1HKJ6bHUiU""
  },
  {
    "{": ""      ""Video ID: dyUsVpFDhXI""
  },
  {
    "{": ""      ""Video ID: jwUxKTI8ukE""
  },
  {
    "{": ""      ""Video ID: EYBhwe2iqqY""
  },
  {
    "{": ""      ""Video ID: rAYUq-sIQFU""
  },
  {
    "{": ""      ""Video ID: 3zCac0pX5p4""
  },
  {
    "{": ""      ""Video ID: i0lhdJhwiak""
  },
  {
    "{": ""      ""Video ID: SXSjwoAQ4tk""
  },
  {
    "{": ""      ""Video ID: HHQBEywYEEI""
  },
  {
    "{": ""      ""Video ID: TFfW2uIOui0""
  },
  {
    "{": ""      ""Video ID: uiPhzVDeUxI""
  },
  {
    "{": ""      ""Video ID: 6OBId_2fCvo""
  },
  {
    "{": ""      ""Video ID: iA2gxdseS9A""
  },
  {
    "{": ""      ""Video ID: QODppeKsy5I""
  },
  {
    "{": ""      ""Video ID: 8_n-Ma0exsM""
  },
  {
    "{": ""      ""Video ID: BMTsWsbw1s4""
  },
  {
    "{": ""      ""Video ID: vg3YfYXoTho""
  },
  {
    "{": ""      ""Video ID: kvHGigXbm20""
  },
  {
    "{": ""      ""Video ID: 0PVgVB3JCZM""
  },
  {
    "{": ""      ""Video ID: ZKSUgH0f0qA""
  },
  {
    "{": ""      ""Video ID: 46sCGB9g8rY""
  },
  {
    "{": ""      ""Video ID: 3LaBdMyjPIE""
  },
  {
    "{": ""      ""Video ID: H7gzgqZWdHE""
  },
  {
    "{": ""      ""Video ID: E-G5QLjIiiY""
  },
  {
    "{": ""      ""Video ID: PAYrDw9_3sM""
  },
  {
    "{": ""      ""Video ID: V76m9PZYCpc""
  },
  {
    "{": ""      ""Video ID: urv03IRN2lI""
  },
  {
    "{": ""      ""Video ID: 8mZmZAW7URI""
  },
  {
    "{": ""      ""Video ID: r5aT9T10x-w""
  },
  {
    "{": ""      ""Video ID: 6RNgtzOC6Qk""
  },
  {
    "{": ""      ""Video ID: TdGVwvkNHfg""
  },
  {
    "{": ""      ""Video ID: sIzOieNRU-k""
  },
  {
    "{": ""      ""Video ID: VsAg_yodQtU""
  },
  {
    "{": ""      ""Video ID: 6zYP-IcnIeg""
  },
  {
    "{": ""      ""Video ID: neqSBxkprvI""
  },
  {
    "{": ""      ""Video ID: sbpglcyBlJA""
  },
  {
    "{": ""      ""Video ID: Ji-NS177CbU""
  },
  {
    "{": ""      ""Video ID: aR8k_d_3Amk""
  },
  {
    "{": ""      ""Video ID: RM0kOdM9KT8""
  },
  {
    "{": ""      ""Video ID: bC3Lb1DVI-Q""
  },
  {
    "{": ""      ""Video ID: gCTzaJrIVyY""
  },
  {
    "{": ""      ""Video ID: HrDMX0emNR0""
  },
  {
    "{": ""      ""Video ID: CAYIDO5832Q""
  },
  {
    "{": ""      ""Video ID: SaUYdeLJvI8""
  },
  {
    "{": ""      ""Video ID: 5SAxu5kgJL4""
  },
  {
    "{": ""      ""Video ID: ORuClN0NlL8""
  },
  {
    "{": ""      ""Video ID: 5ej2rxMbqSM""
  },
  {
    "{": ""      ""Video ID: D-nijNBAnGM""
  },
  {
    "{": ""      ""Video ID: mIv1wzVsvSM""
  },
  {
    "{": ""      ""Video ID: JbYUhttB378""
  },
  {
    "{": ""      ""Video ID: KEc75lh51uE""
  },
  {
    "{": ""      ""Video ID: Vm7LWLcyTUg""
  },
  {
    "{": ""      ""Video ID: 58esO1ds4KE""
  },
  {
    "{": ""      ""Video ID: _B79CVwGx0s""
  },
  {
    "{": ""      ""Video ID: 73-CtwDFi7Q""
  },
  {
    "{": ""      ""Video ID: UyyX8NxlB9A""
  },
  {
    "{": ""      ""Video ID: RwTeiocXgm8""
  },
  {
    "{": ""      ""Video ID: fTv6ZDRyqe8""
  },
  {
    "{": ""      ""Video ID: xAEOoitK4cA""
  },
  {
    "{": ""      ""Video ID: 0Er7y2Pvpss""
  },
  {
    "{": ""      ""Video ID: LFeofmchKwE""
  },
  {
    "{": ""      ""Video ID: KtxAyJdWat8""
  },
  {
    "{": ""      ""Video ID: WXcVYE6hqG8""
  },
  {
    "{": ""      ""Video ID: aD2B7ZdwJ-Y""
  },
  {
    "{": ""      ""Video ID: g_DaMKUP3Og""
  },
  {
    "{": ""      ""Video ID: q4f_PgZrwXU""
  },
  {
    "{": ""      ""Video ID: 3CE8q5K66_0""
  },
  {
    "{": ""      ""Video ID: RQwQQjDGbak""
  },
  {
    "{": ""      ""Video ID: oaHpAD9jcnw""
  },
  {
    "{": ""      ""Video ID: ZOiFk1ePY38""
  },
  {
    "{": ""      ""Video ID: b2RKFnFjWV0""
  },
  {
    "{": ""      ""Video ID: ayM3dbbXRt8""
  },
  {
    "{": ""      ""Video ID: mkVkSWl5oPk""
  },
  {
    "{": ""      ""Video ID: yhnaJp89_6A""
  },
  {
    "{": ""      ""Video ID: cZ13jHp7_P4""
  },
  {
    "{": ""      ""Video ID: LeYgE014mAM""
  },
  {
    "{": ""      ""Video ID: kjiMgwH0ttw""
  },
  {
    "{": ""      ""Video ID: 1e-OtdCJzfo""
  },
  {
    "{": ""      ""Video ID: js-HGzfKTMI""
  },
  {
    "{": ""      ""Video ID: dgsRmNKc-uA""
  },
  {
    "{": ""      ""Video ID: D6UAqakrQOs""
  },
  {
    "{": ""      ""Video ID: iS778lM11pc""
  },
  {
    "{": ""      ""Video ID: tWNkn4PNeVQ""
  },
  {
    "{": ""      ""Video ID: 6SGw4XoeSv4""
  },
  {
    "{": ""      ""Video ID: XsjSr262-6M""
  },
  {
    "{": ""      ""Video ID: hrG3fhc0xns""
  },
  {
    "{": ""      ""Video ID: RHyVR2kqMUw""
  },
  {
    "{": ""      ""Video ID: YbtL5N1TAsQ""
  },
  {
    "{": ""      ""Video ID: lE-Mx3BcY9g""
  },
  {
    "{": ""      ""Video ID: sUYxUyGTS3I""
  },
  {
    "{": ""      ""Video ID: eae_a_XY6lg""
  },
  {
    "{": ""      ""Video ID: F-r791keyI8""
  },
  {
    "{": ""      ""Video ID: 5zq7fVm2NtM""
  },
  {
    "{": ""      ""Video ID: J1voGyccmaA""
  },
  {
    "{": ""      ""Video ID: pTiiblwwLPk""
  },
  {
    "{": ""      ""Video ID: 3_p14nClVTA""
  },
  {
    "{": ""      ""Video ID: 1UsxMxtwMnM""
  },
  {
    "{": ""      ""Video ID: aA4HwFHiYyA""
  },
  {
    "{": ""      ""Video ID: skHwFjaCx2Q""
  },
  {
    "{": ""      ""Video ID: VjgidAICoQI""
  },
  {
    "{": ""      ""Video ID: y8iVE8f0XHc""
  },
  {
    "{": ""      ""Video ID: EkHuRRDshhg""
  },
  {
    "{": ""      ""Video ID: v9gSUbvoMGI""
  },
  {
    "{": ""      ""Video ID: s2dhwr7fSAY""
  },
  {
    "{": ""      ""Video ID: gGQ9TtjUKWo""
  },
  {
    "{": ""      ""Video ID: AzlTjhGxr7Y""
  },
  {
    "{": ""      ""Video ID: hQZ56hkKOlk""
  },
  {
    "{": ""      ""Video ID: pvsADU2OOWM""
  },
  {
    "{": ""      ""Video ID: Ygb5uyPZBkg""
  },
  {
    "{": ""      ""Video ID: 82g3KxcFuoY""
  },
  {
    "{": ""      ""Video ID: mEUO-TQd0I0""
  },
  {
    "{": ""      ""Video ID: pgyUCl-WUhQ""
  },
  {
    "{": ""      ""Video ID: 9LTFNiY5FiU""
  },
  {
    "{": ""      ""Video ID: ngMuiRMe6Ww""
  },
  {
    "{": ""      ""Video ID: X4GLpPCKpgg""
  },
  {
    "{": ""      ""Video ID: qgnvMfDu47c""
  },
  {
    "{": ""      ""Video ID: posHfcILWOk""
  },
  {
    "{": ""      ""Video ID: N-eW_8pJk-s""
  },
  {
    "{": ""      ""Video ID: C3e_Ffdx59I""
  },
  {
    "{": ""      ""Video ID: KLOakCdxfrA""
  },
  {
    "{": ""      ""Video ID: awu6kinTC2k""
  },
  {
    "{": ""      ""Video ID: hZ5eGqQQPTY""
  },
  {
    "{": ""      ""Video ID: ZeK0Je8BbJI""
  },
  {
    "{": ""      ""Video ID: kh94Zi6RO1Q""
  },
  {
    "{": ""      ""Video ID: FKhJORn2wzY""
  },
  {
    "{": ""      ""Video ID: YdJBvUnaVpA""
  },
  {
    "{": ""      ""Video ID: C2S3k2BIi6Y""
  },
  {
    "{": ""      ""Video ID: ZIPbhjIsqyE""
  },
  {
    "{": ""      ""Video ID: APmHR2bmQgw""
  },
  {
    "{": ""      ""Video ID: wIse11cqRJY""
  },
  {
    "{": ""      ""Video ID: BzWOKEueH14""
  },
  {
    "{": ""      ""Video ID: MWuE5ZnNNQg""
  },
  {
    "{": ""      ""Video ID: HN_qNrO2pcA""
  },
  {
    "{": ""      ""Video ID: 40_CCizoULM""
  },
  {
    "{": ""      ""Video ID: ci7EnRnsYHk""
  },
  {
    "{": ""      ""Video ID: RyCV-IZK_p8""
  },
  {
    "{": ""      ""Video ID: wdd8sEYk0gU""
  },
  {
    "{": ""      ""Video ID: oQDN74pvbRk""
  },
  {
    "{": ""      ""Video ID: wrairzx37gc""
  },
  {
    "{": ""      ""Video ID: QyVsa5SgV_A""
  },
  {
    "{": ""      ""Video ID: YtThU4x92vo""
  },
  {
    "{": ""      ""Video ID: PHuASERY11E""
  },
  {
    "{": ""      ""Video ID: 0oIMQiWvRlw""
  },
  {
    "{": ""      ""Video ID: Mzja8u6ueg8""
  },
  {
    "{": ""      ""Video ID: C8MDFNsh5Io""
  },
  {
    "{": ""      ""Video ID: 4n127LUzqXQ""
  },
  {
    "{": ""      ""Video ID: adQo7io7jNk""
  },
  {
    "{": ""      ""Video ID: Id0gZ2kiXeI""
  },
  {
    "{": ""      ""Video ID: 0x9Rls5I96c""
  },
  {
    "{": ""      ""Video ID: -d2K7z1s0Ko""
  },
  {
    "{": ""      ""Video ID: UOa_M-3YF6s""
  },
  {
    "{": ""      ""Video ID: fAivmEyg8Cc""
  },
  {
    "{": ""      ""Video ID: q9WtECn2U6o""
  },
  {
    "{": ""      ""Video ID: ar0BSQTpe4c""
  },
  {
    "{": ""      ""Video ID: k9LLdF81kjE""
  },
  {
    "{": ""      ""Video ID: 4fjEreMVWHY""
  },
  {
    "{": ""      ""Video ID: nbo8GIIIqNQ""
  },
  {
    "{": ""      ""Video ID: 2ANYCV7izGM""
  },
  {
    "{": ""      ""Video ID: AYo1F5vRL5M""
  },
  {
    "{": ""      ""Video ID: KjRJAF64i2w""
  },
  {
    "{": ""      ""Video ID: 6c23AhnmQFM""
  },
  {
    "{": ""      ""Video ID: FsZZ4G8_EbU""
  },
  {
    "{": ""      ""Video ID: 0yuBgu_Vxuw""
  },
  {
    "{": ""      ""Video ID: 2PDSWCpEiro""
  },
  {
    "{": ""      ""Video ID: J-1UPcp-8JQ""
  },
  {
    "{": ""      ""Video ID: XkZfCkWbDFk""
  },
  {
    "{": ""      ""Video ID: miCkFKAEdnM""
  },
  {
    "{": ""      ""Video ID: hfWvOcoWT2c""
  },
  {
    "{": ""      ""Video ID: CgFkCz4wAmE""
  },
  {
    "{": ""      ""Video ID: yHpaacfDtQE""
  },
  {
    "{": ""      ""Video ID: DNteXc1D_pc""
  },
  {
    "{": ""      ""Video ID: 8n-56qmeYfU""
  },
  {
    "{": ""      ""Video ID: NwoxHCvHYpU""
  },
  {
    "{": ""      ""Video ID: 3yYvTXi_Kpk""
  },
  {
    "{": ""      ""Video ID: ZL4W1asy8hU""
  },
  {
    "{": ""      ""Video ID: pSQapltuelw""
  },
  {
    "{": ""      ""Video ID: SF-Mkxnlavs""
  },
  {
    "{": ""      ""Video ID: 9UkboVH6rJ0""
  },
  {
    "{": ""      ""Video ID: Z9sVNAwTzws""
  },
  {
    "{": ""      ""Video ID: wzr2CYfxhPk""
  },
  {
    "{": ""      ""Video ID: m6IvY1xiDD8""
  },
  {
    "{": ""      ""Video ID: brmC2fgpVt4""
  },
  {
    "{": ""      ""Video ID: WBcCl6tsA9M""
  },
  {
    "{": ""      ""Video ID: WsP50jcpZac""
  },
  {
    "{": ""      ""Video ID: uMLxOS0cN-o""
  },
  {
    "{": ""      ""Video ID: nXXpVmPYbCo""
  },
  {
    "{": ""      ""Video ID: QCMcWXEy-po""
  },
  {
    "{": ""      ""Video ID: jJ1fg79EXH8""
  },
  {
    "{": ""      ""Video ID: mXLyuAF1U9c""
  },
  {
    "{": ""      ""Video ID: zBV--7v2eZE""
  },
  {
    "{": ""      ""Video ID: eeRprnS6Gcw""
  },
  {
    "{": ""      ""Video ID: qSbXok744ns""
  },
  {
    "{": ""      ""Video ID: M4GVBkicnbU""
  },
  {
    "{": ""      ""Video ID: VvARQo8qqJo""
  },
  {
    "{": ""      ""Video ID: Ytm5gP_cxEg""
  },
  {
    "{": ""      ""Video ID: 88qW7T_Pux0""
  },
  {
    "{": ""      ""Video ID: sAD-ult6SSU""
  },
  {
    "{": ""      ""Video ID: aCRGsHbQBWI""
  },
  {
    "{": ""      ""Video ID: 2rXdXOEg73Q""
  },
  {
    "{": ""      ""Video ID: JuV49UiE3nM""
  },
  {
    "{": ""      ""Video ID: llGkMtjB8aE""
  },
  {
    "{": ""      ""Video ID: WIWdQpchEU4""
  },
  {
    "{": ""      ""Video ID: kgTiFo0DOzQ""
  },
  {
    "{": ""      ""Video ID: ltZ0T3OacZw""
  },
  {
    "{": ""      ""Video ID: plYIUHvTQVU""
  },
  {
    "{": ""      ""Video ID: D9lPfKzQAXE""
  },
  {
    "{": ""      ""Video ID: PCTqm1y_Qpo""
  },
  {
    "{": ""      ""Video ID: QqugN2jqOug""
  },
  {
    "{": ""      ""Video ID: Qs_wKWgRmdE""
  },
  {
    "{": ""      ""Video ID: Z4X3x48ybcM""
  },
  {
    "{": ""      ""Video ID: Qprb27x2HgE""
  },
  {
    "{": ""      ""Video ID: Eq1WZJilw2s""
  },
  {
    "{": ""      ""Video ID: usF2jzFMJh4""
  },
  {
    "{": ""      ""Video ID: gNICkcG88NQ""
  },
  {
    "{": ""      ""Video ID: jnxn4dxa8jw""
  },
  {
    "{": ""      ""Video ID: 9mMkPkEaU5M""
  },
  {
    "{": ""      ""Video ID: Cd5nmzkvLnk""
  },
  {
    "{": ""      ""Video ID: AtSsBsxRvxE""
  },
  {
    "{": ""      ""Video ID: 06SwNtMP8_o""
  },
  {
    "{": ""      ""Video ID: J72wPa6tYWg""
  },
  {
    "{": ""      ""Video ID: xZUuXtC_9o0""
  },
  {
    "{": ""      ""Video ID: l6WmVVKLhgo""
  },
  {
    "{": ""      ""Video ID: cWnIzmZdRA0""
  },
  {
    "{": ""      ""Video ID: ZOOlDF8SpxI""
  },
  {
    "{": ""      ""Video ID: ehOKenFjGqY""
  },
  {
    "{": ""      ""Video ID: e5I0k8IXTWk""
  },
  {
    "{": ""      ""Video ID: QpF2peub7es""
  },
  {
    "{": ""      ""Video ID: JD7e88xOmPo""
  },
  {
    "{": ""      ""Video ID: FZaR49v4rq8""
  },
  {
    "{": ""      ""Video ID: XhTmSBFemQQ""
  },
  {
    "{": ""      ""Video ID: XeGitslBO0Q""
  },
  {
    "{": ""      ""Video ID: nr9uRbnzI1A""
  },
  {
    "{": ""      ""Video ID: vFWo7C4oEDk""
  },
  {
    "{": ""      ""Video ID: GQStPlJvMuE""
  },
  {
    "{": ""      ""Video ID: WS_zqbDiFe4""
  },
  {
    "{": ""      ""Video ID: FP_5PZusadY""
  },
  {
    "{": ""      ""Video ID: hAnpPyPN9PY""
  },
  {
    "{": ""      ""Video ID: O8GtxYZOjco""
  },
  {
    "{": ""      ""Video ID: 9fpyf6if47s""
  },
  {
    "{": ""      ""Video ID: vxgUCemGxQU""
  },
  {
    "{": ""      ""Video ID: ydtgEHA1ZtI""
  },
  {
    "{": ""      ""Video ID: A9KzSMVkYL4""
  },
  {
    "{": ""      ""Video ID: 8VVn0QXI7I8""
  },
  {
    "{": ""      ""Video ID: rZ2InppMk0o""
  },
  {
    "{": ""      ""Video ID: 1weM8W6k2a8""
  },
  {
    "{": ""      ""Video ID: --DZu2pgBzM""
  },
  {
    "{": ""      ""Video ID: sxwgX7eFmH4""
  },
  {
    "{": ""      ""Video ID: 1rD3C4TV_oc""
  },
  {
    "{": ""      ""Video ID: cUVNhvfeTLE""
  },
  {
    "{": ""      ""Video ID: c1yiMCQnNLM""
  },
  {
    "{": ""      ""Video ID: erxs74Vi9wI""
  },
  {
    "{": ""      ""Video ID: 7VW7dul6nCQ""
  },
  {
    "{": ""      ""Video ID: CaKg6IwgDXE""
  },
  {
    "{": ""      ""Video ID: slwnO2YTelQ""
  },
  {
    "{": ""      ""Video ID: HpyBMI2gIAs""
  },
  {
    "{": ""      ""Video ID: Q0O2k2QMrS8""
  },
  {
    "{": ""      ""Video ID: 3KSr1pozm6Y""
  },
  {
    "{": ""      ""Video ID: ULL2g95Dp4I""
  },
  {
    "{": ""      ""Video ID: Wx6hUSCicto""
  },
  {
    "{": ""      ""Video ID: lZ1wu6OWCug""
  },
  {
    "{": ""      ""Video ID: S4CjZ-OkGDs""
  },
  {
    "{": ""      ""Video ID: kJSA84LdDCM""
  },
  {
    "{": ""      ""Video ID: AvToNRFj_I8""
  },
  {
    "{": ""      ""Video ID: tr-ACvYRVu0""
  },
  {
    "{": ""      ""Video ID: --ZlfX_9530""
  },
  {
    "{": ""      ""Video ID: hlL_jfNMSbc""
  },
  {
    "{": ""      ""Video ID: h1J7TCc29AE""
  },
  {
    "{": ""      ""Video ID: 5ZeWIgT3eac""
  },
  {
    "{": ""      ""Video ID: ZsrTxMX0wwk""
  },
  {
    "{": ""      ""Video ID: L_M7j1zO4JE""
  },
  {
    "{": ""      ""Video ID: TGjUggnP7Zo""
  },
  {
    "{": ""      ""Video ID: Y2OdsBsDSUI""
  },
  {
    "{": ""      ""Video ID: vUdos3c8inc""
  },
  {
    "{": ""      ""Video ID: lPl_IJo1BBc""
  },
  {
    "{": ""      ""Video ID: fZSZcX9Ki4M""
  },
  {
    "{": ""      ""Video ID: OBTHYFCbF_4""
  },
  {
    "{": ""      ""Video ID: 3fht_fvgIJ0""
  },
  {
    "{": ""      ""Video ID: l5G_Lu2ZwdQ""
  },
  {
    "{": ""      ""Video ID: SZedRpuFIVY""
  },
  {
    "{": ""      ""Video ID: h8iAAUB71Dc""
  },
  {
    "{": ""      ""Video ID: tvc8cRdB1ec""
  },
  {
    "{": ""      ""Video ID: 8q7NDUOYnmU""
  },
  {
    "{": ""      ""Video ID: qX1SSRVTfgA""
  },
  {
    "{": ""      ""Video ID: Z9QV-XdcaxI""
  },
  {
    "{": ""      ""Video ID: pE45QHIUfiM""
  },
  {
    "{": ""      ""Video ID: u7gl8nNsDMA""
  },
  {
    "{": ""      ""Video ID: MGeol_aq8dc""
  },
  {
    "{": ""      ""Video ID: _vRTaJTs06w""
  },
  {
    "{": ""      ""Video ID: 34aU3NhqOas""
  },
  {
    "{": ""      ""Video ID: Ofuy5XKWw04""
  },
  {
    "{": ""      ""Video ID: Z7dCteaTZYU""
  },
  {
    "{": ""      ""Video ID: i3g7STNOn_E""
  },
  {
    "{": ""      ""Video ID: 7vTn1diEBh4""
  },
  {
    "{": ""      ""Video ID: byjzu9oEXmg""
  },
  {
    "{": ""      ""Video ID: G-Ecr8tWetI""
  },
  {
    "{": ""      ""Video ID: bfk9xY-dGwI""
  },
  {
    "{": ""      ""Video ID: 3iK2MYlkVXw""
  },
  {
    "{": ""      ""Video ID: bPPf8xNDjsQ""
  },
  {
    "{": ""      ""Video ID: 97PN07vi-n8""
  },
  {
    "{": ""      ""Video ID: YyhAHT99eAk""
  },
  {
    "{": ""      ""Video ID: Q8Pix1hw8q4""
  },
  {
    "{": ""      ""Video ID: s__MIj3LUsk""
  },
  {
    "{": ""      ""Video ID: c5cTshcaBWE""
  },
  {
    "{": ""      ""Video ID: CzZe2fVWOGs""
  },
  {
    "{": ""      ""Video ID: 0csLaBKagpo""
  },
  {
    "{": ""      ""Video ID: ATnuRnUCIf4""
  },
  {
    "{": ""      ""Video ID: nE3qJj3LWIc""
  },
  {
    "{": ""      ""Video ID: QqdXG4PywHg""
  },
  {
    "{": ""      ""Video ID: NYLT62nHX_k""
  },
  {
    "{": ""      ""Video ID: UelJrPMopf4""
  },
  {
    "{": ""      ""Video ID: 0OiamBxxoXA""
  },
  {
    "{": ""      ""Video ID: kb1OsPiHefY""
  },
  {
    "{": ""      ""Video ID: y_o7SfV3XtM""
  },
  {
    "{": ""      ""Video ID: oFsbE-jvHTA""
  },
  {
    "{": ""      ""Video ID: s78pUaIjRDU""
  },
  {
    "{": ""      ""Video ID: TBqPO3eknuQ""
  },
  {
    "{": ""      ""Video ID: CiayepK4WRI""
  },
  {
    "{": ""      ""Video ID: wk4hQlwaWTw""
  },
  {
    "{": ""      ""Video ID: uTx2MAOspS4""
  },
  {
    "{": ""      ""Video ID: 2y6pqFNNVcw""
  },
  {
    "{": ""      ""Video ID: -xroyOn9Ys4""
  },
  {
    "{": ""      ""Video ID: D3ioynT5760""
  },
  {
    "{": ""      ""Video ID: meYCja1S5es""
  },
  {
    "{": ""      ""Video ID: q8xqKBZpbz0""
  },
  {
    "{": ""      ""Video ID: nZ1RBAF4LyE""
  },
  {
    "{": ""      ""Video ID: Be8bD3XsUu8""
  },
  {
    "{": ""      ""Video ID: CW_I5Ru7VtU""
  },
  {
    "{": ""      ""Video ID: 26gOybx5TFE""
  },
  {
    "{": ""      ""Video ID: K_bRu-5qSM0""
  },
  {
    "{": ""      ""Video ID: -LqhGjgSal8""
  },
  {
    "{": ""      ""Video ID: VIglOfwqdNo""
  },
  {
    "{": ""      ""Video ID: wCAkAxHWnKA""
  },
  {
    "{": ""      ""Video ID: vCwN4Vk_vi4""
  },
  {
    "{": ""      ""Video ID: cVnPeHW-Aw4""
  },
  {
    "{": ""      ""Video ID: F251WZiz0qk""
  },
  {
    "{": ""      ""Video ID: i7DCFRqpTEQ""
  },
  {
    "{": ""      ""Video ID: jOkHRQBy3ew""
  },
  {
    "{": ""      ""Video ID: B_goaoKK4tc""
  },
  {
    "{": ""      ""Video ID: 0GJXtVYJ4gk""
  },
  {
    "{": ""      ""Video ID: MycA0VcEMQY""
  },
  {
    "{": ""      ""Video ID: f88xtnQIrQM""
  },
  {
    "{": ""      ""Video ID: nCZ_9_FpWtA""
  },
  {
    "{": ""      ""Video ID: R8j82gzMZMk""
  },
  {
    "{": ""      ""Video ID: LRcTIMXkQ8M""
  },
  {
    "{": ""      ""Video ID: 1cKvHEUMN1w""
  },
  {
    "{": ""      ""Video ID: aur0LJOGAjg""
  },
  {
    "{": ""      ""Video ID: 7p-DpAKYZnc""
  },
  {
    "{": ""      ""Video ID: zRaYXHHCgxo""
  },
  {
    "{": ""      ""Video ID: 7w57_P9DZJ4""
  },
  {
    "{": ""      ""Video ID: xAV6SX_h3i0""
  },
  {
    "{": ""      ""Video ID: VdZ8Fc8grM8""
  },
  {
    "{": ""      ""Video ID: 6yDGEMFZric""
  },
  {
    "{": ""      ""Video ID: TnToHAixW48""
  },
  {
    "{": ""      ""Video ID: IRi6shV_UiE""
  },
  {
    "{": ""      ""Video ID: jxp-iohRdjY""
  },
  {
    "{": ""      ""Video ID: Pguk3cr6XOY""
  },
  {
    "{": ""      ""Video ID: nA_z02y1Cns""
  },
  {
    "{": ""      ""Video ID: H_t6C-FxW9s""
  },
  {
    "{": ""      ""Video ID: _tV5ENAjlDY""
  },
  {
    "{": ""      ""Video ID: LnAFEjhrbEQ""
  },
  {
    "{": ""      ""Video ID: 02F6k5trvkA""
  },
  {
    "{": ""      ""Video ID: R8N7zUvh6iw""
  },
  {
    "{": ""      ""Video ID: -9ao_vOsZkg""
  },
  {
    "{": ""      ""Video ID: 1z_aOHJdHO8""
  },
  {
    "{": ""      ""Video ID: 47ojw-MB1GU""
  },
  {
    "{": ""      ""Video ID: tSiROILG0b4""
  },
  {
    "{": ""      ""Video ID: IQnYvPDYjwc""
  },
  {
    "{": ""      ""Video ID: NPZRflY-rAs""
  },
  {
    "{": ""      ""Video ID: ujnXzX_BWYA""
  },
  {
    "{": ""      ""Video ID: BiyaGQELAOU""
  },
  {
    "{": ""      ""Video ID: 0Txw5Jf8-go""
  },
  {
    "{": ""      ""Video ID: Bnm1RZJshWI""
  },
  {
    "{": ""      ""Video ID: kkhIrsmTa2Q""
  },
  {
    "{": ""      ""Video ID: PLoXbx0mmf4""
  },
  {
    "{": ""      ""Video ID: DVE3hXe4l24""
  },
  {
    "{": ""      ""Video ID: 4PCCZHNsVuw""
  },
  {
    "{": ""      ""Video ID: 2mqc7lb_6FM""
  },
  {
    "{": ""      ""Video ID: EUWDtbs7oC8""
  },
  {
    "{": ""      ""Video ID: AknctH94ACA""
  },
  {
    "{": ""      ""Video ID: Iu9GPGTgwlc""
  },
  {
    "{": ""      ""Video ID: yXdaA6-QYwA""
  },
  {
    "{": ""      ""Video ID: 0pRWwry2Dd0""
  },
  {
    "{": ""      ""Video ID: El9CyWGYblk""
  },
  {
    "{": ""      ""Video ID: Wz2C8w5se7Q""
  },
  {
    "{": ""      ""Video ID: i1YKhJ6EYPM""
  },
  {
    "{": ""      ""Video ID: q_jsXRcNsBo""
  },
  {
    "{": ""      ""Video ID: a3FIftbR1bk""
  },
  {
    "{": ""      ""Video ID: 4jDszR34Wkk""
  },
  {
    "{": ""      ""Video ID: cCkRvzl-nRU""
  },
  {
    "{": ""      ""Video ID: m5EuNf-1pgg""
  },
  {
    "{": ""      ""Video ID: kDEXtn0I2_c""
  },
  {
    "{": ""      ""Video ID: P_9al4IQOhk""
  },
  {
    "{": ""      ""Video ID: rdKCgKhZwxg""
  },
  {
    "{": ""      ""Video ID: JPDFuNW55uA""
  },
  {
    "{": ""      ""Video ID: GGOj0zSbrGw""
  },
  {
    "{": ""      ""Video ID: pw9DZIrriOg""
  },
  {
    "{": ""      ""Video ID: wNfqceheu5E""
  },
  {
    "{": ""      ""Video ID: vEfC2zOFli0""
  },
  {
    "{": ""      ""Video ID: gS6i_eImNI0""
  },
  {
    "{": ""      ""Video ID: ygF-zEr6v2Q""
  },
  {
    "{": ""      ""Video ID: dR38y2I5g5E""
  },
  {
    "{": ""      ""Video ID: ecCF9ficSno""
  },
  {
    "{": ""      ""Video ID: s5h2VHd-pMc""
  },
  {
    "{": ""      ""Video ID: K96GJJ3mvMU""
  },
  {
    "{": ""      ""Video ID: ASe_Z2jdM8I""
  },
  {
    "{": ""      ""Video ID: iIzIpjYeVLw""
  },
  {
    "{": ""      ""Video ID: bEQjrfGMN5w""
  },
  {
    "{": ""      ""Video ID: 4kK8kTbr-yM""
  },
  {
    "{": ""      ""Video ID: HLwqIaresoQ""
  },
  {
    "{": ""      ""Video ID: tzlalM5-aRY""
  },
  {
    "{": ""      ""Video ID: nQ6wONaqM8g""
  },
  {
    "{": ""      ""Video ID: UjSPDrOErXE""
  },
  {
    "{": ""      ""Video ID: qjGf-zOhaew""
  },
  {
    "{": ""      ""Video ID: zGIxHEuqD18""
  },
  {
    "{": ""      ""Video ID: UTySXc5FvFc""
  },
  {
    "{": ""      ""Video ID: e-2ZexPapH4""
  },
  {
    "{": ""      ""Video ID: 6TRdiqVKJJ8""
  },
  {
    "{": ""      ""Video ID: mGAuXid4FYU""
  },
  {
    "{": ""      ""Video ID: Th0fi459hY4""
  },
  {
    "{": ""      ""Video ID: iUk90alM0g0""
  },
  {
    "{": ""      ""Video ID: 6PDApLXdZPI""
  },
  {
    "{": ""      ""Video ID: 7gu-BLfzBKc""
  },
  {
    "{": ""      ""Video ID: -gQAsiHOyII""
  },
  {
    "{": ""      ""Video ID: Fyg0EeAy9PM""
  },
  {
    "{": ""      ""Video ID: -N3oPjTTQTM""
  },
  {
    "{": ""      ""Video ID: 7wpXEJUXIDE""
  },
  {
    "{": ""      ""Video ID: XrOFsMLmiX0""
  },
  {
    "{": ""      ""Video ID: y6VCrcYPnYM""
  },
  {
    "{": ""      ""Video ID: 8mMkyvNEXDM""
  },
  {
    "{": ""      ""Video ID: OlpOVC9td5s""
  },
  {
    "{": ""      ""Video ID: F6qV3EiuaHI""
  },
  {
    "{": ""      ""Video ID: mARHIZEABoA""
  },
  {
    "{": ""      ""Video ID: LZ176RixOZo""
  },
  {
    "{": ""      ""Video ID: epomVCpZUJY""
  },
  {
    "{": ""      ""Video ID: Rqk2Geg9O7U""
  },
  {
    "{": ""      ""Video ID: rU1sn6Sr1zw""
  },
  {
    "{": ""      ""Video ID: NbBK9KpLhtA""
  },
  {
    "{": ""      ""Video ID: PcPj-5YlZjc""
  },
  {
    "{": ""      ""Video ID: QM6B0-jZ7To""
  },
  {
    "{": ""      ""Video ID: Hx02IPIkaNY""
  },
  {
    "{": ""      ""Video ID: 3E04nW37fbo""
  },
  {
    "{": ""      ""Video ID: sFfYNfnlflg""
  },
  {
    "{": ""      ""Video ID: ZjnD6Uxq2AA""
  },
  {
    "{": ""      ""Video ID: qQ1QQaYUnXU""
  },
  {
    "{": ""      ""Video ID: YDqi6_pQW6o""
  },
  {
    "{": ""      ""Video ID: AQbD85cYXHk""
  },
  {
    "{": ""      ""Video ID: VTTVRzg6fUE""
  },
  {
    "{": ""      ""Video ID: LqHwHVbTkKg""
  },
  {
    "{": ""      ""Video ID: UeqpdsNuirU""
  },
  {
    "{": ""      ""Video ID: z1nGhEThmRQ""
  },
  {
    "{": ""      ""Video ID: 1AietUjW1Tg""
  },
  {
    "{": ""      ""Video ID: hIJbWsMcTPw""
  },
  {
    "{": ""      ""Video ID: C1V1qseeiQ4""
  },
  {
    "{": ""      ""Video ID: qHqzls2TYUg""
  },
  {
    "{": ""      ""Video ID: 6Jbgxvk_ndA""
  },
  {
    "{": ""      ""Video ID: -u0_n8wilp8""
  },
  {
    "{": ""      ""Video ID: bQDjIQc_gq4""
  },
  {
    "{": ""      ""Video ID: 1h_B6EFnYfM""
  },
  {
    "{": ""      ""Video ID: Bzw9xLFhP18""
  },
  {
    "{": ""      ""Video ID: fdx2K06ajRQ""
  },
  {
    "{": ""      ""Video ID: 1oX2q0uTy8U""
  },
  {
    "{": ""      ""Video ID: Wk9GUBEKY4w""
  },
  {
    "{": ""      ""Video ID: Aw8hImTcWRs""
  },
  {
    "{": ""      ""Video ID: N0PLTQOW4FU""
  },
  {
    "{": ""      ""Video ID: KrIOUdZtIOI""
  },
  {
    "{": ""      ""Video ID: ZWCW1Jkv27w""
  },
  {
    "{": ""      ""Video ID: O6WcOX4B6Ds""
  },
  {
    "{": ""      ""Video ID: DpOTIWpAjQQ""
  },
  {
    "{": ""      ""Video ID: 0ZC5KL8pdsM""
  },
  {
    "{": ""      ""Video ID: QHLkZwYaoIM""
  },
  {
    "{": ""      ""Video ID: zSxnHWHckMs""
  },
  {
    "{": ""      ""Video ID: p9U7gaunrEY""
  },
  {
    "{": ""      ""Video ID: tVuy3SRyEUY""
  },
  {
    "{": ""      ""Video ID: 7yVjEjyhT50""
  },
  {
    "{": ""      ""Video ID: 3uNfrR4iEF0""
  },
  {
    "{": ""      ""Video ID: htb7HYJ9Pg0""
  },
  {
    "{": ""      ""Video ID: 5zbgHh13peU""
  },
  {
    "{": ""      ""Video ID: gPNxIf2Htsw""
  },
  {
    "{": ""      ""Video ID: YWkV_C9PZXY""
  },
  {
    "{": ""      ""Video ID: ceI3QgPB2YE""
  },
  {
    "{": ""      ""Video ID: _DQrGT-Rrtc""
  },
  {
    "{": ""      ""Video ID: kBbZMuU04tk""
  },
  {
    "{": ""      ""Video ID: BFT0qLrOQ6E""
  },
  {
    "{": ""      ""Video ID: XlkKQoUlOQg""
  },
  {
    "{": ""      ""Video ID: oeEDKBxkNgM""
  },
  {
    "{": ""      ""Video ID: hhjOnYbKJJw""
  },
  {
    "{": ""      ""Video ID: Mpfoh47L8iw""
  },
  {
    "{": ""      ""Video ID: 5ocbZhRQS9I""
  },
  {
    "{": ""      ""Video ID: nZ6eTcL4iGg""
  },
  {
    "{": ""      ""Video ID: 3iKDAhN_hl4""
  },
  {
    "{": ""      ""Video ID: 0v3OeszyaxE""
  },
  {
    "{": ""      ""Video ID: xsI1aioXNuA""
  },
  {
    "{": ""      ""Video ID: Hunsef86WdY""
  },
  {
    "{": ""      ""Video ID: zF6OjKuNjLk""
  },
  {
    "{": ""      ""Video ID: bS4nX72GA3M""
  },
  {
    "{": ""      ""Video ID: cN779g3Xv8A""
  },
  {
    "{": ""      ""Video ID: NOMr_cJlZDw""
  },
  {
    "{": ""      ""Video ID: I6JWqllbhXE""
  },
  {
    "{": ""      ""Video ID: HlgH5JOvtkM""
  },
  {
    "{": ""      ""Video ID: WcYxpHkhLxw""
  },
  {
    "{": ""      ""Video ID: Hcv63UeQ52Q""
  },
  {
    "{": ""      ""Video ID: uDobNR1FPjw""
  },
  {
    "{": ""      ""Video ID: XgjutzKIBXA""
  },
  {
    "{": ""      ""Video ID: 0vIPZdScsu0""
  },
  {
    "{": ""      ""Video ID: EFIF2496Br0""
  },
  {
    "{": ""      ""Video ID: twiduuJ-JHw""
  },
  {
    "{": ""      ""Video ID: 7gGRdn3mm28""
  },
  {
    "{": ""      ""Video ID: ttMA4Db1fBE""
  },
  {
    "{": ""      ""Video ID: WErzvFYOd9s""
  },
  {
    "{": ""      ""Video ID: j-xSSZsvd9w""
  },
  {
    "{": ""      ""Video ID: DPqiSXge3B8""
  },
  {
    "{": ""      ""Video ID: 0RNi0Ct8GpY""
  },
  {
    "{": ""      ""Video ID: YvE_cM50hhs""
  },
  {
    "{": ""      ""Video ID: 6VV0P4M8t3s""
  },
  {
    "{": ""      ""Video ID: 22iYB1SH7TE""
  },
  {
    "{": ""      ""Video ID: n6roDesKdxU""
  },
  {
    "{": ""      ""Video ID: 1YhP-j9Yzy4""
  },
  {
    "{": ""      ""Video ID: SNtDebihAOA""
  },
  {
    "{": ""      ""Video ID: ivLTIm_35C0""
  },
  {
    "{": ""      ""Video ID: KkGTQaerH_8""
  },
  {
    "{": ""      ""Video ID: Wh0dkEFQng4""
  },
  {
    "{": ""      ""Video ID: z44gBaPaKx8""
  },
  {
    "{": ""      ""Video ID: -Hyq7mk0PG8""
  },
  {
    "{": ""      ""Video ID: 09HCGQdg2LE""
  },
  {
    "{": ""      ""Video ID: 6t-uu7gj0oM""
  },
  {
    "{": ""      ""Video ID: VETWsJglYbM""
  },
  {
    "{": ""      ""Video ID: 181ndZG9D3s""
  },
  {
    "{": ""      ""Video ID: de5QrMub_R0""
  },
  {
    "{": ""      ""Video ID: wvfxavTzHlc""
  },
  {
    "{": ""      ""Video ID: QmftaJKnkbI""
  },
  {
    "{": ""      ""Video ID: -PFIpoapc5Y""
  },
  {
    "{": ""      ""Video ID: 71v7jZQ3WDk""
  },
  {
    "{": ""      ""Video ID: TLq2WMm5vso""
  },
  {
    "{": ""      ""Video ID: lfWaXdHhRGI""
  },
  {
    "{": ""      ""Video ID: B2O66W3R_Tw""
  },
  {
    "{": ""      ""Video ID: dbeGY13Fnno""
  },
  {
    "{": ""      ""Video ID: Df1TBsUIYoQ""
  },
  {
    "{": ""      ""Video ID: eGwy3sgVhYI""
  },
  {
    "{": ""      ""Video ID: Y_WOhkALf_4""
  },
  {
    "{": ""      ""Video ID: RXtHsmLoDJ8""
  },
  {
    "{": ""      ""Video ID: YTuOJIi9BTc""
  },
  {
    "{": ""      ""Video ID: 62FS5d3ER-A""
  },
  {
    "{": ""      ""Video ID: r7fLdHUI6Jg""
  },
  {
    "{": ""      ""Video ID: xmOk5eEYMRk""
  },
  {
    "{": ""      ""Video ID: 4dcXCdrnbbI""
  },
  {
    "{": ""      ""Video ID: 0jSemOMm7Bs""
  },
  {
    "{": ""      ""Video ID: uKQCubi0CyM""
  },
  {
    "{": ""      ""Video ID: QesWMb6ErjU""
  },
  {
    "{": ""      ""Video ID: hwDnjHFrllg""
  },
  {
    "{": ""      ""Video ID: Uhku6rYzrp4""
  },
  {
    "{": ""      ""Video ID: RZo_2wLhwog""
  },
  {
    "{": ""      ""Video ID: OYnFOOEPbdI""
  },
  {
    "{": ""      ""Video ID: iw4WoRUUhRw""
  },
  {
    "{": ""      ""Video ID: JpZzDK0UzW0""
  },
  {
    "{": ""      ""Video ID: t-jpIq437EE""
  },
  {
    "{": ""      ""Video ID: ttuWWwOntlk""
  },
  {
    "{": ""      ""Video ID: guTw9Hj06-U""
  },
  {
    "{": ""      ""Video ID: wYBK63jCg_U""
  },
  {
    "{": ""      ""Video ID: 6cmfN_ELZCg""
  },
  {
    "{": ""      ""Video ID: EObou7Iqh-A""
  },
  {
    "{": ""      ""Video ID: CSijwZC9tcI""
  },
  {
    "{": ""      ""Video ID: Xh9g48wEMEA""
  },
  {
    "{": ""      ""Video ID: vKvRQrRU4zM""
  },
  {
    "{": ""      ""Video ID: lWS3r135h14""
  },
  {
    "{": ""      ""Video ID: gCjYr7yc2gM""
  },
  {
    "{": ""      ""Video ID: iYNyauhVbc0""
  },
  {
    "{": ""      ""Video ID: 8IONO36SlAc""
  },
  {
    "{": ""      ""Video ID: GD9zlML3Hq0""
  },
  {
    "{": ""      ""Video ID: v5Yq_UtoUvo""
  },
  {
    "{": ""      ""Video ID: UIeWRlhv-3U""
  },
  {
    "{": ""      ""Video ID: Kd1auLc1jF4""
  },
  {
    "{": ""      ""Video ID: W7uRNgET9KQ""
  },
  {
    "{": ""      ""Video ID: zDSpxv4i0Lo""
  },
  {
    "{": ""      ""Video ID: 0jXRoZviLfw""
  },
  {
    "{": ""      ""Video ID: BGlee6jDw-s""
  },
  {
    "{": ""      ""Video ID: GAi7cHiaf-U""
  },
  {
    "{": ""      ""Video ID: zPWjjT8xchk""
  },
  {
    "{": ""      ""Video ID: 6-4JfCWnf-I""
  },
  {
    "{": ""      ""Video ID: gMiqe8oAhCI""
  },
  {
    "{": ""      ""Video ID: HD3DQnShOVw""
  },
  {
    "{": ""      ""Video ID: scgUKAPgPvY""
  },
  {
    "{": ""      ""Video ID: wlPTx-ynIUM""
  },
  {
    "{": ""      ""Video ID: PmqSEX-14N0""
  },
  {
    "{": ""      ""Video ID: oCBQiHZaamo""
  },
  {
    "{": ""      ""Video ID: VjOW33SJl8g""
  },
  {
    "{": ""      ""Video ID: W0AirhqJ8C8""
  },
  {
    "{": ""      ""Video ID: QKBO9K5aFHw""
  },
  {
    "{": ""      ""Video ID: QjDNREvZKUk""
  },
  {
    "{": ""      ""Video ID: GJrLMZw0Jp4""
  },
  {
    "{": ""      ""Video ID: T0Cy3xVBWk0""
  },
  {
    "{": ""      ""Video ID: dmsRcAZaXx4""
  },
  {
    "{": ""      ""Video ID: FTCNom_dJgc""
  },
  {
    "{": ""      ""Video ID: I61gnK8qbSU""
  },
  {
    "{": ""      ""Video ID: W-plhS0wx0w""
  },
  {
    "{": ""      ""Video ID: vmlSkw0lCuQ""
  },
  {
    "{": ""      ""Video ID: S6CjJ0pYkv0""
  },
  {
    "{": ""      ""Video ID: je7SQpO2V_Y""
  },
  {
    "{": ""      ""Video ID: Q2qFG_Usn2w""
  },
  {
    "{": ""      ""Video ID: x9oSoUhliP4""
  },
  {
    "{": ""      ""Video ID: ecImAc6Ymxs""
  },
  {
    "{": ""      ""Video ID: E2eJoVIXWu4""
  },
  {
    "{": ""      ""Video ID: re7hn-TlBN8""
  },
  {
    "{": ""      ""Video ID: 2sxqTyG1eVw""
  },
  {
    "{": ""      ""Video ID: arOnYqc7ICc""
  },
  {
    "{": ""      ""Video ID: yQxgeX_sX_Y""
  },
  {
    "{": ""      ""Video ID: 3scbJQi8jGY""
  },
  {
    "{": ""      ""Video ID: rPNkbChJcik""
  },
  {
    "{": ""      ""Video ID: rLlKzZ1Db9I""
  },
  {
    "{": ""      ""Video ID: NAswhoYlhLA""
  },
  {
    "{": ""      ""Video ID: GIHWlV04-84""
  },
  {
    "{": ""      ""Video ID: nxmFuQ2JAfk""
  },
  {
    "{": ""      ""Video ID: q_jy6wi9DqA""
  },
  {
    "{": ""      ""Video ID: KKvLdIylY40""
  },
  {
    "{": ""      ""Video ID: E49m_vxPpHw""
  },
  {
    "{": ""      ""Video ID: eFThUp8h7q8""
  },
  {
    "{": ""      ""Video ID: yABigudP91o""
  },
  {
    "{": ""      ""Video ID: KmWQgRcEOZE""
  },
  {
    "{": ""      ""Video ID: 5K29lRSODp0""
  },
  {
    "{": ""      ""Video ID: DFUVGaUkzVc""
  },
  {
    "{": ""      ""Video ID: 7fniKOKEPF4""
  },
  {
    "{": ""      ""Video ID: ijlltvweXYo""
  },
  {
    "{": ""      ""Video ID: RpfMxNi5bAI""
  },
  {
    "{": ""      ""Video ID: jWWIyWxD5u0""
  },
  {
    "{": ""      ""Video ID: A9s62Hbx5Sk""
  },
  {
    "{": ""      ""Video ID: dqog-br6nhY""
  },
  {
    "{": ""      ""Video ID: 398fbYo1SLg""
  },
  {
    "{": ""      ""Video ID: -429sftfed4""
  },
  {
    "{": ""      ""Video ID: LAxaEZ7JNks""
  },
  {
    "{": ""      ""Video ID: LRUhybfg2SI""
  },
  {
    "{": ""      ""Video ID: n3vEb3wkpAY""
  },
  {
    "{": ""      ""Video ID: 0dP6ywxdAVI""
  },
  {
    "{": ""      ""Video ID: xbnelpoq3Es""
  },
  {
    "{": ""      ""Video ID: vWoU0yzVcDM""
  },
  {
    "{": ""      ""Video ID: qDu5ZCortd0""
  },
  {
    "{": ""      ""Video ID: 0ZW9nLQr5o4""
  },
  {
    "{": ""      ""Video ID: eilbPLg5eqg""
  },
  {
    "{": ""      ""Video ID: wxnp8N7K0Dg""
  },
  {
    "{": ""      ""Video ID: vTKH3-CWKV8""
  },
  {
    "{": ""      ""Video ID: k09dueLtZwg""
  },
  {
    "{": ""      ""Video ID: lEs7ANxB7aI""
  },
  {
    "{": ""      ""Video ID: fP93Py8a760""
  },
  {
    "{": ""      ""Video ID: f8Qx4iewBBE""
  },
  {
    "{": ""      ""Video ID: QlC7sCUmFQI""
  },
  {
    "{": ""      ""Video ID: pdCpvXjUJ7c""
  },
  {
    "{": ""      ""Video ID: h1hUhP7RVvA""
  },
  {
    "{": ""      ""Video ID: _2eFv7alF9A""
  },
  {
    "{": ""      ""Video ID: QGomOFvyLAw""
  },
  {
    "{": ""      ""Video ID: frWyuDT-FPo""
  },
  {
    "{": ""      ""Video ID: U0xk5VXsJ_Y""
  },
  {
    "{": ""      ""Video ID: qgowk0HlX2Y""
  },
  {
    "{": ""      ""Video ID: add29yBe9ho""
  },
  {
    "{": ""      ""Video ID: 9Hs-7gz2nsI""
  },
  {
    "{": ""      ""Video ID: sieeyRKGqpY""
  },
  {
    "{": ""      ""Video ID: VEK3418HgNs""
  },
  {
    "{": ""      ""Video ID: FUsltuNO6l8""
  },
  {
    "{": ""      ""Video ID: lyND-XfwRm8""
  },
  {
    "{": ""      ""Video ID: vA5ULpS9nzw""
  },
  {
    "{": ""      ""Video ID: OdkErlnq9NQ""
  },
  {
    "{": ""      ""Video ID: 0Rpb5T_TNSI""
  },
  {
    "{": ""      ""Video ID: 3OahempP490""
  },
  {
    "{": ""      ""Video ID: HcAXOkg0Je0""
  },
  {
    "{": ""      ""Video ID: Kkq8jnjWsgc""
  },
  {
    "{": ""      ""Video ID: CeZN-2x9_lY""
  },
  {
    "{": ""      ""Video ID: x4L9DzsiiqY""
  },
  {
    "{": ""      ""Video ID: u6Vj7z0rqNo""
  },
  {
    "{": ""      ""Video ID: FeoZePXagfo""
  },
  {
    "{": ""      ""Video ID: gPcMgVC7vP4""
  },
  {
    "{": ""      ""Video ID: Jw6oKlPa1_o""
  },
  {
    "{": ""      ""Video ID: gHeV824gCio""
  },
  {
    "{": ""      ""Video ID: 4fe0JtUg4sM""
  },
  {
    "{": ""      ""Video ID: JvPZZyRT6Is""
  },
  {
    "{": ""      ""Video ID: ECjHXzHRxVw""
  },
  {
    "{": ""      ""Video ID: cxz_t_byIvE""
  },
  {
    "{": ""      ""Video ID: 3vX6_EQLHK8""
  },
  {
    "{": ""      ""Video ID: pTojKejA-O8""
  },
  {
    "{": ""      ""Video ID: zZZGYn6824M""
  },
  {
    "{": ""      ""Video ID: J6BQHfGTtVw""
  },
  {
    "{": ""      ""Video ID: 0oTv1w8fO9Y""
  },
  {
    "{": ""      ""Video ID: VBXMGbDHnCc""
  },
  {
    "{": ""      ""Video ID: WPyXV6nRqhQ""
  },
  {
    "{": ""      ""Video ID: Pc9nnbZHjgc""
  },
  {
    "{": ""      ""Video ID: SWTg-jc0QFM""
  },
  {
    "{": ""      ""Video ID: VkJKGThofvY""
  },
  {
    "{": ""      ""Video ID: Zcv4TX7fxuY""
  },
  {
    "{": ""      ""Video ID: EtYu_tHbJCw""
  },
  {
    "{": ""      ""Video ID: 8vGNnfwRwr4""
  },
  {
    "{": ""      ""Video ID: HI9u-tK3D0I""
  },
  {
    "{": ""      ""Video ID: C-KC31H5Sdk""
  },
  {
    "{": ""      ""Video ID: QmS97X_7YWI""
  },
  {
    "{": ""      ""Video ID: ygmm7gFXK74""
  },
  {
    "{": ""      ""Video ID: J0voS_W-xnU""
  },
  {
    "{": ""      ""Video ID: sQT-ALYgCsc""
  },
  {
    "{": ""      ""Video ID: 1jkcF8L7rLs""
  },
  {
    "{": ""      ""Video ID: x_sBv8JEKdc""
  },
  {
    "{": ""      ""Video ID: sRv953XZX6Y""
  },
  {
    "{": ""      ""Video ID: SBHOov5_ygI""
  },
  {
    "{": ""      ""Video ID: w-iWP6_q3Nw""
  },
  {
    "{": ""      ""Video ID: Fm5WPSVVOgI""
  },
  {
    "{": ""      ""Video ID: -FThNQHjKDo""
  },
  {
    "{": ""      ""Video ID: VjVUJYRj-Rs""
  },
  {
    "{": ""      ""Video ID: OROhRKYQE7I""
  },
  {
    "{": ""      ""Video ID: OA9LxX4mAo0""
  },
  {
    "{": ""      ""Video ID: tVyy8A-J_Qs""
  },
  {
    "{": ""      ""Video ID: RjlpamhrId8""
  },
  {
    "{": ""      ""Video ID: yB7FMrZ6a0k""
  },
  {
    "{": ""      ""Video ID: T11n8CUOHJY""
  },
  {
    "{": ""      ""Video ID: zL9R_i9Of1c""
  },
  {
    "{": ""      ""Video ID: MUf9_OQ_0pI""
  },
  {
    "{": ""      ""Video ID: wGllHoq99IY""
  },
  {
    "{": ""      ""Video ID: WcZNHg7op_M""
  },
  {
    "{": ""      ""Video ID: bbtKmAQu2Ho""
  },
  {
    "{": ""      ""Video ID: UYmB9g8G0ss""
  },
  {
    "{": ""      ""Video ID: UFaYfc2U1Kc""
  },
  {
    "{": ""      ""Video ID: KlBs6iLdDUo""
  },
  {
    "{": ""      ""Video ID: xiMoKAybo1A""
  },
  {
    "{": ""      ""Video ID: eKsi341kNy4""
  },
  {
    "{": ""      ""Video ID: ehPOA1H10yQ""
  },
  {
    "{": ""      ""Video ID: j8IHVOSo1aU""
  },
  {
    "{": ""      ""Video ID: uXbaYCrKINw""
  },
  {
    "{": ""      ""Video ID: XqfviqNY6qQ""
  },
  {
    "{": ""      ""Video ID: rngveKKjego""
  },
  {
    "{": ""      ""Video ID: bNjiyUb0bxI""
  },
  {
    "{": ""      ""Video ID: rwHDRazn0w8""
  },
  {
    "{": ""      ""Video ID: A1Iv_q68S3E""
  },
  {
    "{": ""      ""Video ID: TFhW7NixZPA""
  },
  {
    "{": ""      ""Video ID: 2eaWW4-jgiE""
  },
  {
    "{": ""      ""Video ID: mSXaelZFvGE""
  },
  {
    "{": ""      ""Video ID: vWAgHplOd8Y""
  },
  {
    "{": ""      ""Video ID: NtXDKfwuVQI""
  },
  {
    "{": ""      ""Video ID: jS2JXGdY2is""
  },
  {
    "{": ""      ""Video ID: -rIaFYXvR3Q""
  },
  {
    "{": ""      ""Video ID: y0UqHIH-wsM""
  },
  {
    "{": ""      ""Video ID: yQRlHM4U1yo""
  },
  {
    "{": ""      ""Video ID: vdW5oopAvwM""
  },
  {
    "{": ""      ""Video ID: BeHRsybITsw""
  },
  {
    "{": ""      ""Video ID: myH-5_4zmBQ""
  },
  {
    "{": ""      ""Video ID: PJQFKp1Ao1A""
  },
  {
    "{": ""      ""Video ID: 9eMGbDJmgv0""
  },
  {
    "{": ""      ""Video ID: 5fX75oUB1xk""
  },
  {
    "{": ""      ""Video ID: gSneR7lHNpk""
  },
  {
    "{": ""      ""Video ID: VSCNpzD37l4""
  },
  {
    "{": ""      ""Video ID: 5wdl79CJwrA""
  },
  {
    "{": ""      ""Video ID: LE9wEvLHeuQ""
  },
  {
    "{": ""      ""Video ID: Lhbm1PON-yk""
  },
  {
    "{": ""      ""Video ID: 34hHQn8TKzI""
  },
  {
    "{": ""      ""Video ID: 1ucEVxVcldA""
  },
  {
    "{": ""      ""Video ID: UDfFmHoc5Po""
  },
  {
    "{": ""      ""Video ID: xRFT65KSGrY""
  },
  {
    "{": ""      ""Video ID: CjZpqN66-Ww""
  },
  {
    "{": ""      ""Video ID: KJ3UtpBtHjE""
  },
  {
    "{": ""      ""Video ID: n_FE6Z7H1-I""
  },
  {
    "{": ""      ""Video ID: rDE6w3K_xoU""
  },
  {
    "{": ""      ""Video ID: 9eqzT8j4lic""
  },
  {
    "{": ""      ""Video ID: eRvWzpnEZA8""
  },
  {
    "{": ""      ""Video ID: IDGiEuMIwmc""
  },
  {
    "{": ""      ""Video ID: -CMIscaQF98""
  },
  {
    "{": ""      ""Video ID: XI2nDUEtxvM""
  },
  {
    "{": ""      ""Video ID: SYKXKJvApfw""
  },
  {
    "{": ""      ""Video ID: b6px1bV0hBg""
  },
  {
    "{": ""      ""Video ID: 7GRv-kv5XEg""
  },
  {
    "{": ""      ""Video ID: OvHz2aIZozA""
  },
  {
    "{": ""      ""Video ID: au9RoNSoThE""
  },
  {
    "{": ""      ""Video ID: LvAv0bDwV84""
  },
  {
    "{": ""      ""Video ID: KX0879AwWyg""
  },
  {
    "{": ""      ""Video ID: UU2qrdQBtgY""
  },
  {
    "{": ""      ""Video ID: gBUJY3Oz4kE""
  },
  {
    "{": ""      ""Video ID: 1VtjJtEJy7w""
  },
  {
    "{": ""      ""Video ID: 69mFBUANkgI""
  },
  {
    "{": ""      ""Video ID: thLq5yy2sJA""
  },
  {
    "{": ""      ""Video ID: w8FApgaDxWw""
  },
  {
    "{": ""      ""Video ID: p-U1MKZUQk4""
  },
  {
    "{": ""      ""Video ID: 8J5B8MquW44""
  },
  {
    "{": ""      ""Video ID: 8siqrpAR-94""
  },
  {
    "{": ""      ""Video ID: _i1t3ug_CA0""
  },
  {
    "{": ""      ""Video ID: KPzOrCV_zz8""
  },
  {
    "{": ""      ""Video ID: d6Nc1AhYb4g""
  },
  {
    "{": ""      ""Video ID: GgVv0-TzgxA""
  },
  {
    "{": ""      ""Video ID: A84ideqnJqE""
  },
  {
    "{": ""      ""Video ID: dYUtKKbBTkw""
  },
  {
    "{": ""      ""Video ID: o6xraBjNUz0""
  },
  {
    "{": ""      ""Video ID: HmH0FzOzrtc""
  },
  {
    "{": ""      ""Video ID: iMfnl25K60E""
  },
  {
    "{": ""      ""Video ID: Iu2j63qs-_8""
  },
  {
    "{": ""      ""Video ID: K-h4u2TMIuk""
  },
  {
    "{": ""      ""Video ID: S6u76pZYSco""
  },
  {
    "{": ""      ""Video ID: P1-z6pyb4D4""
  },
  {
    "{": ""      ""Video ID: iR8apSr3m9U""
  },
  {
    "{": ""      ""Video ID: eO-A0luP480""
  },
  {
    "{": ""      ""Video ID: UF708b-mB1w""
  },
  {
    "{": ""      ""Video ID: JX6C4lJldDA""
  },
  {
    "{": ""      ""Video ID: 0gYMOuWdgdk""
  },
  {
    "{": ""      ""Video ID: _on5lmyb3CM""
  },
  {
    "{": ""      ""Video ID: g5UI8HoTZAw""
  },
  {
    "{": ""      ""Video ID: nk4Ak4nB9LA""
  },
  {
    "{": ""      ""Video ID: N7RhM0AYGCw""
  },
  {
    "{": ""      ""Video ID: gWIpzfZ4VUA""
  },
  {
    "{": ""      ""Video ID: -2tteRr41Mc""
  },
  {
    "{": ""      ""Video ID: kt-MEu-X3LI""
  },
  {
    "{": ""      ""Video ID: mrNku9hhqVo""
  },
  {
    "{": ""      ""Video ID: 0jBahOKOPdI""
  },
  {
    "{": ""      ""Video ID: t9yhJUrXTf8""
  },
  {
    "{": ""      ""Video ID: c8srVtO5WIA""
  },
  {
    "{": ""      ""Video ID: xDja_ym8sSE""
  },
  {
    "{": ""      ""Video ID: PlOKoaKpvwY""
  },
  {
    "{": ""      ""Video ID: cSmnOvNY1wU""
  },
  {
    "{": ""      ""Video ID: DOMgXOczUyw""
  },
  {
    "{": ""      ""Video ID: i0fp7u_eYZY""
  },
  {
    "{": ""      ""Video ID: 2UxDWFfixY8""
  },
  {
    "{": ""      ""Video ID: hWj84iiztU8""
  },
  {
    "{": ""      ""Video ID: EekkRqbqndk""
  },
  {
    "{": ""      ""Video ID: vqOM1SOZfWA""
  },
  {
    "{": ""      ""Video ID: 9yR4r4vo4Kk""
  },
  {
    "{": ""      ""Video ID: 2D-CpPwPOys""
  },
  {
    "{": ""      ""Video ID: WWKL8rDS1sY""
  },
  {
    "{": ""      ""Video ID: 0zrJ9TEwF7w""
  },
  {
    "{": ""      ""Video ID: sbT4V3XmoGE""
  },
  {
    "{": ""      ""Video ID: oSIy0MQWLbc""
  },
  {
    "{": ""      ""Video ID: dSxwptoG-yo""
  },
  {
    "{": ""      ""Video ID: WPxOmh9b8bk""
  },
  {
    "{": ""      ""Video ID: Mk-SZ_pgfvY""
  },
  {
    "{": ""      ""Video ID: xKmys-Tys90""
  },
  {
    "{": ""      ""Video ID: N8BIrtBhOd8""
  },
  {
    "{": ""      ""Video ID: qQsvP_yGMvQ""
  },
  {
    "{": ""      ""Video ID: nSsM2bIP7Z0""
  },
  {
    "{": ""      ""Video ID: pshZcEvsPfw""
  },
  {
    "{": ""      ""Video ID: JXoOPn70C78""
  },
  {
    "{": ""      ""Video ID: A8bvmd_RwLw""
  },
  {
    "{": ""      ""Video ID: PAb9uxY2QOQ""
  },
  {
    "{": ""      ""Video ID: 8v04_3ekjDs""
  },
  {
    "{": ""      ""Video ID: xqOohxZcdPI""
  },
  {
    "{": ""      ""Video ID: nJOB_23aYiA""
  },
  {
    "{": ""      ""Video ID: m4-sk4_zsKs""
  },
  {
    "{": ""      ""Video ID: I1LJ8YbXMcc""
  },
  {
    "{": ""      ""Video ID: FViWtJtE4JE""
  },
  {
    "{": ""      ""Video ID: rGZcVw_EsaQ""
  },
  {
    "{": ""      ""Video ID: jx3qRtzvkoI""
  },
  {
    "{": ""      ""Video ID: vuY7l8K045k""
  },
  {
    "{": ""      ""Video ID: W0jENak3KRw""
  },
  {
    "{": ""      ""Video ID: KAGh7WbHpYY""
  },
  {
    "{": ""      ""Video ID: KT6exhtCRK0""
  },
  {
    "{": ""      ""Video ID: kSm1Wwly_tE""
  },
  {
    "{": ""      ""Video ID: 8OvDB9yXmTk""
  },
  {
    "{": ""      ""Video ID: NG-AtfnsPWs""
  },
  {
    "{": ""      ""Video ID: uZUjjZ042gw""
  },
  {
    "{": ""      ""Video ID: twtfLXEBub0""
  },
  {
    "{": ""      ""Video ID: SsGpWmms6b8""
  },
  {
    "{": ""      ""Video ID: xJ7NOh4anpQ""
  },
  {
    "{": ""      ""Video ID: jrVkq5ihCY4""
  },
  {
    "{": ""      ""Video ID: TP9Wbj5Jeac""
  },
  {
    "{": ""      ""Video ID: kl72E15MHgg""
  },
  {
    "{": ""      ""Video ID: cfHga3juzZM""
  },
  {
    "{": ""      ""Video ID: iyRPwkq35j8""
  },
  {
    "{": ""      ""Video ID: IKU0TWPF1Ig""
  },
  {
    "{": ""      ""Video ID: ghIsGwuu0_I""
  },
  {
    "{": ""      ""Video ID: vlLgpxGeWhs""
  },
  {
    "{": ""      ""Video ID: ys1BDej3KUQ""
  },
  {
    "{": ""      ""Video ID: djzZ7KOXY-Y""
  },
  {
    "{": ""      ""Video ID: tY9H8_nEPBA""
  },
  {
    "{": ""      ""Video ID: 6tpbp9GXOGU""
  },
  {
    "{": ""      ""Video ID: R-ItfWY3xMQ""
  },
  {
    "{": ""      ""Video ID: cnRgM6CBjSY""
  },
  {
    "{": ""      ""Video ID: Uw8U6QG-04w""
  },
  {
    "{": ""      ""Video ID: -KBzDAOH40E""
  },
  {
    "{": ""      ""Video ID: bNex_dVOI_4""
  },
  {
    "{": ""      ""Video ID: pQsKUJmBGEA""
  },
  {
    "{": ""      ""Video ID: OPEPoJR7-ng""
  },
  {
    "{": ""      ""Video ID: K4KRGpeIBqw""
  },
  {
    "{": ""      ""Video ID: uzhAO3yygOQ""
  },
  {
    "{": ""      ""Video ID: _gN3Fc4hydw""
  },
  {
    "{": ""      ""Video ID: QmqpGZv0YT4""
  },
  {
    "{": ""      ""Video ID: yGFEvC18BV8""
  },
  {
    "{": ""      ""Video ID: giHjccE2wjw""
  },
  {
    "{": ""      ""Video ID: HzdrctEk2ww""
  },
  {
    "{": ""      ""Video ID: AEtuHrUF65c""
  },
  {
    "{": ""      ""Video ID: d-2mk0gjQ8Q""
  },
  {
    "{": ""      ""Video ID: LomtiLtUlBk""
  },
  {
    "{": ""      ""Video ID: H5BFx7dkSGc""
  },
  {
    "{": ""      ""Video ID: tnT7XBmpGfQ""
  },
  {
    "{": ""      ""Video ID: XKpfuLOzomk""
  },
  {
    "{": ""      ""Video ID: G3a8tUYeNN8""
  },
  {
    "{": ""      ""Video ID: BgTtzZIn2Lg""
  },
  {
    "{": ""      ""Video ID: vMap-g17GtI""
  },
  {
    "{": ""      ""Video ID: GjlQVXvip90""
  },
  {
    "{": ""      ""Video ID: CgTegWE2g-E""
  },
  {
    "{": ""      ""Video ID: 9yykrjeiPNw""
  },
  {
    "{": ""      ""Video ID: JQZYu_u8vXU""
  },
  {
    "{": ""      ""Video ID: Mi4pHEj_EKc""
  },
  {
    "{": ""      ""Video ID: Id4XpPybvHo""
  },
  {
    "{": ""      ""Video ID: R1C9wV8zyjo""
  },
  {
    "{": ""      ""Video ID: _K0b8vkhdV0""
  },
  {
    "{": ""      ""Video ID: kp6_oFSh_ss""
  },
  {
    "{": ""      ""Video ID: zDHJ4ztnldQ""
  },
  {
    "{": ""      ""Video ID: BOjeZnjKlp0""
  },
  {
    "{": ""      ""Video ID: i0rcAByKUFM""
  },
  {
    "{": ""      ""Video ID: NpFu_bYkomc""
  },
  {
    "{": ""      ""Video ID: VePqzIrR-ao""
  },
  {
    "{": ""      ""Video ID: P823ubOJB2g""
  },
  {
    "{": ""      ""Video ID: 1NSSTaOxrm8""
  },
  {
    "{": ""      ""Video ID: IXvRWsFaMCU""
  },
  {
    "{": ""      ""Video ID: DcfTTWRQSLs""
  },
  {
    "{": ""      ""Video ID: 1bUZD1vnC8A""
  },
  {
    "{": ""      ""Video ID: BFDidaqofNw""
  },
  {
    "{": ""      ""Video ID: mS1FvYwvNF8""
  },
  {
    "{": ""      ""Video ID: QMYDmN-82kw""
  },
  {
    "{": ""      ""Video ID: J7BHfmXUSO8""
  },
  {
    "{": ""      ""Video ID: IHMVb6UWf2k""
  },
  {
    "{": ""      ""Video ID: ED7SZDgL_lQ""
  },
  {
    "{": ""      ""Video ID: dD5A6Kr8caA""
  },
  {
    "{": ""      ""Video ID: X1cscWI-6kg""
  },
  {
    "{": ""      ""Video ID: pOFjEhYimJ8""
  },
  {
    "{": ""      ""Video ID: M67qV3P5ALA""
  },
  {
    "{": ""      ""Video ID: EO46OSIMifw""
  },
  {
    "{": ""      ""Video ID: La2_jWj3L1U""
  },
  {
    "{": ""      ""Video ID: bHBknpdWxr4""
  },
  {
    "{": ""      ""Video ID: -z31SMXShxE""
  },
  {
    "{": ""      ""Video ID: A_cSz_t6Apg""
  },
  {
    "{": ""      ""Video ID: O4-jxSKbC2U""
  },
  {
    "{": ""      ""Video ID: 1cxjx-r8RdI""
  },
  {
    "{": ""      ""Video ID: UQHViJ94CG4""
  },
  {
    "{": ""      ""Video ID: tNn6qOrXkYM""
  },
  {
    "{": ""      ""Video ID: drZPCAsPWl4""
  },
  {
    "{": ""      ""Video ID: 1-QVQLbwtHA""
  },
  {
    "{": ""      ""Video ID: Lpvvmdw6feE""
  },
  {
    "{": ""      ""Video ID: tXyzXEUtgV0""
  },
  {
    "{": ""      ""Video ID: vhHfFa9HYHg""
  },
  {
    "{": ""      ""Video ID: qSzhXMe9i8Y""
  },
  {
    "{": ""      ""Video ID: 8xwq3eAxE1A""
  },
  {
    "{": ""      ""Video ID: g9tFgJALaZk""
  },
  {
    "{": ""      ""Video ID: xoWrtZX6J4c""
  },
  {
    "{": ""      ""Video ID: k-te5zIqtkQ""
  },
  {
    "{": ""      ""Video ID: rzBsbARfUJk""
  },
  {
    "{": ""      ""Video ID: r1ejSwEBq5Y""
  },
  {
    "{": ""      ""Video ID: 508MHvMGWEg""
  },
  {
    "{": ""      ""Video ID: z3iI9cZyyAs""
  },
  {
    "{": ""      ""Video ID: rf81FcGpipQ""
  },
  {
    "{": ""      ""Video ID: 2SxTjODxFCE""
  },
  {
    "{": ""      ""Video ID: fEhRyqTqRlU""
  },
  {
    "{": ""      ""Video ID: gWIwe4Bu86A""
  },
  {
    "{": ""      ""Video ID: rhSEVdI22BI""
  },
  {
    "{": ""      ""Video ID: uYjIZyRErSA""
  },
  {
    "{": ""      ""Video ID: StusGODhyj4""
  },
  {
    "{": ""      ""Video ID: u54YUYcJapI""
  },
  {
    "{": ""      ""Video ID: eqIuV1de6TQ""
  },
  {
    "{": ""      ""Video ID: NFB4xl-ZmRc""
  },
  {
    "{": ""      ""Video ID: XW0rPrtwcz8""
  },
  {
    "{": ""      ""Video ID: 8_fBiR6Sq88""
  },
  {
    "{": ""      ""Video ID: 785dNEVJGq4""
  },
  {
    "{": ""      ""Video ID: DdGyPZ0v7Ng""
  },
  {
    "{": ""      ""Video ID: rM1MY1IoJBk""
  },
  {
    "{": ""      ""Video ID: V8LmYqzFVJc""
  },
  {
    "{": ""      ""Video ID: DBNnNfZi7QY""
  },
  {
    "{": ""      ""Video ID: 1b-PIS4T98Q""
  },
  {
    "{": ""      ""Video ID: V1Ma7yeZWbY""
  },
  {
    "{": ""      ""Video ID: udQbMhIcXUE""
  },
  {
    "{": ""      ""Video ID: vXnYXs8Hfxo""
  },
  {
    "{": ""      ""Video ID: aYPIi-AuRwg""
  },
  {
    "{": ""      ""Video ID: RPcOUuWhLgc""
  },
  {
    "{": ""      ""Video ID: t7frJFvSfbk""
  },
  {
    "{": ""      ""Video ID: JfAmeKLw2qc""
  },
  {
    "{": ""      ""Video ID: dFajPCFRpHg""
  },
  {
    "{": ""      ""Video ID: _ACyHOVcFOE""
  },
  {
    "{": ""      ""Video ID: UI5PpRtfg_o""
  },
  {
    "{": ""      ""Video ID: cndwqRU8OFE""
  },
  {
    "{": ""      ""Video ID: P2vCvvzIQWg""
  },
  {
    "{": ""      ""Video ID: hbU8Vz_2Uzg""
  },
  {
    "{": ""      ""Video ID: dsUI6FsDIgg""
  },
  {
    "{": ""      ""Video ID: NnG3RM9iOwA""
  },
  {
    "{": ""      ""Video ID: Z4Y4keqTV6w""
  },
  {
    "{": ""      ""Video ID: ooct6mso85c""
  },
  {
    "{": ""      ""Video ID: nke3n6e-F3Q""
  },
  {
    "{": ""      ""Video ID: KjNOZSgKXDY""
  },
  {
    "{": ""      ""Video ID: d4RlVMlM-jk""
  },
  {
    "{": ""      ""Video ID: GB0kgaQAwos""
  },
  {
    "{": ""      ""Video ID: EXcPCAl36hg""
  },
  {
    "{": ""      ""Video ID: 6JDtOjF8pzw""
  },
  {
    "{": ""      ""Video ID: CnQan0XRcmg""
  },
  {
    "{": ""      ""Video ID: WNDh_tFIHn4""
  },
  {
    "{": ""      ""Video ID: RcuVy20z_xc""
  },
  {
    "{": ""      ""Video ID: ZLiJuI5995g""
  },
  {
    "{": ""      ""Video ID: 2bi-rSYbzfU""
  },
  {
    "{": ""      ""Video ID: IPctqzfQQmU""
  },
  {
    "{": ""      ""Video ID: 86Pw4qFUjE4""
  },
  {
    "{": ""      ""Video ID: DUlDOAujcz4""
  },
  {
    "{": ""      ""Video ID: Mm6Ju0xhUW8""
  },
  {
    "{": ""      ""Video ID: nM2VDkXPt0I""
  },
  {
    "{": ""      ""Video ID: dSBnFdGyE5w""
  },
  {
    "{": ""      ""Video ID: HEQDX1pbOSM""
  },
  {
    "{": ""      ""Video ID: NZXW2IIziMM""
  },
  {
    "{": ""      ""Video ID: IEdZpoWTBBw""
  },
  {
    "{": ""      ""Video ID: Kwhp0Yf6-k0""
  },
  {
    "{": ""      ""Video ID: krku9vqV7EU""
  },
  {
    "{": ""      ""Video ID: 6DofAbPYYo4""
  },
  {
    "{": ""      ""Video ID: NH3YpFkM_tg""
  },
  {
    "{": ""      ""Video ID: DVOsvRBl1uk""
  },
  {
    "{": ""      ""Video ID: lvh5hxJNztE""
  },
  {
    "{": ""      ""Video ID: Vz4_tfuEP6A""
  },
  {
    "{": ""      ""Video ID: wTwxvrSTrvY""
  },
  {
    "{": ""      ""Video ID: IQcyLMa716k""
  },
  {
    "{": ""      ""Video ID: rJc1G3NRkLM""
  },
  {
    "{": ""      ""Video ID: G2PkNSdIRsY""
  },
  {
    "{": ""      ""Video ID: 0Rh5OqP-FAI""
  },
  {
    "{": ""      ""Video ID: BfX-s4dcYBg""
  },
  {
    "{": ""      ""Video ID: bW-0Ww5f_aY""
  },
  {
    "{": ""      ""Video ID: v0haHrLCk4Y""
  },
  {
    "{": ""      ""Video ID: XDt203St2Xo""
  },
  {
    "{": ""      ""Video ID: LtTKxCFZ3b8""
  },
  {
    "{": ""      ""Video ID: r-nT_y1JCA8""
  },
  {
    "{": ""      ""Video ID: 7_or1LMwCTA""
  },
  {
    "{": ""      ""Video ID: YcLl01CMexU""
  },
  {
    "{": ""      ""Video ID: H1flDk6t-4I""
  },
  {
    "{": ""      ""Video ID: a-B05a0UlEU""
  },
  {
    "{": ""      ""Video ID: VyA79_qsBlI""
  },
  {
    "{": ""      ""Video ID: myB_8UPTGBQ""
  },
  {
    "{": ""      ""Video ID: TKO7FWwHHMk""
  },
  {
    "{": ""      ""Video ID: Qm_4z3fdO-Q""
  },
  {
    "{": ""      ""Video ID: UFNS5KZP4fE""
  },
  {
    "{": ""      ""Video ID: sAMf1K1MOnU""
  },
  {
    "{": ""      ""Video ID: QPrackODaQE""
  },
  {
    "{": ""      ""Video ID: qQgb2LyDZc4""
  },
  {
    "{": ""      ""Video ID: FFsslbopNIc""
  },
  {
    "{": ""      ""Video ID: zLFHMoTBl2g""
  },
  {
    "{": ""      ""Video ID: kXPeSmViMwM""
  },
  {
    "{": ""      ""Video ID: xCn1SRMZqaE""
  },
  {
    "{": ""      ""Video ID: VIZhaSZQOfI""
  },
  {
    "{": ""      ""Video ID: hLdqNTdhQg8""
  },
  {
    "{": ""      ""Video ID: eyXUl9AoagI""
  },
  {
    "{": ""      ""Video ID: X76l4VKMKqs""
  },
  {
    "{": ""      ""Video ID: K5WJQIE1_Ag""
  },
  {
    "{": ""      ""Video ID: tiWXWyiXmGE""
  },
  {
    "{": ""      ""Video ID: Of_tDZ3F2N8""
  },
  {
    "{": ""      ""Video ID: jBZVoWWtjcA""
  },
  {
    "{": ""      ""Video ID: V_YSmvJ6hso""
  },
  {
    "{": ""      ""Video ID: FE2NatsC5g4""
  },
  {
    "{": ""      ""Video ID: L1Lht5K3Uxc""
  },
  {
    "{": ""      ""Video ID: l-nVHhJl6SQ""
  },
  {
    "{": ""      ""Video ID: pEMlKP8uvuo""
  },
  {
    "{": ""      ""Video ID: cA6krJ0b0dE""
  },
  {
    "{": ""      ""Video ID: 1PXFw1W4rpY""
  },
  {
    "{": ""      ""Video ID: kD4h2qaC-mY""
  },
  {
    "{": ""      ""Video ID: UEgk7tBhkWQ""
  },
  {
    "{": ""      ""Video ID: ZXH1Uzggyp8""
  },
  {
    "{": ""      ""Video ID: 6bUHbkGexsg""
  },
  {
    "{": ""      ""Video ID: OoEBK3Ulzhg""
  },
  {
    "{": ""      ""Video ID: tb0j4nvWexo""
  },
  {
    "{": ""      ""Video ID: KbZjQfntil8""
  },
  {
    "{": ""      ""Video ID: OvXs-rduFZg""
  },
  {
    "{": ""      ""Video ID: zN2QKbOplzM""
  },
  {
    "{": ""      ""Video ID: oxu4qDad8yY""
  },
  {
    "{": ""      ""Video ID: 2sgJcdM-iww""
  },
  {
    "{": ""      ""Video ID: gwtE2HAKyoo""
  },
  {
    "{": ""      ""Video ID: hw9qsZNMBjk""
  },
  {
    "{": ""      ""Video ID: j54paYwGaPw""
  },
  {
    "{": ""      ""Video ID: di5QypLDaos""
  },
  {
    "{": ""      ""Video ID: R1BVHows8wk""
  },
  {
    "{": ""      ""Video ID: yg4_mGpOASg""
  },
  {
    "{": ""      ""Video ID: _h577kEo9OQ""
  },
  {
    "{": ""      ""Video ID: 0Rm2KJdWIvQ""
  },
  {
    "{": ""      ""Video ID: 2mcgJOBOF-E""
  },
  {
    "{": ""      ""Video ID: Rlo5fqXD_5M""
  },
  {
    "{": ""      ""Video ID: Fb6Fpxzk9Js""
  },
  {
    "{": ""      ""Video ID: DBtyPROjUzM""
  },
  {
    "{": ""      ""Video ID: hMv2WFb0WdE""
  },
  {
    "{": ""      ""Video ID: bRusHxeDNH8""
  },
  {
    "{": ""      ""Video ID: 50wSK36DNEw""
  },
  {
    "{": ""      ""Video ID: UeZVjbTElKo""
  },
  {
    "{": ""      ""Video ID: REVg6dMkpFQ""
  },
  {
    "{": ""      ""Video ID: Uw91-pcxpZs""
  },
  {
    "{": ""      ""Video ID: QWd8J8C3Gaw""
  },
  {
    "{": ""      ""Video ID: X2SlwxYm6Cs""
  },
  {
    "{": ""      ""Video ID: a5qsbfFB2jQ""
  },
  {
    "{": ""      ""Video ID: lAFGwIlszFw""
  },
  {
    "{": ""      ""Video ID: O5jE8nupCmM""
  },
  {
    "{": ""      ""Video ID: 4qqOnxTK-qk""
  },
  {
    "{": ""      ""Video ID: R1Ej8D_-I3g""
  },
  {
    "{": ""      ""Video ID: 0TNlgv2t2Y4""
  },
  {
    "{": ""      ""Video ID: FyOl-RJWUvI""
  },
  {
    "{": ""      ""Video ID: FF7oq7R5E90""
  },
  {
    "{": ""      ""Video ID: IWivdqTu2uA""
  },
  {
    "{": ""      ""Video ID: huhFpcorwSY""
  },
  {
    "{": ""      ""Video ID: V6MmHF0C5Gc""
  },
  {
    "{": ""      ""Video ID: SkDDo9coEUQ""
  },
  {
    "{": ""      ""Video ID: 1LfMbycFQWQ""
  },
  {
    "{": ""      ""Video ID: hmde9ar9Gc8""
  },
  {
    "{": ""      ""Video ID: SlvEEk3zOuk""
  },
  {
    "{": ""      ""Video ID: OnwoAocp55s""
  },
  {
    "{": ""      ""Video ID: VLTxO7SAkwc""
  },
  {
    "{": ""      ""Video ID: YE4PNlfrh8g""
  },
  {
    "{": ""      ""Video ID: Qddt-_zu4D0""
  },
  {
    "{": ""      ""Video ID: _u9kieqGppE""
  },
  {
    "{": ""      ""Video ID: 1lKZqqSI9-s""
  },
  {
    "{": ""      ""Video ID: MT1hRqbhM2I""
  },
  {
    "{": ""      ""Video ID: CcHyVxiFJrQ""
  },
  {
    "{": ""      ""Video ID: mmoDqPyofok""
  },
  {
    "{": ""      ""Video ID: H72MF-0mHe4""
  },
  {
    "{": ""      ""Video ID: xqKJ_BKt-R4""
  },
  {
    "{": ""      ""Video ID: GuiQ7rZXXNw""
  },
  {
    "{": ""      ""Video ID: lAU-tHjUeaw""
  },
  {
    "{": ""      ""Video ID: awKmkufA0j8""
  },
  {
    "{": ""      ""Video ID: yagAAN0k_G8""
  },
  {
    "{": ""      ""Video ID: mH94XQN-E8A""
  },
  {
    "{": ""      ""Video ID: GtfD8h9aDCY""
  },
  {
    "{": ""      ""Video ID: AAh6WwKILfk""
  },
  {
    "{": ""      ""Video ID: -yWpnto-hqQ""
  },
  {
    "{": ""      ""Video ID: HnPU7Ca-KJ4""
  },
  {
    "{": ""      ""Video ID: 3Gy16NbdnoE""
  },
  {
    "{": ""      ""Video ID: jhgDlwkk8iw""
  },
  {
    "{": ""      ""Video ID: 42vMF4HOEYk""
  },
  {
    "{": ""      ""Video ID: YpC1JNC6_kQ""
  },
  {
    "{": ""      ""Video ID: jyZ2FmpLFE4""
  },
  {
    "{": ""      ""Video ID: 6oKMIR2brtQ""
  },
  {
    "{": ""      ""Video ID: I5OUQ43Kv7I""
  },
  {
    "{": ""      ""Video ID: vg_ZkoUteLM""
  },
  {
    "{": ""      ""Video ID: Rnn5pDPoGF4""
  },
  {
    "{": ""      ""Video ID: 9qAOExz27h8""
  },
  {
    "{": ""      ""Video ID: 04V3kAqi57Q""
  },
  {
    "{": ""      ""Video ID: gKjSxK-kwnI""
  },
  {
    "{": ""      ""Video ID: 8j-GUFA9TyE""
  },
  {
    "{": ""      ""Video ID: yFooyyy_0gI""
  },
  {
    "{": ""      ""Video ID: YTPuTxalalo""
  },
  {
    "{": ""      ""Video ID: qPBanOKrXDk""
  },
  {
    "{": ""      ""Video ID: xgdaMONudoM""
  },
  {
    "{": ""      ""Video ID: 4OjmOJApmqA""
  },
  {
    "{": ""      ""Video ID: Kom-DrrdhnA""
  },
  {
    "{": ""      ""Video ID: 1QOGB1LqnUc""
  },
  {
    "{": ""      ""Video ID: S3a5U5BZOoQ""
  },
  {
    "{": ""      ""Video ID: MfF7ZvBy9_k""
  },
  {
    "{": ""      ""Video ID: VsymM0KyGaI""
  },
  {
    "{": ""      ""Video ID: _RILVjMf_NQ""
  },
  {
    "{": ""      ""Video ID: n7HjYM-5Exk""
  },
  {
    "{": ""      ""Video ID: PzpQ3K0vtzk""
  },
  {
    "{": ""      ""Video ID: H3cc-Ee4MLA""
  },
  {
    "{": ""      ""Video ID: oTUeGmEyq6A""
  },
  {
    "{": ""      ""Video ID: 2onjyIUtGy0""
  },
  {
    "{": ""      ""Video ID: 3Y45KJRm6cI""
  },
  {
    "{": ""      ""Video ID: M85NmgH6S4A""
  },
  {
    "{": ""      ""Video ID: jAZVZKXjnNI""
  },
  {
    "{": ""      ""Video ID: esnE36TWYOI""
  },
  {
    "{": ""      ""Video ID: nAtAzSnl-0g""
  },
  {
    "{": ""      ""Video ID: 268QNU_G6r4""
  },
  {
    "{": ""      ""Video ID: fkDEMrqYM0g""
  },
  {
    "{": ""      ""Video ID: 19KoKVkTNF0""
  },
  {
    "{": ""      ""Video ID: KREWTHVco9c""
  },
  {
    "{": ""      ""Video ID: yGNvERtCkiM""
  },
  {
    "{": ""      ""Video ID: qeaPdxZy-J0""
  },
  {
    "{": ""      ""Video ID: 4M5PNOTcyc8""
  },
  {
    "{": ""      ""Video ID: sY51zsMVVH4""
  },
  {
    "{": ""      ""Video ID: bTM7AwljLY4""
  },
  {
    "{": ""      ""Video ID: 6RwPNnJ_J4w""
  },
  {
    "{": ""      ""Video ID: yzR4ZgXelVA""
  },
  {
    "{": ""      ""Video ID: PxLgkHPR-KU""
  },
  {
    "{": ""      ""Video ID: rNKefRRvV7g""
  },
  {
    "{": ""      ""Video ID: TZLJaQTxVMA""
  },
  {
    "{": ""      ""Video ID: S-EioW31IKw""
  },
  {
    "{": ""      ""Video ID: ZecQ1Z0xpS8""
  },
  {
    "{": ""      ""Video ID: _DZmy931fQU""
  },
  {
    "{": ""      ""Video ID: qf-WpFdyHZM""
  },
  {
    "{": ""      ""Video ID: MJHc6cCngpg""
  },
  {
    "{": ""      ""Video ID: DucL1s6qEjY""
  },
  {
    "{": ""      ""Video ID: AlkFaOVy3bU""
  },
  {
    "{": ""      ""Video ID: zyKRh7AhUUk""
  },
  {
    "{": ""      ""Video ID: FgO1LQ4iKFs""
  },
  {
    "{": ""      ""Video ID: 85eAECq6vTQ""
  },
  {
    "{": ""      ""Video ID: 3cRJZK6SFA4""
  },
  {
    "{": ""      ""Video ID: v7SxePi8U6o""
  },
  {
    "{": ""      ""Video ID: Zdl5jrM4nZc""
  },
  {
    "{": ""      ""Video ID: pRQ-bOwMgco""
  },
  {
    "{": ""      ""Video ID: OymxUZevLZM""
  },
  {
    "{": ""      ""Video ID: tKIxuFbaF1Y""
  },
  {
    "{": ""      ""Video ID: dMHty_8Ih2w""
  },
  {
    "{": ""      ""Video ID: m9CEQbbaeMk""
  },
  {
    "{": ""      ""Video ID: WrBr2XLYMg8""
  },
  {
    "{": ""      ""Video ID: OSVfgXvBAqU""
  },
  {
    "{": ""      ""Video ID: IQDzmg1dyEE""
  },
  {
    "{": ""      ""Video ID: 1KsAFi5POP8""
  },
  {
    "{": ""      ""Video ID: JsXVUlMqQs4""
  },
  {
    "{": ""      ""Video ID: 3UvhW33ztak""
  },
  {
    "{": ""      ""Video ID: 8b2o2FY4-70""
  },
  {
    "{": ""      ""Video ID: AuwlqeNRElI""
  },
  {
    "{": ""      ""Video ID: 1N8N4Bg92qw""
  },
  {
    "{": ""      ""Video ID: PVqg4G6RbqU""
  },
  {
    "{": ""      ""Video ID: 5aFNaXNjVaY""
  },
  {
    "{": ""      ""Video ID: kP2K4Lhas2o""
  },
  {
    "{": ""      ""Video ID: kX8b1YUGiA8""
  },
  {
    "{": ""      ""Video ID: vV7N6UwXEkw""
  },
  {
    "{": ""      ""Video ID: d5rbZcT_QBk""
  },
  {
    "{": ""      ""Video ID: gj0MooPmGNg""
  },
  {
    "{": ""      ""Video ID: 59Qr_-hxZU8""
  },
  {
    "{": ""      ""Video ID: euTuqcERnRY""
  },
  {
    "{": ""      ""Video ID: BOLgxfypO6I""
  },
  {
    "{": ""      ""Video ID: Amvm5H292u4""
  },
  {
    "{": ""      ""Video ID: 20tgmcvcTo4""
  },
  {
    "{": ""      ""Video ID: mlnFwbzEPRI""
  },
  {
    "{": ""      ""Video ID: ONTCCNIzhMc""
  },
  {
    "{": ""      ""Video ID: 4x279GNMwvY""
  },
  {
    "{": ""      ""Video ID: mISQFviAVAQ""
  },
  {
    "{": ""      ""Video ID: HHOyap0wg7Y""
  },
  {
    "{": ""      ""Video ID: YKfuiFb2V3w""
  },
  {
    "{": ""      ""Video ID: uY28l6HoKww""
  },
  {
    "{": ""      ""Video ID: hkO0CemWdAQ""
  },
  {
    "{": ""      ""Video ID: iAq5nTcQtV0""
  },
  {
    "{": ""      ""Video ID: krExAGCbrMY""
  },
  {
    "{": ""      ""Video ID: e3wShd_bX8A""
  },
  {
    "{": ""      ""Video ID: UArPCrwW0ho""
  },
  {
    "{": ""      ""Video ID: wIivoqLbeeg""
  },
  {
    "{": ""      ""Video ID: FxLsjtRhVZk""
  },
  {
    "{": ""      ""Video ID: -CazKanlYDg""
  },
  {
    "{": ""      ""Video ID: UaSPQnHUnLQ""
  },
  {
    "{": ""      ""Video ID: 1dpSjjqpHsA""
  },
  {
    "{": ""      ""Video ID: 91csSHVUVhg""
  },
  {
    "{": ""      ""Video ID: imf876WWYpM""
  },
  {
    "{": ""      ""Video ID: FLwyox3DpAo""
  },
  {
    "{": ""      ""Video ID: C7F50Cd8LME""
  },
  {
    "{": ""      ""Video ID: 9uhBLETvWX8""
  },
  {
    "{": ""      ""Video ID: 1kirNhQsXfc""
  },
  {
    "{": ""      ""Video ID: R1m4up5YvzM""
  },
  {
    "{": ""      ""Video ID: EazOe4n8peM""
  },
  {
    "{": ""      ""Video ID: FqPUXjFYh38""
  },
  {
    "{": ""      ""Video ID: Y2yHNIzbBXI""
  },
  {
    "{": ""      ""Video ID: CkoDy-urSF8""
  },
  {
    "{": ""      ""Video ID: pb1pMLESmAY""
  },
  {
    "{": ""      ""Video ID: VbvAZB7nbrM""
  },
  {
    "{": ""      ""Video ID: xFZROa0rlMU""
  },
  {
    "{": ""      ""Video ID: g_VY09HchQ0""
  },
  {
    "{": ""      ""Video ID: FbZVbM6UUQI""
  },
  {
    "{": ""      ""Video ID: s8wNt-CWoOo""
  },
  {
    "{": ""      ""Video ID: XyHk73pgYvo""
  },
  {
    "{": ""      ""Video ID: 2EbUbIiC2lo""
  },
  {
    "{": ""      ""Video ID: jYHH20GAsQw""
  },
  {
    "{": ""      ""Video ID: HiBXttk8MLg""
  },
  {
    "{": ""      ""Video ID: gwFVoTkgXEc""
  },
  {
    "{": ""      ""Video ID: nzpPAzuMElE""
  },
  {
    "{": ""      ""Video ID: m9BXosPgNuY""
  },
  {
    "{": ""      ""Video ID: 3kCfUxKoDGQ""
  },
  {
    "{": ""      ""Video ID: Xw3OgWEKLUA""
  },
  {
    "{": ""      ""Video ID: 5jiFM8wbqtY""
  },
  {
    "{": ""      ""Video ID: PbjmWKH8ubY""
  },
  {
    "{": ""      ""Video ID: IX317unlpzs""
  },
  {
    "{": ""      ""Video ID: vOIYHyRn1Mk""
  },
  {
    "{": ""      ""Video ID: SKtzAoM9jzc""
  },
  {
    "{": ""      ""Video ID: SKmbmI7HAdA""
  },
  {
    "{": ""      ""Video ID: gn1-GULjWSA""
  },
  {
    "{": ""      ""Video ID: 5fVSh-p7FeM""
  },
  {
    "{": ""      ""Video ID: thRI4VcvmS0""
  },
  {
    "{": ""      ""Video ID: NtPaifksCdk""
  },
  {
    "{": ""      ""Video ID: L65nTKHq0v4""
  },
  {
    "{": ""      ""Video ID: KitX1jS-tdg""
  },
  {
    "{": ""      ""Video ID: UCr1wfpZD9E""
  },
  {
    "{": ""      ""Video ID: nGU-riWaKLg""
  },
  {
    "{": ""      ""Video ID: 0nP2Kg_xdKE""
  },
  {
    "{": ""      ""Video ID: tsuNS9areMc""
  },
  {
    "{": ""      ""Video ID: 8oRwZQLdhEw""
  },
  {
    "{": ""      ""Video ID: dyTWhZe4nCI""
  },
  {
    "{": ""      ""Video ID: dZia9WmFXmk""
  },
  {
    "{": ""      ""Video ID: 4EIQqMR4z8A""
  },
  {
    "{": ""      ""Video ID: YzMFK_51NQc""
  },
  {
    "{": ""      ""Video ID: u2i1bk7SamQ""
  },
  {
    "{": ""      ""Video ID: UhADUNsIbo4""
  },
  {
    "{": ""      ""Video ID: 2U9tlI6qgI4""
  },
  {
    "{": ""      ""Video ID: CB1RJBuWYbA""
  },
  {
    "{": ""      ""Video ID: E1qbAxqGdIU""
  },
  {
    "{": ""      ""Video ID: Gx5gNpL1hXs""
  },
  {
    "{": ""      ""Video ID: 2jj4OUgtF9g""
  },
  {
    "{": ""      ""Video ID: SCB1uC-xhTs""
  },
  {
    "{": ""      ""Video ID: WU1X8tE9Ql8""
  },
  {
    "{": ""      ""Video ID: VaG8jElpmxU""
  },
  {
    "{": ""      ""Video ID: NROAdD9mOis""
  },
  {
    "{": ""      ""Video ID: 8d-mWSiscp0""
  },
  {
    "{": ""      ""Video ID: c4qwzHB8F0k""
  },
  {
    "{": ""      ""Video ID: vra5pS9DeA4""
  },
  {
    "{": ""      ""Video ID: zWYTuaEPtTI""
  },
  {
    "{": ""      ""Video ID: I_7UrfpKtaE""
  },
  {
    "{": ""      ""Video ID: n4wzcAQSBEU""
  },
  {
    "{": ""      ""Video ID: qhmd8O1HPZY""
  },
  {
    "{": ""      ""Video ID: 08faadshLvg""
  },
  {
    "{": ""      ""Video ID: ZBJB69hRiqE""
  },
  {
    "{": ""      ""Video ID: OICJdlc5Bpk""
  },
  {
    "{": ""      ""Video ID: 20qwkGZ0Z-Y""
  },
  {
    "{": ""      ""Video ID: d65qDBpho40""
  },
  {
    "{": ""      ""Video ID: jWABSO_o8vQ""
  },
  {
    "{": ""      ""Video ID: _9P15YZrnv0""
  },
  {
    "{": ""      ""Video ID: XGLMHHvHVZM""
  },
  {
    "{": ""      ""Video ID: kKy92nlDAsc""
  },
  {
    "{": ""      ""Video ID: RZOu65YIXfA""
  },
  {
    "{": ""      ""Video ID: dP8oqxriWXk""
  },
  {
    "{": ""      ""Video ID: DLUbKzO9S2A""
  },
  {
    "{": ""      ""Video ID: JD19BBNwhRI""
  },
  {
    "{": ""      ""Video ID: QfhxEW4zrgc""
  },
  {
    "{": ""      ""Video ID: kKidDjbF5z0""
  },
  {
    "{": ""      ""Video ID: E_9Xo13FRQg""
  },
  {
    "{": ""      ""Video ID: aqgZohdQzZE""
  },
  {
    "{": ""      ""Video ID: WTRv2edIcY8""
  },
  {
    "{": ""      ""Video ID: 5gv1uCjOWBk""
  },
  {
    "{": ""      ""Video ID: U9PtdI7n1F8""
  },
  {
    "{": ""      ""Video ID: nE6oR9toeTI""
  },
  {
    "{": ""      ""Video ID: 9Zpqvto_ku4""
  },
  {
    "{": ""      ""Video ID: NHxgRKJzCHk""
  },
  {
    "{": ""      ""Video ID: AAb4gRKhASU""
  },
  {
    "{": ""      ""Video ID: T7XpK8lsQRY""
  },
  {
    "{": ""      ""Video ID: sHAi656qwhc""
  },
  {
    "{": ""      ""Video ID: hrRJ3eiE_do""
  },
  {
    "{": ""      ""Video ID: GSUeCHxo-04""
  },
  {
    "{": ""      ""Video ID: 5IUZPyiu9fU""
  },
  {
    "{": ""      ""Video ID: ZRjqVWYeAIk""
  },
  {
    "{": ""      ""Video ID: J6INseiHz1o""
  },
  {
    "{": ""      ""Video ID: mMG7kT5l1EY""
  },
  {
    "{": ""      ""Video ID: VQj8LKFxPlg""
  },
  {
    "{": ""      ""Video ID: VGiLe7OH5gQ""
  },
  {
    "{": ""      ""Video ID: vRm14aCgKV8""
  },
  {
    "{": ""      ""Video ID: 8yqZQREP0Jk""
  },
  {
    "{": ""      ""Video ID: EZ5epvBpiUw""
  },
  {
    "{": ""      ""Video ID: Uc9H6tu7l3s""
  },
  {
    "{": ""      ""Video ID: uCIyJU8MwgQ""
  },
  {
    "{": ""      ""Video ID: PwJ8f1q6Y1A""
  },
  {
    "{": ""      ""Video ID: CvviRfA6ipE""
  },
  {
    "{": ""      ""Video ID: qX_6QzacoEk""
  },
  {
    "{": ""      ""Video ID: OAfEjzFtbnA""
  },
  {
    "{": ""      ""Video ID: BdjLtR3dk6I""
  },
  {
    "{": ""      ""Video ID: xgjeCHhaYH4""
  },
  {
    "{": ""      ""Video ID: 9jLyl04D_ds""
  },
  {
    "{": ""      ""Video ID: WQNDZrD2IHQ""
  },
  {
    "{": ""      ""Video ID: 07A2sky5UQI""
  },
  {
    "{": ""      ""Video ID: UAAEfiKLtZQ""
  },
  {
    "{": ""      ""Video ID: 8Kavky4uk5Q""
  },
  {
    "{": ""      ""Video ID: 1On2redQEOg""
  },
  {
    "{": ""      ""Video ID: J0VW4z2yKQ8""
  },
  {
    "{": ""      ""Video ID: GG4THVq4Fnk""
  },
  {
    "{": ""      ""Video ID: EMcIUcJunV0""
  },
  {
    "{": ""      ""Video ID: ek1_R4rnQLs""
  },
  {
    "{": ""      ""Video ID: sB6FnGsST9k""
  },
  {
    "{": ""      ""Video ID: xdvzvyXOpw0""
  },
  {
    "{": ""      ""Video ID: QPxWU0ol7H0""
  },
  {
    "{": ""      ""Video ID: RKh1j_a4mdI""
  },
  {
    "{": ""      ""Video ID: 0dy3cljMBnw""
  },
  {
    "{": ""      ""Video ID: EVvr7LLHIEA""
  },
  {
    "{": ""      ""Video ID: j027YxLerNY""
  },
  {
    "{": ""      ""Video ID: SNZOLD9CXjQ""
  },
  {
    "{": ""      ""Video ID: _YFnaKiIVuA""
  },
  {
    "{": ""      ""Video ID: BoITemp8koM""
  },
  {
    "{": ""      ""Video ID: eJ0TjbAAPRg""
  },
  {
    "{": ""      ""Video ID: L7WnHtLY_7k""
  },
  {
    "{": ""      ""Video ID: Jft39qmKAcE""
  },
  {
    "{": ""      ""Video ID: 2muZ8KtnIgc""
  },
  {
    "{": ""      ""Video ID: grqigWCpBZA""
  },
  {
    "{": ""      ""Video ID: iE6Rb2VjeUM""
  },
  {
    "{": ""      ""Video ID: 4QgiwZqmVY8""
  },
  {
    "{": ""      ""Video ID: RBQvc8SSQv0""
  },
  {
    "{": ""      ""Video ID: --7WwhZ1G_M""
  },
  {
    "{": ""      ""Video ID: 8uDCq7CL57I""
  },
  {
    "{": ""      ""Video ID: BFOpOhz_-O0""
  },
  {
    "{": ""      ""Video ID: JoyjbzvzXls""
  },
  {
    "{": ""      ""Video ID: paZR1o2e-y0""
  },
  {
    "{": ""      ""Video ID: ClpYOdVwmf0""
  },
  {
    "{": ""      ""Video ID: CH4SEp34Mkk""
  },
  {
    "{": ""      ""Video ID: uvOYomZk0wM""
  },
  {
    "{": ""      ""Video ID: WAFoaWmsM1U""
  },
  {
    "{": ""      ""Video ID: oTWdMm1ZcAQ""
  },
  {
    "{": ""      ""Video ID: d-VmEiMEJEM""
  },
  {
    "{": ""      ""Video ID: KDYoR9ylXhk""
  },
  {
    "{": ""      ""Video ID: DPstUkiOhTY""
  },
  {
    "{": ""      ""Video ID: vwg4k0G1c8w""
  },
  {
    "{": ""      ""Video ID: pJwLn75RQRM""
  },
  {
    "{": ""      ""Video ID: sV_I7cgkqXc""
  },
  {
    "{": ""      ""Video ID: bAhmYzmkvcY""
  },
  {
    "{": ""      ""Video ID: pYOLaf397W8""
  },
  {
    "{": ""      ""Video ID: htEMGcs33kw""
  },
  {
    "{": ""      ""Video ID: m0MLw2gHxZE""
  },
  {
    "{": ""      ""Video ID: tupdG6nZnVg""
  },
  {
    "{": ""      ""Video ID: 4kOYMLI9gc0""
  },
  {
    "{": ""      ""Video ID: y5KHXWx9PSU""
  },
  {
    "{": ""      ""Video ID: VxW_EbDpPYU""
  },
  {
    "{": ""      ""Video ID: LhFXQUwB6bM""
  },
  {
    "{": ""      ""Video ID: q7Z5jymzDN8""
  },
  {
    "{": ""      ""Video ID: mmOQ7rI6n9g""
  },
  {
    "{": ""      ""Video ID: HMnT5Kg20dY""
  },
  {
    "{": ""      ""Video ID: HoEYb9EbHy4""
  },
  {
    "{": ""      ""Video ID: 79ILLEOXNV8""
  },
  {
    "{": ""      ""Video ID: XZ2VkxMx1B0""
  },
  {
    "{": ""      ""Video ID: JP_3WnJ42kw""
  },
  {
    "{": ""      ""Video ID: V6y-fYCDVRc""
  },
  {
    "{": ""      ""Video ID: l3_ZmGZKQhQ""
  },
  {
    "{": ""      ""Video ID: QE-59joicR0""
  },
  {
    "{": ""      ""Video ID: HmOprS8Fsio""
  },
  {
    "{": ""      ""Video ID: iTI_LbB1P_M""
  },
  {
    "{": ""      ""Video ID: ApndrNtsyTc""
  },
  {
    "{": ""      ""Video ID: eEaadMcnRj4""
  },
  {
    "{": ""      ""Video ID: YL7TrL3jZhk""
  },
  {
    "{": ""      ""Video ID: rBib4pqDJzs""
  },
  {
    "{": ""      ""Video ID: d9qjqyoYwJ8""
  },
  {
    "{": ""      ""Video ID: tERgJnH55l0""
  },
  {
    "{": ""      ""Video ID: JrDL53ps21s""
  },
  {
    "{": ""      ""Video ID: D78bUxAj7Us""
  },
  {
    "{": ""      ""Video ID: jVOQpSbPmGw""
  },
  {
    "{": ""      ""Video ID: YAeYz01aGIY""
  },
  {
    "{": ""      ""Video ID: RTn2tjOVObM""
  },
  {
    "{": ""      ""Video ID: Nqm3L05vKv4""
  },
  {
    "{": ""      ""Video ID: 73-x8We1bdA""
  },
  {
    "{": ""      ""Video ID: SRretyZf0qw""
  },
  {
    "{": ""      ""Video ID: 5jRN4QBdYDw""
  },
  {
    "{": ""      ""Video ID: v8szN3ABIDo""
  },
  {
    "{": ""      ""Video ID: gok4HvHVK7s""
  },
  {
    "{": ""      ""Video ID: lL5Z_QQb9go""
  },
  {
    "{": ""      ""Video ID: glckSMdn2zs""
  },
  {
    "{": ""      ""Video ID: bieGPRh0pJE""
  },
  {
    "{": ""      ""Video ID: b-HzIjyFm1s""
  },
  {
    "{": ""      ""Video ID: waxlVWD4TuA""
  },
  {
    "{": ""      ""Video ID: yKMmUaftbnw""
  },
  {
    "{": ""      ""Video ID: _wbmNHmrEnU""
  },
  {
    "{": ""      ""Video ID: 9Md5Xo1CIYI""
  },
  {
    "{": ""      ""Video ID: cZsT9mNd4lY""
  },
  {
    "{": ""      ""Video ID: XlIGvQgJTXw""
  },
  {
    "{": ""      ""Video ID: etgcG5Tqx6I""
  },
  {
    "{": ""      ""Video ID: so6aseBov7c""
  },
  {
    "{": ""      ""Video ID: 19BgRSPRiiE""
  },
  {
    "{": ""      ""Video ID: JIOiN2vKD24""
  },
  {
    "{": ""      ""Video ID: 5zgLCGXxDbY""
  },
  {
    "{": ""      ""Video ID: Hk8cQIAdz-w""
  },
  {
    "{": ""      ""Video ID: UPEm_8gmU7Q""
  },
  {
    "{": ""      ""Video ID: XJfbo9P5R8Q""
  },
  {
    "{": ""      ""Video ID: CKZpylcx010""
  },
  {
    "{": ""      ""Video ID: EeGzxgKi2dA""
  },
  {
    "{": ""      ""Video ID: kUdODFB2ypM""
  },
  {
    "{": ""      ""Video ID: U6Sa96b6qy4""
  },
  {
    "{": ""      ""Video ID: 26Fwya8xTlA""
  },
  {
    "{": ""      ""Video ID: rpXdo9j-hrI""
  },
  {
    "{": ""      ""Video ID: bgeYXexalIU""
  },
  {
    "{": ""      ""Video ID: lZDkhs-p4W0""
  },
  {
    "{": ""      ""Video ID: _DGhj0QIaPg""
  },
  {
    "{": ""      ""Video ID: ocuxHOG82Oc""
  },
  {
    "{": ""      ""Video ID: 9AdfXf22RSQ""
  },
  {
    "{": ""      ""Video ID: ColzIj5Xuu4""
  },
  {
    "{": ""      ""Video ID: Bg86UZZ20Us""
  },
  {
    "{": ""      ""Video ID: 2OEI8vT6VMI""
  },
  {
    "{": ""      ""Video ID: Qh-SB9ja-5A""
  },
  {
    "{": ""      ""Video ID: oBDcTd2j1p8""
  },
  {
    "{": ""      ""Video ID: LsViUCygQ3A""
  },
  {
    "{": ""      ""Video ID: 1jSqU0ktcYk""
  },
  {
    "{": ""      ""Video ID: RLnMMol2qUU""
  },
  {
    "{": ""      ""Video ID: IVuPegpPEsg""
  },
  {
    "{": ""      ""Video ID: CQs2Bh9S2-E""
  },
  {
    "{": ""      ""Video ID: lFMfjqSCV0k""
  },
  {
    "{": ""      ""Video ID: 6MuQVE-54QY""
  },
  {
    "{": ""      ""Video ID: BjnkKuI-YAY""
  },
  {
    "{": ""      ""Video ID: XkV9ryC8Jsc""
  },
  {
    "{": ""      ""Video ID: ya-tuPNIMOk""
  },
  {
    "{": ""      ""Video ID: Bo-2WTIYVnc""
  },
  {
    "{": ""      ""Video ID: f9WVFdlN0Qo""
  },
  {
    "{": ""      ""Video ID: N-u5HSZSxOQ""
  },
  {
    "{": ""      ""Video ID: -QRlasxkEYY""
  },
  {
    "{": ""      ""Video ID: ZbntinKg2Zg""
  },
  {
    "{": ""      ""Video ID: bU-z8ZGobZk""
  },
  {
    "{": ""      ""Video ID: EwOXfYyJqlQ""
  },
  {
    "{": ""      ""Video ID: 9WT8ev14MiQ""
  },
  {
    "{": ""      ""Video ID: I08oDUeK-P8""
  },
  {
    "{": ""      ""Video ID: M359or977mk""
  },
  {
    "{": ""      ""Video ID: Uv-MV1TsqMQ""
  },
  {
    "{": ""      ""Video ID: fbiHrp21zTw""
  },
  {
    "{": ""      ""Video ID: QrFJhTm7xgI""
  },
  {
    "{": ""      ""Video ID: DS5N-weet1E""
  },
  {
    "{": ""      ""Video ID: ESdunrbL-s8""
  },
  {
    "{": ""      ""Video ID: T5IPToL8b3E""
  },
  {
    "{": ""      ""Video ID: MxNgOeBaFUI""
  },
  {
    "{": ""      ""Video ID: YJAv19VUqko""
  },
  {
    "{": ""      ""Video ID: PZiXRNxmeYA""
  },
  {
    "{": ""      ""Video ID: ADqbjC2j-0Y""
  },
  {
    "{": ""      ""Video ID: X-weIQCevFY""
  },
  {
    "{": ""      ""Video ID: xoLJMWCALbA""
  },
  {
    "{": ""      ""Video ID: 9T47ioFS584""
  },
  {
    "{": ""      ""Video ID: QOuC8unvzY8""
  },
  {
    "{": ""      ""Video ID: O_td0OE6aww""
  },
  {
    "{": ""      ""Video ID: bg6Q7LCNYGY""
  },
  {
    "{": ""      ""Video ID: P2deq1TrQ_Q""
  },
  {
    "{": ""      ""Video ID: XHRtYUXI7xU""
  },
  {
    "{": ""      ""Video ID: HmWk5oJJ7R8""
  },
  {
    "{": ""      ""Video ID: 8lo3A54H9Cc""
  },
  {
    "{": ""      ""Video ID: c-OCDMGUo5U""
  },
  {
    "{": ""      ""Video ID: aMu0gA_t9pg""
  },
  {
    "{": ""      ""Video ID: ByeR-BglLi0""
  },
  {
    "{": ""      ""Video ID: _GY8TAj3HzQ""
  },
  {
    "{": ""      ""Video ID: XO5C602RYTY""
  },
  {
    "{": ""      ""Video ID: QgwEkirVJMI""
  },
  {
    "{": ""      ""Video ID: svH5xe_t0-w""
  },
  {
    "{": ""      ""Video ID: gViXfIPKyRA""
  },
  {
    "{": ""      ""Video ID: hmvw9dSEfGI""
  },
  {
    "{": ""      ""Video ID: am9prPYEJwM""
  },
  {
    "{": ""      ""Video ID: hnizDcBvXhM""
  },
  {
    "{": ""      ""Video ID: ctZTUOAK8Zk""
  },
  {
    "{": ""      ""Video ID: xq1Vo1rj0go""
  },
  {
    "{": ""      ""Video ID: 8FiasR8Xmqk""
  },
  {
    "{": ""      ""Video ID: OeSdq6lHV8k""
  },
  {
    "{": ""      ""Video ID: RVxOrlBe5Us""
  },
  {
    "{": ""      ""Video ID: Gz_DiJqu76w""
  },
  {
    "{": ""      ""Video ID: hA1tSUYj2B0""
  },
  {
    "{": ""      ""Video ID: hh1s_25yKK4""
  },
  {
    "{": ""      ""Video ID: WXfkCZm47Fw""
  },
  {
    "{": ""      ""Video ID: qRcTyut4Wp8""
  },
  {
    "{": ""      ""Video ID: 5sKG5nHmv7E""
  },
  {
    "{": ""      ""Video ID: VfR2sOxfbYk""
  },
  {
    "{": ""      ""Video ID: rSiUXC5RAyY""
  },
  {
    "{": ""      ""Video ID: QDoWS2PBUis""
  },
  {
    "{": ""      ""Video ID: C87BUJKWwUk""
  },
  {
    "{": ""      ""Video ID: c1cTNySQ7EE""
  },
  {
    "{": ""      ""Video ID: PsuYDD1Ecbc""
  },
  {
    "{": ""      ""Video ID: mQp9UGsce7g""
  },
  {
    "{": ""      ""Video ID: ivngTq1W_28""
  },
  {
    "{": ""      ""Video ID: WRRItDE0ZuU""
  },
  {
    "{": ""      ""Video ID: wcCm7zezJTY""
  },
  {
    "{": ""      ""Video ID: f74uRJTwrlo""
  },
  {
    "{": ""      ""Video ID: QxZiNtvT20g""
  },
  {
    "{": ""      ""Video ID: _sCD9Tkp2mU""
  },
  {
    "{": ""      ""Video ID: uYL4JJEXERI""
  },
  {
    "{": ""      ""Video ID: fS1fs7JveOc""
  },
  {
    "{": ""      ""Video ID: irxmzKfmo5w""
  },
  {
    "{": ""      ""Video ID: kqI_R4Fn9UE""
  },
  {
    "{": ""      ""Video ID: t9kHwWLDMN4""
  },
  {
    "{": ""      ""Video ID: li9Z8imJBzE""
  },
  {
    "{": ""      ""Video ID: z_EiUsS52a0""
  },
  {
    "{": ""      ""Video ID: qzQB8GwTc7M""
  },
  {
    "{": ""      ""Video ID: u8DxDEhP638""
  },
  {
    "{": ""      ""Video ID: 273bHSSR078""
  },
  {
    "{": ""      ""Video ID: pfvx4nsjPao""
  },
  {
    "{": ""      ""Video ID: D4yu-ra1qBI""
  },
  {
    "{": ""      ""Video ID: V1dg40T9sPA""
  },
  {
    "{": ""      ""Video ID: otn8FLHcTAA""
  },
  {
    "{": ""      ""Video ID: 8FlgNJPoVAU""
  },
  {
    "{": ""      ""Video ID: SJkMQUfiA30""
  },
  {
    "{": ""      ""Video ID: 17enImxu5LM""
  },
  {
    "{": ""      ""Video ID: nqL3wUlRFD0""
  },
  {
    "{": ""      ""Video ID: WsvTr-1bZwM""
  },
  {
    "{": ""      ""Video ID: S42pDLsZwnc""
  },
  {
    "{": ""      ""Video ID: IQF-EM0kb0U""
  },
  {
    "{": ""      ""Video ID: oa09AQvcW6A""
  },
  {
    "{": ""      ""Video ID: yIJQkXz9-lg""
  },
  {
    "{": ""      ""Video ID: BB9IeLiu2dI""
  },
  {
    "{": ""      ""Video ID: Jo-I-sW_C5s""
  },
  {
    "{": ""      ""Video ID: JEkUutU346k""
  },
  {
    "{": ""      ""Video ID: vKqXDJbWtqI""
  },
  {
    "{": ""      ""Video ID: 7gU3-MScNiU""
  },
  {
    "{": ""      ""Video ID: r_5PljYVU98""
  },
  {
    "{": ""      ""Video ID: ak_cpM91zLA""
  },
  {
    "{": ""      ""Video ID: vxx5-6GIi8I""
  },
  {
    "{": ""      ""Video ID: Xj7ij921Iuc""
  },
  {
    "{": ""      ""Video ID: GizsHn3d-O0""
  },
  {
    "{": ""      ""Video ID: 2yRNUmFGUz8""
  },
  {
    "{": ""      ""Video ID: qbFpYalGQ_I""
  },
  {
    "{": ""      ""Video ID: RAzx-hhx0Uo""
  },
  {
    "{": ""      ""Video ID: EjfpWpXZ814""
  },
  {
    "{": ""      ""Video ID: BBC-lghMEfQ""
  },
  {
    "{": ""      ""Video ID: plxpXZxsIYo""
  },
  {
    "{": ""      ""Video ID: KQVXbZPf28Y""
  },
  {
    "{": ""      ""Video ID: 3KSvSDxlOhg""
  },
  {
    "{": ""      ""Video ID: WS3LTbuzFhE""
  },
  {
    "{": ""      ""Video ID: URRaM8jVDlc""
  },
  {
    "{": ""      ""Video ID: FEt3HpXouAE""
  },
  {
    "{": ""      ""Video ID: WB6boQPIG30""
  },
  {
    "{": ""      ""Video ID: XMyoV_TujJE""
  },
  {
    "{": ""      ""Video ID: Tnfew_ux-hM""
  },
  {
    "{": ""      ""Video ID: -LzvbSUl5MM""
  },
  {
    "{": ""      ""Video ID: hyAk-AXW4KY""
  },
  {
    "{": ""      ""Video ID: I04dYt-wYck""
  },
  {
    "{": ""      ""Video ID: WUh7yA_9T1g""
  },
  {
    "{": ""      ""Video ID: ZlW6yaag8Xk""
  },
  {
    "{": ""      ""Video ID: Ts-x5FsYcpk""
  },
  {
    "{": ""      ""Video ID: fiVx_0R-mXw""
  },
  {
    "{": ""      ""Video ID: e3NtJ8xQpJo""
  },
  {
    "{": ""      ""Video ID: 7ZawsCL8ofI""
  },
  {
    "{": ""      ""Video ID: BHZ9VOboTXA""
  },
  {
    "{": ""      ""Video ID: QDG5cktoemA""
  },
  {
    "{": ""      ""Video ID: Xh1qd_klj_s""
  },
  {
    "{": ""      ""Video ID: pKlF2yQGvA0""
  },
  {
    "{": ""      ""Video ID: chGCVl8ycqo""
  },
  {
    "{": ""      ""Video ID: gvAriP-ai8Y""
  },
  {
    "{": ""      ""Video ID: Q_dvxQO3lpM""
  },
  {
    "{": ""      ""Video ID: iscR_5syj9Y""
  },
  {
    "{": ""      ""Video ID: 8h81PggfE8I""
  },
  {
    "{": ""      ""Video ID: qFiv6sNN_jA""
  },
  {
    "{": ""      ""Video ID: AkPhR36Pu2c""
  },
  {
    "{": ""      ""Video ID: Wull6pjk1EQ""
  },
  {
    "{": ""      ""Video ID: WsctkSjnx50""
  },
  {
    "{": ""      ""Video ID: 7YgSeMsu6QE""
  },
  {
    "{": ""      ""Video ID: pBz63VOqA2A""
  },
  {
    "{": ""      ""Video ID: 3-t-AONaZPU""
  },
  {
    "{": ""      ""Video ID: 3O4HOMPD-1E""
  },
  {
    "{": ""      ""Video ID: RanCZlTquX8""
  },
  {
    "{": ""      ""Video ID: JgkWeftmWUs""
  },
  {
    "{": ""      ""Video ID: VruBLzQlzxI""
  },
  {
    "{": ""      ""Video ID: RiFTZws2obA""
  },
  {
    "{": ""      ""Video ID: tRL8oJ-GrMQ""
  },
  {
    "{": ""      ""Video ID: lNp4tMcpM10""
  },
  {
    "{": ""      ""Video ID: 1cRZvyOv_Xc""
  },
  {
    "{": ""      ""Video ID: 9hQEyT9rA64""
  },
  {
    "{": ""      ""Video ID: BsYRuXQ7iYg""
  },
  {
    "{": ""      ""Video ID: Sn2GD9MUsIY""
  },
  {
    "{": ""      ""Video ID: LtR9lP9KlgM""
  },
  {
    "{": ""      ""Video ID: cWevkCbxc_Q""
  },
  {
    "{": ""      ""Video ID: dxNaAPnZVTA""
  },
  {
    "{": ""      ""Video ID: TSCxgtt6-6Y""
  },
  {
    "{": ""      ""Video ID: GmZDRBNtYhs""
  },
  {
    "{": ""      ""Video ID: EkF4JD2rO3Q""
  },
  {
    "{": ""      ""Video ID: JqI2lvoljpo""
  },
  {
    "{": ""      ""Video ID: Ges0D3XMWAo""
  },
  {
    "{": ""      ""Video ID: kCTO4OWHxoc""
  },
  {
    "{": ""      ""Video ID: VXTp2pFj9dg""
  },
  {
    "{": ""      ""Video ID: 9qNSpSOyT7U""
  },
  {
    "{": ""      ""Video ID: bFw6INV6xmo""
  },
  {
    "{": ""      ""Video ID: 8qXDK43a9QU""
  },
  {
    "{": ""      ""Video ID: c_zoILUx7vw""
  },
  {
    "{": ""      ""Video ID: Z6QfHLykAzA""
  },
  {
    "{": ""      ""Video ID: pPol_m8wm8Y""
  },
  {
    "{": ""      ""Video ID: bPVLc7rsFjg""
  },
  {
    "{": ""      ""Video ID: 6TPIOAXijHU""
  },
  {
    "{": ""      ""Video ID: PBdjwpanbzM""
  },
  {
    "{": ""      ""Video ID: 3K3pRfhTbtM""
  },
  {
    "{": ""      ""Video ID: 4P87mwS0h0M""
  },
  {
    "{": ""      ""Video ID: 2obr5ULgoWo""
  },
  {
    "{": ""      ""Video ID: qqPNkEhpnDM""
  },
  {
    "{": ""      ""Video ID: tvE5X36j738""
  },
  {
    "{": ""      ""Video ID: EATfie4_75s""
  },
  {
    "{": ""      ""Video ID: 1_7_Cc3LOVA""
  },
  {
    "{": ""      ""Video ID: 5xQ0ywP-bbU""
  },
  {
    "{": ""      ""Video ID: UwPDJiNXN4k""
  },
  {
    "{": ""      ""Video ID: CWuV-FpnW_k""
  },
  {
    "{": ""      ""Video ID: _Gm1RSvWXbg""
  },
  {
    "{": ""      ""Video ID: wbVj6UDh7-s""
  },
  {
    "{": ""      ""Video ID: kJxiCzUNxI8""
  },
  {
    "{": ""      ""Video ID: 3mYQaRVNAFc""
  },
  {
    "{": ""      ""Video ID: GHn6f6T7s0c""
  },
  {
    "{": ""      ""Video ID: Cm_Tke8Tdhw""
  },
  {
    "{": ""      ""Video ID: 5mFwYdq5QFE""
  },
  {
    "{": ""      ""Video ID: JLiqRHhTT8M""
  },
  {
    "{": ""      ""Video ID: j5J9b3aABt8""
  },
  {
    "{": ""      ""Video ID: 4Pp0VqblMPA""
  },
  {
    "{": ""      ""Video ID: z6DvIxp7nno""
  },
  {
    "{": ""      ""Video ID: 9VTbThH-4nU""
  },
  {
    "{": ""      ""Video ID: 1rHBYXIljKs""
  },
  {
    "{": ""      ""Video ID: s-x9nIsgk6A""
  },
  {
    "{": ""      ""Video ID: OnLYeaYDQAE""
  },
  {
    "{": ""      ""Video ID: mbyfrxSd7b0""
  },
  {
    "{": ""      ""Video ID: N7qBtcrWvzM""
  },
  {
    "{": ""      ""Video ID: sEscatBtOzI""
  },
  {
    "{": ""      ""Video ID: s2LrgUOFOT4""
  },
  {
    "{": ""      ""Video ID: u2QQYhszwZA""
  },
  {
    "{": ""      ""Video ID: rAJCuTWwY24""
  },
  {
    "{": ""      ""Video ID: pcPCx8g9A_I""
  },
  {
    "{": ""      ""Video ID: hpsdo-2Vxd4""
  },
  {
    "{": ""      ""Video ID: ugze8aZs0bE""
  },
  {
    "{": ""      ""Video ID: 7vNLH-WKxcQ""
  },
  {
    "{": ""      ""Video ID: 9jpAOm78ofc""
  },
  {
    "{": ""      ""Video ID: iM96jz-utz8""
  },
  {
    "{": ""      ""Video ID: t5XqrdszKeM""
  },
  {
    "{": ""      ""Video ID: qwfrvEYT9eI""
  },
  {
    "{": ""      ""Video ID: QwKb9fvQ-QE""
  },
  {
    "{": ""      ""Video ID: Z7h8qkMBE_E""
  },
  {
    "{": ""      ""Video ID: HGnQLgzq8Zo""
  },
  {
    "{": ""      ""Video ID: ZlDFDEvm1FI""
  },
  {
    "{": ""      ""Video ID: KA5J7892O2c""
  },
  {
    "{": ""      ""Video ID: 9Y6oMsroBvU""
  },
  {
    "{": ""      ""Video ID: 3pHCki_GKh4""
  },
  {
    "{": ""      ""Video ID: 74R2hL6JsCs""
  },
  {
    "{": ""      ""Video ID: gSZ2pNwUOac""
  },
  {
    "{": ""      ""Video ID: h3qI13SZwFI""
  },
  {
    "{": ""      ""Video ID: vu83agSl5XM""
  },
  {
    "{": ""      ""Video ID: DhFsGOyBGQw""
  },
  {
    "{": ""      ""Video ID: Pcuw-_AOk6g""
  },
  {
    "{": ""      ""Video ID: JpKoN40K7mA""
  },
  {
    "{": ""      ""Video ID: DYnadAE685o""
  },
  {
    "{": ""      ""Video ID: L-Z0aSVcKQ8""
  },
  {
    "{": ""      ""Video ID: n_QoffvYQpw""
  },
  {
    "{": ""      ""Video ID: HtXQNhoxACY""
  },
  {
    "{": ""      ""Video ID: ZPfazp5jHSE""
  },
  {
    "{": ""      ""Video ID: yNGWn-aWn5g""
  },
  {
    "{": ""      ""Video ID: Dr7A0aB3iJ8""
  },
  {
    "{": ""      ""Video ID: j1e3oPddJuE""
  },
  {
    "{": ""      ""Video ID: J3_6aQXtglA""
  },
  {
    "{": ""      ""Video ID: r_sAw8Y7cZ0""
  },
  {
    "{": ""      ""Video ID: huBlNu8EcMw""
  },
  {
    "{": ""      ""Video ID: 6KtF7ql3FJc""
  },
  {
    "{": ""      ""Video ID: x5sXk5tHbqA""
  },
  {
    "{": ""      ""Video ID: JHuMZJEH9O4""
  },
  {
    "{": ""      ""Video ID: xs7MvKVlneA""
  },
  {
    "{": ""      ""Video ID: 5uUHX2QMA5g""
  },
  {
    "{": ""      ""Video ID: qlqe4CQD0R0""
  },
  {
    "{": ""      ""Video ID: dJ6w4LoRUE4""
  },
  {
    "{": ""      ""Video ID: JXUqkR7-i5w""
  },
  {
    "{": ""      ""Video ID: MW0i4Hfjrho""
  },
  {
    "{": ""      ""Video ID: YDr1UfgYjcg""
  },
  {
    "{": ""      ""Video ID: 0UnsOJF-DFQ""
  },
  {
    "{": ""      ""Video ID: NV9ovtoCBJ4""
  },
  {
    "{": ""      ""Video ID: 2yTiBoseR2s""
  },
  {
    "{": ""      ""Video ID: WIYjEDn5uyg""
  },
  {
    "{": ""      ""Video ID: Q5RFbX2eZ-o""
  },
  {
    "{": ""      ""Video ID: XFQXcv1k9OM""
  },
  {
    "{": ""      ""Video ID: yoYRbAmsLmA""
  },
  {
    "{": ""      ""Video ID: pyNxIGeNbDQ""
  },
  {
    "{": ""      ""Video ID: aKQH3rM0acE""
  },
  {
    "{": ""      ""Video ID: 0JgUtLEvyIA""
  },
  {
    "{": ""      ""Video ID: ueRyL6uBzCw""
  },
  {
    "{": ""      ""Video ID: DbKXP7t_RlU""
  },
  {
    "{": ""      ""Video ID: MeSSwKffj9o""
  },
  {
    "{": ""      ""Video ID: pf-ScC37zTI""
  },
  {
    "{": ""      ""Video ID: JrTikDPOjnw""
  },
  {
    "{": ""      ""Video ID: vCZmgWe73AY""
  },
  {
    "{": ""      ""Video ID: dHLtrLioTis""
  },
  {
    "{": ""      ""Video ID: pzAIZN9HuFg""
  },
  {
    "{": ""      ""Video ID: CmV998nCcAg""
  },
  {
    "{": ""      ""Video ID: X9DV3qbrMzk""
  },
  {
    "{": ""      ""Video ID: b3tYqr9fHdU""
  },
  {
    "{": ""      ""Video ID: _BFSQA6TBmo""
  },
  {
    "{": ""      ""Video ID: C5ctJXaXCs0""
  },
  {
    "{": ""      ""Video ID: E9Lwwt8qtOI""
  },
  {
    "{": ""      ""Video ID: JgSymvZLpOw""
  },
  {
    "{": ""      ""Video ID: zWgNWKRztFU""
  },
  {
    "{": ""      ""Video ID: 2MCy1dRwxzY""
  },
  {
    "{": ""      ""Video ID: QQxLmYfh2kU""
  },
  {
    "{": ""      ""Video ID: ynA_xcWjCm8""
  },
  {
    "{": ""      ""Video ID: 1I_Xaadm6Sg""
  },
  {
    "{": ""      ""Video ID: E8Q2irptevU""
  },
  {
    "{": ""      ""Video ID: 5Mz9pDGHBTo""
  },
  {
    "{": ""      ""Video ID: dy_SOn4WsGU""
  },
  {
    "{": ""      ""Video ID: MVXSFutIYw0""
  },
  {
    "{": ""      ""Video ID: SUYLkYF3MMA""
  },
  {
    "{": ""      ""Video ID: OA_CfSbhNrA""
  },
  {
    "{": ""      ""Video ID: jOozI2qKggA""
  },
  {
    "{": ""      ""Video ID: Fqst_XPH7rI""
  },
  {
    "{": ""      ""Video ID: eMNc0lQCxb8""
  },
  {
    "{": ""      ""Video ID: Irgbcw73d70""
  },
  {
    "{": ""      ""Video ID: Z_MeRDQx0Ys""
  },
  {
    "{": ""      ""Video ID: VJ6DfD5ojH8""
  },
  {
    "{": ""      ""Video ID: ttF4-rI_Mi4""
  },
  {
    "{": ""      ""Video ID: qeBvrkbZTss""
  },
  {
    "{": ""      ""Video ID: QEcBjpsP1bU""
  },
  {
    "{": ""      ""Video ID: Mm5kifHP844""
  },
  {
    "{": ""      ""Video ID: xPJIHdfYgas""
  },
  {
    "{": ""      ""Video ID: HqeztaT0eU0""
  },
  {
    "{": ""      ""Video ID: bFJxw15EN20""
  },
  {
    "{": ""      ""Video ID: rnQ_ZDJgpTI""
  },
  {
    "{": ""      ""Video ID: LfeWn3BmreM""
  },
  {
    "{": ""      ""Video ID: e4ibkrOqVh0""
  },
  {
    "{": ""      ""Video ID: zkZewgnGCiw""
  },
  {
    "{": ""      ""Video ID: yPqVjeEm1r8""
  },
  {
    "{": ""      ""Video ID: S_ACBm1SuFU""
  },
  {
    "{": ""      ""Video ID: 4wyCBF5CsCA""
  },
  {
    "{": ""      ""Video ID: pYATbsu2cP8""
  },
  {
    "{": ""      ""Video ID: 1GDtEHljhhA""
  },
  {
    "{": ""      ""Video ID: t8fknhbB-Xo""
  },
  {
    "{": ""      ""Video ID: OVSxwK9s-g0""
  },
  {
    "{": ""      ""Video ID: nmAjgpj6yyI""
  },
  {
    "{": ""      ""Video ID: ZmWTzJlG-7U""
  },
  {
    "{": ""      ""Video ID: FG2AFftpZwk""
  },
  {
    "{": ""      ""Video ID: ZP2CLdUyY4Y""
  },
  {
    "{": ""      ""Video ID: zPe2fTxMH4w""
  },
  {
    "{": ""      ""Video ID: kQDA9KKs0ZY""
  },
  {
    "{": ""      ""Video ID: yTT7V0HxlPI""
  },
  {
    "{": ""      ""Video ID: O96ZMPXuv1A""
  },
  {
    "{": ""      ""Video ID: RCMZtM6bTVM""
  },
  {
    "{": ""      ""Video ID: 21ZY771W3U8""
  },
  {
    "{": ""      ""Video ID: FOI-0hdoEsk""
  },
  {
    "{": ""      ""Video ID: VnpIfUTkXoY""
  },
  {
    "{": ""      ""Video ID: 3OUQpjECmAM""
  },
  {
    "{": ""      ""Video ID: KjZBOCAgR64""
  },
  {
    "{": ""      ""Video ID: I-16u9x3tfE""
  },
  {
    "{": ""      ""Video ID: ALdlsyUv75Q""
  },
  {
    "{": ""      ""Video ID: 4YnnTzyidNI""
  },
  {
    "{": ""      ""Video ID: zxkb8uldt-8""
  },
  {
    "{": ""      ""Video ID: R4QO7zXTljE""
  },
  {
    "{": ""      ""Video ID: fO7r485TBM4""
  },
  {
    "{": ""      ""Video ID: ryMliyeIDp4""
  },
  {
    "{": ""      ""Video ID: CLQvdtuJ2kk""
  },
  {
    "{": ""      ""Video ID: fOfF5wsdKqs""
  },
  {
    "{": ""      ""Video ID: b3UhI-p-Vd0""
  },
  {
    "{": ""      ""Video ID: Qo5yF-hu9C4""
  },
  {
    "{": ""      ""Video ID: MoQrnz78Njw""
  },
  {
    "{": ""      ""Video ID: NEXRC_QPEa4""
  },
  {
    "{": ""      ""Video ID: kDQAgPjv94M""
  },
  {
    "{": ""      ""Video ID: 4PpMdTmVMpo""
  },
  {
    "{": ""      ""Video ID: O-1ISx68w1s""
  },
  {
    "{": ""      ""Video ID: ntuQvvXzJC0""
  },
  {
    "{": ""      ""Video ID: wT3V1_jLV0c""
  },
  {
    "{": ""      ""Video ID: ZSGLH8XgaD8""
  },
  {
    "{": ""      ""Video ID: AYHm1a7dolo""
  },
  {
    "{": ""      ""Video ID: n3R-ybGeBVo""
  },
  {
    "{": ""      ""Video ID: 8IwCtMc0ZP8""
  },
  {
    "{": ""      ""Video ID: dWMPHJFLDN8""
  },
  {
    "{": ""      ""Video ID: _-oJKyHHxKk""
  },
  {
    "{": ""      ""Video ID: icLLvJnPC1g""
  },
  {
    "{": ""      ""Video ID: 4JxTa71N2MY""
  },
  {
    "{": ""      ""Video ID: d4lTcjcyNDs""
  },
  {
    "{": ""      ""Video ID: 1pEaxLFdOZY""
  },
  {
    "{": ""      ""Video ID: cC90EEuayQY""
  },
  {
    "{": ""      ""Video ID: SE_gpXH7CtA""
  },
  {
    "{": ""      ""Video ID: 0MoIHXKmVUs""
  },
  {
    "{": ""      ""Video ID: Jnws7xbRXOg""
  },
  {
    "{": ""      ""Video ID: PsYao5VO_gk""
  },
  {
    "{": ""      ""Video ID: OBC-17DacPY""
  },
  {
    "{": ""      ""Video ID: zil8uTgmf_k""
  },
  {
    "{": ""      ""Video ID: -z506-8iFb4""
  },
  {
    "{": ""      ""Video ID: 2DVM9Be7xyU""
  },
  {
    "{": ""      ""Video ID: WojmnD7KhL8""
  },
  {
    "{": ""      ""Video ID: tWMIRHvEpgY""
  },
  {
    "{": ""      ""Video ID: FQUDHhY2lHQ""
  },
  {
    "{": ""      ""Video ID: s2lws-Tj6jM""
  },
  {
    "{": ""      ""Video ID: G5Sh4c3My2Y""
  },
  {
    "{": ""      ""Video ID: 7FZXp-Eegq0""
  },
  {
    "{": ""      ""Video ID: 3x47mA1cJxk""
  },
  {
    "{": ""      ""Video ID: Mg55phlL1tQ""
  },
  {
    "{": ""      ""Video ID: V-8-iS3z30o""
  },
  {
    "{": ""      ""Video ID: IBT7DZ0iMuo""
  },
  {
    "{": ""      ""Video ID: Q4ltC0Tzaiw""
  },
  {
    "{": ""      ""Video ID: jj0nLDiFUpU""
  },
  {
    "{": ""      ""Video ID: AC6gKs3kBBc""
  },
  {
    "{": ""      ""Video ID: tIeBsxBCIRc""
  },
  {
    "{": ""      ""Video ID: sWRKlNlRsgI""
  },
  {
    "{": ""      ""Video ID: I6BNfMrmZdk""
  },
  {
    "{": ""      ""Video ID: n8w2ISMTRlA""
  },
  {
    "{": ""      ""Video ID: 5kZv7emX5TQ""
  },
  {
    "{": ""      ""Video ID: byxtVw2Mz8A""
  },
  {
    "{": ""      ""Video ID: Bap7gEYEN9I""
  },
  {
    "{": ""      ""Video ID: TghlHfB1BKg""
  },
  {
    "{": ""      ""Video ID: -UsXdil5buI""
  },
  {
    "{": ""      ""Video ID: GaK-l64KW6w""
  },
  {
    "{": ""      ""Video ID: 0ePHPNu6LSA""
  },
  {
    "{": ""      ""Video ID: hUNDuYz3jaI""
  },
  {
    "{": ""      ""Video ID: T2z2iDAhcDc""
  },
  {
    "{": ""      ""Video ID: t_LCvT9aU4o""
  },
  {
    "{": ""      ""Video ID: fulFkfMmbjk""
  },
  {
    "{": ""      ""Video ID: bm6nVGmoD1U""
  },
  {
    "{": ""      ""Video ID: lLuEj52QqHk""
  },
  {
    "{": ""      ""Video ID: xE_R5PiIrkA""
  },
  {
    "{": ""      ""Video ID: HEVcnq4VVMA""
  },
  {
    "{": ""      ""Video ID: J8hazJOFajM""
  },
  {
    "{": ""      ""Video ID: EkIPvp67GI4""
  },
  {
    "{": ""      ""Video ID: 4rsL8o5gMog""
  },
  {
    "{": ""      ""Video ID: kVZuF-QGjVE""
  },
  {
    "{": ""      ""Video ID: vf6D4FynMgI""
  },
  {
    "{": ""      ""Video ID: I2WMUI9hFHM""
  },
  {
    "{": ""      ""Video ID: 8WWl80PeqSU""
  },
  {
    "{": ""      ""Video ID: yYCi_4WJz1w""
  },
  {
    "{": ""      ""Video ID: APr9c0TxMsE""
  },
  {
    "{": ""      ""Video ID: iJ2evsE0K_g""
  },
  {
    "{": ""      ""Video ID: e-pQPsTkvWk""
  },
  {
    "{": ""      ""Video ID: Mx-Ulu10sKM""
  },
  {
    "{": ""      ""Video ID: oI4eKP9VROQ""
  },
  {
    "{": ""      ""Video ID: XbJqJ_tuT5c""
  },
  {
    "{": ""      ""Video ID: CFJ0LufmMEg""
  },
  {
    "{": ""      ""Video ID: ubzLXHdO4FY""
  },
  {
    "{": ""      ""Video ID: QjLxG6ZiBhg""
  },
  {
    "{": ""      ""Video ID: OQQwwRrsTak""
  },
  {
    "{": ""      ""Video ID: rlRxQ_PEWOo""
  },
  {
    "{": ""      ""Video ID: bAp8E-9-PTk""
  },
  {
    "{": ""      ""Video ID: S0Jkd18Afzs""
  },
  {
    "{": ""      ""Video ID: LeYW4kyrvBw""
  },
  {
    "{": ""      ""Video ID: ElI0GvDpyVk""
  },
  {
    "{": ""      ""Video ID: Gi3Sn6LO7Pk""
  },
  {
    "{": ""      ""Video ID: ocoaP09jJFo""
  },
  {
    "{": ""      ""Video ID: -RA6LXm5cFQ""
  },
  {
    "{": ""      ""Video ID: yqyiQMJCsAk""
  },
  {
    "{": ""      ""Video ID: RL0LG_0T864""
  },
  {
    "{": ""      ""Video ID: cQIEfi0H2co""
  },
  {
    "{": ""      ""Video ID: 6rL6CXMgwKg""
  },
  {
    "{": ""      ""Video ID: en8PbEZ4SK0""
  },
  {
    "{": ""      ""Video ID: 6hLLJ7DozP0""
  },
  {
    "{": ""      ""Video ID: f1gPEuWlAkc""
  },
  {
    "{": ""      ""Video ID: oegg6xemzd0""
  },
  {
    "{": ""      ""Video ID: P4V0dIjEbWw""
  },
  {
    "{": ""      ""Video ID: yxZRq2hiS-w""
  },
  {
    "{": ""      ""Video ID: 9R5m4XHFDpc""
  },
  {
    "{": ""      ""Video ID: DX63sCv3bqs""
  },
  {
    "{": ""      ""Video ID: H8TSCiiG3YQ""
  },
  {
    "{": ""      ""Video ID: F7bcNuu4vko""
  },
  {
    "{": ""      ""Video ID: 6w8WpRj_d3U""
  },
  {
    "{": ""      ""Video ID: HjThl4CxgSk""
  },
  {
    "{": ""      ""Video ID: cekkzbHot_I""
  },
  {
    "{": ""      ""Video ID: R7oZ_Ytn9Hw""
  },
  {
    "{": ""      ""Video ID: Jy5btt1CcOM""
  },
  {
    "{": ""      ""Video ID: GuAnkq8cMHw""
  },
  {
    "{": ""      ""Video ID: qH-qrwMhFiQ""
  },
  {
    "{": ""      ""Video ID: dNAaqSJnqDg""
  },
  {
    "{": ""      ""Video ID: 1uwOL4rB-go""
  },
  {
    "{": ""      ""Video ID: eiQNuhPMU48""
  },
  {
    "{": ""      ""Video ID: WmX821YzYTs""
  },
  {
    "{": ""      ""Video ID: IbuCZp6d8go""
  },
  {
    "{": ""      ""Video ID: cnTDKlKF6K0""
  },
  {
    "{": ""      ""Video ID: gswPW9g6pKM""
  },
  {
    "{": ""      ""Video ID: HVO_5b0C1pc""
  },
  {
    "{": ""      ""Video ID: yA-L60k0tbM""
  },
  {
    "{": ""      ""Video ID: LdyOOysDsQc""
  },
  {
    "{": ""      ""Video ID: kYll7uARNdk""
  },
  {
    "{": ""      ""Video ID: UlP6wbiPhB4""
  },
  {
    "{": ""      ""Video ID: uRcdTPHAiik""
  },
  {
    "{": ""      ""Video ID: e2o2Et2X97k""
  },
  {
    "{": ""      ""Video ID: KxADhFK5PgM""
  },
  {
    "{": ""      ""Video ID: kYcy0gZXmSY""
  },
  {
    "{": ""      ""Video ID: ndgzCTKvgIo""
  },
  {
    "{": ""      ""Video ID: z9VDpoQUZZc""
  },
  {
    "{": ""      ""Video ID: 5tSHhE8as5Q""
  },
  {
    "{": ""      ""Video ID: Q2uarAnyhzw""
  },
  {
    "{": ""      ""Video ID: lu7ycbDy_8o""
  },
  {
    "{": ""      ""Video ID: vJpPvDG7WXE""
  },
  {
    "{": ""      ""Video ID: MdWEn297dLk""
  },
  {
    "{": ""      ""Video ID: d1fhnPFP50s""
  },
  {
    "{": ""      ""Video ID: vyqgjCKm9nQ""
  },
  {
    "{": ""      ""Video ID: D3sMZbhs7QA""
  },
  {
    "{": ""      ""Video ID: OaQsb6jfadY""
  },
  {
    "{": ""      ""Video ID: k4slA3upMyo""
  },
  {
    "{": ""      ""Video ID: MZ-R-6k48qc""
  },
  {
    "{": ""      ""Video ID: RD3LXcJC1-E""
  },
  {
    "{": ""      ""Video ID: fchd05mJZbo""
  },
  {
    "{": ""      ""Video ID: 4AMMAOg0xzY""
  },
  {
    "{": ""      ""Video ID: oSF0yoHkz7Q""
  },
  {
    "{": ""      ""Video ID: idon1YPlCdA""
  },
  {
    "{": ""      ""Video ID: N8_pSmY-CdQ""
  },
  {
    "{": ""      ""Video ID: 7i7XMnE_eHU""
  },
  {
    "{": ""      ""Video ID: 8p6OfIuT-BU""
  },
  {
    "{": ""      ""Video ID: o8WwPoTVylA""
  },
  {
    "{": ""      ""Video ID: 9MEgMgd2V9s""
  },
  {
    "{": ""      ""Video ID: 6tlNWKr2hYg""
  },
  {
    "{": ""      ""Video ID: W72WpVfKGhU""
  },
  {
    "{": ""      ""Video ID: nFnVzaK7O4k""
  },
  {
    "{": ""      ""Video ID: NpSpApMqJ9w""
  },
  {
    "{": ""      ""Video ID: XhnefEAC5sQ""
  },
  {
    "{": ""      ""Video ID: snZ-nNEzcus""
  },
  {
    "{": ""      ""Video ID: LnFRvYhdbyM""
  },
  {
    "{": ""      ""Video ID: UMive3zN6Sk""
  },
  {
    "{": ""      ""Video ID: eVq1kvXaMMM""
  },
  {
    "{": ""      ""Video ID: GYdZ-wsUt-U""
  },
  {
    "{": ""      ""Video ID: r640Acq-Dx8""
  },
  {
    "{": ""      ""Video ID: eSjhosHGU5I""
  },
  {
    "{": ""      ""Video ID: gcMPhuhqVO4""
  },
  {
    "{": ""      ""Video ID: P21nx7il5u0""
  },
  {
    "{": ""      ""Video ID: Z1jfJVPCR_0""
  },
  {
    "{": ""      ""Video ID: WkU6ir0Ofdo""
  },
  {
    "{": ""      ""Video ID: yM_Q2Dd5Y08""
  },
  {
    "{": ""      ""Video ID: lnY5nuosn-o""
  },
  {
    "{": ""      ""Video ID: 3JE2cr1fTx4""
  },
  {
    "{": ""      ""Video ID: -EjsB-FRfvg""
  },
  {
    "{": ""      ""Video ID: 3KPeg4m1U-E""
  },
  {
    "{": ""      ""Video ID: CC5oVzy_OU4""
  },
  {
    "{": ""      ""Video ID: lvLXCalUxa0""
  },
  {
    "{": ""      ""Video ID: c-sK4Lz60aU""
  },
  {
    "{": ""      ""Video ID: YV2iljlOglE""
  },
  {
    "{": ""      ""Video ID: W3P3PGpD3bM""
  },
  {
    "{": ""      ""Video ID: btc4w1xOarA""
  },
  {
    "{": ""      ""Video ID: c7rrp0Brrbc""
  },
  {
    "{": ""      ""Video ID: nJ6p7xkFXW4""
  },
  {
    "{": ""      ""Video ID: -Ib-jB58GEg""
  },
  {
    "{": ""      ""Video ID: E2xRaERiEPE""
  },
  {
    "{": ""      ""Video ID: 1B_-g1dS2sU""
  },
  {
    "{": ""      ""Video ID: TTqdmXDjLBg""
  },
  {
    "{": ""      ""Video ID: v2gRGu1BJ2g""
  },
  {
    "{": ""      ""Video ID: AdqRmRvV49c""
  },
  {
    "{": ""      ""Video ID: 1x0x9eK2FXM""
  },
  {
    "{": ""      ""Video ID: TIakeVdJ3AY""
  },
  {
    "{": ""      ""Video ID: sxHBctDg00c""
  },
  {
    "{": ""      ""Video ID: EAjVa83fK4E""
  },
  {
    "{": ""      ""Video ID: -ofwpwoCNJk""
  },
  {
    "{": ""      ""Video ID: YpTWYetUL8w""
  },
  {
    "{": ""      ""Video ID: 8LYgrWShdx4""
  },
  {
    "{": ""      ""Video ID: _--ap9NmV8s""
  },
  {
    "{": ""      ""Video ID: YkS8KVMFF4I""
  },
  {
    "{": ""      ""Video ID: _9BTqr6nIzs""
  },
  {
    "{": ""      ""Video ID: JSM8QSASFaA""
  },
  {
    "{": ""      ""Video ID: aeFPBYSyWCQ""
  },
  {
    "{": ""      ""Video ID: kXfaDo-PMDo""
  },
  {
    "{": ""      ""Video ID: blBzKTly4Yc""
  },
  {
    "{": ""      ""Video ID: QwXSk9uRsMg""
  },
  {
    "{": ""      ""Video ID: YpYMwj8F_OA""
  },
  {
    "{": ""      ""Video ID: IlzBtDs0Xqc""
  },
  {
    "{": ""      ""Video ID: zzhA6wdwCkY""
  },
  {
    "{": ""      ""Video ID: 5ysKd1cswlo""
  },
  {
    "{": ""      ""Video ID: NzzTjfPuP10""
  },
  {
    "{": ""      ""Video ID: XvvmEAnDaSk""
  },
  {
    "{": ""      ""Video ID: OpWiXUYyTPo""
  },
  {
    "{": ""      ""Video ID: Izuo-45rVNs""
  },
  {
    "{": ""      ""Video ID: 6LuKr4dl9mA""
  },
  {
    "{": ""      ""Video ID: gVHyLCzV1Y0""
  },
  {
    "{": ""      ""Video ID: dPzyZGWuhLM""
  },
  {
    "{": ""      ""Video ID: op4byt-DtsI""
  },
  {
    "{": ""      ""Video ID: 2pa-Dtir0V8""
  },
  {
    "{": ""      ""Video ID: p3pkzfliyW4""
  },
  {
    "{": ""      ""Video ID: WmHmCQkR7Oo""
  },
  {
    "{": ""      ""Video ID: 3CoGjohyUPs""
  },
  {
    "{": ""      ""Video ID: Gc4nPyxF7yw""
  },
  {
    "{": ""      ""Video ID: tz-IpDMHu7g""
  },
  {
    "{": ""      ""Video ID: 3DMBZKmksHY""
  },
  {
    "{": ""      ""Video ID: WIqyv2lLUp0""
  },
  {
    "{": ""      ""Video ID: 4SLGT_bXe38""
  },
  {
    "{": ""      ""Video ID: 4KipP_03SrI""
  },
  {
    "{": ""      ""Video ID: XmDe__Lu0AY""
  },
  {
    "{": ""      ""Video ID: mDpZ9R9A_80""
  },
  {
    "{": ""      ""Video ID: q0KeelCigzo""
  },
  {
    "{": ""      ""Video ID: v0X_pKdW2eE""
  },
  {
    "{": ""      ""Video ID: nYkIMVO5qUM""
  },
  {
    "{": ""      ""Video ID: Drn_7PKwvIU""
  },
  {
    "{": ""      ""Video ID: hhYd2_maroY""
  },
  {
    "{": ""      ""Video ID: GQNII1M6_jw""
  },
  {
    "{": ""      ""Video ID: tfcS9Ib1ars""
  },
  {
    "{": ""      ""Video ID: KdKefn1BYPM""
  },
  {
    "{": ""      ""Video ID: OYf749dPsIg""
  },
  {
    "{": ""      ""Video ID: W5xE_2wY4YI""
  },
  {
    "{": ""      ""Video ID: Pp-1h1b0ICQ""
  },
  {
    "{": ""      ""Video ID: D-wxPkVMHT0""
  },
  {
    "{": ""      ""Video ID: PerdWqBj3Yo""
  },
  {
    "{": ""      ""Video ID: xef0Fzu0W1Y""
  },
  {
    "{": ""      ""Video ID: 1BHOBeA85Aw""
  },
  {
    "{": ""      ""Video ID: YK5WyT6MSQw""
  },
  {
    "{": ""      ""Video ID: tAzIoLyf56c""
  },
  {
    "{": ""      ""Video ID: Hv_b8dPJu8g""
  },
  {
    "{": ""      ""Video ID: UXrqaOtVoxs""
  },
  {
    "{": ""      ""Video ID: xkv_EDCcnV8""
  },
  {
    "{": ""      ""Video ID: LWQpPEu37JQ""
  },
  {
    "{": ""      ""Video ID: TXbBSLn8srk""
  },
  {
    "{": ""      ""Video ID: Dxg7a7qcGLA""
  },
  {
    "{": ""      ""Video ID: WFajhXmPHXg""
  },
  {
    "{": ""      ""Video ID: mqC7axJo20g""
  },
  {
    "{": ""      ""Video ID: fCxYcMq5mU8""
  },
  {
    "{": ""      ""Video ID: E4JcXl4dU6Q""
  },
  {
    "{": ""      ""Video ID: 5_97LyhU9cg""
  },
  {
    "{": ""      ""Video ID: NlCtNHrDqTY""
  },
  {
    "{": ""      ""Video ID: yIMKXvn33YQ""
  },
  {
    "{": ""      ""Video ID: zWFVntEt-kc""
  },
  {
    "{": ""      ""Video ID: vyiYOw94BRI""
  },
  {
    "{": ""      ""Video ID: Z-HjmP7BCVc""
  },
  {
    "{": ""      ""Video ID: 00c08ijIlHo""
  },
  {
    "{": ""      ""Video ID: PK0Yqd5M9UQ""
  },
  {
    "{": ""      ""Video ID: 5ApNtdN0xMw""
  },
  {
    "{": ""      ""Video ID: 70SQCLk5e7Q""
  },
  {
    "{": ""      ""Video ID: -VMKiIT0lME""
  },
  {
    "{": ""      ""Video ID: LwY3pB_KYtE""
  },
  {
    "{": ""      ""Video ID: MbTISLBgDfk""
  },
  {
    "{": ""      ""Video ID: rRn86EtzhZA""
  },
  {
    "{": ""      ""Video ID: EINb5UVzbk4""
  },
  {
    "{": ""      ""Video ID: bkUzxZ7-cMo""
  },
  {
    "{": ""      ""Video ID: 1vMPPgn0GSg""
  },
  {
    "{": ""      ""Video ID: fqwqSHyfkPM""
  },
  {
    "{": ""      ""Video ID: hrGtRKoLvJU""
  },
  {
    "{": ""      ""Video ID: goLwuzTIt6o""
  },
  {
    "{": ""      ""Video ID: VfyZauRu9T8""
  },
  {
    "{": ""      ""Video ID: y3lKzrtl8ZU""
  },
  {
    "{": ""      ""Video ID: lQ0REFNCPTc""
  },
  {
    "{": ""      ""Video ID: ROpZ32l8CiE""
  },
  {
    "{": ""      ""Video ID: 6CZLD485R0I""
  },
  {
    "{": ""      ""Video ID: vqHcp-MksgI""
  },
  {
    "{": ""      ""Video ID: H9tIXeE8frU""
  },
  {
    "{": ""      ""Video ID: vTovnkUkopY""
  },
  {
    "{": ""      ""Video ID: I2OgziqZ4WU""
  },
  {
    "{": ""      ""Video ID: 4nHF2gGBcVI""
  },
  {
    "{": ""      ""Video ID: Ge1RZnl-bb8""
  },
  {
    "{": ""      ""Video ID: JNZaa1Ifsm8""
  },
  {
    "{": ""      ""Video ID: 6lpSH6xLy5I""
  },
  {
    "{": ""      ""Video ID: a3RzZIKQ59A""
  },
  {
    "{": ""      ""Video ID: d5OKvWCoZG8""
  },
  {
    "{": ""      ""Video ID: oZEfnyy-0qM""
  },
  {
    "{": ""      ""Video ID: EdxZgg88yuY""
  },
  {
    "{": ""      ""Video ID: 8VhmtLdClTA""
  },
  {
    "{": ""      ""Video ID: -Cy_O-uX1fY""
  },
  {
    "{": ""      ""Video ID: QvyskAURwCs""
  },
  {
    "{": ""      ""Video ID: ngSWyBn5Jq8""
  },
  {
    "{": ""      ""Video ID: ZKSxHYK_wfs""
  },
  {
    "{": ""      ""Video ID: LOS6L1LQjRg""
  },
  {
    "{": ""      ""Video ID: rwg2h-kmvyQ""
  },
  {
    "{": ""      ""Video ID: yrdeZ-4rqyU""
  },
  {
    "{": ""      ""Video ID: yLcYgtd1Yw8""
  },
  {
    "{": ""      ""Video ID: WvNso8IB_xc""
  },
  {
    "{": ""      ""Video ID: oF7aYVwi7Uw""
  },
  {
    "{": ""      ""Video ID: e3FfgbW-C7M""
  },
  {
    "{": ""      ""Video ID: cx9lXOyQK9E""
  },
  {
    "{": ""      ""Video ID: _P9NyNTFShM""
  },
  {
    "{": ""      ""Video ID: jX-zfCDhHrY""
  },
  {
    "{": ""      ""Video ID: gd-8AKWgs3g""
  },
  {
    "{": ""      ""Video ID: y8G4kRH9VlU""
  },
  {
    "{": ""      ""Video ID: QgVfHqq4GtA""
  },
  {
    "{": ""      ""Video ID: lhcXqQIBSOU""
  },
  {
    "{": ""      ""Video ID: Y4isG90mWJo""
  },
  {
    "{": ""      ""Video ID: s_MPkiO0Zq0""
  },
  {
    "{": ""      ""Video ID: IOa3bGlbkew""
  },
  {
    "{": ""      ""Video ID: NQWnRkByfts""
  },
  {
    "{": ""      ""Video ID: TiWbeH_132I""
  },
  {
    "{": ""      ""Video ID: Hlolf2sLyiI""
  },
  {
    "{": ""      ""Video ID: r7nPn3YJTCI""
  },
  {
    "{": ""      ""Video ID: wuhQpQ6iC8s""
  },
  {
    "{": ""      ""Video ID: TcGJLKkxFOU""
  },
  {
    "{": ""      ""Video ID: aG40-BzqPYI""
  },
  {
    "{": ""      ""Video ID: UEAVzWyl6IE""
  },
  {
    "{": ""      ""Video ID: lEjmZfVJl5c""
  },
  {
    "{": ""      ""Video ID: ZTfM6Nyn0UU""
  },
  {
    "{": ""      ""Video ID: fVQPMTRBfno""
  },
  {
    "{": ""      ""Video ID: ncVvs5obZoY""
  },
  {
    "{": ""      ""Video ID: bIf84llCRPc""
  },
  {
    "{": ""      ""Video ID: k7d7u2AKVU0""
  },
  {
    "{": ""      ""Video ID: vslINxEE9AE""
  },
  {
    "{": ""      ""Video ID: BZAJafHAzX0""
  },
  {
    "{": ""      ""Video ID: RbOuf39xHmg""
  },
  {
    "{": ""      ""Video ID: g6gkiaiyhaI""
  },
  {
    "{": ""      ""Video ID: McBCKW3X7bQ""
  },
  {
    "{": ""      ""Video ID: yhbhXWIitOo""
  },
  {
    "{": ""      ""Video ID: 8gZLmqTbluw""
  },
  {
    "{": ""      ""Video ID: 2V5lIllO4DQ""
  },
  {
    "{": ""      ""Video ID: vbTJ8gDAvn8""
  },
  {
    "{": ""      ""Video ID: RkM2igp82Ec""
  },
  {
    "{": ""      ""Video ID: TIJnHEGC0Hc""
  },
  {
    "{": ""      ""Video ID: SrGxOb0Vb_M""
  },
  {
    "{": ""      ""Video ID: xSiYgi2duCc""
  },
  {
    "{": ""      ""Video ID: VzT2jw9wxKc""
  },
  {
    "{": ""      ""Video ID: JDin4Xr2t9E""
  },
  {
    "{": ""      ""Video ID: Te5ub4jkACU""
  },
  {
    "{": ""      ""Video ID: hCHi2jPcZ90""
  },
  {
    "{": ""      ""Video ID: 1zsu5sRsz50""
  },
  {
    "{": ""      ""Video ID: orbJ0JN6CyU""
  },
  {
    "{": ""      ""Video ID: aCIhebuFZSM""
  },
  {
    "{": ""      ""Video ID: px5fmBDjZnU""
  },
  {
    "{": ""      ""Video ID: Cmo1GDfcCrA""
  },
  {
    "{": ""      ""Video ID: Pb-eKPfqnLo""
  },
  {
    "{": ""      ""Video ID: znVJFpOKWD8""
  },
  {
    "{": ""      ""Video ID: VzmAWdwjSCs""
  },
  {
    "{": ""      ""Video ID: AvPwBb8N7nE""
  },
  {
    "{": ""      ""Video ID: X4SGlw8dd84""
  },
  {
    "{": ""      ""Video ID: dulYIceS_j0""
  },
  {
    "{": ""      ""Video ID: EPna4PCIb7k""
  },
  {
    "{": ""      ""Video ID: GCMdaQOPJdU""
  },
  {
    "{": ""      ""Video ID: n-sDyGR05qQ""
  },
  {
    "{": ""      ""Video ID: RnaD6pVdY7M""
  },
  {
    "{": ""      ""Video ID: G1r206kxYxE""
  },
  {
    "{": ""      ""Video ID: cLP-qM7DF_Q""
  },
  {
    "{": ""      ""Video ID: LfdHxZHj74s""
  },
  {
    "{": ""      ""Video ID: AnE4DJVVvm8""
  },
  {
    "{": ""      ""Video ID: pQYCcf8AloU""
  },
  {
    "{": ""      ""Video ID: 8ekqsIfWj0U""
  },
  {
    "{": ""      ""Video ID: 4Uk-uIc3ZLw""
  },
  {
    "{": ""      ""Video ID: XpFbJSbtJFI""
  },
  {
    "{": ""      ""Video ID: bltm5Qyb5s0""
  },
  {
    "{": ""      ""Video ID: sDsK8ZnmhC4""
  },
  {
    "{": ""      ""Video ID: hzVkmYmhILE""
  },
  {
    "{": ""      ""Video ID: bvJDMBexqaE""
  },
  {
    "{": ""      ""Video ID: E-45clkazs0""
  },
  {
    "{": ""      ""Video ID: rppYLLO52lQ""
  },
  {
    "{": ""      ""Video ID: wEMu7xi2oUY""
  },
  {
    "{": ""      ""Video ID: TmcjyhJaOkM""
  },
  {
    "{": ""      ""Video ID: tRyeTwsBkVA""
  },
  {
    "{": ""      ""Video ID: sQTZKsbk31M""
  },
  {
    "{": ""      ""Video ID: DaIZB7cIyHA""
  },
  {
    "{": ""      ""Video ID: 12bT7ZdEsdc""
  },
  {
    "{": ""      ""Video ID: 3AA9yp4r_Rk""
  },
  {
    "{": ""      ""Video ID: HVRzClouH00""
  },
  {
    "{": ""      ""Video ID: ycUq1c9p9Dk""
  },
  {
    "{": ""      ""Video ID: NyrLQ17AOsg""
  },
  {
    "{": ""      ""Video ID: bd-xhM0r1mQ""
  },
  {
    "{": ""      ""Video ID: MApmcen13LU""
  },
  {
    "{": ""      ""Video ID: uvNPQ9YwkSg""
  },
  {
    "{": ""      ""Video ID: Yh0xahfip7w""
  },
  {
    "{": ""      ""Video ID: LJJMspXle3w""
  },
  {
    "{": ""      ""Video ID: IaytO_wPoPI""
  },
  {
    "{": ""      ""Video ID: fS1HfGPrXLs""
  },
  {
    "{": ""      ""Video ID: qDhk8m93GhA""
  },
  {
    "{": ""      ""Video ID: wA4inMj2mww""
  },
  {
    "{": ""      ""Video ID: XgGm98KFcfo""
  },
  {
    "{": ""      ""Video ID: fmzKbdQ37xA""
  },
  {
    "{": ""      ""Video ID: PwUTfzkk70Q""
  },
  {
    "{": ""      ""Video ID: 7s0wQszVGPE""
  },
  {
    "{": ""      ""Video ID: rr9ulBiCPQE""
  },
  {
    "{": ""      ""Video ID: cWZ0mS_R5as""
  },
  {
    "{": ""      ""Video ID: 4v2wF6JuUbA""
  },
  {
    "{": ""      ""Video ID: WB_nrW01EHw""
  },
  {
    "{": ""      ""Video ID: OwL0MLuEZGU""
  },
  {
    "{": ""      ""Video ID: 9r0XGXvi6O8""
  },
  {
    "{": ""      ""Video ID: spldjKFXjbM""
  },
  {
    "{": ""      ""Video ID: 1EXA2oEzGZY""
  },
  {
    "{": ""      ""Video ID: 3O4lVqanAF8""
  },
  {
    "{": ""      ""Video ID: PRRtfQKzYxE""
  },
  {
    "{": ""      ""Video ID: JWi5a0_27cM""
  },
  {
    "{": ""      ""Video ID: rNr9bg5cuJs""
  },
  {
    "{": ""      ""Video ID: 3GBRgOodbO0""
  },
  {
    "{": ""      ""Video ID: IG6wgKojMMs""
  },
  {
    "{": ""      ""Video ID: o58kWLBO-ik""
  },
  {
    "{": ""      ""Video ID: IASzpztq84Q""
  },
  {
    "{": ""      ""Video ID: TUOxn4-gSYU""
  },
  {
    "{": ""      ""Video ID: Ubs6r9vKZe4""
  },
  {
    "{": ""      ""Video ID: LOdM-RbWgi4""
  },
  {
    "{": ""      ""Video ID: vwhoQXFCcDQ""
  },
  {
    "{": ""      ""Video ID: yUtyfF71UDI""
  },
  {
    "{": ""      ""Video ID: pTpYBuD4p-0""
  },
  {
    "{": ""      ""Video ID: B_XQqa-u85M""
  },
  {
    "{": ""      ""Video ID: m3u-YeH52Yk""
  },
  {
    "{": ""      ""Video ID: idhHq1mn1XA""
  },
  {
    "{": ""      ""Video ID: ij_gvHI3cNQ""
  },
  {
    "{": ""      ""Video ID: xDeyGqkC82I""
  },
  {
    "{": ""      ""Video ID: TLW2MHqkQ3g""
  },
  {
    "{": ""      ""Video ID: n3PhmxfJPa0""
  },
  {
    "{": ""      ""Video ID: df2fIpewVfM""
  },
  {
    "{": ""      ""Video ID: uDjlxqt1FZk""
  },
  {
    "{": ""      ""Video ID: xCturRlrFL0""
  },
  {
    "{": ""      ""Video ID: Yxp9n89EgjY""
  },
  {
    "{": ""      ""Video ID: BcPIO-jvdMg""
  },
  {
    "{": ""      ""Video ID: jb6GoqdMHDw""
  },
  {
    "{": ""      ""Video ID: l-I0rYReldY""
  },
  {
    "{": ""      ""Video ID: x8d_ij33Gyk""
  },
  {
    "{": ""      ""Video ID: qSvyNXycwSw""
  },
  {
    "{": ""      ""Video ID: ExKKNtkTQGM""
  },
  {
    "{": ""      ""Video ID: zrnkhiPKSRk""
  },
  {
    "{": ""      ""Video ID: KGJOaMVT-ww""
  },
  {
    "{": ""      ""Video ID: 3uah3gutsCY""
  },
  {
    "{": ""      ""Video ID: Kz_rFbxJuuM""
  },
  {
    "{": ""      ""Video ID: dTXF3CfGyks""
  },
  {
    "{": ""      ""Video ID: bbinL-ER1oQ""
  },
  {
    "{": ""      ""Video ID: S2YiZ8vVyCI""
  },
  {
    "{": ""      ""Video ID: XVbiIzXbzLI""
  },
  {
    "{": ""      ""Video ID: hxDg6e5sp4M""
  },
  {
    "{": ""      ""Video ID: WFb9ST3SkZw""
  },
  {
    "{": ""      ""Video ID: w5xjCbUDOf4""
  },
  {
    "{": ""      ""Video ID: fIGu1e7foxw""
  },
  {
    "{": ""      ""Video ID: A8E7IjYu0Iw""
  },
  {
    "{": ""      ""Video ID: FAT-Fbhl3t4""
  },
  {
    "{": ""      ""Video ID: 4a8UFps40-U""
  },
  {
    "{": ""      ""Video ID: VuPjI7S3Aa8""
  },
  {
    "{": ""      ""Video ID: rlGAOmLK7i4""
  },
  {
    "{": ""      ""Video ID: 1fag_o6Kf08""
  },
  {
    "{": ""      ""Video ID: fsuFVc39p00""
  },
  {
    "{": ""      ""Video ID: ggNkSlWrcbU""
  },
  {
    "{": ""      ""Video ID: An-ajUOcRmY""
  },
  {
    "{": ""      ""Video ID: h0oPCW_WI2M""
  },
  {
    "{": ""      ""Video ID: -0_EL5F5DwE""
  },
  {
    "{": ""      ""Video ID: 6ZgPmvvn45A""
  },
  {
    "{": ""      ""Video ID: DIEMdmaKWus""
  },
  {
    "{": ""      ""Video ID: lff9fzcddS4""
  },
  {
    "{": ""      ""Video ID: HX5Yedr1rpM""
  },
  {
    "{": ""      ""Video ID: ILVEVK3TcEs""
  },
  {
    "{": ""      ""Video ID: 2DXKNRqnymk""
  },
  {
    "{": ""      ""Video ID: YFlVQPRtp1I""
  },
  {
    "{": ""      ""Video ID: 2f8DpbDbyXA""
  },
  {
    "{": ""      ""Video ID: szEKorDfphM""
  },
  {
    "{": ""      ""Video ID: valnyoEW9-k""
  },
  {
    "{": ""      ""Video ID: Zodf6_YGujo""
  },
  {
    "{": ""      ""Video ID: UcKqyn-gUbY""
  },
  {
    "{": ""      ""Video ID: RWfntZibC1M""
  },
  {
    "{": ""      ""Video ID: Zxk_WywMTzc""
  },
  {
    "{": ""      ""Video ID: -8zmgBIiB2I""
  },
  {
    "{": ""      ""Video ID: yei0NMqUaZ8""
  },
  {
    "{": ""      ""Video ID: 0-eKPs_xPtE""
  },
  {
    "{": ""      ""Video ID: qgnx8Kkl0xo""
  },
  {
    "{": ""      ""Video ID: gpK4iU6-8HM""
  },
  {
    "{": ""      ""Video ID: XuvDzv16NKg""
  },
  {
    "{": ""      ""Video ID: 9r2hihu9m4Q""
  },
  {
    "{": ""      ""Video ID: _OpDa48q5m0""
  },
  {
    "{": ""      ""Video ID: Ddr_bP_784A""
  },
  {
    "{": ""      ""Video ID: RA_Q7xAS4GY""
  },
  {
    "{": ""      ""Video ID: iT044ty7Kqw""
  },
  {
    "{": ""      ""Video ID: ftSFqkPIKOI""
  },
  {
    "{": ""      ""Video ID: FGHrEepL8NU""
  },
  {
    "{": ""      ""Video ID: e1HpYkGDM6g""
  },
  {
    "{": ""      ""Video ID: O4kDC4sZ5Jg""
  },
  {
    "{": ""      ""Video ID: MLJPIQNRYW0""
  },
  {
    "{": ""      ""Video ID: eqSOlUW8BI8""
  },
  {
    "{": ""      ""Video ID: M0OXtJk4YI8""
  },
  {
    "{": ""      ""Video ID: FrFdndWjz9w""
  },
  {
    "{": ""      ""Video ID: s_LQOW_sj1E""
  },
  {
    "{": ""      ""Video ID: TlKW6FNf0q4""
  },
  {
    "{": ""      ""Video ID: H8YpBIScJSM""
  },
  {
    "{": ""      ""Video ID: us7YB7eiOeQ""
  },
  {
    "{": ""      ""Video ID: GVV8tvE-B7E""
  },
  {
    "{": ""      ""Video ID: xGzr_hlKcsg""
  },
  {
    "{": ""      ""Video ID: H2t0lF_5oeo""
  },
  {
    "{": ""      ""Video ID: 4kShkZLfooY""
  },
  {
    "{": ""      ""Video ID: ZIbE646cdlg""
  },
  {
    "{": ""      ""Video ID: QhrVXur0Q-o""
  },
  {
    "{": ""      ""Video ID: Y_YH1DTpWec""
  },
  {
    "{": ""      ""Video ID: SV29FnEBx4o""
  },
  {
    "{": ""      ""Video ID: 2sD0Bwg5Dic""
  },
  {
    "{": ""      ""Video ID: hvq65ZLl75M""
  },
  {
    "{": ""      ""Video ID: 770NROWOInw""
  },
  {
    "{": ""      ""Video ID: LPALtHcwtSw""
  },
  {
    "{": ""      ""Video ID: 1x6ffnxL_SI""
  },
  {
    "{": ""      ""Video ID: 4SpuJOCCl9E""
  },
  {
    "{": ""      ""Video ID: m2laDUYtO4g""
  },
  {
    "{": ""      ""Video ID: rTK7oxG2Q-8""
  },
  {
    "{": ""      ""Video ID: M4mUUyUCcyU""
  },
  {
    "{": ""      ""Video ID: 9b_BwtoUK3o""
  },
  {
    "{": ""      ""Video ID: gsanzcCxxAk""
  },
  {
    "{": ""      ""Video ID: vvC_DNrCxMY""
  },
  {
    "{": ""      ""Video ID: -WLSBBcYG4E""
  },
  {
    "{": ""      ""Video ID: q7MDdYj9YAc""
  },
  {
    "{": ""      ""Video ID: Qma6XJ3IfQk""
  },
  {
    "{": ""      ""Video ID: xlGu51uqNgQ""
  },
  {
    "{": ""      ""Video ID: sflJel9ye7Q""
  },
  {
    "{": ""      ""Video ID: ww7SnmoIONM""
  },
  {
    "{": ""      ""Video ID: QsmiIeAkE-o""
  },
  {
    "{": ""      ""Video ID: 1CPRgWSvg_k""
  },
  {
    "{": ""      ""Video ID: TjmOK4TTvwg""
  },
  {
    "{": ""      ""Video ID: 8PKndk7vu-E""
  },
  {
    "{": ""      ""Video ID: l5LDwyWa3X8""
  },
  {
    "{": ""      ""Video ID: Ep3CRtzAM_E""
  },
  {
    "{": ""      ""Video ID: IpwaTJiLXzM""
  },
  {
    "{": ""      ""Video ID: 97CMSfwdfHo""
  },
  {
    "{": ""      ""Video ID: ZqdsVT1SWlo""
  },
  {
    "{": ""      ""Video ID: 6QV3msZ6b_8""
  },
  {
    "{": ""      ""Video ID: vETU61daXY8""
  },
  {
    "{": ""      ""Video ID: vGEtEJGHJnw""
  },
  {
    "{": ""      ""Video ID: iU8KwWH9z1I""
  },
  {
    "{": ""      ""Video ID: tPYbwaZsSFg""
  },
  {
    "{": ""      ""Video ID: iZdkYX2Mni8""
  },
  {
    "{": ""      ""Video ID: kYFE1-KsrDs""
  },
  {
    "{": ""      ""Video ID: mgr4SbZKF1k""
  },
  {
    "{": ""      ""Video ID: bqg_ceFM30I""
  },
  {
    "{": ""      ""Video ID: nOKKSU2bFEo""
  },
  {
    "{": ""      ""Video ID: 0VZjE6P-E0o""
  },
  {
    "{": ""      ""Video ID: kN0SVBCJqLs""
  },
  {
    "{": ""      ""Video ID: ujOuO30h9kQ""
  },
  {
    "{": ""      ""Video ID: ik_PBFdDpF0""
  },
  {
    "{": ""      ""Video ID: raoXIRbPWuo""
  },
  {
    "{": ""      ""Video ID: s4TBAahdClU""
  },
  {
    "{": ""      ""Video ID: VZF5n0giVb0""
  },
  {
    "{": ""      ""Video ID: zJMouHGpK20""
  },
  {
    "{": ""      ""Video ID: f3O5bAKi0n8""
  },
  {
    "{": ""      ""Video ID: FYNSjxHsW2o""
  },
  {
    "{": ""      ""Video ID: -6Av5wattko""
  },
  {
    "{": ""      ""Video ID: UdLadvHjmmE""
  },
  {
    "{": ""      ""Video ID: QaH-sYFsP0o""
  },
  {
    "{": ""      ""Video ID: 5-ziuuvbbGk""
  },
  {
    "{": ""      ""Video ID: enRzksGXG1c""
  },
  {
    "{": ""      ""Video ID: Eq0LzDFyvTo""
  },
  {
    "{": ""      ""Video ID: 8xzFEnOQRpI""
  },
  {
    "{": ""      ""Video ID: -iI61dd7IxI""
  },
  {
    "{": ""      ""Video ID: dmZbOPtEotI""
  },
  {
    "{": ""      ""Video ID: 1vSt27lMlDI""
  },
  {
    "{": ""      ""Video ID: s-v4P7zKOf0""
  },
  {
    "{": ""      ""Video ID: oVyjLeVeaYI""
  },
  {
    "{": ""      ""Video ID: jWSrmgDN6Ao""
  },
  {
    "{": ""      ""Video ID: JXhZQ6jhxs0""
  },
  {
    "{": ""      ""Video ID: C72HNAsnCgg""
  },
  {
    "{": ""      ""Video ID: R66OJPMxLQE""
  },
  {
    "{": ""      ""Video ID: KN-pYyU9a7A""
  },
  {
    "{": ""      ""Video ID: TyZpeEjj18Q""
  },
  {
    "{": ""      ""Video ID: fHnY-MOpPEM""
  },
  {
    "{": ""      ""Video ID: 6gh8soXbZk0""
  },
  {
    "{": ""      ""Video ID: 6Ga0yvasaJg""
  },
  {
    "{": ""      ""Video ID: X_IbFDVGELk""
  },
  {
    "{": ""      ""Video ID: f8Edek8rZtI""
  },
  {
    "{": ""      ""Video ID: 4Hcs8wCCyIo""
  },
  {
    "{": ""      ""Video ID: bvcZMzJe_fQ""
  },
  {
    "{": ""      ""Video ID: xdyjxaM27_k""
  },
  {
    "{": ""      ""Video ID: M3Lc0OcadPs""
  },
  {
    "{": ""      ""Video ID: Tv13kzR4wBU""
  },
  {
    "{": ""      ""Video ID: 5jVDumAM5_Q""
  },
  {
    "{": ""      ""Video ID: I04GGND3bNg""
  },
  {
    "{": ""      ""Video ID: 1jdcXE0Jmvo""
  },
  {
    "{": ""      ""Video ID: 2VQxDkrXeWI""
  },
  {
    "{": ""      ""Video ID: FMjLotOuLaY""
  },
  {
    "{": ""      ""Video ID: 9cNjTYsy_1E""
  },
  {
    "{": ""      ""Video ID: bXdtPEwQGCU""
  },
  {
    "{": ""      ""Video ID: W8cdaUgXbrU""
  },
  {
    "{": ""      ""Video ID: hpDabBFf3vk""
  },
  {
    "{": ""      ""Video ID: xmuIkJtL42g""
  },
  {
    "{": ""      ""Video ID: Kn90uvj9Pgw""
  },
  {
    "{": ""      ""Video ID: Ah-SLuwkKik""
  },
  {
    "{": ""      ""Video ID: Rqqaw9iN0Js""
  },
  {
    "{": ""      ""Video ID: jE80W5xYbTI""
  },
  {
    "{": ""      ""Video ID: 475_Zzixj5M""
  },
  {
    "{": ""      ""Video ID: zAG-kX_IlUw""
  },
  {
    "{": ""      ""Video ID: k4PEV_TYFDc""
  },
  {
    "{": ""      ""Video ID: 31QQ1gNpAaY""
  },
  {
    "{": ""      ""Video ID: MRvwVSaMBRc""
  },
  {
    "{": ""      ""Video ID: SHoDKldosXk""
  },
  {
    "{": ""      ""Video ID: Yq7tnNdaP88""
  },
  {
    "{": ""      ""Video ID: w8vL2RQ_ZJM""
  },
  {
    "{": ""      ""Video ID: 5Ib9L47osgY""
  },
  {
    "{": ""      ""Video ID: 95Bdb9y6Qog""
  },
  {
    "{": ""      ""Video ID: 97ZNMhNiwyQ""
  },
  {
    "{": ""      ""Video ID: xO0gSJGJ7Fs""
  },
  {
    "{": ""      ""Video ID: D1GqJX2u5gU""
  },
  {
    "{": ""      ""Video ID: Eo-hZPQN2NU""
  },
  {
    "{": ""      ""Video ID: sVvtIS2YGVI""
  },
  {
    "{": ""      ""Video ID: K82boqdinzQ""
  },
  {
    "{": ""      ""Video ID: pogGN7yPdP8""
  },
  {
    "{": ""      ""Video ID: 26L0jdrUlNo""
  },
  {
    "{": ""      ""Video ID: b_ZWOFqH0Rk""
  },
  {
    "{": ""      ""Video ID: 4xtksN8RIq8""
  },
  {
    "{": ""      ""Video ID: qwiE9GZVClk""
  },
  {
    "{": ""      ""Video ID: oILT-J3Twt8""
  },
  {
    "{": ""      ""Video ID: wZ4ren19Y74""
  },
  {
    "{": ""      ""Video ID: wWOGMKQ1aHo""
  },
  {
    "{": ""      ""Video ID: _pECNTuKi7w""
  },
  {
    "{": ""      ""Video ID: UXDoL14Q2YE""
  },
  {
    "{": ""      ""Video ID: NqVQ3NPdIX4""
  },
  {
    "{": ""      ""Video ID: 47NxXROfKRc""
  },
  {
    "{": ""      ""Video ID: RV4L6nmvPzQ""
  },
  {
    "{": ""      ""Video ID: 9Y5wMXd4ZxA""
  },
  {
    "{": ""      ""Video ID: Jj0NPLHoP_U""
  },
  {
    "{": ""      ""Video ID: lc6uZs8ddnI""
  },
  {
    "{": ""      ""Video ID: t7d0Z3Y62WA""
  },
  {
    "{": ""      ""Video ID: v7y-gloYUaw""
  },
  {
    "{": ""      ""Video ID: h4dJnh-8oSs""
  },
  {
    "{": ""      ""Video ID: OIizBF4fe3w""
  },
  {
    "{": ""      ""Video ID: DQoAXOUNFrw""
  },
  {
    "{": ""      ""Video ID: zYCq8R08Yvk""
  },
  {
    "{": ""      ""Video ID: fPp2S0Jf_f8""
  },
  {
    "{": ""      ""Video ID: yQXMfBJ1Zis""
  },
  {
    "{": ""      ""Video ID: EE5El41gnpk""
  },
  {
    "{": ""      ""Video ID: cTPhis2W1MM""
  },
  {
    "{": ""      ""Video ID: LRom3fMug8I""
  },
  {
    "{": ""      ""Video ID: 1-QW5Fkvijc""
  },
  {
    "{": ""      ""Video ID: mjweB5P3KdU""
  },
  {
    "{": ""      ""Video ID: youm845zkS0""
  },
  {
    "{": ""      ""Video ID: zsmlXF1MQ3A""
  },
  {
    "{": ""      ""Video ID: W1t_vYb0SJI""
  },
  {
    "{": ""      ""Video ID: jHq0i2Dwujg""
  },
  {
    "{": ""      ""Video ID: nFrcPgyRG9w""
  },
  {
    "{": ""      ""Video ID: sFUbsFQiLBE""
  },
  {
    "{": ""      ""Video ID: HPgIvqx9ZO0""
  },
  {
    "{": ""      ""Video ID: NrewpOyt5KE""
  },
  {
    "{": ""      ""Video ID: mU9hU6LHkHg""
  },
  {
    "{": ""      ""Video ID: FR3ZHEoWtVg""
  },
  {
    "{": ""      ""Video ID: nzULIAibvEk""
  },
  {
    "{": ""      ""Video ID: B-mKd2WY7-M""
  },
  {
    "{": ""      ""Video ID: q4QZ58V9AtM""
  },
  {
    "{": ""      ""Video ID: QWR5fAu76GI""
  },
  {
    "{": ""      ""Video ID: SIFa7vTfins""
  },
  {
    "{": ""      ""Video ID: rM0jhhk3MZc""
  },
  {
    "{": ""      ""Video ID: x1JxRYql7O0""
  },
  {
    "{": ""      ""Video ID: 5yH2_3MYR0U""
  },
  {
    "{": ""      ""Video ID: YCeou0ZrS08""
  },
  {
    "{": ""      ""Video ID: tuzHuZi17NI""
  },
  {
    "{": ""      ""Video ID: rxgUEJm296w""
  },
  {
    "{": ""      ""Video ID: USzTcRKohx0""
  },
  {
    "{": ""      ""Video ID: IxVnzwmgs9A""
  },
  {
    "{": ""      ""Video ID: V9YXU-RhbL0""
  },
  {
    "{": ""      ""Video ID: zPij7fyIiUQ""
  },
  {
    "{": ""      ""Video ID: _-FTUfH4BPA""
  },
  {
    "{": ""      ""Video ID: n9ipTkin2sY""
  },
  {
    "{": ""      ""Video ID: EAvhv7GGamI""
  },
  {
    "{": ""      ""Video ID: -EnXxXEhEbk""
  },
  {
    "{": ""      ""Video ID: TC-I4fMwXpI""
  },
  {
    "{": ""      ""Video ID: IOl8MwR4Kkg""
  },
  {
    "{": ""      ""Video ID: TPoRS1_sI54""
  },
  {
    "{": ""      ""Video ID: EbnmjKjD5k0""
  },
  {
    "{": ""      ""Video ID: pN49GfdXpbs""
  },
  {
    "{": ""      ""Video ID: gAL0wzwtRIs""
  },
  {
    "{": ""      ""Video ID: GUkBc1vQAWA""
  },
  {
    "{": ""      ""Video ID: -Atbc1sy4gA""
  },
  {
    "{": ""      ""Video ID: 3rmYr-xjYb0""
  },
  {
    "{": ""      ""Video ID: _6WVRrMY32c""
  },
  {
    "{": ""      ""Video ID: -pBlggPbPR4""
  },
  {
    "{": ""      ""Video ID: SGozAlMe3Fk""
  },
  {
    "{": ""      ""Video ID: rVnfPA2NB3Q""
  },
  {
    "{": ""      ""Video ID: qzRIVVcV4rQ""
  },
  {
    "{": ""      ""Video ID: 2KDCwtk-Oac""
  },
  {
    "{": ""      ""Video ID: XhjpiarRfiM""
  },
  {
    "{": ""      ""Video ID: R5pW12TAzio""
  },
  {
    "{": ""      ""Video ID: R4AjcelCV4o""
  },
  {
    "{": ""      ""Video ID: v_a3N0mx8zE""
  },
  {
    "{": ""      ""Video ID: 9TbgvL9Zyac""
  },
  {
    "{": ""      ""Video ID: LGa6E95u66Q""
  },
  {
    "{": ""      ""Video ID: uY1oRj6opt8""
  },
  {
    "{": ""      ""Video ID: 4w5mavA-g-o""
  },
  {
    "{": ""      ""Video ID: utn3bV0mHC4""
  },
  {
    "{": ""      ""Video ID: tvv4VAPUZT4""
  },
  {
    "{": ""      ""Video ID: Yiwp6jThiOc""
  },
  {
    "{": ""      ""Video ID: ltYSMNsun2E""
  },
  {
    "{": ""      ""Video ID: y_XtdtlrKT4""
  },
  {
    "{": ""      ""Video ID: -mlcfjUEXXw""
  },
  {
    "{": ""      ""Video ID: miHJUIQ1UK8""
  },
  {
    "{": ""      ""Video ID: 93jh4DEyd7I""
  },
  {
    "{": ""      ""Video ID: J6LnvnoEZ94""
  },
  {
    "{": ""      ""Video ID: sMSS1b250j8""
  },
  {
    "{": ""      ""Video ID: 8v1_6iFAHws""
  },
  {
    "{": ""      ""Video ID: Ll83CT-Lmdk""
  },
  {
    "{": ""      ""Video ID: 4yndReNRrRY""
  },
  {
    "{": ""      ""Video ID: pQ8uPJnf6Ww""
  },
  {
    "{": ""      ""Video ID: 1_bthMflRhU""
  },
  {
    "{": ""      ""Video ID: IsJNGRZK8N0""
  },
  {
    "{": ""      ""Video ID: lYOxeXSvhXQ""
  },
  {
    "{": ""      ""Video ID: XBrgtZUBUQE""
  },
  {
    "{": ""      ""Video ID: xcDYlLyubcQ""
  },
  {
    "{": ""      ""Video ID: Mg-GZWzUsY4""
  },
  {
    "{": ""      ""Video ID: j51K6ca5cd4""
  },
  {
    "{": ""      ""Video ID: AocOpFKCLTw""
  },
  {
    "{": ""      ""Video ID: sHNbae7-Q5E""
  },
  {
    "{": ""      ""Video ID: DIr2MCD2VoY""
  },
  {
    "{": ""      ""Video ID: h48KiQFJ1Wo""
  },
  {
    "{": ""      ""Video ID: DQYgFw7RgEQ""
  },
  {
    "{": ""      ""Video ID: M2Ltn1hazrI""
  },
  {
    "{": ""      ""Video ID: WCxxXCckX-U""
  },
  {
    "{": ""      ""Video ID: vP4f95AK8L4""
  },
  {
    "{": ""      ""Video ID: cGN0Uy9Env8""
  },
  {
    "{": ""      ""Video ID: HMyn7ZqkTlY""
  },
  {
    "{": ""      ""Video ID: lv4Potdpjhw""
  },
  {
    "{": ""      ""Video ID: Wl-m6V--jJM""
  },
  {
    "{": ""      ""Video ID: ZKSOyL1zz9o""
  },
  {
    "{": ""      ""Video ID: -z3tfSqdgO8""
  },
  {
    "{": ""      ""Video ID: iTnENYzmYdk""
  },
  {
    "{": ""      ""Video ID: K-mGQ0-ATo4""
  },
  {
    "{": ""      ""Video ID: y37MVtnFaR0""
  },
  {
    "{": ""      ""Video ID: jTMgbCFmKiY""
  },
  {
    "{": ""      ""Video ID: d77ipeCxLPM""
  },
  {
    "{": ""      ""Video ID: zpLS_rT7n1s""
  },
  {
    "{": ""      ""Video ID: IkgEO5rxUKo""
  },
  {
    "{": ""      ""Video ID: LyuFbhbZ7Wo""
  },
  {
    "{": ""      ""Video ID: Cwx9Gazxy2Q""
  },
  {
    "{": ""      ""Video ID: wP6SUQ-qBks""
  },
  {
    "{": ""      ""Video ID: gmY37dTpInM""
  },
  {
    "{": ""      ""Video ID: 6_ZxldeB43M""
  },
  {
    "{": ""      ""Video ID: s5FPuqhKFeo""
  },
  {
    "{": ""      ""Video ID: -eU5VMcZqfo""
  },
  {
    "{": ""      ""Video ID: FBykGza6Mt8""
  },
  {
    "{": ""      ""Video ID: 30u1d26jeH0""
  },
  {
    "{": ""      ""Video ID: d3tQXTlAtAQ""
  },
  {
    "{": ""      ""Video ID: DLnSphQ88_w""
  },
  {
    "{": ""      ""Video ID: bmczczTsD9w""
  },
  {
    "{": ""      ""Video ID: hSfN6dGHuho""
  },
  {
    "{": ""      ""Video ID: D4Im2xohBUs""
  },
  {
    "{": ""      ""Video ID: 0nji4Uge3rU""
  },
  {
    "{": ""      ""Video ID: 0bRa8M1-hqw""
  },
  {
    "{": ""      ""Video ID: FmCJMq3z03Y""
  },
  {
    "{": ""      ""Video ID: QfXPqYBvEeE""
  },
  {
    "{": ""      ""Video ID: Hb28XIElvt0""
  },
  {
    "{": ""      ""Video ID: ET0MqER_mPA""
  },
  {
    "{": ""      ""Video ID: Lzn5AjcMOvM""
  },
  {
    "{": ""      ""Video ID: FDheALX9SBM""
  },
  {
    "{": ""      ""Video ID: 5u0tD8x9zyA""
  },
  {
    "{": ""      ""Video ID: n8HYtVU3K00""
  },
  {
    "{": ""      ""Video ID: ZbBnJs0AWEk""
  },
  {
    "{": ""      ""Video ID: FdiSOYNQpfc""
  },
  {
    "{": ""      ""Video ID: aWe_fdVoDU0""
  },
  {
    "{": ""      ""Video ID: HF3NMGHVqKA""
  },
  {
    "{": ""      ""Video ID: KnKu_xH8KWA""
  },
  {
    "{": ""      ""Video ID: u1U1TfxG4So""
  },
  {
    "{": ""      ""Video ID: U1KY53bebL8""
  },
  {
    "{": ""      ""Video ID: f3Ri_leWazQ""
  },
  {
    "{": ""      ""Video ID: EalyADT5Rlw""
  },
  {
    "{": ""      ""Video ID: 1bXdKTDAa_s""
  },
  {
    "{": ""      ""Video ID: NXpTSModbDI""
  },
  {
    "{": ""      ""Video ID: ntgIa5QRjU8""
  },
  {
    "{": ""      ""Video ID: Llt2dY25yug""
  },
  {
    "{": ""      ""Video ID: -SXIRZkGD8k""
  },
  {
    "{": ""      ""Video ID: 2uXeC39ut_8""
  },
  {
    "{": ""      ""Video ID: maBa5Hgd3XA""
  },
  {
    "{": ""      ""Video ID: CulbDhmptTM""
  },
  {
    "{": ""      ""Video ID: MuXK1nr9_jg""
  },
  {
    "{": ""      ""Video ID: A3kQKzR7SA0""
  },
  {
    "{": ""      ""Video ID: 8oGWOV59vQg""
  },
  {
    "{": ""      ""Video ID: pu3FwgIHsQA""
  },
  {
    "{": ""      ""Video ID: WS0GGC_LD2U""
  },
  {
    "{": ""      ""Video ID: onkMOtggfpM""
  },
  {
    "{": ""      ""Video ID: mZGh5cCiEF8""
  },
  {
    "{": ""      ""Video ID: x9te7QwhmMk""
  },
  {
    "{": ""      ""Video ID: 5YIPNEBbYjw""
  },
  {
    "{": ""      ""Video ID: OLd2SjpJJ_w""
  },
  {
    "{": ""      ""Video ID: 8MYxfp72644""
  },
  {
    "{": ""      ""Video ID: B8lWJ0SSsew""
  },
  {
    "{": ""      ""Video ID: t0DfBsJfEGw""
  },
  {
    "{": ""      ""Video ID: Esgyv8ynk_c""
  },
  {
    "{": ""      ""Video ID: L8FlHalmlgk""
  },
  {
    "{": ""      ""Video ID: 0tmZCn9LkGI""
  },
  {
    "{": ""      ""Video ID: 3w9bJlUOEXs""
  },
  {
    "{": ""      ""Video ID: KI2aidI-ZMo""
  },
  {
    "{": ""      ""Video ID: a-7lVKY4PY0""
  },
  {
    "{": ""      ""Video ID: HgA1iP5cfRw""
  },
  {
    "{": ""      ""Video ID: T5Yn0WdmCFY""
  },
  {
    "{": ""      ""Video ID: 9CaL5NslOxE""
  },
  {
    "{": ""      ""Video ID: h7befTC5CoM""
  },
  {
    "{": ""      ""Video ID: 3G4KnhYuWD8""
  },
  {
    "{": ""      ""Video ID: -FeAK-q5Cok""
  },
  {
    "{": ""      ""Video ID: q5Kr7PBTqKQ""
  },
  {
    "{": ""      ""Video ID: I7p7TRwdgXs""
  },
  {
    "{": ""      ""Video ID: 8BWbVrbi-ZY""
  },
  {
    "{": ""      ""Video ID: eqbpfBB6_HE""
  },
  {
    "{": ""      ""Video ID: XSFEpKU9MB4""
  },
  {
    "{": ""      ""Video ID: gpfy9ZmkvMg""
  },
  {
    "{": ""      ""Video ID: ZctsM8xHvGY""
  },
  {
    "{": ""      ""Video ID: PGxbewgsKzs""
  },
  {
    "{": ""      ""Video ID: dxG9AwiWwT8""
  },
  {
    "{": ""      ""Video ID: WW4-68uY9w4""
  },
  {
    "{": ""      ""Video ID: mP2qOHzUqDM""
  },
  {
    "{": ""      ""Video ID: f5Vn_iHhX3A""
  },
  {
    "{": ""      ""Video ID: H7FDFq927TA""
  },
  {
    "{": ""      ""Video ID: ZygKc4D63q4""
  },
  {
    "{": ""      ""Video ID: GC2uRE0Khyc""
  },
  {
    "{": ""      ""Video ID: UYx6SBPZawo""
  },
  {
    "{": ""      ""Video ID: fXN9OOC639E""
  },
  {
    "{": ""      ""Video ID: zZhiM2mSuiI""
  },
  {
    "{": ""      ""Video ID: iRT7fpO00ys""
  },
  {
    "{": ""      ""Video ID: MJheuVMVvyo""
  },
  {
    "{": ""      ""Video ID: LVetaw8SMZs""
  },
  {
    "{": ""      ""Video ID: vPlp-5yqMT8""
  },
  {
    "{": ""      ""Video ID: x2wrHoM5yks""
  },
  {
    "{": ""      ""Video ID: rFW8zH1BOxo""
  },
  {
    "{": ""      ""Video ID: 5rPa5X0DWAI""
  },
  {
    "{": ""      ""Video ID: ax3oPkRqGM8""
  },
  {
    "{": ""      ""Video ID: JTUJ6vV2VSo""
  },
  {
    "{": ""      ""Video ID: b7c7ATeTMJU""
  },
  {
    "{": ""      ""Video ID: 8J-7ASEidrI""
  },
  {
    "{": ""      ""Video ID: Q8Ae6-rjiMQ""
  },
  {
    "{": ""      ""Video ID: GKX2qPvJr-U""
  },
  {
    "{": ""      ""Video ID: m584z5aE4Uc""
  },
  {
    "{": ""      ""Video ID: Twy_f_4AwHg""
  },
  {
    "{": ""      ""Video ID: zaJKAwnj1jo""
  },
  {
    "{": ""      ""Video ID: JZbwXF6uSrw""
  },
  {
    "{": ""      ""Video ID: 6zJI2OFCEWo""
  },
  {
    "{": ""      ""Video ID: YRxJWQtq9S4""
  },
  {
    "{": ""      ""Video ID: Xew4nAc_bow""
  },
  {
    "{": ""      ""Video ID: p22AbInOj5g""
  },
  {
    "{": ""      ""Video ID: OEa821YE9Cw""
  },
  {
    "{": ""      ""Video ID: svOMkO1ypA0""
  },
  {
    "{": ""      ""Video ID: oXjCV6Rra7U""
  },
  {
    "{": ""      ""Video ID: vW62EilDXPY""
  },
  {
    "{": ""      ""Video ID: AcMHZNT_uy0""
  },
  {
    "{": ""      ""Video ID: xsP3LihTjAk""
  },
  {
    "{": ""      ""Video ID: PCrU1yenwCM""
  },
  {
    "{": ""      ""Video ID: UGpxfoF3SYg""
  },
  {
    "{": ""      ""Video ID: AFVwXzaleTg""
  },
  {
    "{": ""      ""Video ID: jxKc9aTLbAg""
  },
  {
    "{": ""      ""Video ID: v_dVkh7v0KA""
  },
  {
    "{": ""      ""Video ID: _XI0IoWanSA""
  },
  {
    "{": ""      ""Video ID: 2SrrHV7Hrbw""
  },
  {
    "{": ""      ""Video ID: eL9YWGG_840""
  },
  {
    "{": ""      ""Video ID: Ovaxmo26VeE""
  },
  {
    "{": ""      ""Video ID: SADGwaGz0Ec""
  },
  {
    "{": ""      ""Video ID: k4MFNguvsp8""
  },
  {
    "{": ""      ""Video ID: UnR9Isj-4z0""
  },
  {
    "{": ""      ""Video ID: GibAdE3186k""
  },
  {
    "{": ""      ""Video ID: erYSqpfbg9U""
  },
  {
    "{": ""      ""Video ID: NqXgSTCYpfA""
  },
  {
    "{": ""      ""Video ID: qMMSealOPSY""
  },
  {
    "{": ""      ""Video ID: DIPBIdg_3Z0""
  },
  {
    "{": ""      ""Video ID: hR7u_PKtZ5w""
  },
  {
    "{": ""      ""Video ID: i-VxDa-9tdM""
  },
  {
    "{": ""      ""Video ID: CN4X-OI1Z1U""
  },
  {
    "{": ""      ""Video ID: 5L2Igd6uCrA""
  },
  {
    "{": ""      ""Video ID: T2rlX0rF2oE""
  },
  {
    "{": ""      ""Video ID: bfpqcwG5L0I""
  },
  {
    "{": ""      ""Video ID: Up_aNfylKYg""
  },
  {
    "{": ""      ""Video ID: wjVlmB2uPKU""
  },
  {
    "{": ""      ""Video ID: svL1GuxxpvA""
  },
  {
    "{": ""      ""Video ID: FFC_x0vOc8o""
  },
  {
    "{": ""      ""Video ID: iM392KMpfmA""
  },
  {
    "{": ""      ""Video ID: xfzolk7FRXk""
  },
  {
    "{": ""      ""Video ID: KEwNPrDst3c""
  },
  {
    "{": ""      ""Video ID: mC70NvYiSm0""
  },
  {
    "{": ""      ""Video ID: ZcD80u-4kqI""
  },
  {
    "{": ""      ""Video ID: ipkNE_1kWQ4""
  },
  {
    "{": ""      ""Video ID: VeQqYbY3S5c""
  },
  {
    "{": ""      ""Video ID: CT_fFwV-xIk""
  },
  {
    "{": ""      ""Video ID: M9U0xBmxj-U""
  },
  {
    "{": ""      ""Video ID: 90B7CUzuY4U""
  },
  {
    "{": ""      ""Video ID: T0lXN7OXaG0""
  },
  {
    "{": ""      ""Video ID: jUDsGZuGt0M""
  },
  {
    "{": ""      ""Video ID: YZQrQaET2_Y""
  },
  {
    "{": ""      ""Video ID: Ps-3gBkmZUg""
  },
  {
    "{": ""      ""Video ID: vLQDHG_RlA8""
  },
  {
    "{": ""      ""Video ID: 5DQHDpLFgtY""
  },
  {
    "{": ""      ""Video ID: TfRETarezH4""
  },
  {
    "{": ""      ""Video ID: 1IchAMQ6CzI""
  },
  {
    "{": ""      ""Video ID: jn8HUMi0pLs""
  },
  {
    "{": ""      ""Video ID: RcAAYNmoRp8""
  },
  {
    "{": ""      ""Video ID: 1Q8V9sBRRhU""
  },
  {
    "{": ""      ""Video ID: ApFj67BdDeg""
  },
  {
    "{": ""      ""Video ID: Z7-tybYhnfM""
  },
  {
    "{": ""      ""Video ID: wH5B_BkduqI""
  },
  {
    "{": ""      ""Video ID: dn0NaxuvA0g""
  },
  {
    "{": ""      ""Video ID: 45Kjd4QqOQY""
  },
  {
    "{": ""      ""Video ID: T0f6cp56Gxg""
  },
  {
    "{": ""      ""Video ID: _X_YARLori8""
  },
  {
    "{": ""      ""Video ID: WT_-8CxWVDw""
  },
  {
    "{": ""      ""Video ID: _qNkTtEjmFM""
  },
  {
    "{": ""      ""Video ID: fLrEffInMSo""
  },
  {
    "{": ""      ""Video ID: jrGdk-E8O9k""
  },
  {
    "{": ""      ""Video ID: UH6VgMpbWQk""
  },
  {
    "{": ""      ""Video ID: psYjm_bZGNA""
  },
  {
    "{": ""      ""Video ID: baZEd4xqfnw""
  },
  {
    "{": ""      ""Video ID: XcURyYb-bVM""
  },
  {
    "{": ""      ""Video ID: AWZv045ZdgA""
  },
  {
    "{": ""      ""Video ID: lMcgETKs2OY""
  },
  {
    "{": ""      ""Video ID: OLV8KiZY3BI""
  },
  {
    "{": ""      ""Video ID: Y8TaMPL7wjs""
  },
  {
    "{": ""      ""Video ID: HtHhPaWuxW4""
  },
  {
    "{": ""      ""Video ID: s4102LGV8-s""
  },
  {
    "{": ""      ""Video ID: g8f55wPv1ec""
  },
  {
    "{": ""      ""Video ID: IUiNFzzF-ZI""
  },
  {
    "{": ""      ""Video ID: AC1xFjGcZ7c""
  },
  {
    "{": ""      ""Video ID: f-4fpyQOQME""
  },
  {
    "{": ""      ""Video ID: lPF-OQPn6uM""
  },
  {
    "{": ""      ""Video ID: xmDPdCzCfFM""
  },
  {
    "{": ""      ""Video ID: LY26nB5ngAc""
  },
  {
    "{": ""      ""Video ID: 5ytkh6b08wM""
  },
  {
    "{": ""      ""Video ID: mbK80TS3aQ4""
  },
  {
    "{": ""      ""Video ID: HCI95vCauz8""
  },
  {
    "{": ""      ""Video ID: 4KIAKPDvIls""
  },
  {
    "{": ""      ""Video ID: C0Maj1I6kH0""
  },
  {
    "{": ""      ""Video ID: qCYIiHAhIdo""
  },
  {
    "{": ""      ""Video ID: 1w4aRPtUOT4""
  },
  {
    "{": ""      ""Video ID: BSQueZhmWgc""
  },
  {
    "{": ""      ""Video ID: NMHORX6fUds""
  },
  {
    "{": ""      ""Video ID: j8-aPVP7itM""
  },
  {
    "{": ""      ""Video ID: G84KV3Xje2s""
  },
  {
    "{": ""      ""Video ID: PQ7mB8vxOEs""
  },
  {
    "{": ""      ""Video ID: Ih19VqlKTm8""
  },
  {
    "{": ""      ""Video ID: KIwbFnEAbOk""
  },
  {
    "{": ""      ""Video ID: fbMWlesY8KU""
  },
  {
    "{": ""      ""Video ID: AFoklSZgEMY""
  },
  {
    "{": ""      ""Video ID: c7ksI86PD9Y""
  },
  {
    "{": ""      ""Video ID: 9wPrqDNxY68""
  },
  {
    "{": ""      ""Video ID: AfJC2XZMO-k""
  },
  {
    "{": ""      ""Video ID: kWXVvcnXTMw""
  },
  {
    "{": ""      ""Video ID: o-8w_xc-LYA""
  },
  {
    "{": ""      ""Video ID: h3iFO5hSHLk""
  },
  {
    "{": ""      ""Video ID: yJdWafq62u4""
  },
  {
    "{": ""      ""Video ID: hdGcX-s99Rg""
  },
  {
    "{": ""      ""Video ID: raz86JP5NwQ""
  },
  {
    "{": ""      ""Video ID: 1I1lfe1ngtc""
  },
  {
    "{": ""      ""Video ID: re7Vl8VEgv4""
  },
  {
    "{": ""      ""Video ID: Ic8epHchbc0""
  },
  {
    "{": ""      ""Video ID: QUTTLE5nIkQ""
  },
  {
    "{": ""      ""Video ID: CoEfDWA-8sc""
  },
  {
    "{": ""      ""Video ID: u0QVkf-B0qc""
  },
  {
    "{": ""      ""Video ID: 0NfopsVX2P0""
  },
  {
    "{": ""      ""Video ID: MfYcKNqQoJo""
  },
  {
    "{": ""      ""Video ID: X9nKSMCSKEw""
  },
  {
    "{": ""      ""Video ID: PeilR-gZ4k0""
  },
  {
    "{": ""      ""Video ID: CUWl9QPg1Yc""
  },
  {
    "{": ""      ""Video ID: I3Yp2p0xesg""
  },
  {
    "{": ""      ""Video ID: xaagszBx9cE""
  },
  {
    "{": ""      ""Video ID: S6fpqU8F4j8""
  },
  {
    "{": ""      ""Video ID: 0Oo0-mnNheE""
  },
  {
    "{": ""      ""Video ID: g68XAAxKuvA""
  },
  {
    "{": ""      ""Video ID: KD7rBVivCvQ""
  },
  {
    "{": ""      ""Video ID: -9dlMkOFCzE""
  },
  {
    "{": ""      ""Video ID: ZvT4VkLEIJA""
  },
  {
    "{": ""      ""Video ID: mL5zqE-8fBc""
  },
  {
    "{": ""      ""Video ID: rdMfdMBm_NE""
  },
  {
    "{": ""      ""Video ID: 1ckvpYRNUxM""
  },
  {
    "{": ""      ""Video ID: jL1MQacIj4s""
  },
  {
    "{": ""      ""Video ID: p3Jec-9Frq4""
  },
  {
    "{": ""      ""Video ID: X7TSo_8zJHw""
  },
  {
    "{": ""      ""Video ID: yrZ0ogejQRo""
  },
  {
    "{": ""      ""Video ID: 6P_tYkcB47c""
  },
  {
    "{": ""      ""Video ID: PzTCpXhP9EY""
  },
  {
    "{": ""      ""Video ID: nJEOq1PdXzg""
  },
  {
    "{": ""      ""Video ID: N675mHss_uQ""
  },
  {
    "{": ""      ""Video ID: hZzpQhbOx00""
  },
  {
    "{": ""      ""Video ID: AeuLfyYsRug""
  },
  {
    "{": ""      ""Video ID: IC1Mmo9CCZA""
  },
  {
    "{": ""      ""Video ID: sHnXOSxka1Q""
  },
  {
    "{": ""      ""Video ID: HRccMPmUCm0""
  },
  {
    "{": ""      ""Video ID: 4i6LVcwVXnA""
  },
  {
    "{": ""      ""Video ID: xvYD5nUUneU""
  },
  {
    "{": ""      ""Video ID: TM-tAb-bM-s""
  },
  {
    "{": ""      ""Video ID: 13OvfjGo_7s""
  },
  {
    "{": ""      ""Video ID: 7sRmz6_9Cf4""
  },
  {
    "{": ""      ""Video ID: JHTpREbCH6c""
  },
  {
    "{": ""      ""Video ID: vQdnxswgeYc""
  },
  {
    "{": ""      ""Video ID: fibHU_nGDo4""
  },
  {
    "{": ""      ""Video ID: KfC_u0-PvJg""
  },
  {
    "{": ""      ""Video ID: _DJLARAeiyY""
  },
  {
    "{": ""      ""Video ID: kfHaKlhncAs""
  },
  {
    "{": ""      ""Video ID: MysU0LEL4Gw""
  },
  {
    "{": ""      ""Video ID: vDssPKkHtYU""
  },
  {
    "{": ""      ""Video ID: -Xx8ZC5XsOw""
  },
  {
    "{": ""      ""Video ID: KAHDk0RYT8Y""
  },
  {
    "{": ""      ""Video ID: iaV-7kWVShs""
  },
  {
    "{": ""      ""Video ID: CHChw2rjiPU""
  },
  {
    "{": ""      ""Video ID: TwP9ONlFBf4""
  },
  {
    "{": ""      ""Video ID: RY3kPmZ2k38""
  },
  {
    "{": ""      ""Video ID: vErJFmUF7DM""
  },
  {
    "{": ""      ""Video ID: InPlY9L5eFY""
  },
  {
    "{": ""      ""Video ID: _5Dgv54J-L0""
  },
  {
    "{": ""      ""Video ID: T1uJBKPw4Bs""
  },
  {
    "{": ""      ""Video ID: KniV2OGwSms""
  },
  {
    "{": ""      ""Video ID: lUzkWQIVFkk""
  },
  {
    "{": ""      ""Video ID: HEXVnkxiz6A""
  },
  {
    "{": ""      ""Video ID: evIMpZVqM_Y""
  },
  {
    "{": ""      ""Video ID: UL2Ipy1Y_ZY""
  },
  {
    "{": ""      ""Video ID: JffmWtjxVq8""
  },
  {
    "{": ""      ""Video ID: wsXwjFhIXzU""
  },
  {
    "{": ""      ""Video ID: RvfVT6kpR04""
  },
  {
    "{": ""      ""Video ID: K2GTauJT5Vg""
  },
  {
    "{": ""      ""Video ID: u4kokZW-p5k""
  },
  {
    "{": ""      ""Video ID: WuY95J5IvT0""
  },
  {
    "{": ""      ""Video ID: 49z5AtlFxzs""
  },
  {
    "{": ""      ""Video ID: cagJOAvdSi4""
  },
  {
    "{": ""      ""Video ID: 2neF5S9DTH0""
  },
  {
    "{": ""      ""Video ID: cZHpWnzuaBA""
  },
  {
    "{": ""      ""Video ID: RMz7svTcmsk""
  },
  {
    "{": ""      ""Video ID: Kac-rEahSzo""
  },
  {
    "{": ""      ""Video ID: mwR5ly_9oLg""
  },
  {
    "{": ""      ""Video ID: 4_vnrDXzgg0""
  },
  {
    "{": ""      ""Video ID: vm1IhkvVYrs""
  },
  {
    "{": ""      ""Video ID: 7jYHMYisNW8""
  },
  {
    "{": ""      ""Video ID: R8dX7IkOlzk""
  },
  {
    "{": ""      ""Video ID: sOAkjssChzs""
  },
  {
    "{": ""      ""Video ID: IIbLnmwb2oQ""
  },
  {
    "{": ""      ""Video ID: oF_F0zR4TRQ""
  },
  {
    "{": ""      ""Video ID: maCQ5qZJn0Y""
  },
  {
    "{": ""      ""Video ID: PyMigiJ0MHY""
  },
  {
    "{": ""      ""Video ID: c5FmzI2Cfjk""
  },
  {
    "{": ""      ""Video ID: bzlUlOCtTdg""
  },
  {
    "{": ""      ""Video ID: 1uGN20m-8vI""
  },
  {
    "{": ""      ""Video ID: mLmCBG9Yh3E""
  },
  {
    "{": ""      ""Video ID: 9GHgqGUoX88""
  },
  {
    "{": ""      ""Video ID: llPdxCi2zq0""
  },
  {
    "{": ""      ""Video ID: sf5Jf_bnF_4""
  },
  {
    "{": ""      ""Video ID: FOrAmSgZ974""
  },
  {
    "{": ""      ""Video ID: -Igcei_pm2M""
  },
  {
    "{": ""      ""Video ID: JupV0lRvB3c""
  },
  {
    "{": ""      ""Video ID: vM-GcarLxlE""
  },
  {
    "{": ""      ""Video ID: F7mltqYCJCk""
  },
  {
    "{": ""      ""Video ID: xcAAK8nN4As""
  },
  {
    "{": ""      ""Video ID: CHD5SMSRHZA""
  },
  {
    "{": ""      ""Video ID: Urn-HE5xoNc""
  },
  {
    "{": ""      ""Video ID: NAJ-CklVjJc""
  },
  {
    "{": ""      ""Video ID: dK_dUAK10og""
  },
  {
    "{": ""      ""Video ID: R8qA-S_MzGs""
  },
  {
    "{": ""      ""Video ID: uyeSqOp0R1k""
  },
  {
    "{": ""      ""Video ID: SCqVW5Jm28s""
  },
  {
    "{": ""      ""Video ID: NlOx4z86Yuc""
  },
  {
    "{": ""      ""Video ID: LgQ4EFzrFVs""
  },
  {
    "{": ""      ""Video ID: X0SQa-VWj54""
  },
  {
    "{": ""      ""Video ID: 9Or_b3T4yXY""
  },
  {
    "{": ""      ""Video ID: 1BfbYip3LzY""
  },
  {
    "{": ""      ""Video ID: XJcT1n77pkU""
  },
  {
    "{": ""      ""Video ID: nbo4C6KCr7o""
  },
  {
    "{": ""      ""Video ID: Q0n0Zzxo_F0""
  },
  {
    "{": ""      ""Video ID: K0KqoT3NrwA""
  },
  {
    "{": ""      ""Video ID: qeY-TLMZKaM""
  },
  {
    "{": ""      ""Video ID: -r5QsX7a-Lk""
  },
  {
    "{": ""      ""Video ID: arB8hCCl7NY""
  },
  {
    "{": ""      ""Video ID: FfBEec1Gh0c""
  },
  {
    "{": ""      ""Video ID: lkisAfdNqUI""
  },
  {
    "{": ""      ""Video ID: eBFK7g_ic9I""
  },
  {
    "{": ""      ""Video ID: sqRMZuwdSnI""
  },
  {
    "{": ""      ""Video ID: vLv5rIsAp4s""
  },
  {
    "{": ""      ""Video ID: v2xZDojNpsc""
  },
  {
    "{": ""      ""Video ID: -3_zvzhs5Oo""
  },
  {
    "{": ""      ""Video ID: KmAy0NyG6vI""
  },
  {
    "{": ""      ""Video ID: zyzU5lZds_0""
  },
  {
    "{": ""      ""Video ID: AIEKLJ886Qs""
  },
  {
    "{": ""      ""Video ID: 2-syJjcn-7k""
  },
  {
    "{": ""      ""Video ID: NEsIpDqd0-k""
  },
  {
    "{": ""      ""Video ID: w_xM3z97UYo""
  },
  {
    "{": ""      ""Video ID: ZSEyXT36Iks""
  },
  {
    "{": ""      ""Video ID: sCXQHQTVi-E""
  },
  {
    "{": ""      ""Video ID: iPHgjtDv2WA""
  },
  {
    "{": ""      ""Video ID: STc-LrIEGr4""
  },
  {
    "{": ""      ""Video ID: upeM4tGwSTk""
  },
  {
    "{": ""      ""Video ID: 3zdZSTEQnbE""
  },
  {
    "{": ""      ""Video ID: aBYDji6f-78""
  },
  {
    "{": ""      ""Video ID: EmhEIQ8sMlQ""
  },
  {
    "{": ""      ""Video ID: bvlRQ90c9Bk""
  },
  {
    "{": ""      ""Video ID: ICAfNYith5M""
  },
  {
    "{": ""      ""Video ID: 7dJJKt5MlMk""
  },
  {
    "{": ""      ""Video ID: 0wrJa6Thle8""
  },
  {
    "{": ""      ""Video ID: QyrUsKDwzJs""
  },
  {
    "{": ""      ""Video ID: X7vru70QMHE""
  },
  {
    "{": ""      ""Video ID: vW5IV2l_HCE""
  },
  {
    "{": ""      ""Video ID: XIVTn0pIUXY""
  },
  {
    "{": ""      ""Video ID: YvQ7ZNaQdR0""
  },
  {
    "{": ""      ""Video ID: l_qvkIz3Eng""
  },
  {
    "{": ""      ""Video ID: Q_b5ZWPMfYI""
  },
  {
    "{": ""      ""Video ID: lTQ5rNSVExg""
  },
  {
    "{": ""      ""Video ID: QIL0mhP4tzo""
  },
  {
    "{": ""      ""Video ID: 9mjos3YKmIU""
  },
  {
    "{": ""      ""Video ID: oYYFJlP5H40""
  },
  {
    "{": ""      ""Video ID: ppFJrZUU7mU""
  },
  {
    "{": ""      ""Video ID: gfDPoMFhdXQ""
  },
  {
    "{": ""      ""Video ID: zSRgBqfQBzo""
  },
  {
    "{": ""      ""Video ID: 09Fpl29clq0""
  },
  {
    "{": ""      ""Video ID: AP71bZ9vu3I""
  },
  {
    "{": ""      ""Video ID: F0AiN0nemSY""
  },
  {
    "{": ""      ""Video ID: MJS9xGN1HxM""
  },
  {
    "{": ""      ""Video ID: 7D-50lU9a-M""
  },
  {
    "{": ""      ""Video ID: ZQYthBLV5mI""
  },
  {
    "{": ""      ""Video ID: s2wOHqY2uXk""
  },
  {
    "{": ""      ""Video ID: okOrlSebfb0""
  },
  {
    "{": ""      ""Video ID: Qbgv0Mp-Wi4""
  },
  {
    "{": ""      ""Video ID: 9_lPnqbsKQE""
  },
  {
    "{": ""      ""Video ID: 9TQi-LqoL0M""
  },
  {
    "{": ""      ""Video ID: 0ifoaMAscic""
  },
  {
    "{": ""      ""Video ID: Xb_GXcNfceI""
  },
  {
    "{": ""      ""Video ID: balM4ILwmPQ""
  },
  {
    "{": ""      ""Video ID: BOkg-CUPviI""
  },
  {
    "{": ""      ""Video ID: 0ISyHUh1FCE""
  },
  {
    "{": ""      ""Video ID: eqWeoKW8ItQ""
  },
  {
    "{": ""      ""Video ID: WQ30cJdKQu4""
  },
  {
    "{": ""      ""Video ID: J7i6LFO642E""
  },
  {
    "{": ""      ""Video ID: K6nx0Cx3uMk""
  },
  {
    "{": ""      ""Video ID: vBrnBmUmVzI""
  },
  {
    "{": ""      ""Video ID: sqbmasNeOmM""
  },
  {
    "{": ""      ""Video ID: d2B1Bxo9kZg""
  },
  {
    "{": ""      ""Video ID: r3ZoED2pBRU""
  },
  {
    "{": ""      ""Video ID: Fm0MEdy7rJE""
  },
  {
    "{": ""      ""Video ID: rEiyWH-xW1g""
  },
  {
    "{": ""      ""Video ID: NzHure-YBmA""
  },
  {
    "{": ""      ""Video ID: f3bthY07BO8""
  },
  {
    "{": ""      ""Video ID: rAWW9NOPC6E""
  },
  {
    "{": ""      ""Video ID: SvSP7s-kmKI""
  },
  {
    "{": ""      ""Video ID: ED6RYjbI9y0""
  },
  {
    "{": ""      ""Video ID: obrV4JnFLDo""
  },
  {
    "{": ""      ""Video ID: g58kFEZjOvY""
  },
  {
    "{": ""      ""Video ID: eRG8Io3upyo""
  },
  {
    "{": ""      ""Video ID: 3jysfFHMNm4""
  },
  {
    "{": ""      ""Video ID: tqPw3kSae50""
  },
  {
    "{": ""      ""Video ID: WZ022tQ3kaU""
  },
  {
    "{": ""      ""Video ID: 68TEGDjKW3s""
  },
  {
    "{": ""      ""Video ID: w7sZEkDxja8""
  },
  {
    "{": ""      ""Video ID: iF6GWkWnAqs""
  },
  {
    "{": ""      ""Video ID: esUT1OETff8""
  },
  {
    "{": ""      ""Video ID: A-pKOw7MyTQ""
  },
  {
    "{": ""      ""Video ID: OEbh0iH7e98""
  },
  {
    "{": ""      ""Video ID: v2_jJ_46zko""
  },
  {
    "{": ""      ""Video ID: xFnVDtzBVHA""
  },
  {
    "{": ""      ""Video ID: uXhbScVsc50""
  },
  {
    "{": ""      ""Video ID: WiaRP58ljno""
  },
  {
    "{": ""      ""Video ID: -I8VxsWnxfk""
  },
  {
    "{": ""      ""Video ID: s76ezfUEBM0""
  },
  {
    "{": ""      ""Video ID: 7BtAkotmxjs""
  },
  {
    "{": ""      ""Video ID: GgFZy8FYk9I""
  },
  {
    "{": ""      ""Video ID: EXwXsm4qRoQ""
  },
  {
    "{": ""      ""Video ID: OWMkBpF8phc""
  },
  {
    "{": ""      ""Video ID: _FEUouspU8g""
  },
  {
    "{": ""      ""Video ID: I2RmzSYYR6w""
  },
  {
    "{": ""      ""Video ID: J0BkPqvad9M""
  },
  {
    "{": ""      ""Video ID: AvwKI_UukTo""
  },
  {
    "{": ""      ""Video ID: UnrWxVBxnho""
  },
  {
    "{": ""      ""Video ID: iByt8IinjC0""
  },
  {
    "{": ""      ""Video ID: bF_9_ideyvI""
  },
  {
    "{": ""      ""Video ID: C-Qy1m38fh4""
  },
  {
    "{": ""      ""Video ID: jiJNwIPALs8""
  },
  {
    "{": ""      ""Video ID: Tvy7iS4K0Os""
  },
  {
    "{": ""      ""Video ID: zdkHR6ibBg8""
  },
  {
    "{": ""      ""Video ID: zT2M7PkcDt0""
  },
  {
    "{": ""      ""Video ID: 6bupoG1AKM4""
  },
  {
    "{": ""      ""Video ID: 3q46xaZGNF0""
  },
  {
    "{": ""      ""Video ID: SBpIvrUyWM8""
  },
  {
    "{": ""      ""Video ID: tz6RyI3jMqU""
  },
  {
    "{": ""      ""Video ID: PEDbLzvzANQ""
  },
  {
    "{": ""      ""Video ID: 5HgYgXA9-XY""
  },
  {
    "{": ""      ""Video ID: P_subW63WjE""
  },
  {
    "{": ""      ""Video ID: yhtdK7Oab4c""
  },
  {
    "{": ""      ""Video ID: 06jtDOxjMPM""
  },
  {
    "{": ""      ""Video ID: Wt8_9BLrZHA""
  },
  {
    "{": ""      ""Video ID: 4ApPM0nBxps""
  },
  {
    "{": ""      ""Video ID: Yb9h64zn-Io""
  },
  {
    "{": ""      ""Video ID: 0yDnC6VYj3o""
  },
  {
    "{": ""      ""Video ID: lwLkbidU9vk""
  },
  {
    "{": ""      ""Video ID: N2piqkdX6MQ""
  },
  {
    "{": ""      ""Video ID: rvhdD6wJRlI""
  },
  {
    "{": ""      ""Video ID: ySDKjgGXKR8""
  },
  {
    "{": ""      ""Video ID: 5quXyKb-2kg""
  },
  {
    "{": ""      ""Video ID: oPstp_bPbPo""
  },
  {
    "{": ""      ""Video ID: qkYJYJdyodQ""
  },
  {
    "{": ""      ""Video ID: 1oVG7c5E74U""
  },
  {
    "{": ""      ""Video ID: CEverENV58s""
  },
  {
    "{": ""      ""Video ID: SgR13dKAZVU""
  },
  {
    "{": ""      ""Video ID: HdYgMNap2_A""
  },
  {
    "{": ""      ""Video ID: zDSNjs-60nI""
  },
  {
    "{": ""      ""Video ID: s_BZaHiuNkw""
  },
  {
    "{": ""      ""Video ID: n34o4ed9ab0""
  },
  {
    "{": ""      ""Video ID: Gq7fVflfx0Q""
  },
  {
    "{": ""      ""Video ID: 46sYWfvkQpg""
  },
  {
    "{": ""      ""Video ID: GguXI5WC9aY""
  },
  {
    "{": ""      ""Video ID: TTv6ZQ1XSUo""
  },
  {
    "{": ""      ""Video ID: nIO_-TvdrVg""
  },
  {
    "{": ""      ""Video ID: VcMOXU8_kfQ""
  },
  {
    "{": ""      ""Video ID: cUplX_KTITk""
  },
  {
    "{": ""      ""Video ID: mpSAt5FAawI""
  },
  {
    "{": ""      ""Video ID: oLvO2DA85nk""
  },
  {
    "{": ""      ""Video ID: g9yFmBm-3F4""
  },
  {
    "{": ""      ""Video ID: ruA0lVcrfxw""
  },
  {
    "{": ""      ""Video ID: -dZqPmfpi9c""
  },
  {
    "{": ""      ""Video ID: FzZWqYWhdQw""
  },
  {
    "{": ""      ""Video ID: f7m2iPlmCbE""
  },
  {
    "{": ""      ""Video ID: dRxdLbXovhA""
  },
  {
    "{": ""      ""Video ID: qHFmKg_rnJg""
  },
  {
    "{": ""      ""Video ID: Vxb7n55LL1I""
  },
  {
    "{": ""      ""Video ID: 34Gq_94Ce3I""
  },
  {
    "{": ""      ""Video ID: 3kkhP_0Rmgc""
  },
  {
    "{": ""      ""Video ID: Vgp7Le7oPng""
  },
  {
    "{": ""      ""Video ID: qxOIbQsm3F0""
  },
  {
    "{": ""      ""Video ID: dfsEC8-DcgY""
  },
  {
    "{": ""      ""Video ID: fsPT0gU2UzU""
  },
  {
    "{": ""      ""Video ID: JYwXSwP2AC0""
  },
  {
    "{": ""      ""Video ID: ZOGMhuVLjTA""
  },
  {
    "{": ""      ""Video ID: AvekktHOTCo""
  },
  {
    "{": ""      ""Video ID: _X_p_plomns""
  },
  {
    "{": ""      ""Video ID: B7D0Oj8sJrU""
  },
  {
    "{": ""      ""Video ID: aE66WKVVfSU""
  },
  {
    "{": ""      ""Video ID: 6Wu4Ht-jxGE""
  },
  {
    "{": ""      ""Video ID: Ys6yYqP-t4g""
  },
  {
    "{": ""      ""Video ID: lA8jIhZ80Pk""
  },
  {
    "{": ""      ""Video ID: FT060JGp9sQ""
  },
  {
    "{": ""      ""Video ID: -7nnE6b0_g4""
  },
  {
    "{": ""      ""Video ID: BNuec61xR-Q""
  },
  {
    "{": ""      ""Video ID: XuS4Ihd_qt0""
  },
  {
    "{": ""      ""Video ID: JlhcDkUfKbA""
  },
  {
    "{": ""      ""Video ID: BQZdyR1ff_c""
  },
  {
    "{": ""      ""Video ID: qVxqwFa3Y4c""
  },
  {
    "{": ""      ""Video ID: rlDbp4AlU3c""
  },
  {
    "{": ""      ""Video ID: WGaQabXUwUc""
  },
  {
    "{": ""      ""Video ID: 3cGtUd_zBEA""
  },
  {
    "{": ""      ""Video ID: dwTDvfjcUJU""
  },
  {
    "{": ""      ""Video ID: 4O2_rZIgrQI""
  },
  {
    "{": ""      ""Video ID: nfTMka5JQqE""
  },
  {
    "{": ""      ""Video ID: lZ5aKzgynVw""
  },
  {
    "{": ""      ""Video ID: dFtwLghNPfo""
  },
  {
    "{": ""      ""Video ID: xVzve97shIU""
  },
  {
    "{": ""      ""Video ID: ZXUdDmwaXT8""
  },
  {
    "{": ""      ""Video ID: GGFk-U4GaHI""
  },
  {
    "{": ""      ""Video ID: wV3yYS4QNMM""
  },
  {
    "{": ""      ""Video ID: wA06PHmBEd0""
  },
  {
    "{": ""      ""Video ID: vXdovXoz5Ic""
  },
  {
    "{": ""      ""Video ID: 4m__xUr1wsc""
  },
  {
    "{": ""      ""Video ID: p3jcsyXpt2k""
  },
  {
    "{": ""      ""Video ID: 01rAh6nbbS0""
  },
  {
    "{": ""      ""Video ID: kpW5ioorT0o""
  },
  {
    "{": ""      ""Video ID: inxfzGothHo""
  },
  {
    "{": ""      ""Video ID: K6Mw6b1T50U""
  },
  {
    "{": ""      ""Video ID: T1g8BrzFBLs""
  },
  {
    "{": ""      ""Video ID: agjWx7RBCkY""
  },
  {
    "{": ""      ""Video ID: STZyphYsjmc""
  },
  {
    "{": ""      ""Video ID: APPlTam0lqI""
  },
  {
    "{": ""      ""Video ID: qJkHJim_L5Q""
  },
  {
    "{": ""      ""Video ID: HaTkdR3BACw""
  },
  {
    "{": ""      ""Video ID: WYNI5RPOlp4""
  },
  {
    "{": ""      ""Video ID: RCf9hkt9S6A""
  },
  {
    "{": ""      ""Video ID: WEl07iZK0cg""
  },
  {
    "{": ""      ""Video ID: _U749u6FISk""
  },
  {
    "{": ""      ""Video ID: rJUhVVpVzLk""
  },
  {
    "{": ""      ""Video ID: JYyOhc-WAQY""
  },
  {
    "{": ""      ""Video ID: j85OkWdO_8g""
  },
  {
    "{": ""      ""Video ID: L7rL37jJIsQ""
  },
  {
    "{": ""      ""Video ID: UH-jkLMuUoc""
  },
  {
    "{": ""      ""Video ID: 2_lOyI5Flj4""
  },
  {
    "{": ""      ""Video ID: K-9F23TtAQA""
  },
  {
    "{": ""      ""Video ID: DD44k-PjHRg""
  },
  {
    "{": ""      ""Video ID: Vdqh4shak5s""
  },
  {
    "{": ""      ""Video ID: 9m6XMnwfT7U""
  },
  {
    "{": ""      ""Video ID: PVdc6NsT05o""
  },
  {
    "{": ""      ""Video ID: Gpr498vngFQ""
  },
  {
    "{": ""      ""Video ID: QvlFGplH6ws""
  },
  {
    "{": ""      ""Video ID: d9R4zekHecI""
  },
  {
    "{": ""      ""Video ID: UqWfhPsBcOo""
  },
  {
    "{": ""      ""Video ID: EslorkYSJrE""
  },
  {
    "{": ""      ""Video ID: rDtINX9qgyE""
  },
  {
    "{": ""      ""Video ID: xpV8UxgzHKE""
  },
  {
    "{": ""      ""Video ID: zZPabRsjusU""
  },
  {
    "{": ""      ""Video ID: tvoXv0c0Yrc""
  },
  {
    "{": ""      ""Video ID: pd099hnvfO8""
  },
  {
    "{": ""      ""Video ID: ljQtbs-Wr6s""
  },
  {
    "{": ""      ""Video ID: g-yPwXTgFns""
  },
  {
    "{": ""      ""Video ID: 7EbeqPynF2s""
  },
  {
    "{": ""      ""Video ID: aQ7K5NzrGwI""
  },
  {
    "{": ""      ""Video ID: ARjWU6Ly0kI""
  },
  {
    "{": ""      ""Video ID: C2NDAtFgKPU""
  },
  {
    "{": ""      ""Video ID: IWthxY-RDcs""
  },
  {
    "{": ""      ""Video ID: PJYxCSXjhLI""
  },
  {
    "{": ""      ""Video ID: msrR2ohcBkY""
  },
  {
    "{": ""      ""Video ID: 12mQ_iKjiAc""
  },
  {
    "{": ""      ""Video ID: 8cBuCcuN1t8""
  },
  {
    "{": ""      ""Video ID: cuoLp-ylBxM""
  },
  {
    "{": ""      ""Video ID: o7Xpsh2MLoI""
  },
  {
    "{": ""      ""Video ID: ftTtSM17TH0""
  },
  {
    "{": ""      ""Video ID: in5WL0FzWh8""
  },
  {
    "{": ""      ""Video ID: nPQ3bc0LMuA""
  },
  {
    "{": ""      ""Video ID: uEWjxOezliY""
  },
  {
    "{": ""      ""Video ID: IiJhuWjYvd4""
  },
  {
    "{": ""      ""Video ID: MgmTNxnEXd4""
  },
  {
    "{": ""      ""Video ID: wZRDzvxDxak""
  },
  {
    "{": ""      ""Video ID: 7BOp9w_Y6pI""
  },
  {
    "{": ""      ""Video ID: mFrRXjbmLHM""
  },
  {
    "{": ""      ""Video ID: 4LJdAqeI7OY""
  },
  {
    "{": ""      ""Video ID: 0uCF3VGr_yI""
  },
  {
    "{": ""      ""Video ID: J1mTlHpijdQ""
  },
  {
    "{": ""      ""Video ID: M4L-qIkxaHc""
  },
  {
    "{": ""      ""Video ID: MThEoxSWURA""
  },
  {
    "{": ""      ""Video ID: RR5Te8T5T_c""
  },
  {
    "{": ""      ""Video ID: H7TSnE1b-Bs""
  },
  {
    "{": ""      ""Video ID: Iv_v62OlmQA""
  },
  {
    "{": ""      ""Video ID: AntqKkT6Glc""
  },
  {
    "{": ""      ""Video ID: 0TvlHPAXAgo""
  },
  {
    "{": ""      ""Video ID: EYJ19Q7d-DA""
  },
  {
    "{": ""      ""Video ID: _gOuvFmXTrI""
  },
  {
    "{": ""      ""Video ID: syV1fMJq21A""
  },
  {
    "{": ""      ""Video ID: oV7xwDLW0hY""
  },
  {
    "{": ""      ""Video ID: pk9UBxxebsE""
  },
  {
    "{": ""      ""Video ID: w_-HBEc4JQ0""
  },
  {
    "{": ""      ""Video ID: cCwx_wRo2dI""
  },
  {
    "{": ""      ""Video ID: dK5gK0nUwOc""
  },
  {
    "{": ""      ""Video ID: cVok04Psy1I""
  },
  {
    "{": ""      ""Video ID: iRb7XxuxH_o""
  },
  {
    "{": ""      ""Video ID: eN_Su8ywLwk""
  },
  {
    "{": ""      ""Video ID: a7GckaXKK1M""
  },
  {
    "{": ""      ""Video ID: _1AilnxSF0g""
  },
  {
    "{": ""      ""Video ID: A6PcAmCXpXM""
  },
  {
    "{": ""      ""Video ID: mvUnErDPHgM""
  },
  {
    "{": ""      ""Video ID: kUFI2HEdgsQ""
  },
  {
    "{": ""      ""Video ID: _Qy97pFDLig""
  },
  {
    "{": ""      ""Video ID: f8U-k_g56RA""
  },
  {
    "{": ""      ""Video ID: n18_aDor0I8""
  },
  {
    "{": ""      ""Video ID: X99FcDF67cY""
  },
  {
    "{": ""      ""Video ID: 6SkC6iTMhho""
  },
  {
    "{": ""      ""Video ID: EqgtL7lMvaA""
  },
  {
    "{": ""      ""Video ID: sfM-a6RNZFo""
  },
  {
    "{": ""      ""Video ID: WEgi1Pu6bIQ""
  },
  {
    "{": ""      ""Video ID: 9r0VtuI_EvI""
  },
  {
    "{": ""      ""Video ID: lSgTHMsi2pI""
  },
  {
    "{": ""      ""Video ID: psTgOBqHsvI""
  },
  {
    "{": ""      ""Video ID: ifRt9mri5zA""
  },
  {
    "{": ""      ""Video ID: Ud_etP1nqYw""
  },
  {
    "{": ""      ""Video ID: Vdu2lVzI7xk""
  },
  {
    "{": ""      ""Video ID: OWcaRdCa1Jw""
  },
  {
    "{": ""      ""Video ID: iLixUxMN4M4""
  },
  {
    "{": ""      ""Video ID: 7zsr0UpVjoE""
  },
  {
    "{": ""      ""Video ID: IqwEl-06Rak""
  },
  {
    "{": ""      ""Video ID: 2NWUzpgHfuQ""
  },
  {
    "{": ""      ""Video ID: Q-2CSaK9cMs""
  },
  {
    "{": ""      ""Video ID: 9jVG5v_gYBg""
  },
  {
    "{": ""      ""Video ID: MR3poisUoOI""
  },
  {
    "{": ""      ""Video ID: X01WX6F3b9w""
  },
  {
    "{": ""      ""Video ID: vkida-NB8wU""
  },
  {
    "{": ""      ""Video ID: 6CkkBYEx7Gc""
  },
  {
    "{": ""      ""Video ID: R135XyH1qoI""
  },
  {
    "{": ""      ""Video ID: frj3fOaKwV4""
  },
  {
    "{": ""      ""Video ID: gA2kzXD-fyY""
  },
  {
    "{": ""      ""Video ID: XpvyM9clpfs""
  },
  {
    "{": ""      ""Video ID: z7EGHOXYEsU""
  },
  {
    "{": ""      ""Video ID: SPxU8a9V_5M""
  },
  {
    "{": ""      ""Video ID: ql-wr8EzbQM""
  },
  {
    "{": ""      ""Video ID: I9-Ih4H70MM""
  },
  {
    "{": ""      ""Video ID: E0DoxrNCImI""
  },
  {
    "{": ""      ""Video ID: -Jdp4YPX30s""
  },
  {
    "{": ""      ""Video ID: YyXqp0jTuDk""
  },
  {
    "{": ""      ""Video ID: f6Rf35j5wlI""
  },
  {
    "{": ""      ""Video ID: PrsJVZe41Dg""
  },
  {
    "{": ""      ""Video ID: GtWNa5ov2_w""
  },
  {
    "{": ""      ""Video ID: lHlLBxaoJtM""
  },
  {
    "{": ""      ""Video ID: fbEFQVNRyyo""
  },
  {
    "{": ""      ""Video ID: MIH_7q5cDOQ""
  },
  {
    "{": ""      ""Video ID: d6iyWuMu5vc""
  },
  {
    "{": ""      ""Video ID: 0lJg1RnlGnY""
  },
  {
    "{": ""      ""Video ID: gLkqvd-Gevo""
  },
  {
    "{": ""      ""Video ID: USLFOf4xfRg""
  },
  {
    "{": ""      ""Video ID: 3BQQbyizlH8""
  },
  {
    "{": ""      ""Video ID: k7WRFqsMsWI""
  },
  {
    "{": ""      ""Video ID: IS144axdefU""
  },
  {
    "{": ""      ""Video ID: 65_RTRKgy3E""
  },
  {
    "{": ""      ""Video ID: 3uVXZS6oEhg""
  },
  {
    "{": ""      ""Video ID: WLxs5ZJnqzE""
  },
  {
    "{": ""      ""Video ID: 0XKxv1_0oLk""
  },
  {
    "{": ""      ""Video ID: 3eIPNOMW7F0""
  },
  {
    "{": ""      ""Video ID: TvINiJkAdg8""
  },
  {
    "{": ""      ""Video ID: Ru8rRaufbdY""
  },
  {
    "{": ""      ""Video ID: 8G2jZC-ynV0""
  },
  {
    "{": ""      ""Video ID: Z93YDhFW0c8""
  },
  {
    "{": ""      ""Video ID: OX9Log2hzXA""
  },
  {
    "{": ""      ""Video ID: HF6Zf3fRP9g""
  },
  {
    "{": ""      ""Video ID: CZ_SZiHLke4""
  },
  {
    "{": ""      ""Video ID: PrUdNBzqJSo""
  },
  {
    "{": ""      ""Video ID: l6NbR9AyZ3A""
  },
  {
    "{": ""      ""Video ID: HnUVpiFHhmM""
  },
  {
    "{": ""      ""Video ID: arWJ358tZgU""
  },
  {
    "{": ""      ""Video ID: jzqMJWlKMsY""
  },
  {
    "{": ""      ""Video ID: 7octwsoi4HM""
  },
  {
    "{": ""      ""Video ID: vhTDXL9TtbA""
  },
  {
    "{": ""      ""Video ID: FlvN0D5hLI0""
  },
  {
    "{": ""      ""Video ID: J9jcMS87GZI""
  },
  {
    "{": ""      ""Video ID: AG3tiyV8FP8""
  },
  {
    "{": ""      ""Video ID: 7nj73Ixn5p4""
  },
  {
    "{": ""      ""Video ID: yimnVUB7cso""
  },
  {
    "{": ""      ""Video ID: ugTfFhOarc4""
  },
  {
    "{": ""      ""Video ID: ZCSb5k_0rCY""
  },
  {
    "{": ""      ""Video ID: zGTVNhalatM""
  },
  {
    "{": ""      ""Video ID: ztOCcRaR35A""
  },
  {
    "{": ""      ""Video ID: kT7mpseI-3k""
  },
  {
    "{": ""      ""Video ID: ejheJvP0Ddk""
  },
  {
    "{": ""      ""Video ID: 9grHLZ8S27w""
  },
  {
    "{": ""      ""Video ID: 7fvOdXO8d34""
  },
  {
    "{": ""      ""Video ID: OWRtlPas4ko""
  },
  {
    "{": ""      ""Video ID: Q0cMq8BJY5Q""
  },
  {
    "{": ""      ""Video ID: 5vNMJ2w2Ltc""
  },
  {
    "{": ""      ""Video ID: G1V01D53B6k""
  },
  {
    "{": ""      ""Video ID: C59_45N0fho""
  },
  {
    "{": ""      ""Video ID: 4AqyK5c9gKc""
  },
  {
    "{": ""      ""Video ID: of1t_Xdo31M""
  },
  {
    "{": ""      ""Video ID: UdYVMEMDkyQ""
  },
  {
    "{": ""      ""Video ID: NFOdOht5Ccs""
  },
  {
    "{": ""      ""Video ID: A8Nb0oWAW-I""
  },
  {
    "{": ""      ""Video ID: rOGVw-XljRM""
  },
  {
    "{": ""      ""Video ID: begmUPHD-X8""
  },
  {
    "{": ""      ""Video ID: vTFUsckSDe8""
  },
  {
    "{": ""      ""Video ID: wVt59yd2W0U""
  },
  {
    "{": ""      ""Video ID: w2pF-22z8XA""
  },
  {
    "{": ""      ""Video ID: XYzDIhbgDtg""
  },
  {
    "{": ""      ""Video ID: ulODoND4V5Y""
  },
  {
    "{": ""      ""Video ID: wsR-mDUvdoU""
  },
  {
    "{": ""      ""Video ID: a4KKUS3JR-s""
  },
  {
    "{": ""      ""Video ID: smHgv4iJJss""
  },
  {
    "{": ""      ""Video ID: 0fnCQZT-Xlc""
  },
  {
    "{": ""      ""Video ID: igUaCWhA66E""
  },
  {
    "{": ""      ""Video ID: zB_XQszXKcM""
  },
  {
    "{": ""      ""Video ID: _7w4xc1hk0c""
  },
  {
    "{": ""      ""Video ID: qD0zFX3BFz4""
  },
  {
    "{": ""      ""Video ID: Vtf0p2ScGPg""
  },
  {
    "{": ""      ""Video ID: QP9FoxeMQQ8""
  },
  {
    "{": ""      ""Video ID: ZC-SNSGE7kI""
  },
  {
    "{": ""      ""Video ID: DRNWRRR1rtc""
  },
  {
    "{": ""      ""Video ID: dBVfb0HXSgo""
  },
  {
    "{": ""      ""Video ID: o1Rzz-BhZ4Y""
  },
  {
    "{": ""      ""Video ID: v0RgAI5Ipe4""
  },
  {
    "{": ""      ""Video ID: uprN9_3gahc""
  },
  {
    "{": ""      ""Video ID: M_MCdw8S7aw""
  },
  {
    "{": ""      ""Video ID: hDanuupdDdk""
  },
  {
    "{": ""      ""Video ID: bNz1Jd-Umec""
  },
  {
    "{": ""      ""Video ID: aepb-0RnUV4""
  },
  {
    "{": ""      ""Video ID: I4kMV6EYTIw""
  },
  {
    "{": ""      ""Video ID: 9WDTfctPeiY""
  },
  {
    "{": ""      ""Video ID: XB-sNaaaJRU""
  },
  {
    "{": ""      ""Video ID: gaIoAgR5OEE""
  },
  {
    "{": ""      ""Video ID: golUZjKJTAE""
  },
  {
    "{": ""      ""Video ID: YUjWqRTBRzQ""
  },
  {
    "{": ""      ""Video ID: UMYmxjB8Mhw""
  },
  {
    "{": ""      ""Video ID: FX20RCa1C14""
  },
  {
    "{": ""      ""Video ID: mhYt7s0MWtk""
  },
  {
    "{": ""      ""Video ID: luUbEUhfEOc""
  },
  {
    "{": ""      ""Video ID: I0nEUhiAaSc""
  },
  {
    "{": ""      ""Video ID: nrff-ydui74""
  },
  {
    "{": ""      ""Video ID: TboHGtItQgw""
  },
  {
    "{": ""      ""Video ID: RgOXdC8jMmk""
  },
  {
    "{": ""      ""Video ID: pbQNoeWTvtI""
  },
  {
    "{": ""      ""Video ID: vgvLiQvW3Y8""
  },
  {
    "{": ""      ""Video ID: wawosYVpvPw""
  },
  {
    "{": ""      ""Video ID: HHpLHJ8WpaM""
  },
  {
    "{": ""      ""Video ID: 5ULLZm_x_YE""
  },
  {
    "{": ""      ""Video ID: WvHWNRIbEI4""
  },
  {
    "{": ""      ""Video ID: J0XCLo71nCo""
  },
  {
    "{": ""      ""Video ID: KNjgw0_R9xk""
  },
  {
    "{": ""      ""Video ID: B_kyNIevsIs""
  },
  {
    "{": ""      ""Video ID: UufTBjgEE5Q""
  },
  {
    "{": ""      ""Video ID: bX7kuQ2h_zc""
  },
  {
    "{": ""      ""Video ID: TYIR9b1yS4A""
  },
  {
    "{": ""      ""Video ID: HyT-xn_npLw""
  },
  {
    "{": ""      ""Video ID: xLceo8J2UP8""
  },
  {
    "{": ""      ""Video ID: dksTzfkNua8""
  },
  {
    "{": ""      ""Video ID: dCyKnc1BVV8""
  },
  {
    "{": ""      ""Video ID: WjxJxwHNNlw""
  },
  {
    "{": ""      ""Video ID: 7Jap2Tl2k50""
  },
  {
    "{": ""      ""Video ID: qGVAQOUi6ec""
  },
  {
    "{": ""      ""Video ID: jMkKzDxVGis""
  },
  {
    "{": ""      ""Video ID: p1ZMF_z_CFc""
  },
  {
    "{": ""      ""Video ID: YH0kESbFHCk""
  },
  {
    "{": ""      ""Video ID: HumFpqRozDo""
  },
  {
    "{": ""      ""Video ID: iQ_ajEBoaL0""
  },
  {
    "{": ""      ""Video ID: sUucuUJUrL8""
  },
  {
    "{": ""      ""Video ID: Ybb4oxL-9Ek""
  },
  {
    "{": ""      ""Video ID: __DdFiV7aT8""
  },
  {
    "{": ""      ""Video ID: 75C9ERQ11kI""
  },
  {
    "{": ""      ""Video ID: qpELweyBZXE""
  },
  {
    "{": ""      ""Video ID: I3nFsjPHYG0""
  },
  {
    "{": ""      ""Video ID: ZM1lbwHGqgw""
  },
  {
    "{": ""      ""Video ID: MzHJEmMar04""
  },
  {
    "{": ""      ""Video ID: JKvqXJItRSU""
  },
  {
    "{": ""      ""Video ID: oELj5F81pDs""
  },
  {
    "{": ""      ""Video ID: AMpgnESssP4""
  },
  {
    "{": ""      ""Video ID: h_uMoi_0ULc""
  },
  {
    "{": ""      ""Video ID: FDBJf2qsFCU""
  },
  {
    "{": ""      ""Video ID: 2ZUEbX_Bkm4""
  },
  {
    "{": ""      ""Video ID: 0EXH5TXw1FU""
  },
  {
    "{": ""      ""Video ID: _dka_z6scSE""
  },
  {
    "{": ""      ""Video ID: uPAanmB2NX0""
  },
  {
    "{": ""      ""Video ID: kTNsbs4WXLw""
  },
  {
    "{": ""      ""Video ID: 34RZ4VqI3JI""
  },
  {
    "{": ""      ""Video ID: DoRcOCO0e3A""
  },
  {
    "{": ""      ""Video ID: QBL0XqB1uZo""
  },
  {
    "{": ""      ""Video ID: 4KWmPzzcjpk""
  },
  {
    "{": ""      ""Video ID: CO_PzhKLkbc""
  },
  {
    "{": ""      ""Video ID: ADtxPZaD75Y""
  },
  {
    "{": ""      ""Video ID: G8xKunqlj_Y""
  },
  {
    "{": ""      ""Video ID: nPf6jTUpI54""
  },
  {
    "{": ""      ""Video ID: 5U4jFrKvI1M""
  },
  {
    "{": ""      ""Video ID: PbEBgTYEoEM""
  },
  {
    "{": ""      ""Video ID: bOSclhDEkjY""
  },
  {
    "{": ""      ""Video ID: Ua1PB0Kqcpc""
  },
  {
    "{": ""      ""Video ID: 1dPZjGqFnso""
  },
  {
    "{": ""      ""Video ID: OFg7wVETAjk""
  },
  {
    "{": ""      ""Video ID: LGSWEdS1E54""
  },
  {
    "{": ""      ""Video ID: 8NK2CIqUgFE""
  },
  {
    "{": ""      ""Video ID: lrrlPk4RfXI""
  },
  {
    "{": ""      ""Video ID: vFjmdOuGTLg""
  },
  {
    "{": ""      ""Video ID: VdKgL0Bnuqg""
  },
  {
    "{": ""      ""Video ID: zMTndhA21O0""
  },
  {
    "{": ""      ""Video ID: R8k_Bd6wgs4""
  },
  {
    "{": ""      ""Video ID: 42k9n-kD5dE""
  },
  {
    "{": ""      ""Video ID: qWCo13lqy08""
  },
  {
    "{": ""      ""Video ID: RwO6v9POt74""
  },
  {
    "{": ""      ""Video ID: PnV_6AxRquU""
  },
  {
    "{": ""      ""Video ID: fxcq6F9Van4""
  },
  {
    "{": ""      ""Video ID: gygIouKq4Qc""
  },
  {
    "{": ""      ""Video ID: M70V38ZqVVU""
  },
  {
    "{": ""      ""Video ID: vvFnC7Zd9bc""
  },
  {
    "{": ""      ""Video ID: VX5wS1-GQmo""
  },
  {
    "{": ""      ""Video ID: KNn_pdU3Ap4""
  },
  {
    "{": ""      ""Video ID: 5eB0q5-jkgQ""
  },
  {
    "{": ""      ""Video ID: YgMc0Xv7mD8""
  },
  {
    "{": ""      ""Video ID: Ekiz3bk6URA""
  },
  {
    "{": ""      ""Video ID: LpwRHannFWk""
  },
  {
    "{": ""      ""Video ID: NqKiagw0IQg""
  },
  {
    "{": ""      ""Video ID: U3IMFs8tXHY""
  },
  {
    "{": ""      ""Video ID: Uws5nqNEhvo""
  },
  {
    "{": ""      ""Video ID: FG_bACkcDL8""
  },
  {
    "{": ""      ""Video ID: P15FrQAkbg0""
  },
  {
    "{": ""      ""Video ID: DdeFv6MgwYQ""
  },
  {
    "{": ""      ""Video ID: aj4R0G2wOhU""
  },
  {
    "{": ""      ""Video ID: yPYwP1Gu5ek""
  },
  {
    "{": ""      ""Video ID: 5aat3Bs4YFU""
  },
  {
    "{": ""      ""Video ID: nzwM4O4AkKI""
  },
  {
    "{": ""      ""Video ID: 5WY1aP2Ft84""
  },
  {
    "{": ""      ""Video ID: 2pCdIDlssME""
  },
  {
    "{": ""      ""Video ID: 0YFzWOwsv6U""
  },
  {
    "{": ""      ""Video ID: 0WBSG03CfD0""
  },
  {
    "{": ""      ""Video ID: Zvnqjge8qKs""
  },
  {
    "{": ""      ""Video ID: Hl4Sr3xeYf4""
  },
  {
    "{": ""      ""Video ID: nzLR_gT01SA""
  },
  {
    "{": ""      ""Video ID: CJsFUm-5kL4""
  },
  {
    "{": ""      ""Video ID: eSj1rArOuHU""
  },
  {
    "{": ""      ""Video ID: xrN58ZjB6LI""
  },
  {
    "{": ""      ""Video ID: iGCV_3bg9K8""
  },
  {
    "{": ""      ""Video ID: 1Ag0XD_wFqQ""
  },
  {
    "{": ""      ""Video ID: aBqKDKaZzm0""
  },
  {
    "{": ""      ""Video ID: AbQ2eLgrH4k""
  },
  {
    "{": ""      ""Video ID: jGOH-eUe-2E""
  },
  {
    "{": ""      ""Video ID: jpPsNNdS_E4""
  },
  {
    "{": ""      ""Video ID: yB_LB8Id6yU""
  },
  {
    "{": ""      ""Video ID: b-XXk-LOY8I""
  },
  {
    "{": ""      ""Video ID: gXgCvvvgrbc""
  },
  {
    "{": ""      ""Video ID: Tsx4vrthtk8""
  },
  {
    "{": ""      ""Video ID: Plq8yOC1IBg""
  },
  {
    "{": ""      ""Video ID: WF8LPQQdkD8""
  },
  {
    "{": ""      ""Video ID: Eeix5ME-brI""
  },
  {
    "{": ""      ""Video ID: Uzqa2KsZMF0""
  },
  {
    "{": ""      ""Video ID: rRk4XTkDt9c""
  },
  {
    "{": ""      ""Video ID: EiSYnbuYDtw""
  },
  {
    "{": ""      ""Video ID: G5KanpeInbQ""
  },
  {
    "{": ""      ""Video ID: e9d4fjY7efQ""
  },
  {
    "{": ""      ""Video ID: wzjP48muo0k""
  },
  {
    "{": ""      ""Video ID: SRFrMO4oDdM""
  },
  {
    "{": ""      ""Video ID: 5x-UE6kbrpk""
  },
  {
    "{": ""      ""Video ID: Y_qeCNg8fO0""
  },
  {
    "{": ""      ""Video ID: _QP2IL7rnXs""
  },
  {
    "{": ""      ""Video ID: J1rytD69DPo""
  },
  {
    "{": ""      ""Video ID: ra5D0QgvpKM""
  },
  {
    "{": ""      ""Video ID: 2FHzEkFNKQM""
  },
  {
    "{": ""      ""Video ID: DIYXcD_2qgs""
  },
  {
    "{": ""      ""Video ID: B1oaxqJfF10""
  },
  {
    "{": ""      ""Video ID: GRbhgaqFNyE""
  },
  {
    "{": ""      ""Video ID: _TWDHbJZbSU""
  },
  {
    "{": ""      ""Video ID: pqO_eiVtVnA""
  },
  {
    "{": ""      ""Video ID: sI8Sus_KRpY""
  },
  {
    "{": ""      ""Video ID: ffvnRh1T_3s""
  },
  {
    "{": ""      ""Video ID: XVQNt64PxfE""
  },
  {
    "{": ""      ""Video ID: 0-PIUXO7f64""
  },
  {
    "{": ""      ""Video ID: IdIRTChOreo""
  },
  {
    "{": ""      ""Video ID: n-VzSbXBoEQ""
  },
  {
    "{": ""      ""Video ID: q-4SfZny8O8""
  },
  {
    "{": ""      ""Video ID: VIKXJjZubGU""
  },
  {
    "{": ""      ""Video ID: IUUfbb6uBcE""
  },
  {
    "{": ""      ""Video ID: 94n_KkpGzd8""
  },
  {
    "{": ""      ""Video ID: c9aiKfQIYL8""
  },
  {
    "{": ""      ""Video ID: TTupFd6YNXI""
  },
  {
    "{": ""      ""Video ID: EGRIjblEGeM""
  },
  {
    "{": ""      ""Video ID: YXyMih3bygc""
  },
  {
    "{": ""      ""Video ID: 9oWwCmNDLqI""
  },
  {
    "{": ""      ""Video ID: gq4PFnl1S6Q""
  },
  {
    "{": ""      ""Video ID: Tte3LvwLxl4""
  },
  {
    "{": ""      ""Video ID: Ty9E-yFqAeo""
  },
  {
    "{": ""      ""Video ID: 8tlXxwpczrg""
  },
  {
    "{": ""      ""Video ID: tIL8smShMnI""
  },
  {
    "{": ""      ""Video ID: ZpAjb2V_Ew4""
  },
  {
    "{": ""      ""Video ID: EB9b793ePi0""
  },
  {
    "{": ""      ""Video ID: L5C99JyP2ns""
  },
  {
    "{": ""      ""Video ID: TbIwQMBeC2c""
  },
  {
    "{": ""      ""Video ID: dZsDU4dL_SY""
  },
  {
    "{": ""      ""Video ID: 244IMzOGpJs""
  },
  {
    "{": ""      ""Video ID: TNDbFfzGQng""
  },
  {
    "{": ""      ""Video ID: djDz9aJOI8k""
  },
  {
    "{": ""      ""Video ID: GAwe34puy8c""
  },
  {
    "{": ""      ""Video ID: RjmqPPZW2TQ""
  },
  {
    "{": ""      ""Video ID: C1jJmJfTrBI""
  },
  {
    "{": ""      ""Video ID: w39GiUzVPHs""
  },
  {
    "{": ""      ""Video ID: rNnBk02hBQE""
  },
  {
    "{": ""      ""Video ID: crloMfrJLKU""
  },
  {
    "{": ""      ""Video ID: xu_Mm9fA00E""
  },
  {
    "{": ""      ""Video ID: AqRYRaQMo6U""
  },
  {
    "{": ""      ""Video ID: o8Ph654OB_w""
  },
  {
    "{": ""      ""Video ID: llQH3hLQRB8""
  },
  {
    "{": ""      ""Video ID: 7fNuShaUt3k""
  },
  {
    "{": ""      ""Video ID: n8e450nbiKw""
  },
  {
    "{": ""      ""Video ID: cwXCoooOknA""
  },
  {
    "{": ""      ""Video ID: IQkn1iJcBpA""
  },
  {
    "{": ""      ""Video ID: BFPMjBhqbrM""
  },
  {
    "{": ""      ""Video ID: mxmGziYUtJM""
  },
  {
    "{": ""      ""Video ID: 4bY_UDJbjk0""
  },
  {
    "{": ""      ""Video ID: KS5LlzDZ2mA""
  },
  {
    "{": ""      ""Video ID: XCce9B4wVN0""
  },
  {
    "{": ""      ""Video ID: -h6fysPsTis""
  },
  {
    "{": ""      ""Video ID: Moby6F_W4qE""
  },
  {
    "{": ""      ""Video ID: vs00gC0PRWI""
  },
  {
    "{": ""      ""Video ID: q3dClw6wSs8""
  },
  {
    "{": ""      ""Video ID: SHm5DtkUk4o""
  },
  {
    "{": ""      ""Video ID: gGxY-ALoXv0""
  },
  {
    "{": ""      ""Video ID: dLRcIR1Akh4""
  },
  {
    "{": ""      ""Video ID: Msle1pKXq8A""
  },
  {
    "{": ""      ""Video ID: wWcergcmW0M""
  },
  {
    "{": ""      ""Video ID: v-g_316Xzzo""
  },
  {
    "{": ""      ""Video ID: 0z2N3rHwarA""
  },
  {
    "{": ""      ""Video ID: VAapbiofRBA""
  },
  {
    "{": ""      ""Video ID: 9bvAGNY_gvM""
  },
  {
    "{": ""      ""Video ID: WdTsZJtkYJM""
  },
  {
    "{": ""      ""Video ID: JwKWHQKX4xE""
  },
  {
    "{": ""      ""Video ID: x6SwC1yUn80""
  },
  {
    "{": ""      ""Video ID: S6zePkd1UNs""
  },
  {
    "{": ""      ""Video ID: OxRjyvtcnkw""
  },
  {
    "{": ""      ""Video ID: NrVQcj8fR2A""
  },
  {
    "{": ""      ""Video ID: mYJpzP0Vpbs""
  },
  {
    "{": ""      ""Video ID: BsRv-IS7Hjw""
  },
  {
    "{": ""      ""Video ID: FHCSmyQlDp4""
  },
  {
    "{": ""      ""Video ID: KYD-kANZvQw""
  },
  {
    "{": ""      ""Video ID: FPTJZGp4ViI""
  },
  {
    "{": ""      ""Video ID: F0qAeJSDk8c""
  },
  {
    "{": ""      ""Video ID: sAGDE0e9Msk""
  },
  {
    "{": ""      ""Video ID: j4rGOUvR3G4""
  },
  {
    "{": ""      ""Video ID: n1U2IQyFZok""
  },
  {
    "{": ""      ""Video ID: 4xie6rCmNS0""
  },
  {
    "{": ""      ""Video ID: CrOo40GZ5Ek""
  },
  {
    "{": ""      ""Video ID: uGnw6j0nHDE""
  },
  {
    "{": ""      ""Video ID: nJJDytnyCoo""
  },
  {
    "{": ""      ""Video ID: YKkQKvFidi4""
  },
  {
    "{": ""      ""Video ID: FN_tH_ZufaA""
  },
  {
    "{": ""      ""Video ID: nkfvQvc9ipI""
  },
  {
    "{": ""      ""Video ID: nwHZfZlI9bk""
  },
  {
    "{": ""      ""Video ID: U1Wb3TsiggI""
  },
  {
    "{": ""      ""Video ID: lSeazwhILo4""
  },
  {
    "{": ""      ""Video ID: KlSLiGrgjyE""
  },
  {
    "{": ""      ""Video ID: 2VVS70vMumw""
  },
  {
    "{": ""      ""Video ID: mkWju4IV9aU""
  },
  {
    "{": ""      ""Video ID: u33juJWjcmY""
  },
  {
    "{": ""      ""Video ID: 9MiKmOtYGgE""
  },
  {
    "{": ""      ""Video ID: t6100uVVhXs""
  },
  {
    "{": ""      ""Video ID: CJWkOlriaFc""
  },
  {
    "{": ""      ""Video ID: LDJtaxuD1FI""
  },
  {
    "{": ""      ""Video ID: z0s2l6nPQ9w""
  },
  {
    "{": ""      ""Video ID: uGFPdjc1RAw""
  },
  {
    "{": ""      ""Video ID: Db561jKucNQ""
  },
  {
    "{": ""      ""Video ID: lc4FzebZDXk""
  },
  {
    "{": ""      ""Video ID: SBTEsywsMEk""
  },
  {
    "{": ""      ""Video ID: blNYvtpuK6g""
  },
  {
    "{": ""      ""Video ID: Jk31242CnkU""
  },
  {
    "{": ""      ""Video ID: _rTq6lDtCsU""
  },
  {
    "{": ""      ""Video ID: vBDITmACFZ0""
  },
  {
    "{": ""      ""Video ID: 1XIRDAfo2UU""
  },
  {
    "{": ""      ""Video ID: 2mCt7WraJCc""
  },
  {
    "{": ""      ""Video ID: eMyGoKayYVI""
  },
  {
    "{": ""      ""Video ID: E3wDZtFSJ_Q""
  },
  {
    "{": ""      ""Video ID: Om7LxJIVkN0""
  },
  {
    "{": ""      ""Video ID: F5MhUO60qHY""
  },
  {
    "{": ""      ""Video ID: yTZCjFbec4Y""
  },
  {
    "{": ""      ""Video ID: u1dXMOds97E""
  },
  {
    "{": ""      ""Video ID: dWiy_FMdjxw""
  },
  {
    "{": ""      ""Video ID: scIf4HJqOcM""
  },
  {
    "{": ""      ""Video ID: o-7UON9ijkw""
  },
  {
    "{": ""      ""Video ID: mx_d9PD5Jio""
  },
  {
    "{": ""      ""Video ID: Tw4aQOdHwcI""
  },
  {
    "{": ""      ""Video ID: s6M_uf0OGpE""
  },
  {
    "{": ""      ""Video ID: fZzgHv3Ag-g""
  },
  {
    "{": ""      ""Video ID: 7kFxYKmqKao""
  },
  {
    "{": ""      ""Video ID: 40IOFELHVS4""
  },
  {
    "{": ""      ""Video ID: fPc4GCUxHVA""
  },
  {
    "{": ""      ""Video ID: DR2Oioi7CU0""
  },
  {
    "{": ""      ""Video ID: ncbBOEoV4PE""
  },
  {
    "{": ""      ""Video ID: msJc7rT--Vw""
  },
  {
    "{": ""      ""Video ID: Lpi1Q2X3Y6s""
  },
  {
    "{": ""      ""Video ID: FRObiTAdATU""
  },
  {
    "{": ""      ""Video ID: v34GN0IvPWc""
  },
  {
    "{": ""      ""Video ID: K77Fx7hei8I""
  },
  {
    "{": ""      ""Video ID: Wiapjhw80sE""
  },
  {
    "{": ""      ""Video ID: UngkawZUksw""
  },
  {
    "{": ""      ""Video ID: S98Xjx3LMYk""
  },
  {
    "{": ""      ""Video ID: YqsoLwu--As""
  },
  {
    "{": ""      ""Video ID: 4Q4ZG_ADSMA""
  },
  {
    "{": ""      ""Video ID: n5QypK_0Ofg""
  },
  {
    "{": ""      ""Video ID: rnqNV3k2B6A""
  },
  {
    "{": ""      ""Video ID: Oy9LroX_RpI""
  },
  {
    "{": ""      ""Video ID: Dn6uqnOALJ0""
  },
  {
    "{": ""      ""Video ID: d5LEwHbKCqw""
  },
  {
    "{": ""      ""Video ID: AZPH14zZi9M""
  },
  {
    "{": ""      ""Video ID: yWlMQUSv96E""
  },
  {
    "{": ""      ""Video ID: ol-wk2alxec""
  },
  {
    "{": ""      ""Video ID: ni6iQjzrZ3w""
  },
  {
    "{": ""      ""Video ID: RT7uQfY_HP0""
  },
  {
    "{": ""      ""Video ID: 8-VPUaY-uIs""
  },
  {
    "{": ""      ""Video ID: gmOI2adSYmQ""
  },
  {
    "{": ""      ""Video ID: 00U8E055Upg""
  },
  {
    "{": ""      ""Video ID: h6oK6yWfg6w""
  },
  {
    "{": ""      ""Video ID: MGpULXuKOfQ""
  },
  {
    "{": ""      ""Video ID: 3VOxuvBznC8""
  },
  {
    "{": ""      ""Video ID: _e8rISDg-ik""
  },
  {
    "{": ""      ""Video ID: agHCaK_iaoc""
  },
  {
    "{": ""      ""Video ID: m7wW7xioE_g""
  },
  {
    "{": ""      ""Video ID: Oe9V8dEFedg""
  },
  {
    "{": ""      ""Video ID: dQs_8lP_dl4""
  },
  {
    "{": ""      ""Video ID: MQmIIH5Byf4""
  },
  {
    "{": ""      ""Video ID: PX8kacMmuoo""
  },
  {
    "{": ""      ""Video ID: 0OshjnMPLhE""
  },
  {
    "{": ""      ""Video ID: YoPYifUB49c""
  },
  {
    "{": ""      ""Video ID: VOKRozgU4Rc""
  },
  {
    "{": ""      ""Video ID: At7pMECywGw""
  },
  {
    "{": ""      ""Video ID: J9j8G5_Dh9s""
  },
  {
    "{": ""      ""Video ID: Xyv2N7N9s3c""
  },
  {
    "{": ""      ""Video ID: kUdG2vMbTWY""
  },
  {
    "{": ""      ""Video ID: 0dG15H-j5QU""
  },
  {
    "{": ""      ""Video ID: fyc5DO25p1w""
  },
  {
    "{": ""      ""Video ID: vNo9DFXfdJE""
  },
  {
    "{": ""      ""Video ID: 4E0aIEPTYOY""
  },
  {
    "{": ""      ""Video ID: puOnH1IsrLs""
  },
  {
    "{": ""      ""Video ID: 70TpoveOA-0""
  },
  {
    "{": ""      ""Video ID: gRCGuHMFC8k""
  },
  {
    "{": ""      ""Video ID: JWrKbO9Udmg""
  },
  {
    "{": ""      ""Video ID: EX5sU2i5KTM""
  },
  {
    "{": ""      ""Video ID: kgAD3j8pG58""
  },
  {
    "{": ""      ""Video ID: dVZL4NJXF7c""
  },
  {
    "{": ""      ""Video ID: Bj4SkEE-kN0""
  },
  {
    "{": ""      ""Video ID: TuM382Nwt04""
  },
  {
    "{": ""      ""Video ID: a61KcuuYeos""
  },
  {
    "{": ""      ""Video ID: uNpBTzNvHi4""
  },
  {
    "{": ""      ""Video ID: QTIH7BXCyKc""
  },
  {
    "{": ""      ""Video ID: GQvBcvFEJbQ""
  },
  {
    "{": ""      ""Video ID: EuOAZbHGlkQ""
  },
  {
    "{": ""      ""Video ID: SlS2mUi6_k4""
  },
  {
    "{": ""      ""Video ID: h5jj1_mxiUk""
  },
  {
    "{": ""      ""Video ID: TuNP_rFu91I""
  },
  {
    "{": ""      ""Video ID: jUrtrX1vaEo""
  },
  {
    "{": ""      ""Video ID: M75MlZa9whk""
  },
  {
    "{": ""      ""Video ID: wjfm9Sx04A0""
  },
  {
    "{": ""      ""Video ID: g9mEUOpoWdg""
  },
  {
    "{": ""      ""Video ID: 79dBmaHEPUY""
  },
  {
    "{": ""      ""Video ID: XBSUbf20yLk""
  },
  {
    "{": ""      ""Video ID: gJakLqEilrs""
  },
  {
    "{": ""      ""Video ID: EBoB20shjsc""
  },
  {
    "{": ""      ""Video ID: fliU5c1XpGI""
  },
  {
    "{": ""      ""Video ID: jJmZyGKGgoE""
  },
  {
    "{": ""      ""Video ID: RR3gXqCaVZI""
  },
  {
    "{": ""      ""Video ID: KwY8yfcVWoA""
  },
  {
    "{": ""      ""Video ID: KulstiOmw30""
  },
  {
    "{": ""      ""Video ID: WXazMx51e0o""
  },
  {
    "{": ""      ""Video ID: iKeHvjC__Ng""
  },
  {
    "{": ""      ""Video ID: BDSIuAg8F_U""
  },
  {
    "{": ""      ""Video ID: cqoxedHrf_g""
  },
  {
    "{": ""      ""Video ID: DTzs9bcNgMQ""
  },
  {
    "{": ""      ""Video ID: I0Wchb2C7nU""
  },
  {
    "{": ""      ""Video ID: J31klTM6q78""
  },
  {
    "{": ""      ""Video ID: sTNpC6lYYrs""
  },
  {
    "{": ""      ""Video ID: EcqL8N9NReQ""
  },
  {
    "{": ""      ""Video ID: nGQKNzPDTio""
  },
  {
    "{": ""      ""Video ID: hUoJBerFDsA""
  },
  {
    "{": ""      ""Video ID: VuPja5y4RfI""
  },
  {
    "{": ""      ""Video ID: xzgHPJ-_Ed0""
  },
  {
    "{": ""      ""Video ID: KIcnEL8Ym4I""
  },
  {
    "{": ""      ""Video ID: 87J1gQkz71o""
  },
  {
    "{": ""      ""Video ID: lOS1EF4XQYs""
  },
  {
    "{": ""      ""Video ID: W90gx91uSjc""
  },
  {
    "{": ""      ""Video ID: gV_X17iP0AQ""
  },
  {
    "{": ""      ""Video ID: Ak2j9x9Ts_k""
  },
  {
    "{": ""      ""Video ID: vetyGCqJ_rU""
  },
  {
    "{": ""      ""Video ID: fn02le8e0nQ""
  },
  {
    "{": ""      ""Video ID: wVrRT82Up6U""
  },
  {
    "{": ""      ""Video ID: jznoeOW4DdA""
  },
  {
    "{": ""      ""Video ID: WiS9e-ZMh1U""
  },
  {
    "{": ""      ""Video ID: dm-PC7u69xw""
  },
  {
    "{": ""      ""Video ID: nkvBAqt5y_k""
  },
  {
    "{": ""      ""Video ID: 3B6cJ7S6saY""
  },
  {
    "{": ""      ""Video ID: 4U0EDVSgm7M""
  },
  {
    "{": ""      ""Video ID: jEJ3l0MlzGI""
  },
  {
    "{": ""      ""Video ID: 3SPfSBhVf60""
  },
  {
    "{": ""      ""Video ID: 72d31-K2mi4""
  },
  {
    "{": ""      ""Video ID: SyhT27D8Nx8""
  },
  {
    "{": ""      ""Video ID: eGhuWW2vf9Q""
  },
  {
    "{": ""      ""Video ID: DeVbMiqVuV0""
  },
  {
    "{": ""      ""Video ID: JUbMGNOew50""
  },
  {
    "{": ""      ""Video ID: B3PAhNHVQ7Y""
  },
  {
    "{": ""      ""Video ID: eRfZRXDdy1s""
  },
  {
    "{": ""      ""Video ID: mslyfxJd0T0""
  },
  {
    "{": ""      ""Video ID: HajjMFjdzPg""
  },
  {
    "{": ""      ""Video ID: M5D3l1mq08g""
  },
  {
    "{": ""      ""Video ID: Y8_yLjtekaM""
  },
  {
    "{": ""      ""Video ID: k-cbiYzlHOk""
  },
  {
    "{": ""      ""Video ID: 20Of_mna-Rs""
  },
  {
    "{": ""      ""Video ID: taOxwemkZvs""
  },
  {
    "{": ""      ""Video ID: oqJ02u2Lv2Y""
  },
  {
    "{": ""      ""Video ID: sSy88EtEX_g""
  },
  {
    "{": ""      ""Video ID: hhIGuPrZJ6E""
  },
  {
    "{": ""      ""Video ID: 0pAmVipomcA""
  },
  {
    "{": ""      ""Video ID: h3LiXJOQ8I0""
  },
  {
    "{": ""      ""Video ID: tpnkmIi1o6M""
  },
  {
    "{": ""      ""Video ID: 2DYfBmIDbtw""
  },
  {
    "{": ""      ""Video ID: u1iCFLRqwx8""
  },
  {
    "{": ""      ""Video ID: cDusenm5-ho""
  },
  {
    "{": ""      ""Video ID: EGFyX0_lygg""
  },
  {
    "{": ""      ""Video ID: -utkZVqCIrs""
  },
  {
    "{": ""      ""Video ID: XD9CuMwD5PI""
  },
  {
    "{": ""      ""Video ID: xnUFuJcInH0""
  },
  {
    "{": ""      ""Video ID: QH8FX38_PR8""
  },
  {
    "{": ""      ""Video ID: 83C216WsYmc""
  },
  {
    "{": ""      ""Video ID: 67qytrErmaE""
  },
  {
    "{": ""      ""Video ID: tTRGww2So7U""
  },
  {
    "{": ""      ""Video ID: m1IRxTN-_kU""
  },
  {
    "{": ""      ""Video ID: 6WVS-isbG9Y""
  },
  {
    "{": ""      ""Video ID: cL-mR79GErU""
  },
  {
    "{": ""      ""Video ID: 6Scukhxt2wo""
  },
  {
    "{": ""      ""Video ID: 4wvBKFQIAdo""
  },
  {
    "{": ""      ""Video ID: Gzu5UeSldqw""
  },
  {
    "{": ""      ""Video ID: C_hM0kimMp0""
  },
  {
    "{": ""      ""Video ID: RCU_UoW2pKY""
  },
  {
    "{": ""      ""Video ID: FjSUudLvBAs""
  },
  {
    "{": ""      ""Video ID: t-e6zY27-Ik""
  },
  {
    "{": ""      ""Video ID: ILYpzscQZlY""
  },
  {
    "{": ""      ""Video ID: tod0bLkbZaA""
  },
  {
    "{": ""      ""Video ID: itMsBf60SVk""
  },
  {
    "{": ""      ""Video ID: Rq6nFyCL6FU""
  },
  {
    "{": ""      ""Video ID: GunrtW4-JbM""
  },
  {
    "{": ""      ""Video ID: CuBg5gwcX0Q""
  },
  {
    "{": ""      ""Video ID: R5nQ3IGGKac""
  },
  {
    "{": ""      ""Video ID: 8jEIRr0cTF8""
  },
  {
    "{": ""      ""Video ID: 4l1KxyYjaHU""
  },
  {
    "{": ""      ""Video ID: fHAK5DDNF3k""
  },
  {
    "{": ""      ""Video ID: bqcB4sdhCjs""
  },
  {
    "{": ""      ""Video ID: EVUGVjrUq_E""
  },
  {
    "{": ""      ""Video ID: 6UtjWp2WPLI""
  },
  {
    "{": ""      ""Video ID: -um0OuVokLE""
  },
  {
    "{": ""      ""Video ID: psKF_s8jFAI""
  },
  {
    "{": ""      ""Video ID: 2419ZwUtrFQ""
  },
  {
    "{": ""      ""Video ID: AhawXgfK--g""
  },
  {
    "{": ""      ""Video ID: rNNU887A-8g""
  },
  {
    "{": ""      ""Video ID: Fs299lPuYZo""
  },
  {
    "{": ""      ""Video ID: 1CFt1aeMa9I""
  },
  {
    "{": ""      ""Video ID: SC8AsyZFqPc""
  },
  {
    "{": ""      ""Video ID: jGBNRGdebVE""
  },
  {
    "{": ""      ""Video ID: rhcTCU_v83o""
  },
  {
    "{": ""      ""Video ID: iqDoBbcI_tM""
  },
  {
    "{": ""      ""Video ID: PgeEBxFcEZY""
  },
  {
    "{": ""      ""Video ID: 15NX2UE-Sdw""
  },
  {
    "{": ""      ""Video ID: uQImF5NB9mg""
  },
  {
    "{": ""      ""Video ID: WgPQoM5ZZoo""
  },
  {
    "{": ""      ""Video ID: XWqkYWHB89Q""
  },
  {
    "{": ""      ""Video ID: wLsggQbnOSE""
  },
  {
    "{": ""      ""Video ID: dzli5ZunLoc""
  },
  {
    "{": ""      ""Video ID: rVh5EuFrmuA""
  },
  {
    "{": ""      ""Video ID: I0_cmPDXR-4""
  },
  {
    "{": ""      ""Video ID: 5NrAFzZd95Y""
  },
  {
    "{": ""      ""Video ID: IF6wkye_nis""
  },
  {
    "{": ""      ""Video ID: 9LO03pd6X-4""
  },
  {
    "{": ""      ""Video ID: ASW3UCc17AI""
  },
  {
    "{": ""      ""Video ID: opoCilsdCWk""
  },
  {
    "{": ""      ""Video ID: 2irxOKNQoVg""
  },
  {
    "{": ""      ""Video ID: OCqMxW5u_Lw""
  },
  {
    "{": ""      ""Video ID: Q1floOvTmIs""
  },
  {
    "{": ""      ""Video ID: KjItCybkLj8""
  },
  {
    "{": ""      ""Video ID: EylRlsPqf2E""
  },
  {
    "{": ""      ""Video ID: koaBmFAQLHE""
  },
  {
    "{": ""      ""Video ID: HvB2nhfTlmg""
  },
  {
    "{": ""      ""Video ID: wYrV9M6Pd2g""
  },
  {
    "{": ""      ""Video ID: MdQ1ecBrue4""
  },
  {
    "{": ""      ""Video ID: dwo9jnqE2Sc""
  },
  {
    "{": ""      ""Video ID: mywacnA8WmI""
  },
  {
    "{": ""      ""Video ID: D3LFX77FnmE""
  },
  {
    "{": ""      ""Video ID: cLoM3lH3qJ8""
  },
  {
    "{": ""      ""Video ID: fcoSgjC44eM""
  },
  {
    "{": ""      ""Video ID: eTf85cD0BmA""
  },
  {
    "{": ""      ""Video ID: kEuo4UnkxmI""
  },
  {
    "{": ""      ""Video ID: x98wIMPKowY""
  },
  {
    "{": ""      ""Video ID: XBE-pBB04ok""
  },
  {
    "{": ""      ""Video ID: W0dyvoVV5Tk""
  },
  {
    "{": ""      ""Video ID: hRzm4SkzsnM""
  },
  {
    "{": ""      ""Video ID: HbR7PoyioDk""
  },
  {
    "{": ""      ""Video ID: CIxk7LvGf_A""
  },
  {
    "{": ""      ""Video ID: QTpBAr5tH3c""
  },
  {
    "{": ""      ""Video ID: pr-MFw4g-_E""
  },
  {
    "{": ""      ""Video ID: ntdtnF0ln08""
  },
  {
    "{": ""      ""Video ID: 7mACbHxcAAM""
  },
  {
    "{": ""      ""Video ID: WWrgfk1gl_s""
  },
  {
    "{": ""      ""Video ID: 78txYZMRxj4""
  },
  {
    "{": ""      ""Video ID: 4JgNs6x3syU""
  },
  {
    "{": ""      ""Video ID: FNeYb31mLUs""
  },
  {
    "{": ""      ""Video ID: ML02nf6t3rA""
  },
  {
    "{": ""      ""Video ID: Q9skthaumao""
  },
  {
    "{": ""      ""Video ID: OEHGNpxlQSU""
  },
  {
    "{": ""      ""Video ID: A8vmB_ykeTs""
  },
  {
    "{": ""      ""Video ID: TiWcq6cdqF4""
  },
  {
    "{": ""      ""Video ID: kKfzWILcfP0""
  },
  {
    "{": ""      ""Video ID: rS4EhwvF0MA""
  },
  {
    "{": ""      ""Video ID: 9Mn647_xLWg""
  },
  {
    "{": ""      ""Video ID: NYRzGASljMc""
  },
  {
    "{": ""      ""Video ID: htXZ0tJHmrU""
  },
  {
    "{": ""      ""Video ID: aIjcaEyr23k""
  },
  {
    "{": ""      ""Video ID: OnSThxLRBW4""
  },
  {
    "{": ""      ""Video ID: 0U3iqMLLaUQ""
  },
  {
    "{": ""      ""Video ID: vZ1xepJ3W70""
  },
  {
    "{": ""      ""Video ID: wQiodDx2xcM""
  },
  {
    "{": ""      ""Video ID: lrmhkL-tNnk""
  },
  {
    "{": ""      ""Video ID: HvUFrEu1xVc""
  },
  {
    "{": ""      ""Video ID: Ln_DuSykoro""
  },
  {
    "{": ""      ""Video ID: uQze4dTsVjM""
  },
  {
    "{": ""      ""Video ID: 6vFTrnVLPvE""
  },
  {
    "{": ""      ""Video ID: xZ0S3gtqrcA""
  },
  {
    "{": ""      ""Video ID: dyj5DSxP9NU""
  },
  {
    "{": ""      ""Video ID: g9phYP24crY""
  },
  {
    "{": ""      ""Video ID: ad6ptd281wg""
  },
  {
    "{": ""      ""Video ID: tOIv3aEhdcU""
  },
  {
    "{": ""      ""Video ID: nLOrPiDPuz8""
  },
  {
    "{": ""      ""Video ID: QqpeLU-tJP8""
  },
  {
    "{": ""      ""Video ID: yGbFrCoLX7o""
  },
  {
    "{": ""      ""Video ID: QBXI8H3aRck""
  },
  {
    "{": ""      ""Video ID: OBb5fuOoiJA""
  },
  {
    "{": ""      ""Video ID: DpGNqb-AlJ8""
  },
  {
    "{": ""      ""Video ID: BtMkF4PfA5g""
  },
  {
    "{": ""      ""Video ID: LRB9MbJwhik""
  },
  {
    "{": ""      ""Video ID: lSY1h4Lvxq0""
  },
  {
    "{": ""      ""Video ID: d_-aN3fffEs""
  },
  {
    "{": ""      ""Video ID: z_GccpxH1R8""
  },
  {
    "{": ""      ""Video ID: PVoNiX8IfZE""
  },
  {
    "{": ""      ""Video ID: IX7g2WfJNLg""
  },
  {
    "{": ""      ""Video ID: a-ZXLZrxkHg""
  },
  {
    "{": ""      ""Video ID: CBi8p0KAznQ""
  },
  {
    "{": ""      ""Video ID: 6EYOGD1hcmM""
  },
  {
    "{": ""      ""Video ID: 3oSmQYYzMaQ""
  },
  {
    "{": ""      ""Video ID: WH3N72upypw""
  },
  {
    "{": ""      ""Video ID: 6mfy1vhy-tE""
  },
  {
    "{": ""      ""Video ID: qdilScQRoYQ""
  },
  {
    "{": ""      ""Video ID: f2SAAo5x9Mg""
  },
  {
    "{": ""      ""Video ID: Nqe_jE41RnY""
  },
  {
    "{": ""      ""Video ID: aqOE5SmtwT0""
  },
  {
    "{": ""      ""Video ID: T5PPu1d-4G0""
  },
  {
    "{": ""      ""Video ID: WbfiVfYuoJo""
  },
  {
    "{": ""      ""Video ID: fbHxZlOuDkI""
  },
  {
    "{": ""      ""Video ID: UQSCzrKnbpQ""
  },
  {
    "{": ""      ""Video ID: 3xT_FlLr_KY""
  },
  {
    "{": ""      ""Video ID: r1bOK84TuWk""
  },
  {
    "{": ""      ""Video ID: CjH450b_bS8""
  },
  {
    "{": ""      ""Video ID: 3RuyfQF4bMM""
  },
  {
    "{": ""      ""Video ID: 8FKTZAfsFbA""
  },
  {
    "{": ""      ""Video ID: LfylNDDAB_c""
  },
  {
    "{": ""      ""Video ID: h2q8ZaErmKo""
  },
  {
    "{": ""      ""Video ID: FtSvL-03FDE""
  },
  {
    "{": ""      ""Video ID: QGIISxhYRYE""
  },
  {
    "{": ""      ""Video ID: Ffd9iGRwrHQ""
  },
  {
    "{": ""      ""Video ID: TgL6TRlOLug""
  },
  {
    "{": ""      ""Video ID: 0CUdWCyw10Y""
  },
  {
    "{": ""      ""Video ID: dtBY9nOlpoo""
  },
  {
    "{": ""      ""Video ID: OYzRlPlJ09U""
  },
  {
    "{": ""      ""Video ID: d-nHxS3cCKA""
  },
  {
    "{": ""      ""Video ID: iJPCHSUkruo""
  },
  {
    "{": ""      ""Video ID: Y8klW9trVTQ""
  },
  {
    "{": ""      ""Video ID: w6sFzWjaFEY""
  },
  {
    "{": ""      ""Video ID: tFI1h10I7Xs""
  },
  {
    "{": ""      ""Video ID: j9cLaGX8xb8""
  },
  {
    "{": ""      ""Video ID: P91azQ9ofGI""
  },
  {
    "{": ""      ""Video ID: g6M7Ty6cIMc""
  },
  {
    "{": ""      ""Video ID: IwPAnLxLhwE""
  },
  {
    "{": ""      ""Video ID: dYenNQR-eXc""
  },
  {
    "{": ""      ""Video ID: sGv-H_UA05Y""
  },
  {
    "{": ""      ""Video ID: IROmpFvRNf8""
  },
  {
    "{": ""      ""Video ID: iAVClgEG-iY""
  },
  {
    "{": ""      ""Video ID: 103UZZmEDDo""
  },
  {
    "{": ""      ""Video ID: tGwo5KoLpH0""
  },
  {
    "{": ""      ""Video ID: 8owXF_cMcO4""
  },
  {
    "{": ""      ""Video ID: BC8QcbwZbkc""
  },
  {
    "{": ""      ""Video ID: ulPT9c5souY""
  },
  {
    "{": ""      ""Video ID: lOM3qQh1fSY""
  },
  {
    "{": ""      ""Video ID: EpkcjCvQJes""
  },
  {
    "{": ""      ""Video ID: NPQQfLMunm0""
  },
  {
    "{": ""      ""Video ID: pbtHz5d_G90""
  },
  {
    "{": ""      ""Video ID: UhXmibpXIKs""
  },
  {
    "{": ""      ""Video ID: f9Ec7YofnUc""
  },
  {
    "{": ""      ""Video ID: qupv6VLgyBQ""
  },
  {
    "{": ""      ""Video ID: ZXEzMSWCeg8""
  },
  {
    "{": ""      ""Video ID: J8aWG8SYAQ0""
  },
  {
    "{": ""      ""Video ID: pkmPPQkA6cQ""
  },
  {
    "{": ""      ""Video ID: rFpbBm7JHLs""
  },
  {
    "{": ""      ""Video ID: Q5ShSs4KvS8""
  },
  {
    "{": ""      ""Video ID: SW8aPcobIZA""
  },
  {
    "{": ""      ""Video ID: sJzHve5RW30""
  },
  {
    "{": ""      ""Video ID: qs3RKZjSzYg""
  },
  {
    "{": ""      ""Video ID: g8Q2Db17v5U""
  },
  {
    "{": ""      ""Video ID: qvmR1exv0ro""
  },
  {
    "{": ""      ""Video ID: 5l_c7MH-auA""
  },
  {
    "{": ""      ""Video ID: VXo-_cCffDk""
  },
  {
    "{": ""      ""Video ID: Q65HpJGg2Bg""
  },
  {
    "{": ""      ""Video ID: w81JS35b5gw""
  },
  {
    "{": ""      ""Video ID: beA5yJIA64s""
  },
  {
    "{": ""      ""Video ID: dJ_zNIMqmMc""
  },
  {
    "{": ""      ""Video ID: H2GawXV47xk""
  },
  {
    "{": ""      ""Video ID: 60yjTLXdK7M""
  },
  {
    "{": ""      ""Video ID: M5NVmr-mV7w""
  },
  {
    "{": ""      ""Video ID: QiTydz7jWj0""
  },
  {
    "{": ""      ""Video ID: wKqf6rfEsSk""
  },
  {
    "{": ""      ""Video ID: _BQhW4txyQI""
  },
  {
    "{": ""      ""Video ID: y3PtTpi9BmU""
  },
  {
    "{": ""      ""Video ID: YStvujyySZs""
  },
  {
    "{": ""      ""Video ID: 6FQpPRNDKWM""
  },
  {
    "{": ""      ""Video ID: jaLoaXzJoLU""
  },
  {
    "{": ""      ""Video ID: IY95lfigBvI""
  },
  {
    "{": ""      ""Video ID: XkQAFohGRZU""
  },
  {
    "{": ""      ""Video ID: 7CIHPor_haA""
  },
  {
    "{": ""      ""Video ID: xZuknsnphEU""
  },
  {
    "{": ""      ""Video ID: vyboXCIVJY0""
  },
  {
    "{": ""      ""Video ID: XT-mrvrPJIs""
  },
  {
    "{": ""      ""Video ID: BZUVVt1MGts""
  },
  {
    "{": ""      ""Video ID: 68X1wbKHX34""
  },
  {
    "{": ""      ""Video ID: TIZT9Apv8aE""
  },
  {
    "{": ""      ""Video ID: E4RH4RD9kSE""
  },
  {
    "{": ""      ""Video ID: averBTstkPI""
  },
  {
    "{": ""      ""Video ID: 6bFyFcbJT4U""
  },
  {
    "{": ""      ""Video ID: UUu0DNPlv5Y""
  },
  {
    "{": ""      ""Video ID: zWYsOQ4-eJ4""
  },
  {
    "{": ""      ""Video ID: JfchN7G-oQk""
  },
  {
    "{": ""      ""Video ID: -tCBWWNha8Y""
  },
  {
    "{": ""      ""Video ID: roDhWM_Rtj4""
  },
  {
    "{": ""      ""Video ID: VsZx36kVMxo""
  },
  {
    "{": ""      ""Video ID: oCJxeHcPgUM""
  },
  {
    "{": ""      ""Video ID: RwUNbSZD-vs""
  },
  {
    "{": ""      ""Video ID: tHxok-hv6ok""
  },
  {
    "{": ""      ""Video ID: F6XwOmjb0IU""
  },
  {
    "{": ""      ""Video ID: yR3Z-8DCKqI""
  },
  {
    "{": ""      ""Video ID: sLwKjZlramI""
  },
  {
    "{": ""      ""Video ID: etvnHjl9VEY""
  },
  {
    "{": ""      ""Video ID: HrPsxq_He7E""
  },
  {
    "{": ""      ""Video ID: 7MusUFHe89E""
  },
  {
    "{": ""      ""Video ID: 7nD7dbkkBIA""
  },
  {
    "{": ""      ""Video ID: _v6xUGSrApk""
  },
  {
    "{": ""      ""Video ID: mNv79hywH8c""
  },
  {
    "{": ""      ""Video ID: NNC9oJyHEc8""
  },
  {
    "{": ""      ""Video ID: cU_cftIagzA""
  },
  {
    "{": ""      ""Video ID: 0JODIAqxTrA""
  },
  {
    "{": ""      ""Video ID: NDpAVFC5sm8""
  },
  {
    "{": ""      ""Video ID: dZU5X_SDvV4""
  },
  {
    "{": ""      ""Video ID: OG6dslMSxhw""
  },
  {
    "{": ""      ""Video ID: mEMrUfJypO4""
  },
  {
    "{": ""      ""Video ID: UPjykjiwiEc""
  },
  {
    "{": ""      ""Video ID: pjcmBaE2uG8""
  },
  {
    "{": ""      ""Video ID: mPFGALIqlCg""
  },
  {
    "{": ""      ""Video ID: yP95DtwldIk""
  },
  {
    "{": ""      ""Video ID: HK9y_twG3L0""
  },
  {
    "{": ""      ""Video ID: d-O38-nmNao""
  },
  {
    "{": ""      ""Video ID: A0DyT6gQaGQ""
  },
  {
    "{": ""      ""Video ID: ue-PwHC6oPQ""
  },
  {
    "{": ""      ""Video ID: ivfDtc9uaTM""
  },
  {
    "{": ""      ""Video ID: vCX9btvgR8o""
  },
  {
    "{": ""      ""Video ID: txIThKhZXkQ""
  },
  {
    "{": ""      ""Video ID: 9tz0SxNP5YM""
  },
  {
    "{": ""      ""Video ID: 6HNAy43lenE""
  },
  {
    "{": ""      ""Video ID: az902dSgaRI""
  },
  {
    "{": ""      ""Video ID: 89Iah2mwY58""
  },
  {
    "{": ""      ""Video ID: 1RC26_xEYt0""
  },
  {
    "{": ""      ""Video ID: uUyPYwhNl0c""
  },
  {
    "{": ""      ""Video ID: NZsqQpem30k""
  },
  {
    "{": ""      ""Video ID: z4sWLdfLYf8""
  },
  {
    "{": ""      ""Video ID: BCjwVOtpHss""
  },
  {
    "{": ""      ""Video ID: twLd0UCsZxw""
  },
  {
    "{": ""      ""Video ID: 4gvKZXH48AQ""
  },
  {
    "{": ""      ""Video ID: i0kEjttb2mE""
  },
  {
    "{": ""      ""Video ID: vwFP6DmgY-U""
  },
  {
    "{": ""      ""Video ID: tzuTXnY8ShY""
  },
  {
    "{": ""      ""Video ID: 12qM_GBcY6A""
  },
  {
    "{": ""      ""Video ID: wcyfHdAU-TI""
  },
  {
    "{": ""      ""Video ID: b0-6fUWvfFA""
  },
  {
    "{": ""      ""Video ID: rOxAd2KN-ck""
  },
  {
    "{": ""      ""Video ID: IXtKWVNCsWM""
  },
  {
    "{": ""      ""Video ID: 1rnO2FjzBIA""
  },
  {
    "{": ""      ""Video ID: TP3NkTQ_4i4""
  },
  {
    "{": ""      ""Video ID: HiAvr_ufeQc""
  },
  {
    "{": ""      ""Video ID: qsZTbJyB7io""
  },
  {
    "{": ""      ""Video ID: tedtnuQ0Yw4""
  },
  {
    "{": ""      ""Video ID: apJSoAO7kL0""
  },
  {
    "{": ""      ""Video ID: PopRsOJHNWc""
  },
  {
    "{": ""      ""Video ID: 8QoqBVvNx_Y""
  },
  {
    "{": ""      ""Video ID: fJGS1UlWf34""
  },
  {
    "{": ""      ""Video ID: OivWwblC1L0""
  },
  {
    "{": ""      ""Video ID: XsdjYEFgGys""
  },
  {
    "{": ""      ""Video ID: y2_pGjWKTm8""
  },
  {
    "{": ""      ""Video ID: VuHzzQyeV1w""
  },
  {
    "{": ""      ""Video ID: gsjLEbPbaH8""
  },
  {
    "{": ""      ""Video ID: MnRPZOUVhJ4""
  },
  {
    "{": ""      ""Video ID: uutq2ih1HRg""
  },
  {
    "{": ""      ""Video ID: 5P9XPYWrCdE""
  },
  {
    "{": ""      ""Video ID: VKye2F8vG7s""
  },
  {
    "{": ""      ""Video ID: YsP8bXuV3yE""
  },
  {
    "{": ""      ""Video ID: w4M-iWtmJMs""
  },
  {
    "{": ""      ""Video ID: avsqo5Z_bdk""
  },
  {
    "{": ""      ""Video ID: vuvhhYO29bk""
  },
  {
    "{": ""      ""Video ID: FDccpojS228""
  },
  {
    "{": ""      ""Video ID: taH3qthvxfo""
  },
  {
    "{": ""      ""Video ID: DaaKFSWXUP0""
  },
  {
    "{": ""      ""Video ID: U1E9BpFgAgU""
  },
  {
    "{": ""      ""Video ID: ZRx7l1gaBos""
  },
  {
    "{": ""      ""Video ID: GZbeIELpDSY""
  },
  {
    "{": ""      ""Video ID: nmDx8VGD-2M""
  },
  {
    "{": ""      ""Video ID: vUDy7EGI5sQ""
  },
  {
    "{": ""      ""Video ID: ZsSHainoMT4""
  },
  {
    "{": ""      ""Video ID: sDWpFgmB4eo""
  },
  {
    "{": ""      ""Video ID: _MhqkWLDRuY""
  },
  {
    "{": ""      ""Video ID: 1CjvmtbcZ1k""
  },
  {
    "{": ""      ""Video ID: 2jJ_e9QlkEQ""
  },
  {
    "{": ""      ""Video ID: Llu0FktCvlQ""
  },
  {
    "{": ""      ""Video ID: xk0Jpnt0JcY""
  },
  {
    "{": ""      ""Video ID: h0nQSOhDW-k""
  },
  {
    "{": ""      ""Video ID: Xxv3bU6QPSY""
  },
  {
    "{": ""      ""Video ID: uT5P-ASP-9w""
  },
  {
    "{": ""      ""Video ID: sJVICLDooYU""
  },
  {
    "{": ""      ""Video ID: t6AwmDDdGm8""
  },
  {
    "{": ""      ""Video ID: ZRaTCPsKrdY""
  },
  {
    "{": ""      ""Video ID: 0FELcZssp1I""
  },
  {
    "{": ""      ""Video ID: gGoz4y6QIjk""
  },
  {
    "{": ""      ""Video ID: eOS20plm7UM""
  },
  {
    "{": ""      ""Video ID: 4aCArkFMqeE""
  },
  {
    "{": ""      ""Video ID: rK6Hz98hrBw""
  },
  {
    "{": ""      ""Video ID: UB_OmkXK89o""
  },
  {
    "{": ""      ""Video ID: tG9jexb0uZg""
  },
  {
    "{": ""      ""Video ID: VAscAiy-CpQ""
  },
  {
    "{": ""      ""Video ID: dH28QFyJSTU""
  },
  {
    "{": ""      ""Video ID: PVoiSetJYiE""
  },
  {
    "{": ""      ""Video ID: q7yTUpwlCZY""
  },
  {
    "{": ""      ""Video ID: H_AP0xErYms""
  },
  {
    "{": ""      ""Video ID: w--CRrLdZq0""
  },
  {
    "{": ""      ""Video ID: UxvYpfWJn1o""
  },
  {
    "{": ""      ""Video ID: 9aMXWw4JigI""
  },
  {
    "{": ""      ""Video ID: VSzP9fhLQm8""
  },
  {
    "{": ""      ""Video ID: vXJbp1MpI4I""
  },
  {
    "{": ""      ""Video ID: L3-2gEP4xPY""
  },
  {
    "{": ""      ""Video ID: m3T9KYVhVnI""
  },
  {
    "{": ""      ""Video ID: i4K3mqp3EDo""
  },
  {
    "{": ""      ""Video ID: eqd1xT1mts8""
  },
  {
    "{": ""      ""Video ID: s5qQbJyLPYU""
  },
  {
    "{": ""      ""Video ID: E-Y1WO_kWtg""
  },
  {
    "{": ""      ""Video ID: -ckdvwHSTuI""
  },
  {
    "{": ""      ""Video ID: dNJhMZiktow""
  },
  {
    "{": ""      ""Video ID: P9CxPTZh0ao""
  },
  {
    "{": ""      ""Video ID: tyvkBG-D72o""
  },
  {
    "{": ""      ""Video ID: Cf84oq8050g""
  },
  {
    "{": ""      ""Video ID: lzoG27mSmlA""
  },
  {
    "{": ""      ""Video ID: likIT6NV05A""
  },
  {
    "{": ""      ""Video ID: 0KGYsMjLlPs""
  },
  {
    "{": ""      ""Video ID: mGw2tQLGjaw""
  },
  {
    "{": ""      ""Video ID: Pf7izXdJKrc""
  },
  {
    "{": ""      ""Video ID: B-EJ9dQ5BmA""
  },
  {
    "{": ""      ""Video ID: pophXFPSmc0""
  },
  {
    "{": ""      ""Video ID: TJaYwGonNFk""
  },
  {
    "{": ""      ""Video ID: neubuK7bTaU""
  },
  {
    "{": ""      ""Video ID: EJYc6xZczB4""
  },
  {
    "{": ""      ""Video ID: 6AAcB8h0Sz4""
  },
  {
    "{": ""      ""Video ID: sSMFHEjHwVA""
  },
  {
    "{": ""      ""Video ID: 35xvWUXfQTw""
  },
  {
    "{": ""      ""Video ID: mSZ3ZWn18RY""
  },
  {
    "{": ""      ""Video ID: o5yoZ6ZLHac""
  },
  {
    "{": ""      ""Video ID: W266BJKp_uw""
  },
  {
    "{": ""      ""Video ID: vBT560lOOiQ""
  },
  {
    "{": ""      ""Video ID: w8hy9gptnLc""
  },
  {
    "{": ""      ""Video ID: vc5qG5xMkVk""
  },
  {
    "{": ""      ""Video ID: IEPE5iysFb4""
  },
  {
    "{": ""      ""Video ID: osX7kV2ufMo""
  },
  {
    "{": ""      ""Video ID: Y1HkqMPV7HQ""
  },
  {
    "{": ""      ""Video ID: i6DXArd_gi8""
  },
  {
    "{": ""      ""Video ID: SEp-Kf46Sxw""
  },
  {
    "{": ""      ""Video ID: tvpKvGQCHoQ""
  },
  {
    "{": ""      ""Video ID: Iah6WhUG2s4""
  },
  {
    "{": ""      ""Video ID: dRsXU4Q6a0Q""
  },
  {
    "{": ""      ""Video ID: XMMKXEcXB-E""
  },
  {
    "{": ""      ""Video ID: PfhuU73WStg""
  },
  {
    "{": ""      ""Video ID: jtZfp6tPq3E""
  },
  {
    "{": ""      ""Video ID: 9-jCvw3Y1_g""
  },
  {
    "{": ""      ""Video ID: tTh9mmBf_PE""
  },
  {
    "{": ""      ""Video ID: O9EKUTohTro""
  },
  {
    "{": ""      ""Video ID: LVkqOgteqCU""
  },
  {
    "{": ""      ""Video ID: yopUThZ4pHM""
  },
  {
    "{": ""      ""Video ID: svw42Y9a6ug""
  },
  {
    "{": ""      ""Video ID: 28d03Ykv18I""
  },
  {
    "{": ""      ""Video ID: 76PeBYvi_5Y""
  },
  {
    "{": ""      ""Video ID: BiLxxkbUzIc""
  },
  {
    "{": ""      ""Video ID: nrJTp-tSqLA""
  },
  {
    "{": ""      ""Video ID: x09G3xEgifs""
  },
  {
    "{": ""      ""Video ID: ZqAUjYtqOJ0""
  },
  {
    "{": ""      ""Video ID: 7NgbgPIypLk""
  },
  {
    "{": ""      ""Video ID: gF3GdsaHCsw""
  },
  {
    "{": ""      ""Video ID: YTEshwPppFM""
  },
  {
    "{": ""      ""Video ID: H66-zxgs0QY""
  },
  {
    "{": ""      ""Video ID: jgg0GIfbszg""
  },
  {
    "{": ""      ""Video ID: R1U6ZQ_KaHs""
  },
  {
    "{": ""      ""Video ID: R6_8bG_u1x8""
  },
  {
    "{": ""      ""Video ID: cNhNNlaBjwE""
  },
  {
    "{": ""      ""Video ID: 7wQbGDmaKZc""
  },
  {
    "{": ""      ""Video ID: cbztBGa2Qi0""
  },
  {
    "{": ""      ""Video ID: qyRxPvbj6I4""
  },
  {
    "{": ""      ""Video ID: TP6Os56tWkc""
  },
  {
    "{": ""      ""Video ID: 8iTvH7Xil7s""
  },
  {
    "{": ""      ""Video ID: MmKNB9hgUW0""
  },
  {
    "{": ""      ""Video ID: bNUhKC7CCYU""
  },
  {
    "{": ""      ""Video ID: NSjauMRHebo""
  },
  {
    "{": ""      ""Video ID: jQMQWE-U37A""
  },
  {
    "{": ""      ""Video ID: gv7P7f1JGpU""
  },
  {
    "{": ""      ""Video ID: H1F8zdXtsp0""
  },
  {
    "{": ""      ""Video ID: ZWuoE4tTfgk""
  },
  {
    "{": ""      ""Video ID: BSxcUAtz0ec""
  },
  {
    "{": ""      ""Video ID: FFXV3YWzLk8""
  },
  {
    "{": ""      ""Video ID: n8Pm8MkqFXk""
  },
  {
    "{": ""      ""Video ID: VWdUJsY1Szg""
  },
  {
    "{": ""      ""Video ID: GjntHUJNQQs""
  },
  {
    "{": ""      ""Video ID: Ld-evl93kzQ""
  },
  {
    "{": ""      ""Video ID: CiHWr6ybKFQ""
  },
  {
    "{": ""      ""Video ID: NeU4lENMtr8""
  },
  {
    "{": ""      ""Video ID: Vdc-lKTsSPU""
  },
  {
    "{": ""      ""Video ID: A8xLFL8jHUw""
  },
  {
    "{": ""      ""Video ID: 0MCMsPT9y7Q""
  },
  {
    "{": ""      ""Video ID: Bcc8yjCxfpw""
  },
  {
    "{": ""      ""Video ID: Vh6nvcabqHQ""
  },
  {
    "{": ""      ""Video ID: AjoJHuWTCb4""
  },
  {
    "{": ""      ""Video ID: Ul0_EfsUBJ0""
  },
  {
    "{": ""      ""Video ID: dG20pp9clXo""
  },
  {
    "{": ""      ""Video ID: TT9DMjm-MRY""
  },
  {
    "{": ""      ""Video ID: zclzajmZ8fc""
  },
  {
    "{": ""      ""Video ID: OTzY7zVkmZY""
  },
  {
    "{": ""      ""Video ID: Cp9qFK2UMck""
  },
  {
    "{": ""      ""Video ID: BCTTrpcYWnw""
  },
  {
    "{": ""      ""Video ID: QHkT2YfqHE4""
  },
  {
    "{": ""      ""Video ID: Ycgegp0KdE4""
  },
  {
    "{": ""      ""Video ID: mZ8miTErh-o""
  },
  {
    "{": ""      ""Video ID: XpgH1ukz8LE""
  },
  {
    "{": ""      ""Video ID: I5exx257hJg""
  },
  {
    "{": ""      ""Video ID: 4P7sdo_Aj0o""
  },
  {
    "{": ""      ""Video ID: rslwvTkvUrs""
  },
  {
    "{": ""      ""Video ID: m9bfwitYXWY""
  },
  {
    "{": ""      ""Video ID: _CrCM-wj-PM""
  },
  {
    "{": ""      ""Video ID: 3DHct2FNhDs""
  },
  {
    "{": ""      ""Video ID: XITKl_06V8A""
  },
  {
    "{": ""      ""Video ID: xqeA4oT-Eqs""
  },
  {
    "{": ""      ""Video ID: 5RCIPQ9zv3c""
  },
  {
    "{": ""      ""Video ID: th6yAy0Ry_Q""
  },
  {
    "{": ""      ""Video ID: 8Vm5q1tjZCk""
  },
  {
    "{": ""      ""Video ID: U_yHhY_ZqFA""
  },
  {
    "{": ""      ""Video ID: 6Q-Iy25vb4w""
  },
  {
    "{": ""      ""Video ID: MsC5qOKZkAE""
  },
  {
    "{": ""      ""Video ID: JbcPLOVVojY""
  },
  {
    "{": ""      ""Video ID: P5GpUaNmTY8""
  },
  {
    "{": ""      ""Video ID: Dd6yYLjwl8A""
  },
  {
    "{": ""      ""Video ID: 5G5uKx84Pxg""
  },
  {
    "{": ""      ""Video ID: 3QatOXouVsY""
  },
  {
    "{": ""      ""Video ID: bYVO2CZF9GI""
  },
  {
    "{": ""      ""Video ID: Ld70khbfssM""
  },
  {
    "{": ""      ""Video ID: AU1udQ11c5I""
  },
  {
    "{": ""      ""Video ID: WV9LswFjSNg""
  },
  {
    "{": ""      ""Video ID: qo9Bqf7CPYs""
  },
  {
    "{": ""      ""Video ID: m6A7DelvGjc""
  },
  {
    "{": ""      ""Video ID: TthuOMVsm48""
  },
  {
    "{": ""      ""Video ID: ISS3nU4PmF0""
  },
  {
    "{": ""      ""Video ID: y-hyoxTCK30""
  },
  {
    "{": ""      ""Video ID: 1VcXonqbSmE""
  },
  {
    "{": ""      ""Video ID: JkaevPkg4dc""
  },
  {
    "{": ""      ""Video ID: pTWDsYWjZv0""
  },
  {
    "{": ""      ""Video ID: -3MBwLS2SWw""
  },
  {
    "{": ""      ""Video ID: fDDECTLk3EQ""
  },
  {
    "{": ""      ""Video ID: 5PYkai2zdSc""
  },
  {
    "{": ""      ""Video ID: naEHaIvVWaY""
  },
  {
    "{": ""      ""Video ID: 1O7boCAqjF4""
  },
  {
    "{": ""      ""Video ID: jJNXLVIPSH0""
  },
  {
    "{": ""      ""Video ID: ATvnC7l6SDY""
  },
  {
    "{": ""      ""Video ID: 2A29Cs6UXyU""
  },
  {
    "{": ""      ""Video ID: HXKbYeXtmPA""
  },
  {
    "{": ""      ""Video ID: nUnNB37A_Uw""
  },
  {
    "{": ""      ""Video ID: SxwgZ56Z30w""
  },
  {
    "{": ""      ""Video ID: dC0Zmu6TU0E""
  },
  {
    "{": ""      ""Video ID: OG5n2mBs4P8""
  },
  {
    "{": ""      ""Video ID: p7IYXlKosAM""
  },
  {
    "{": ""      ""Video ID: K8bGrSfdmGI""
  },
  {
    "{": ""      ""Video ID: TdxrcNBozIY""
  },
  {
    "{": ""      ""Video ID: cZyIQXajKKw""
  },
  {
    "{": ""      ""Video ID: icx-60epY4w""
  },
  {
    "{": ""      ""Video ID: Ze5uJg_4064""
  },
  {
    "{": ""      ""Video ID: qLe_t63dBxY""
  },
  {
    "{": ""      ""Video ID: dEmibSHh_XM""
  },
  {
    "{": ""      ""Video ID: PIQe-PcFQ9I""
  },
  {
    "{": ""      ""Video ID: KClKTV7G5YU""
  },
  {
    "{": ""      ""Video ID: Qw-BFsTAHYM""
  },
  {
    "{": ""      ""Video ID: kYB2c9mP-zY""
  },
  {
    "{": ""      ""Video ID: b2N27e79EdY""
  },
  {
    "{": ""      ""Video ID: rg4MPjQcbdc""
  },
  {
    "{": ""      ""Video ID: GEo-t2_qofg""
  },
  {
    "{": ""      ""Video ID: avfaE6qXqCE""
  },
  {
    "{": ""      ""Video ID: xw2w0L_6Qcg""
  },
  {
    "{": ""      ""Video ID: dLI2OR6vXIE""
  },
  {
    "{": ""      ""Video ID: 5gThSGrLf0s""
  },
  {
    "{": ""      ""Video ID: xoZATpwXjSw""
  },
  {
    "{": ""      ""Video ID: nW22SdCCVe4""
  },
  {
    "{": ""      ""Video ID: bSkDfTO9pYM""
  },
  {
    "{": ""      ""Video ID: sKHwa7q_wFM""
  },
  {
    "{": ""      ""Video ID: QjO6esKN0hk""
  },
  {
    "{": ""      ""Video ID: PsCjZfdkgxM""
  },
  {
    "{": ""      ""Video ID: Jzk3cozxqGk""
  },
  {
    "{": ""      ""Video ID: A4wK_CU0v7o""
  },
  {
    "{": ""      ""Video ID: eopzcBbIl1Y""
  },
  {
    "{": ""      ""Video ID: tIvNopv9Pa8""
  },
  {
    "{": ""      ""Video ID: ZDgg9WjkUdM""
  },
  {
    "{": ""      ""Video ID: LzmPMZx7rig""
  },
  {
    "{": ""      ""Video ID: v5I7ilIRJgQ""
  },
  {
    "{": ""      ""Video ID: lSXyHK64OeU""
  },
  {
    "{": ""      ""Video ID: IiZuZwf3VAg""
  },
  {
    "{": ""      ""Video ID: _cr3CZDVCgk""
  },
  {
    "{": ""      ""Video ID: 5u48FyhZ8RM""
  },
  {
    "{": ""      ""Video ID: X7T3iRE8Lok""
  },
  {
    "{": ""      ""Video ID: 9CyPT6-3Flk""
  },
  {
    "{": ""      ""Video ID: -GBkFp0j5F4""
  },
  {
    "{": ""      ""Video ID: tWvxijHNWB4""
  },
  {
    "{": ""      ""Video ID: kjl6jICfpVw""
  },
  {
    "{": ""      ""Video ID: tBsoTTZ5dj8""
  },
  {
    "{": ""      ""Video ID: xXf8ei4Tt8U""
  },
  {
    "{": ""      ""Video ID: 0DZbDiNgCdU""
  },
  {
    "{": ""      ""Video ID: DLp9dHW15sw""
  },
  {
    "{": ""      ""Video ID: svYBDduIVkg""
  },
  {
    "{": ""      ""Video ID: kY2kDfHxHfQ""
  },
  {
    "{": ""      ""Video ID: d0YQuU8iFpg""
  },
  {
    "{": ""      ""Video ID: TmUyuvqCth8""
  },
  {
    "{": ""      ""Video ID: N-wfrnASN_0""
  },
  {
    "{": ""      ""Video ID: KxqsPSlRjHQ""
  },
  {
    "{": ""      ""Video ID: wd_sGiVaNeQ""
  },
  {
    "{": ""      ""Video ID: 3xnTqYUla2I""
  },
  {
    "{": ""      ""Video ID: 3Bi41LBUHtA""
  },
  {
    "{": ""      ""Video ID: nCmpYWMTJMg""
  },
  {
    "{": ""      ""Video ID: HvOqS9yITbo""
  },
  {
    "{": ""      ""Video ID: lv35aftgDdM""
  },
  {
    "{": ""      ""Video ID: Hcy_x5IKgEo""
  },
  {
    "{": ""      ""Video ID: T6YPQKHkNvg""
  },
  {
    "{": ""      ""Video ID: 5eL255gTaJw""
  },
  {
    "{": ""      ""Video ID: i9bzrWTff5U""
  },
  {
    "{": ""      ""Video ID: 5vkE7zokbRU""
  },
  {
    "{": ""      ""Video ID: vB8kG1ZY3vs""
  },
  {
    "{": ""      ""Video ID: FqXdiz57Jd0""
  },
  {
    "{": ""      ""Video ID: cpK2S-efQPE""
  },
  {
    "{": ""      ""Video ID: 6DswnIlT4VM""
  },
  {
    "{": ""      ""Video ID: j0jrhRUj0jo""
  },
  {
    "{": ""      ""Video ID: cP5TlJKRA1Y""
  },
  {
    "{": ""      ""Video ID: _bSZSwWqum8""
  },
  {
    "{": ""      ""Video ID: 4z_jaFgSKDI""
  },
  {
    "{": ""      ""Video ID: lFPd_aGRWFo""
  },
  {
    "{": ""      ""Video ID: mN3WWbojfhc""
  },
  {
    "{": ""      ""Video ID: 9Ur0JO7y4DY""
  },
  {
    "{": ""      ""Video ID: fWgZEz3TSbk""
  },
  {
    "{": ""      ""Video ID: 8RpYJLA5_50""
  },
  {
    "{": ""      ""Video ID: E9OMs5xPjuw""
  },
  {
    "{": ""      ""Video ID: LmuNPDBbDyE""
  },
  {
    "{": ""      ""Video ID: 2dtcNxEnkms""
  },
  {
    "{": ""      ""Video ID: Hh8lOAKh434""
  },
  {
    "{": ""      ""Video ID: JQvj6Dj9Hho""
  },
  {
    "{": ""      ""Video ID: bys8r1alzmA""
  },
  {
    "{": ""      ""Video ID: 93QCeO_BA0Y""
  },
  {
    "{": ""      ""Video ID: Fujy5iVQYJU""
  },
  {
    "{": ""      ""Video ID: ynRNAM_Sx0E""
  },
  {
    "{": ""      ""Video ID: L4Y7vmrSflw""
  },
  {
    "{": ""      ""Video ID: yCQ7-U8QgMc""
  },
  {
    "{": ""      ""Video ID: 56IqliBpp9k""
  },
  {
    "{": ""      ""Video ID: aD_essjItLQ""
  },
  {
    "{": ""      ""Video ID: CdOhYsCq1GA""
  },
  {
    "{": ""      ""Video ID: KNliEjzdSu4""
  },
  {
    "{": ""      ""Video ID: bqrmj8VM32Y""
  },
  {
    "{": ""      ""Video ID: hpUtMqumvu0""
  },
  {
    "{": ""      ""Video ID: KIvsoGoR5DI""
  },
  {
    "{": ""      ""Video ID: Tst8sIfrNvg""
  },
  {
    "{": ""      ""Video ID: m3St7RYYoKo""
  },
  {
    "{": ""      ""Video ID: O3291AaNoIc""
  },
  {
    "{": ""      ""Video ID: QiJ6-5Me1F0""
  },
  {
    "{": ""      ""Video ID: finfmrpx6PE""
  },
  {
    "{": ""      ""Video ID: -4JIElfzN8Q""
  },
  {
    "{": ""      ""Video ID: _5BWV8uR580""
  },
  {
    "{": ""      ""Video ID: KQRWLWAA5OA""
  },
  {
    "{": ""      ""Video ID: akN4m8I0wBo""
  },
  {
    "{": ""      ""Video ID: MNV9MKCmZ_o""
  },
  {
    "{": ""      ""Video ID: 5-vBtgUDYPQ""
  },
  {
    "{": ""      ""Video ID: uPqNRmDa4mc""
  },
  {
    "{": ""      ""Video ID: WR_4-B1l5T0""
  },
  {
    "{": ""      ""Video ID: xXwFfOuevSs""
  },
  {
    "{": ""      ""Video ID: IhTHV-jFumc""
  },
  {
    "{": ""      ""Video ID: cMzDLl0vWJY""
  },
  {
    "{": ""      ""Video ID: smA4Y3RzpgQ""
  },
  {
    "{": ""      ""Video ID: 2JXoC-hkwzk""
  },
  {
    "{": ""      ""Video ID: 2SXiLU3XigY""
  },
  {
    "{": ""      ""Video ID: TkVHfrvhhnk""
  },
  {
    "{": ""      ""Video ID: di4O6M7o-oo""
  },
  {
    "{": ""      ""Video ID: UemZkJXJ8Ak""
  },
  {
    "{": ""      ""Video ID: TdPecutw-PQ""
  },
  {
    "{": ""      ""Video ID: qUjgy1gn9v4""
  },
  {
    "{": ""      ""Video ID: Bp0s5dmJojA""
  },
  {
    "{": ""      ""Video ID: 1AlX7hoObBs""
  },
  {
    "{": ""      ""Video ID: vn6H6134luE""
  },
  {
    "{": ""      ""Video ID: EZh1oF8-cq4""
  },
  {
    "{": ""      ""Video ID: w6Xfyj9qbKw""
  },
  {
    "{": ""      ""Video ID: ZJNpMb6n7io""
  },
  {
    "{": ""      ""Video ID: m11kUF4GlsM""
  },
  {
    "{": ""      ""Video ID: tI9-B7Qe0rg""
  },
  {
    "{": ""      ""Video ID: WreXbo7AE8k""
  },
  {
    "{": ""      ""Video ID: KjOCTqFbeCQ""
  },
  {
    "{": ""      ""Video ID: d8lzaUI2KH0""
  },
  {
    "{": ""      ""Video ID: Wss9uiaKmrk""
  },
  {
    "{": ""      ""Video ID: XXGA-fmrQ7Q""
  },
  {
    "{": ""      ""Video ID: E-H_8EoytbU""
  },
  {
    "{": ""      ""Video ID: z46IDiQRNrI""
  },
  {
    "{": ""      ""Video ID: LOtGLe7hr2A""
  },
  {
    "{": ""      ""Video ID: OQrlbg6VxoI""
  },
  {
    "{": ""      ""Video ID: CPom7fo0Mr0""
  },
  {
    "{": ""      ""Video ID: iijKgLaU-OI""
  },
  {
    "{": ""      ""Video ID: rEtc751yjCs""
  },
  {
    "{": ""      ""Video ID: LZVaLd1O_Qo""
  },
  {
    "{": ""      ""Video ID: YrIFK2VCvuY""
  },
  {
    "{": ""      ""Video ID: U1ozkymT7b4""
  },
  {
    "{": ""      ""Video ID: jySvp4tBbzo""
  },
  {
    "{": ""      ""Video ID: RrZQ8-mqGGc""
  },
  {
    "{": ""      ""Video ID: bRDgvVDk-x0""
  },
  {
    "{": ""      ""Video ID: RN2ZteQ7ZFg""
  },
  {
    "{": ""      ""Video ID: EEIVCsKuAdw""
  },
  {
    "{": ""      ""Video ID: lT-MQIBYFRg""
  },
  {
    "{": ""      ""Video ID: zzvwxgW5IJk""
  },
  {
    "{": ""      ""Video ID: M-FoDm3o_vg""
  },
  {
    "{": ""      ""Video ID: 3_91I3HYC6I""
  },
  {
    "{": ""      ""Video ID: lfALnNfkRUg""
  },
  {
    "{": ""      ""Video ID: AFFTFWXylPQ""
  },
  {
    "{": ""      ""Video ID: 4wnGMlfVc3w""
  },
  {
    "{": ""      ""Video ID: 1UUMVzsCrwg""
  },
  {
    "{": ""      ""Video ID: Yd1Y3dMfppI""
  },
  {
    "{": ""      ""Video ID: y9en1PDV5so""
  },
  {
    "{": ""      ""Video ID: N5hW3AmBi5U""
  },
  {
    "{": ""      ""Video ID: B8wml2fTTTo""
  },
  {
    "{": ""      ""Video ID: F9FoggdgUSw""
  },
  {
    "{": ""      ""Video ID: _kESzoVO21c""
  },
  {
    "{": ""      ""Video ID: wKtgaybI8nQ""
  },
  {
    "{": ""      ""Video ID: GpjkWX7qyYE""
  },
  {
    "{": ""      ""Video ID: r4BQCGL5pAU""
  },
  {
    "{": ""      ""Video ID: PDZCulFHLNE""
  },
  {
    "{": ""      ""Video ID: Gh0lRryLpm0""
  },
  {
    "{": ""      ""Video ID: MEFNfngG7XI""
  },
  {
    "{": ""      ""Video ID: hLZmeCDfy9U""
  },
  {
    "{": ""      ""Video ID: head1QVANwI""
  },
  {
    "{": ""      ""Video ID: cPOytDDoPGg""
  },
  {
    "{": ""      ""Video ID: zx3vbk1BdC0""
  },
  {
    "{": ""      ""Video ID: SA5Tj_OZeLs""
  },
  {
    "{": ""      ""Video ID: Schs0UC5nFU""
  },
  {
    "{": ""      ""Video ID: 6mUPs0D6Z6E""
  },
  {
    "{": ""      ""Video ID: oZnu51jyg28""
  },
  {
    "{": ""      ""Video ID: eUE9sgxGaNg""
  },
  {
    "{": ""      ""Video ID: zHY_tqiLWDE""
  },
  {
    "{": ""      ""Video ID: J8tGfxyX-qU""
  },
  {
    "{": ""      ""Video ID: KoDOGAoaOwc""
  },
  {
    "{": ""      ""Video ID: uutI5-ctj8U""
  },
  {
    "{": ""      ""Video ID: 4COW37Nau0Q""
  },
  {
    "{": ""      ""Video ID: p5iQ2g6UjjA""
  },
  {
    "{": ""      ""Video ID: jMT5R098iJI""
  },
  {
    "{": ""      ""Video ID: cIg1V-p4YE0""
  },
  {
    "{": ""      ""Video ID: m2r9b78utiY""
  },
  {
    "{": ""      ""Video ID: UxpM1_bn9Z8""
  },
  {
    "{": ""      ""Video ID: osFwW35GV30""
  },
  {
    "{": ""      ""Video ID: Ic3ULcR58kg""
  },
  {
    "{": ""      ""Video ID: hgobLkNExfc""
  },
  {
    "{": ""      ""Video ID: C3XfMkKWz-g""
  },
  {
    "{": ""      ""Video ID: wrYiiqGBWe0""
  },
  {
    "{": ""      ""Video ID: fJVydzNJrno""
  },
  {
    "{": ""      ""Video ID: Ffw4-OMmchY""
  },
  {
    "{": ""      ""Video ID: 3OZcx2CrTpI""
  },
  {
    "{": ""      ""Video ID: xCHGBzkm3pY""
  },
  {
    "{": ""      ""Video ID: -m24t-OTBvI""
  },
  {
    "{": ""      ""Video ID: 9iX0crIYrLY""
  },
  {
    "{": ""      ""Video ID: 9MwLs6ie5DQ""
  },
  {
    "{": ""      ""Video ID: AJEIDKd3MR4""
  },
  {
    "{": ""      ""Video ID: HwWaDsDu2kU""
  },
  {
    "{": ""      ""Video ID: 2G4RW9BvMpQ""
  },
  {
    "{": ""      ""Video ID: MbG-CnTE5DA""
  },
  {
    "{": ""      ""Video ID: JUr0yiOeqcY""
  },
  {
    "{": ""      ""Video ID: BxQCDOXvUzw""
  },
  {
    "{": ""      ""Video ID: c4QwdhvGVbo""
  },
  {
    "{": ""      ""Video ID: C30TG9amc3Q""
  },
  {
    "{": ""      ""Video ID: Wm4OLfXwfls""
  },
  {
    "{": ""      ""Video ID: CFU2zofzzHM""
  },
  {
    "{": ""      ""Video ID: IYecoo-3wg8""
  },
  {
    "{": ""      ""Video ID: XWRbhdJYX4g""
  },
  {
    "{": ""      ""Video ID: hX8gQ8CuYSo""
  },
  {
    "{": ""      ""Video ID: q2_pc5UEs1M""
  },
  {
    "{": ""      ""Video ID: XsZjeCbbMZw""
  },
  {
    "{": ""      ""Video ID: D0jrNy5sCKo""
  },
  {
    "{": ""      ""Video ID: c4MD-_uzoFA""
  },
  {
    "{": ""      ""Video ID: giRHf1_pX1k""
  },
  {
    "{": ""      ""Video ID: AuJE3XHSNaw""
  },
  {
    "{": ""      ""Video ID: mwtojTV0BG8""
  },
  {
    "{": ""      ""Video ID: 3VBZVjQ48CE""
  },
  {
    "{": ""      ""Video ID: RxlEIg__z7E""
  },
  {
    "{": ""      ""Video ID: Ha12TmYjWq0""
  },
  {
    "{": ""      ""Video ID: lLAvJAvqtjI""
  },
  {
    "{": ""      ""Video ID: iTVzJQhcl5g""
  },
  {
    "{": ""      ""Video ID: EgBTTHxiiBg""
  },
  {
    "{": ""      ""Video ID: -0SzJSBQxFA""
  },
  {
    "{": ""      ""Video ID: j-2Aa1zN27c""
  },
  {
    "{": ""      ""Video ID: JW04j4ufKDw""
  },
  {
    "{": ""      ""Video ID: iJ4DFnI36Mg""
  },
  {
    "{": ""      ""Video ID: VXU4ctbn5ZI""
  },
  {
    "{": ""      ""Video ID: -ur8s01zhso""
  },
  {
    "{": ""      ""Video ID: whWyd-nlwjQ""
  },
  {
    "{": ""      ""Video ID: 2QAs7LsO9r4""
  },
  {
    "{": ""      ""Video ID: X7WoAHrgVL0""
  },
  {
    "{": ""      ""Video ID: EjXk9M1JJRI""
  },
  {
    "{": ""      ""Video ID: kh0CRFjlOQM""
  },
  {
    "{": ""      ""Video ID: aYSr-a2b4B0""
  },
  {
    "{": ""      ""Video ID: -N5twmzavI4""
  },
  {
    "{": ""      ""Video ID: KthddcXichw""
  },
  {
    "{": ""      ""Video ID: DwXkw_YdmTU""
  },
  {
    "{": ""      ""Video ID: 16LWpitaU2M""
  },
  {
    "{": ""      ""Video ID: AjZfw4lovo4""
  },
  {
    "{": ""      ""Video ID: bH1xA39P860""
  },
  {
    "{": ""      ""Video ID: 8ky4PytjCRE""
  },
  {
    "{": ""      ""Video ID: -g4Y-6Mi2zU""
  },
  {
    "{": ""      ""Video ID: FID2zIHr_BE""
  },
  {
    "{": ""      ""Video ID: IqmowgmKt1o""
  },
  {
    "{": ""      ""Video ID: hzcwYYtbkow""
  },
  {
    "{": ""      ""Video ID: lfPkw4-76Lo""
  },
  {
    "{": ""      ""Video ID: mQ9MYyYLdzs""
  },
  {
    "{": ""      ""Video ID: YJn8_1FwW_c""
  },
  {
    "{": ""      ""Video ID: UF1IUgLtrmM""
  },
  {
    "{": ""      ""Video ID: yUz_tXVjDtw""
  },
  {
    "{": ""      ""Video ID: sYZQu91e6ok""
  },
  {
    "{": ""      ""Video ID: XvaIO9Gb7Jg""
  },
  {
    "{": ""      ""Video ID: a8lDedYark0""
  },
  {
    "{": ""      ""Video ID: sQHRY8Nsft0""
  },
  {
    "{": ""      ""Video ID: TL_B9HqfCaU""
  },
  {
    "{": ""      ""Video ID: JMb7fUBezXE""
  },
  {
    "{": ""      ""Video ID: Lk70KMrQX9U""
  },
  {
    "{": ""      ""Video ID: aC4dgkKWzhI""
  },
  {
    "{": ""      ""Video ID: aDvGCjNfO4w""
  },
  {
    "{": ""      ""Video ID: TMYRyPyg_fQ""
  },
  {
    "{": ""      ""Video ID: Ou9WxuKAKEc""
  },
  {
    "{": ""      ""Video ID: zrJ26hG5Mjo""
  },
  {
    "{": ""      ""Video ID: nsWHCJPVTZw""
  },
  {
    "{": ""      ""Video ID: -ef4UqdHdRw""
  },
  {
    "{": ""      ""Video ID: JcU4tgSAoWA""
  },
  {
    "{": ""      ""Video ID: b-ZNAIBaT5Q""
  },
  {
    "{": ""      ""Video ID: VT2CAbraGjc""
  },
  {
    "{": ""      ""Video ID: AW-zR5LtaGs""
  },
  {
    "{": ""      ""Video ID: Utev3p0y3Mo""
  },
  {
    "{": ""      ""Video ID: wpdNNrS0gF8""
  },
  {
    "{": ""      ""Video ID: UQZSl9zySME""
  },
  {
    "{": ""      ""Video ID: O-b9srVaBoo""
  },
  {
    "{": ""      ""Video ID: 7YIgSp6CROs""
  },
  {
    "{": ""      ""Video ID: 91Xha3G4EEk""
  },
  {
    "{": ""      ""Video ID: vLx9m81JPzc""
  },
  {
    "{": ""      ""Video ID: uGsCLMrHl4A""
  },
  {
    "{": ""      ""Video ID: sVCymNoEMg8""
  },
  {
    "{": ""      ""Video ID: jC0N5PShjcQ""
  },
  {
    "{": ""      ""Video ID: nDWhf81iQfk""
  },
  {
    "{": ""      ""Video ID: on8XI0iSAsQ""
  },
  {
    "{": ""      ""Video ID: eGWh-oW2CtY""
  },
  {
    "{": ""      ""Video ID: lNby8Vov-vk""
  },
  {
    "{": ""      ""Video ID: c_LPLIS5Hoo""
  },
  {
    "{": ""      ""Video ID: M3gt0nfJlHk""
  },
  {
    "{": ""      ""Video ID: sSvhkeA3lGs""
  },
  {
    "{": ""      ""Video ID: W4ffY95oPP8""
  },
  {
    "{": ""      ""Video ID: PPMWzsMjc0g""
  },
  {
    "{": ""      ""Video ID: qvK-Dy5Plmw""
  },
  {
    "{": ""      ""Video ID: oQFOtht43gI""
  },
  {
    "{": ""      ""Video ID: I0TBPMH0weo""
  },
  {
    "{": ""      ""Video ID: 61DMg1Iz4Zc""
  },
  {
    "{": ""      ""Video ID: zY29ceVBtho""
  },
  {
    "{": ""      ""Video ID: w_eXRCXFqlw""
  },
  {
    "{": ""      ""Video ID: saUBqsc4rVU""
  },
  {
    "{": ""      ""Video ID: Lup7c2CbtMY""
  },
  {
    "{": ""      ""Video ID: fiqE9y6kE5M""
  },
  {
    "{": ""      ""Video ID: nXsaQd7ZlgQ""
  },
  {
    "{": ""      ""Video ID: fmmxYuNhkpU""
  },
  {
    "{": ""      ""Video ID: 54aTchMvwJ4""
  },
  {
    "{": ""      ""Video ID: 5Gq-pW1_5f8""
  },
  {
    "{": ""      ""Video ID: IiV2m_P1Emw""
  },
  {
    "{": ""      ""Video ID: Tcn3zzYnxTA""
  },
  {
    "{": ""      ""Video ID: OqJTso2rJCg""
  },
  {
    "{": ""      ""Video ID: eHrMqjyNcnQ""
  },
  {
    "{": ""      ""Video ID: 3PWn_D6D3vE""
  },
  {
    "{": ""      ""Video ID: 96bN5u-tEIU""
  },
  {
    "{": ""      ""Video ID: s_sq6I7RXCo""
  },
  {
    "{": ""      ""Video ID: 3W5H0sGfxUo""
  },
  {
    "{": ""      ""Video ID: NBp6wwIYx1M""
  },
  {
    "{": ""      ""Video ID: kBc3V-KbJyw""
  },
  {
    "{": ""      ""Video ID: F5dIZEEILSo""
  },
  {
    "{": ""      ""Video ID: vnucfkTYv3M""
  },
  {
    "{": ""      ""Video ID: DC4EFFsw3Oo""
  },
  {
    "{": ""      ""Video ID: L0sl2zGrD5U""
  },
  {
    "{": ""      ""Video ID: crt-O_be-hI""
  },
  {
    "{": ""      ""Video ID: E7ewcdF0OLM""
  },
  {
    "{": ""      ""Video ID: 7Wi1NpGnoxE""
  },
  {
    "{": ""      ""Video ID: 7JYTr3MYg5k""
  },
  {
    "{": ""      ""Video ID: pMmy-QDNwww""
  },
  {
    "{": ""      ""Video ID: k0kIvvU_29Y""
  },
  {
    "{": ""      ""Video ID: DkasGW-4tms""
  },
  {
    "{": ""      ""Video ID: vlyv62N7w-o""
  },
  {
    "{": ""      ""Video ID: vMmiw-hMlfM""
  },
  {
    "{": ""      ""Video ID: ss7zGjbz6Yc""
  },
  {
    "{": ""      ""Video ID: -XjZqTm5Bpk""
  },
  {
    "{": ""      ""Video ID: cpntRqw6Lio""
  },
  {
    "{": ""      ""Video ID: ADhhd1cirxc""
  },
  {
    "{": ""      ""Video ID: De2PY3uj0ls""
  },
  {
    "{": ""      ""Video ID: Z4Fntn8kvKM""
  },
  {
    "{": ""      ""Video ID: LXxALBVjXtw""
  },
  {
    "{": ""      ""Video ID: YM89Gbrwy74""
  },
  {
    "{": ""      ""Video ID: LK1OjwuJEPo""
  },
  {
    "{": ""      ""Video ID: 1B5q5jINUzY""
  },
  {
    "{": ""      ""Video ID: 6dOSSceakZk""
  },
  {
    "{": ""      ""Video ID: 50NeXKSWglE""
  },
  {
    "{": ""      ""Video ID: 0yiOnqEjgWU""
  },
  {
    "{": ""      ""Video ID: mXE9BlxAljQ""
  },
  {
    "{": ""      ""Video ID: zXyZrB3e1zY""
  },
  {
    "{": ""      ""Video ID: im9DqFzZE-w""
  },
  {
    "{": ""      ""Video ID: mT2_ST5aQnk""
  },
  {
    "{": ""      ""Video ID: aM6cXHUf-6k""
  },
  {
    "{": ""      ""Video ID: DPZkOhcFYZY""
  },
  {
    "{": ""      ""Video ID: ZTfuiGjmaYA""
  },
  {
    "{": ""      ""Video ID: lgVFkt6Lk6U""
  },
  {
    "{": ""      ""Video ID: 4w8UitHzIK8""
  },
  {
    "{": ""      ""Video ID: z7mW59eRv_k""
  },
  {
    "{": ""      ""Video ID: jfiRftzbh9o""
  },
  {
    "{": ""      ""Video ID: 62dKyJ4SE4E""
  },
  {
    "{": ""      ""Video ID: VeC9kS9UZ_U""
  },
  {
    "{": ""      ""Video ID: JuLWWDoN85E""
  },
  {
    "{": ""      ""Video ID: M-Gw5xTxF80""
  },
  {
    "{": ""      ""Video ID: 0S_ST6NPKkw""
  },
  {
    "{": ""      ""Video ID: fTvcPLuMPa0""
  },
  {
    "{": ""      ""Video ID: xUqdLuzVxNc""
  },
  {
    "{": ""      ""Video ID: 3K6FUBpuVj0""
  },
  {
    "{": ""      ""Video ID: r0HQtvToKYs""
  },
  {
    "{": ""      ""Video ID: 359O0bW6M3Q""
  },
  {
    "{": ""      ""Video ID: XFZnF0QkMPs""
  },
  {
    "{": ""      ""Video ID: oHQpxF51yWo""
  },
  {
    "{": ""      ""Video ID: QCnhqm30Ips""
  },
  {
    "{": ""      ""Video ID: gdpJltRoLRY""
  },
  {
    "{": ""      ""Video ID: BLvQGrezK2o""
  },
  {
    "{": ""      ""Video ID: CQUWvlZ7w9s""
  },
  {
    "{": ""      ""Video ID: Q1G5h183wTU""
  },
  {
    "{": ""      ""Video ID: QwzScYRqVgU""
  },
  {
    "{": ""      ""Video ID: TMbLyS7CwGc""
  },
  {
    "{": ""      ""Video ID: 6WkTeBGh9Ks""
  },
  {
    "{": ""      ""Video ID: poOaWpUa0ys""
  },
  {
    "{": ""      ""Video ID: QuL9tMhvEwg""
  },
  {
    "{": ""      ""Video ID: 8OhvmOFJ06I""
  },
  {
    "{": ""      ""Video ID: pk5xdyMfny0""
  },
  {
    "{": ""      ""Video ID: WpHG3imEB3Q""
  },
  {
    "{": ""      ""Video ID: wkoZuYovN98""
  },
  {
    "{": ""      ""Video ID: T5w-Z_6uWgQ""
  },
  {
    "{": ""      ""Video ID: n4mfRWp-aBA""
  },
  {
    "{": ""      ""Video ID: _oY7D22ypMU""
  },
  {
    "{": ""      ""Video ID: rIcHyy7xRZc""
  },
  {
    "{": ""      ""Video ID: Wz3TBs0WbK4""
  },
  {
    "{": ""      ""Video ID: mNbEp2d6Dik""
  },
  {
    "{": ""      ""Video ID: Swpn_iALUnE""
  },
  {
    "{": ""      ""Video ID: jXUGB-dE0LE""
  },
  {
    "{": ""      ""Video ID: QGUZgzfCQMk""
  },
  {
    "{": ""      ""Video ID: 5VDZ0cKRlFA""
  },
  {
    "{": ""      ""Video ID: cU5Sv3gc83g""
  },
  {
    "{": ""      ""Video ID: j7CtUxFTe4I""
  },
  {
    "{": ""      ""Video ID: IC7Pv3CVt5o""
  },
  {
    "{": ""      ""Video ID: 8_ilAyPiUB8""
  },
  {
    "{": ""      ""Video ID: oNGHjNtkNs8""
  },
  {
    "{": ""      ""Video ID: EOlDmjYhUb0""
  },
  {
    "{": ""      ""Video ID: oWmzRBhoAHE""
  },
  {
    "{": ""      ""Video ID: YLdEhQfgGE8""
  },
  {
    "{": ""      ""Video ID: s0HLTvq_7Tw""
  },
  {
    "{": ""      ""Video ID: -Xagx60F2JY""
  },
  {
    "{": ""      ""Video ID: -O6PsuNUyDA""
  },
  {
    "{": ""      ""Video ID: -9RbYRYfIi8""
  },
  {
    "{": ""      ""Video ID: okqO9WQb-_I""
  },
  {
    "{": ""      ""Video ID: NwpeaaptIZg""
  },
  {
    "{": ""      ""Video ID: zSBqGLZoYyE""
  },
  {
    "{": ""      ""Video ID: SsPvOM_rw_0""
  },
  {
    "{": ""      ""Video ID: D-IZKMIiymY""
  },
  {
    "{": ""      ""Video ID: Sq2FVre-cLQ""
  },
  {
    "{": ""      ""Video ID: ILboNRKexTg""
  },
  {
    "{": ""      ""Video ID: NI8nkXqk6Fc""
  },
  {
    "{": ""      ""Video ID: lnYKuSB92O8""
  },
  {
    "{": ""      ""Video ID: 78iC9dNAYhM""
  },
  {
    "{": ""      ""Video ID: 3WD3_PF_fYA""
  },
  {
    "{": ""      ""Video ID: Vc8v1RTZg9Y""
  },
  {
    "{": ""      ""Video ID: lzQIzKg6yjg""
  },
  {
    "{": ""      ""Video ID: jiHg8hIZCQQ""
  },
  {
    "{": ""      ""Video ID: jQSMuuuIobc""
  },
  {
    "{": ""      ""Video ID: wqN9Gswpruc""
  },
  {
    "{": ""      ""Video ID: _AWd2dUEjOY""
  },
  {
    "{": ""      ""Video ID: O8muBCO7lDQ""
  },
  {
    "{": ""      ""Video ID: F-Ivo0vey30""
  },
  {
    "{": ""      ""Video ID: tZmsIeujGLo""
  },
  {
    "{": ""      ""Video ID: 8wWJeogrvWs""
  },
  {
    "{": ""      ""Video ID: XpoKDo5cYNU""
  },
  {
    "{": ""      ""Video ID: VROjPCGA7j0""
  },
  {
    "{": ""      ""Video ID: qhBKANIpUT0""
  },
  {
    "{": ""      ""Video ID: gWgVr545yNA""
  },
  {
    "{": ""      ""Video ID: WzAX07Ce9Og""
  },
  {
    "{": ""      ""Video ID: 4V56j7wMhtA""
  },
  {
    "{": ""      ""Video ID: u4tBIRv6dK4""
  },
  {
    "{": ""      ""Video ID: 3UGjfKdxi94""
  },
  {
    "{": ""      ""Video ID: lWQ2dwnbc8c""
  },
  {
    "{": ""      ""Video ID: KuF4dtYOM2Q""
  },
  {
    "{": ""      ""Video ID: MGd0wbTQyZQ""
  },
  {
    "{": ""      ""Video ID: 6IXRDH0SPug""
  },
  {
    "{": ""      ""Video ID: DrXXUE6T5eY""
  },
  {
    "{": ""      ""Video ID: WQr3r1qFY2Y""
  },
  {
    "{": ""      ""Video ID: O0vGkTVMzYU""
  },
  {
    "{": ""      ""Video ID: OiiaFZbVErk""
  },
  {
    "{": ""      ""Video ID: Qqo6__WBuvY""
  },
  {
    "{": ""      ""Video ID: xDFm8YGBugg""
  },
  {
    "{": ""      ""Video ID: eL_tMXU6btw""
  },
  {
    "{": ""      ""Video ID: _UoCrrUhXxA""
  },
  {
    "{": ""      ""Video ID: u4SI3kLMscU""
  },
  {
    "{": ""      ""Video ID: MsYVis61PAw""
  },
  {
    "{": ""      ""Video ID: u_NGZF8_zx4""
  },
  {
    "{": ""      ""Video ID: f9mG0INibGU""
  },
  {
    "{": ""      ""Video ID: OnIiux5Jtec""
  },
  {
    "{": ""      ""Video ID: cg6aktOshuI""
  },
  {
    "{": ""      ""Video ID: mSO1a22sacY""
  },
  {
    "{": ""      ""Video ID: 0ILPnh4mOKo""
  },
  {
    "{": ""      ""Video ID: xVpQjFQLd9w""
  },
  {
    "{": ""      ""Video ID: 3taSyvuQIbo""
  },
  {
    "{": ""      ""Video ID: _sM9vcAIYyc""
  },
  {
    "{": ""      ""Video ID: Zy7jx8D0hkg""
  },
  {
    "{": ""      ""Video ID: GlFHwVbxaWw""
  },
  {
    "{": ""      ""Video ID: qFVm7bEMl_U""
  },
  {
    "{": ""      ""Video ID: 3GA0o3nXmnI""
  },
  {
    "{": ""      ""Video ID: PwNv6jF1uU0""
  },
  {
    "{": ""      ""Video ID: wFWon54vr0o""
  },
  {
    "{": ""      ""Video ID: sdi6fuKPd90""
  },
  {
    "{": ""      ""Video ID: Oy24qH5uN8I""
  },
  {
    "{": ""      ""Video ID: EJdsQefJ55g""
  },
  {
    "{": ""      ""Video ID: 3cAbgdZkuYI""
  },
  {
    "{": ""      ""Video ID: Lt3m4s9kQPM""
  },
  {
    "{": ""      ""Video ID: Fjzv2Coa8pM""
  },
  {
    "{": ""      ""Video ID: rjMVQdN_Jhs""
  },
  {
    "{": ""      ""Video ID: t8MGGIrNDj8""
  },
  {
    "{": ""      ""Video ID: z9RQx-lfVPo""
  },
  {
    "{": ""      ""Video ID: a10GpKs-YQ0""
  },
  {
    "{": ""      ""Video ID: 6KCWzRfFyr4""
  },
  {
    "{": ""      ""Video ID: AoPeVS03A3A""
  },
  {
    "{": ""      ""Video ID: IvSBLF1N7Fw""
  },
  {
    "{": ""      ""Video ID: BCOIlhKQnIs""
  },
  {
    "{": ""      ""Video ID: VpaoGysZTsA""
  },
  {
    "{": ""      ""Video ID: gisZP98vBEE""
  },
  {
    "{": ""      ""Video ID: -BExbkQ_rQA""
  },
  {
    "{": ""      ""Video ID: ejhsWxPJhbU""
  },
  {
    "{": ""      ""Video ID: NFLuAaJ7WCQ""
  },
  {
    "{": ""      ""Video ID: Qjfmt6-TZVw""
  },
  {
    "{": ""      ""Video ID: lpf3IFL-kVM""
  },
  {
    "{": ""      ""Video ID: 6aXLGkAXYHg""
  },
  {
    "{": ""      ""Video ID: So4T2HzlaG0""
  },
  {
    "{": ""      ""Video ID: 6Tv-iXVKkks""
  },
  {
    "{": ""      ""Video ID: NPofxeFmDjU""
  },
  {
    "{": ""      ""Video ID: 3p_RyHw_ldk""
  },
  {
    "{": ""      ""Video ID: B6pEbGJNI-I""
  },
  {
    "{": ""      ""Video ID: cty1SYjOZBY""
  },
  {
    "{": ""      ""Video ID: kAwTZ1kUikk""
  },
  {
    "{": ""      ""Video ID: 6wvc6DbiFiU""
  },
  {
    "{": ""      ""Video ID: MGc-wE0UY68""
  },
  {
    "{": ""      ""Video ID: s6WME89MSRU""
  },
  {
    "{": ""      ""Video ID: dd-XsWaCWPU""
  },
  {
    "{": ""      ""Video ID: 05h2uv0jgB8""
  },
  {
    "{": ""      ""Video ID: aZXLDX010Hw""
  },
  {
    "{": ""      ""Video ID: m-evTCquwsM""
  },
  {
    "{": ""      ""Video ID: ghnwIOmUe9I""
  },
  {
    "{": ""      ""Video ID: 9w-U_6CNJzQ""
  },
  {
    "{": ""      ""Video ID: 6D2C-OjKqkk""
  },
  {
    "{": ""      ""Video ID: KycSBl1Oc4s""
  },
  {
    "{": ""      ""Video ID: pTLEyJoercg""
  },
  {
    "{": ""      ""Video ID: jijOo3RF1L8""
  },
  {
    "{": ""      ""Video ID: EBpa2CADNJA""
  },
  {
    "{": ""      ""Video ID: a3DwM1p9mQo""
  },
  {
    "{": ""      ""Video ID: OvmBMFOS2BQ""
  },
  {
    "{": ""      ""Video ID: VLmQ_UTeCt4""
  },
  {
    "{": ""      ""Video ID: 1NoYrAy-vZU""
  },
  {
    "{": ""      ""Video ID: QnWE_NrKeOI""
  },
  {
    "{": ""      ""Video ID: rV9nn3NG_vM""
  },
  {
    "{": ""      ""Video ID: cNZQkUA2YRg""
  },
  {
    "{": ""      ""Video ID: IOHs7vmpPBc""
  },
  {
    "{": ""      ""Video ID: 4lYF_oPZqjI""
  },
  {
    "{": ""      ""Video ID: -jY3dPZdS-M""
  },
  {
    "{": ""      ""Video ID: 2ujttzq9Q4w""
  },
  {
    "{": ""      ""Video ID: NPw74VdPoEA""
  },
  {
    "{": ""      ""Video ID: 8VK-MzKjTI0""
  },
  {
    "{": ""      ""Video ID: rCAYG_FptA4""
  },
  {
    "{": ""      ""Video ID: T7XoEbuVFlw""
  },
  {
    "{": ""      ""Video ID: CXs8OSex56w""
  },
  {
    "{": ""      ""Video ID: Qo4HvubOZdw""
  },
  {
    "{": ""      ""Video ID: ZfaUEII-Qzc""
  },
  {
    "{": ""      ""Video ID: VeRHPu08Ck0""
  },
  {
    "{": ""      ""Video ID: UMWeDpR8TTE""
  },
  {
    "{": ""      ""Video ID: QOF0XLBhfbo""
  },
  {
    "{": ""      ""Video ID: SR46e8yUnRc""
  },
  {
    "{": ""      ""Video ID: bU_bmFbIKlk""
  },
  {
    "{": ""      ""Video ID: t44lVR4_Hx4""
  },
  {
    "{": ""      ""Video ID: dLbLLoqFOOo""
  },
  {
    "{": ""      ""Video ID: iXG85kL-9kk""
  },
  {
    "{": ""      ""Video ID: mUCECDBOOjw""
  },
  {
    "{": ""      ""Video ID: JgPIc22VRdg""
  },
  {
    "{": ""      ""Video ID: SRlKQa6TpHg""
  },
  {
    "{": ""      ""Video ID: n-mlYr4WQvs""
  },
  {
    "{": ""      ""Video ID: uS8wf7k8sCw""
  },
  {
    "{": ""      ""Video ID: 8NNiPNvKIak""
  },
  {
    "{": ""      ""Video ID: hMtzQhzOvIw""
  },
  {
    "{": ""      ""Video ID: NzdRg6lo4j0""
  },
  {
    "{": ""      ""Video ID: uKUvQLTlySU""
  },
  {
    "{": ""      ""Video ID: UT9SjpNB0CI""
  },
  {
    "{": ""      ""Video ID: k45koZrW-e4""
  },
  {
    "{": ""      ""Video ID: rmdYIxDefHk""
  },
  {
    "{": ""      ""Video ID: aqxWwSqqNpM""
  },
  {
    "{": ""      ""Video ID: F4fHnJ1W1nE""
  },
  {
    "{": ""      ""Video ID: 8V2pVlYvjds""
  },
  {
    "{": ""      ""Video ID: VquW5MLCe_8""
  },
  {
    "{": ""      ""Video ID: qIgMLtEYnjU""
  },
  {
    "{": ""      ""Video ID: pGhEDK_Nu1s""
  },
  {
    "{": ""      ""Video ID: MDOX0RDxnyA""
  },
  {
    "{": ""      ""Video ID: J_VquWguuk8""
  },
  {
    "{": ""      ""Video ID: Aiw14cIhGPg""
  },
  {
    "{": ""      ""Video ID: XOhYNq9HhcM""
  },
  {
    "{": ""      ""Video ID: zvbMwupvEPY""
  },
  {
    "{": ""      ""Video ID: gLqfeGgU5rM""
  },
  {
    "{": ""      ""Video ID: iwSnhYE7nOo""
  },
  {
    "{": ""      ""Video ID: xWnJ1MMknMs""
  },
  {
    "{": ""      ""Video ID: u6ZbH3UWRVU""
  },
  {
    "{": ""      ""Video ID: TmUYj4U9J8M""
  },
  {
    "{": ""      ""Video ID: LJ0Hq_WIRAQ""
  },
  {
    "{": ""      ""Video ID: Fze2J2Ve9is""
  },
  {
    "{": ""      ""Video ID: OzjUCpqjx4w""
  },
  {
    "{": ""      ""Video ID: OGpvS2JX1AA""
  },
  {
    "{": ""      ""Video ID: skq3-N_-pVc""
  },
  {
    "{": ""      ""Video ID: cbtdWexyMoQ""
  },
  {
    "{": ""      ""Video ID: RMBhl36QuQ8""
  },
  {
    "{": ""      ""Video ID: viCk9NSeG1Y""
  },
  {
    "{": ""      ""Video ID: WQlL2TBFUKA""
  },
  {
    "{": ""      ""Video ID: A7jcAPeq8K0""
  },
  {
    "{": ""      ""Video ID: u8DjVZrIDuA""
  },
  {
    "{": ""      ""Video ID: Yo8ccXGsOdA""
  },
  {
    "{": ""      ""Video ID: vUozrGMX61g""
  },
  {
    "{": ""      ""Video ID: KtIDykvGn4Q""
  },
  {
    "{": ""      ""Video ID: XR79XymL44E""
  },
  {
    "{": ""      ""Video ID: tFqBduDf9b8""
  },
  {
    "{": ""      ""Video ID: Yw7c6fOUa18""
  },
  {
    "{": ""      ""Video ID: dEs0LwRRVkY""
  },
  {
    "{": ""      ""Video ID: C6rRkTfiCrI""
  },
  {
    "{": ""      ""Video ID: HMHfjDsN1jo""
  },
  {
    "{": ""      ""Video ID: VdvmdVu0qGI""
  },
  {
    "{": ""      ""Video ID: UA59WinHLWA""
  },
  {
    "{": ""      ""Video ID: eQ-Nsdj9DdE""
  },
  {
    "{": ""      ""Video ID: EpQOZ7HukmY""
  },
  {
    "{": ""      ""Video ID: 33gNcFC1fbo""
  },
  {
    "{": ""      ""Video ID: GTvybiyfmbE""
  },
  {
    "{": ""      ""Video ID: Rhp5uqWnUUA""
  },
  {
    "{": ""      ""Video ID: xpQKXsJi8us""
  },
  {
    "{": ""      ""Video ID: XCkGf-I8jnc""
  },
  {
    "{": ""      ""Video ID: MWbSPFuOQoo""
  },
  {
    "{": ""      ""Video ID: IuZq5M6ot2I""
  },
  {
    "{": ""      ""Video ID: vZ1jFaXgTnw""
  },
  {
    "{": ""      ""Video ID: Vqm556DoaM4""
  },
  {
    "{": ""      ""Video ID: SeTssvexa9s""
  },
  {
    "{": ""      ""Video ID: IQSWEz8uvco""
  },
  {
    "{": ""      ""Video ID: Iq-7g2B-o8g""
  },
  {
    "{": ""      ""Video ID: TFxiMz3w2sM""
  },
  {
    "{": ""      ""Video ID: KpnXSPaRyu4""
  },
  {
    "{": ""      ""Video ID: 20QuZHWGWUE""
  },
  {
    "{": ""      ""Video ID: sEpxgRLcuRw""
  },
  {
    "{": ""      ""Video ID: P7J_ereCiTo""
  },
  {
    "{": ""      ""Video ID: 8Bhodyt4fmU""
  },
  {
    "{": ""      ""Video ID: PwMqfappbyk""
  },
  {
    "{": ""      ""Video ID: Y-aTz6iNkvA""
  },
  {
    "{": ""      ""Video ID: IZjMgbRUsZM""
  },
  {
    "{": ""      ""Video ID: yDt7xwnLv-k""
  },
  {
    "{": ""      ""Video ID: oy8EaMT7XPs""
  },
  {
    "{": ""      ""Video ID: -xucSAVqJJg""
  },
  {
    "{": ""      ""Video ID: GuweGoV10Os""
  },
  {
    "{": ""      ""Video ID: _5LpE-kA3gs""
  },
  {
    "{": ""      ""Video ID: yfzOrJESXt8""
  },
  {
    "{": ""      ""Video ID: qTdtZvmS7Kg""
  },
  {
    "{": ""      ""Video ID: ZTzlod-1DFU""
  },
  {
    "{": ""      ""Video ID: 4WsV6fJJ51Q""
  },
  {
    "{": ""      ""Video ID: yyoSY-J-BzQ""
  },
  {
    "{": ""      ""Video ID: _unKt5-E8Rk""
  },
  {
    "{": ""      ""Video ID: IaP16aUvC1Y""
  },
  {
    "{": ""      ""Video ID: gmslJ9OeSzw""
  },
  {
    "{": ""      ""Video ID: zW466xcM0Yk""
  },
  {
    "{": ""      ""Video ID: Vez5NO-9o-g""
  },
  {
    "{": ""      ""Video ID: bWQmByCodXM""
  },
  {
    "{": ""      ""Video ID: xuUVq9c58Lk""
  },
  {
    "{": ""      ""Video ID: _ycjY3Yu-NQ""
  },
  {
    "{": ""      ""Video ID: AtNneV6RKrw""
  },
  {
    "{": ""      ""Video ID: 8l6uuq_bHD0""
  },
  {
    "{": ""      ""Video ID: tOmwO9OyqjI""
  },
  {
    "{": ""      ""Video ID: rmUmjsGQysA""
  },
  {
    "{": ""      ""Video ID: NiG14X2x-z0""
  },
  {
    "{": ""      ""Video ID: dqxu0vkUPMo""
  },
  {
    "{": ""      ""Video ID: izOyx54GgiM""
  },
  {
    "{": ""      ""Video ID: IGIomHliJjE""
  },
  {
    "{": ""      ""Video ID: 6b8mLE4AKJ0""
  },
  {
    "{": ""      ""Video ID: MehuZLtGYRE""
  },
  {
    "{": ""      ""Video ID: F3ZJDFuyoXM""
  },
  {
    "{": ""      ""Video ID: wADOnRX29LI""
  },
  {
    "{": ""      ""Video ID: RRvtbdXcwJ0""
  },
  {
    "{": ""      ""Video ID: r03dQZfivlM""
  },
  {
    "{": ""      ""Video ID: xs_pybRpIZ0""
  },
  {
    "{": ""      ""Video ID: h75_TGiwg78""
  },
  {
    "{": ""      ""Video ID: G6YYUOx6fBU""
  },
  {
    "{": ""      ""Video ID: M9JagAv2nUE""
  },
  {
    "{": ""      ""Video ID: QpQHIO2kw58""
  },
  {
    "{": ""      ""Video ID: iNeshiY4ixI""
  },
  {
    "{": ""      ""Video ID: kzPOu1TtAFw""
  },
  {
    "{": ""      ""Video ID: yR22qyfCwO4""
  },
  {
    "{": ""      ""Video ID: eYVwTHqU2gw""
  },
  {
    "{": ""      ""Video ID: 9d7os_HakPY""
  },
  {
    "{": ""      ""Video ID: QVeMBNB0cII""
  },
  {
    "{": ""      ""Video ID: YagQ79Vnk6c""
  },
  {
    "{": ""      ""Video ID: Q4S0C0jpK2U""
  },
  {
    "{": ""      ""Video ID: 8PZnibTByEc""
  },
  {
    "{": ""      ""Video ID: tB8W35pNyWA""
  },
  {
    "{": ""      ""Video ID: XqOOursW4dk""
  },
  {
    "{": ""      ""Video ID: zgWVrZbXmJE""
  },
  {
    "{": ""      ""Video ID: QwHotsSZAM4""
  },
  {
    "{": ""      ""Video ID: KtAFuJq1W_0""
  },
  {
    "{": ""      ""Video ID: X7CgNJJ73PI""
  },
  {
    "{": ""      ""Video ID: kIwHFBbP2hA""
  },
  {
    "{": ""      ""Video ID: 3p1fSQUHDy0""
  },
  {
    "{": ""      ""Video ID: BDY_w_rdKk0""
  },
  {
    "{": ""      ""Video ID: Qgk3wVEi8kw""
  },
  {
    "{": ""      ""Video ID: waX9VLoboes""
  },
  {
    "{": ""      ""Video ID: bfjlHoOoKKk""
  },
  {
    "{": ""      ""Video ID: Iiw2RYhymxA""
  },
  {
    "{": ""      ""Video ID: XeY0dFxgAeo""
  },
  {
    "{": ""      ""Video ID: cF3wZL4BZvY""
  },
  {
    "{": ""      ""Video ID: RcEZlC2A588""
  },
  {
    "{": ""      ""Video ID: n5sg8hHCbbk""
  },
  {
    "{": ""      ""Video ID: 8Qud40wXTuw""
  },
  {
    "{": ""      ""Video ID: X5RW2K9C7r0""
  },
  {
    "{": ""      ""Video ID: xo0OReiyzek""
  },
  {
    "{": ""      ""Video ID: vBQigrJObwg""
  },
  {
    "{": ""      ""Video ID: U_lQYC7vqBg""
  },
  {
    "{": ""      ""Video ID: XhZ8yk6E_IA""
  },
  {
    "{": ""      ""Video ID: 70wOzCkWN5g""
  },
  {
    "{": ""      ""Video ID: 6Fif4XA7jAo""
  },
  {
    "{": ""      ""Video ID: Q3jPlfc67SE""
  },
  {
    "{": ""      ""Video ID: o5Ouim9GXlU""
  },
  {
    "{": ""      ""Video ID: 17BEBPTd1sc""
  },
  {
    "{": ""      ""Video ID: R02UZYItMGo""
  },
  {
    "{": ""      ""Video ID: Ls9yD4ZC6tA""
  },
  {
    "{": ""      ""Video ID: WcWMYAgNX2w""
  },
  {
    "{": ""      ""Video ID: tZvo6ryp6yo""
  },
  {
    "{": ""      ""Video ID: Qetpi5PvFDI""
  },
  {
    "{": ""      ""Video ID: 9szhm3JzJvA""
  },
  {
    "{": ""      ""Video ID: 5AVjMhMVYpQ""
  },
  {
    "{": ""      ""Video ID: 1cq6CcU52dk""
  },
  {
    "{": ""      ""Video ID: Jdrx_wPv-14""
  },
  {
    "{": ""      ""Video ID: fMuOQVLyT3c""
  },
  {
    "{": ""      ""Video ID: e3FGEoOfVrE""
  },
  {
    "{": ""      ""Video ID: tbeur1kNq-A""
  },
  {
    "{": ""      ""Video ID: hQUAwxmo-sE""
  },
  {
    "{": ""      ""Video ID: de4ev_cE8QY""
  },
  {
    "{": ""      ""Video ID: NPSO6nztoIY""
  },
  {
    "{": ""      ""Video ID: OO1sw2Qf1Kc""
  },
  {
    "{": ""      ""Video ID: Vw3dLtjdXcc""
  },
  {
    "{": ""      ""Video ID: Gxpat-BS9CA""
  },
  {
    "{": ""      ""Video ID: tkwIvsKVR18""
  },
  {
    "{": ""      ""Video ID: Yr9RoZguG6w""
  },
  {
    "{": ""      ""Video ID: 32fYr5G5_0I""
  },
  {
    "{": ""      ""Video ID: AQWEc-f3GoU""
  },
  {
    "{": ""      ""Video ID: JL-ux3oBFB4""
  },
  {
    "{": ""      ""Video ID: yuSwj5ok24k""
  },
  {
    "{": ""      ""Video ID: vBA8_UDkF60""
  },
  {
    "{": ""      ""Video ID: UJsybbSHfx4""
  },
  {
    "{": ""      ""Video ID: OrngtVuexXo""
  },
  {
    "{": ""      ""Video ID: GTehS3wBL28""
  },
  {
    "{": ""      ""Video ID: 7fk6W8YhI-s""
  },
  {
    "{": ""      ""Video ID: mXuA5v7ZBO8""
  },
  {
    "{": ""      ""Video ID: QOPQe24ghaE""
  },
  {
    "{": ""      ""Video ID: 8L8xTG7tufM""
  },
  {
    "{": ""      ""Video ID: QVLjIJUCiAs""
  },
  {
    "{": ""      ""Video ID: _M9qtQJi3E8""
  },
  {
    "{": ""      ""Video ID: uu02cey1h2I""
  },
  {
    "{": ""      ""Video ID: esuMpx-scK8""
  },
  {
    "{": ""      ""Video ID: fhrRrlbiVRA""
  },
  {
    "{": ""      ""Video ID: m8X_JXV-9Vw""
  },
  {
    "{": ""      ""Video ID: wZYBEFnwx6Y""
  },
  {
    "{": ""      ""Video ID: oT-RF8hKcNM""
  },
  {
    "{": ""      ""Video ID: HZ985KmgRjs""
  },
  {
    "{": ""      ""Video ID: CnhUYWbW3jQ""
  },
  {
    "{": ""      ""Video ID: FH_KIzvALnY""
  },
  {
    "{": ""      ""Video ID: dIUsey8dG-Q""
  },
  {
    "{": ""      ""Video ID: XIMLT78iMKg""
  },
  {
    "{": ""      ""Video ID: zNeZBaFyXJQ""
  },
  {
    "{": ""      ""Video ID: -0lE2xsc5o4""
  },
  {
    "{": ""      ""Video ID: 5kJpk60rFh4""
  },
  {
    "{": ""      ""Video ID: 1oJ6YH2UXf4""
  },
  {
    "{": ""      ""Video ID: QdA--wAWhrg""
  },
  {
    "{": ""      ""Video ID: fQ13ih74o4A""
  },
  {
    "{": ""      ""Video ID: 2mcfTMsq2hE""
  },
  {
    "{": ""      ""Video ID: c6qHsUmKWks""
  },
  {
    "{": ""      ""Video ID: G5ex87s--98""
  },
  {
    "{": ""      ""Video ID: EvO5kD4yr1Y""
  },
  {
    "{": ""      ""Video ID: gxIaFRErFmg""
  },
  {
    "{": ""      ""Video ID: IunLNAHrqKI""
  },
  {
    "{": ""      ""Video ID: OgDvCmQUIww""
  },
  {
    "{": ""      ""Video ID: JWHvfb2VtsM""
  },
  {
    "{": ""      ""Video ID: hfjmw-VROWM""
  },
  {
    "{": ""      ""Video ID: 0Jo_ffnLrwM""
  },
  {
    "{": ""      ""Video ID: pmVpGBcw9ys""
  },
  {
    "{": ""      ""Video ID: r9gNr5VfQEo""
  },
  {
    "{": ""      ""Video ID: Nilb4NKMk1U""
  },
  {
    "{": ""      ""Video ID: wjziCs6jjIo""
  },
  {
    "{": ""      ""Video ID: X9HjJcfj1Q8""
  },
  {
    "{": ""      ""Video ID: ol0IroaWAMw""
  },
  {
    "{": ""      ""Video ID: NH4d4fTki3w""
  },
  {
    "{": ""      ""Video ID: fxiby4D4FGs""
  },
  {
    "{": ""      ""Video ID: yG3NQE0ONJs""
  },
  {
    "{": ""      ""Video ID: mFII0BQDaHc""
  },
  {
    "{": ""      ""Video ID: -ive4l1lqwI""
  },
  {
    "{": ""      ""Video ID: -FEK6tsBJkc""
  },
  {
    "{": ""      ""Video ID: wQ4Vq-8oVOI""
  },
  {
    "{": ""      ""Video ID: DTBiWxN4BlM""
  },
  {
    "{": ""      ""Video ID: -fR__iQFbZI""
  },
  {
    "{": ""      ""Video ID: P8X8glLOfmA""
  },
  {
    "{": ""      ""Video ID: ASqxKOex68s""
  },
  {
    "{": ""      ""Video ID: m-XI1ThYihY""
  },
  {
    "{": ""      ""Video ID: qdOSyMlzblM""
  },
  {
    "{": ""      ""Video ID: 96i7TxFQCGU""
  },
  {
    "{": ""      ""Video ID: mWZf2t3loSs""
  },
  {
    "{": ""      ""Video ID: oIBpoglCWJ0""
  },
  {
    "{": ""      ""Video ID: wdXyIf9PQbw""
  },
  {
    "{": ""      ""Video ID: 5hgh4z-K2Eg""
  },
  {
    "{": ""      ""Video ID: K7nWs0RPiDE""
  },
  {
    "{": ""      ""Video ID: rNg95xuwuCs""
  },
  {
    "{": ""      ""Video ID: EV9UuqRBulM""
  },
  {
    "{": ""      ""Video ID: cTiCIZYuHZU""
  },
  {
    "{": ""      ""Video ID: q_pB5BhDmzQ""
  },
  {
    "{": ""      ""Video ID: sPT9WV4BKoU""
  },
  {
    "{": ""      ""Video ID: ju3NGBVcrEs""
  },
  {
    "{": ""      ""Video ID: fkrEEbdC7Ik""
  },
  {
    "{": ""      ""Video ID: 5OkE4XfEBVY""
  },
  {
    "{": ""      ""Video ID: MyzzgkAqdXQ""
  },
  {
    "{": ""      ""Video ID: wlDfEFqJyQ8""
  },
  {
    "{": ""      ""Video ID: YVcr309jq8c""
  },
  {
    "{": ""      ""Video ID: hVIeg8EZJV8""
  },
  {
    "{": ""      ""Video ID: r9zI2UedeAg""
  },
  {
    "{": ""      ""Video ID: -cVHKky_zTk""
  },
  {
    "{": ""      ""Video ID: gJ4gdASWK6s""
  },
  {
    "{": ""      ""Video ID: puTdSbGpQug""
  },
  {
    "{": ""      ""Video ID: uzEZZSneVXM""
  },
  {
    "{": ""      ""Video ID: _5ywQU1HRS0""
  },
  {
    "{": ""      ""Video ID: -BZoIO48xHU""
  },
  {
    "{": ""      ""Video ID: ECPa-4Qx1FU""
  },
  {
    "{": ""      ""Video ID: D7H2VppWXZQ""
  },
  {
    "{": ""      ""Video ID: dj0RbgsqHl4""
  },
  {
    "{": ""      ""Video ID: jAduYj_ySCg""
  },
  {
    "{": ""      ""Video ID: zCx8kQ3FHP0""
  },
  {
    "{": ""      ""Video ID: DBJyq0v5MGE""
  },
  {
    "{": ""      ""Video ID: aUhke9vWpzw""
  },
  {
    "{": ""      ""Video ID: PocekJ77RGE""
  },
  {
    "{": ""      ""Video ID: lRzGGVfbCfI""
  },
  {
    "{": ""      ""Video ID: 71EMST3T77M""
  },
  {
    "{": ""      ""Video ID: 4GyVoSlQFng""
  },
  {
    "{": ""      ""Video ID: -bugCc6QFhE""
  },
  {
    "{": ""      ""Video ID: 3sy29MN82pg""
  },
  {
    "{": ""      ""Video ID: xYDQECz2yIw""
  },
  {
    "{": ""      ""Video ID: 7s4i_cj2Nzo""
  },
  {
    "{": ""      ""Video ID: DVWUqlqVLlM""
  },
  {
    "{": ""      ""Video ID: ThJideEsdhQ""
  },
  {
    "{": ""      ""Video ID: m3D9Lnv09YM""
  },
  {
    "{": ""      ""Video ID: WwJZJ9GyqKQ""
  },
  {
    "{": ""      ""Video ID: Svsz5qbxmuY""
  },
  {
    "{": ""      ""Video ID: lLfXLSitzlM""
  },
  {
    "{": ""      ""Video ID: iOgxsplkfkM""
  },
  {
    "{": ""      ""Video ID: MuiECYXyLcU""
  },
  {
    "{": ""      ""Video ID: Zv0QlZHu3oc""
  },
  {
    "{": ""      ""Video ID: xzxf_DwvxDI""
  },
  {
    "{": ""      ""Video ID: pd_WGC6bbEs""
  },
  {
    "{": ""      ""Video ID: 9SDjzW43XrY""
  },
  {
    "{": ""      ""Video ID: UolkXm957ew""
  },
  {
    "{": ""      ""Video ID: p7_X1I2hMSQ""
  },
  {
    "{": ""      ""Video ID: UjH2X19xKyo""
  },
  {
    "{": ""      ""Video ID: czYQmzuYkfY""
  },
  {
    "{": ""      ""Video ID: jTrS2rT3f2c""
  },
  {
    "{": ""      ""Video ID: RkcaCCwE-ok""
  },
  {
    "{": ""      ""Video ID: N-_4taNCIqY""
  },
  {
    "{": ""      ""Video ID: hY8gwEXQLC0""
  },
  {
    "{": ""      ""Video ID: pR8x-54tKrc""
  },
  {
    "{": ""      ""Video ID: YVb6andT95U""
  },
  {
    "{": ""      ""Video ID: T1y4TkS7u4k""
  },
  {
    "{": ""      ""Video ID: 9_3mWKRfHwc""
  },
  {
    "{": ""      ""Video ID: Zec6OdLsXmg""
  },
  {
    "{": ""      ""Video ID: A9_LQKlLSBo""
  },
  {
    "{": ""      ""Video ID: 9qG8JLp9fFU""
  },
  {
    "{": ""      ""Video ID: 1M00K37TXpM""
  },
  {
    "{": ""      ""Video ID: -SgJM_uFdR4""
  },
  {
    "{": ""      ""Video ID: 4jqSBHarmno""
  },
  {
    "{": ""      ""Video ID: okLfu5AgwLs""
  },
  {
    "{": ""      ""Video ID: Xr9T-3yvLIQ""
  },
  {
    "{": ""      ""Video ID: -_sVUXHlPmo""
  },
  {
    "{": ""      ""Video ID: 4bVrquf0E44""
  },
  {
    "{": ""      ""Video ID: vV1d0NzaGnk""
  },
  {
    "{": ""      ""Video ID: Yr2UH32vPhc""
  },
  {
    "{": ""      ""Video ID: Y0jSaDMoHb8""
  },
  {
    "{": ""      ""Video ID: EpfzE3eMkJw""
  },
  {
    "{": ""      ""Video ID: alxjl4IjZ9k""
  },
  {
    "{": ""      ""Video ID: YcRD_te3YBM""
  },
  {
    "{": ""      ""Video ID: fZXWW4C2kpE""
  },
  {
    "{": ""      ""Video ID: LZLZNm0jcAQ""
  },
  {
    "{": ""      ""Video ID: Js0LuRRDnQc""
  },
  {
    "{": ""      ""Video ID: 3sd60dbQPrM""
  },
  {
    "{": ""      ""Video ID: tO6VQ1KvGnU""
  },
  {
    "{": ""      ""Video ID: YBBcHWw6ypE""
  },
  {
    "{": ""      ""Video ID: JWFX8gfppzk""
  },
  {
    "{": ""      ""Video ID: a8m_7mW5MNE""
  },
  {
    "{": ""      ""Video ID: HloPISq-VKw""
  },
  {
    "{": ""      ""Video ID: 5b44JgsWh3I""
  },
  {
    "{": ""      ""Video ID: WLDgw5hFnR4""
  },
  {
    "{": ""      ""Video ID: 6Q0aEyGHkUs""
  },
  {
    "{": ""      ""Video ID: AQKnErKX2ho""
  },
  {
    "{": ""      ""Video ID: gKK9-ohIIQY""
  },
  {
    "{": ""      ""Video ID: Tns3PEsiD24""
  },
  {
    "{": ""      ""Video ID: Bid_urt5JzY""
  },
  {
    "{": ""      ""Video ID: pivRBzEnZxU""
  },
  {
    "{": ""      ""Video ID: UhYQ-GQyEB0""
  },
  {
    "{": ""      ""Video ID: 7ffwY74XbS4""
  },
  {
    "{": ""      ""Video ID: YcAVFPoxzOM""
  },
  {
    "{": ""      ""Video ID: zLOVXS14Gpg""
  },
  {
    "{": ""      ""Video ID: fijFDVCeyj0""
  },
  {
    "{": ""      ""Video ID: 6O0p4ZDnDoQ""
  },
  {
    "{": ""      ""Video ID: xuzqRhY_7fw""
  },
  {
    "{": ""      ""Video ID: Rp6nwJspU3E""
  },
  {
    "{": ""      ""Video ID: p9KtAWVcqw0""
  },
  {
    "{": ""      ""Video ID: ir59yOHCUpA""
  },
  {
    "{": ""      ""Video ID: yOeoFQThTFo""
  },
  {
    "{": ""      ""Video ID: Z_k-NL_wwAA""
  },
  {
    "{": ""      ""Video ID: b6ijbd6AkGg""
  },
  {
    "{": ""      ""Video ID: T4DIj7SU98E""
  },
  {
    "{": ""      ""Video ID: GtPBmotxMvg""
  },
  {
    "{": ""      ""Video ID: QCP-4ojeH-I""
  },
  {
    "{": ""      ""Video ID: 4h-Jb37cubU""
  },
  {
    "{": ""      ""Video ID: udF2IWam-uo""
  },
  {
    "{": ""      ""Video ID: QU2G08A8kP8""
  },
  {
    "{": ""      ""Video ID: N5NJoZRYOJk""
  },
  {
    "{": ""      ""Video ID: XIKzTDJabJE""
  },
  {
    "{": ""      ""Video ID: 1r2Z8YTIeGU""
  },
  {
    "{": ""      ""Video ID: AKB4IPFO5ao""
  },
  {
    "{": ""      ""Video ID: QQxm0v6IQ4E""
  },
  {
    "{": ""      ""Video ID: b-xf5IQFhQ0""
  },
  {
    "{": ""      ""Video ID: pXb6WNT6KoY""
  },
  {
    "{": ""      ""Video ID: Dsf5NHK_CAk""
  },
  {
    "{": ""      ""Video ID: vCmlZamH438""
  },
  {
    "{": ""      ""Video ID: EVevJk-K6As""
  },
  {
    "{": ""      ""Video ID: Ja2siHDoCiA""
  },
  {
    "{": ""      ""Video ID: emUGBl6WsK0""
  },
  {
    "{": ""      ""Video ID: xioqSLekGgQ""
  },
  {
    "{": ""      ""Video ID: YfTcR3Sy3Wo""
  },
  {
    "{": ""      ""Video ID: X80NTlEoLb4""
  },
  {
    "{": ""      ""Video ID: MuDIT-LWwg4""
  },
  {
    "{": ""      ""Video ID: SfiXSVANzgY""
  },
  {
    "{": ""      ""Video ID: XoO3lNQ9dX0""
  },
  {
    "{": ""      ""Video ID: y5razk4_2xE""
  },
  {
    "{": ""      ""Video ID: 1nHp90Z2NJk""
  },
  {
    "{": ""      ""Video ID: 37-LHOj7j6U""
  },
  {
    "{": ""      ""Video ID: aKQyvlKrNQQ""
  },
  {
    "{": ""      ""Video ID: 5KVqh5NAYxs""
  },
  {
    "{": ""      ""Video ID: tu4_rWhwtT4""
  },
  {
    "{": ""      ""Video ID: wniuF3-QQZ4""
  },
  {
    "{": ""      ""Video ID: rs_-fUDsVSU""
  },
  {
    "{": ""      ""Video ID: totsIB_V4CM""
  },
  {
    "{": ""      ""Video ID: tpnFJsEtK-8""
  },
  {
    "{": ""      ""Video ID: dKlBksiBRTU""
  },
  {
    "{": ""      ""Video ID: 3mACUDDtNI8""
  },
  {
    "{": ""      ""Video ID: GMMRlPGNKs8""
  },
  {
    "{": ""      ""Video ID: Csm47JBgW_0""
  },
  {
    "{": ""      ""Video ID: O9I9kgNw6bc""
  },
  {
    "{": ""      ""Video ID: i8btoMhv03s""
  },
  {
    "{": ""      ""Video ID: 6zHqX2ijSDM""
  },
  {
    "{": ""      ""Video ID: u8rTexGh_Mk""
  },
  {
    "{": ""      ""Video ID: -8HbwkluaTc""
  },
  {
    "{": ""      ""Video ID: xEgsuxYplS0""
  },
  {
    "{": ""      ""Video ID: upUx3R0JpZ8""
  },
  {
    "{": ""      ""Video ID: _S12OJykSuc""
  },
  {
    "{": ""      ""Video ID: 0iJM0ykdS_A""
  },
  {
    "{": ""      ""Video ID: izq2R_sETfc""
  },
  {
    "{": ""      ""Video ID: Pl6Kv8yzNHo""
  },
  {
    "{": ""      ""Video ID: BvXpzAZQEUQ""
  },
  {
    "{": ""      ""Video ID: nKI6vrJG8yM""
  },
  {
    "{": ""      ""Video ID: kH3htMOFTeY""
  },
  {
    "{": ""      ""Video ID: n7dbcFxK46Y""
  },
  {
    "{": ""      ""Video ID: Qpytq6s5DBk""
  },
  {
    "{": ""      ""Video ID: Q_bLw7xyymQ""
  },
  {
    "{": ""      ""Video ID: 1vjRyHLLYLU""
  },
  {
    "{": ""      ""Video ID: BOzBTGGVWNg""
  },
  {
    "{": ""      ""Video ID: UFCYrZCfX60""
  },
  {
    "{": ""      ""Video ID: z2zHyVVUJ3w""
  },
  {
    "{": ""      ""Video ID: jdu5GcwDZUQ""
  },
  {
    "{": ""      ""Video ID: lDOsX9XQZkE""
  },
  {
    "{": ""      ""Video ID: XN-zu1Q4o0w""
  },
  {
    "{": ""      ""Video ID: JmberMK2F5A""
  },
  {
    "{": ""      ""Video ID: cH2KKRBYIs4""
  },
  {
    "{": ""      ""Video ID: Ruz5oUSx2OI""
  },
  {
    "{": ""      ""Video ID: p0tQd3Tg2Lg""
  },
  {
    "{": ""      ""Video ID: aKQ4XCEZXLk""
  },
  {
    "{": ""      ""Video ID: XfproQcY4r4""
  },
  {
    "{": ""      ""Video ID: Z0Oha0f2LkY""
  },
  {
    "{": ""      ""Video ID: CPvpagEZQr8""
  },
  {
    "{": ""      ""Video ID: qW3OGcLeSYw""
  },
  {
    "{": ""      ""Video ID: LahgxK-tWtU""
  },
  {
    "{": ""      ""Video ID: dtVLuUJs7ts""
  },
  {
    "{": ""      ""Video ID: b1wd1MtlHyo""
  },
  {
    "{": ""      ""Video ID: 2tatqYQJZRk""
  },
  {
    "{": ""      ""Video ID: SMrrdfOUNxs""
  },
  {
    "{": ""      ""Video ID: 9TJPs9CQvAo""
  },
  {
    "{": ""      ""Video ID: 4WRv_eYgNF8""
  },
  {
    "{": ""      ""Video ID: CB2ipdmtYuI""
  },
  {
    "{": ""      ""Video ID: np10nf3TUnQ""
  },
  {
    "{": ""      ""Video ID: VXEVwQ1u52g""
  },
  {
    "{": ""      ""Video ID: frGdT2kMDg0""
  },
  {
    "{": ""      ""Video ID: p0DQmAsOI_8""
  },
  {
    "{": ""      ""Video ID: hCyT-fCrkU4""
  },
  {
    "{": ""      ""Video ID: rX8uz1Wb6Fk""
  },
  {
    "{": ""      ""Video ID: Ry28RikVmIw""
  },
  {
    "{": ""      ""Video ID: 3FglPZT433U""
  },
  {
    "{": ""      ""Video ID: aGG1SbjQmdY""
  },
  {
    "{": ""      ""Video ID: oZiru5S3WJQ""
  },
  {
    "{": ""      ""Video ID: 4xxiK2KvBgQ""
  },
  {
    "{": ""      ""Video ID: HypEbrxOvTw""
  },
  {
    "{": ""      ""Video ID: 2XSZLBFaFqY""
  },
  {
    "{": ""      ""Video ID: drgXoDEjTKQ""
  },
  {
    "{": ""      ""Video ID: avmQe_i6uAk""
  },
  {
    "{": ""      ""Video ID: QTL-c1O_Wbg""
  },
  {
    "{": ""      ""Video ID: 8_mUBURILaE""
  },
  {
    "{": ""      ""Video ID: j1YGq-UKZLQ""
  },
  {
    "{": ""      ""Video ID: SAyT6SPu9pQ""
  },
  {
    "{": ""      ""Video ID: VrE0GoAsjY8""
  },
  {
    "{": ""      ""Video ID: y__n1Yvlb_4""
  },
  {
    "{": ""      ""Video ID: g48ttmpUBac""
  },
  {
    "{": ""      ""Video ID: EANNbpTooFE""
  },
  {
    "{": ""      ""Video ID: kJB02JWp5Oo""
  },
  {
    "{": ""      ""Video ID: EqgfD-5Ux3M""
  },
  {
    "{": ""      ""Video ID: OISpAFrtMH8""
  },
  {
    "{": ""      ""Video ID: _MhwbHBWMmM""
  },
  {
    "{": ""      ""Video ID: 2mrg7CBP1RY""
  },
  {
    "{": ""      ""Video ID: TpOqDOh9_B8""
  },
  {
    "{": ""      ""Video ID: ZlVH9g8b4Ic""
  },
  {
    "{": ""      ""Video ID: RyoLgiNLSxQ""
  },
  {
    "{": ""      ""Video ID: f1Ep6SJL_zM""
  },
  {
    "{": ""      ""Video ID: 3Fq-Sr1H3Rc""
  },
  {
    "{": ""      ""Video ID: kAMIlPudalQ""
  },
  {
    "{": ""      ""Video ID: bOjmH1N7lZU""
  },
  {
    "{": ""      ""Video ID: RzV_D7tTeIE""
  },
  {
    "{": ""      ""Video ID: 826BvCTcqic""
  },
  {
    "{": ""      ""Video ID: NQ-rQDB5ogs""
  },
  {
    "{": ""      ""Video ID: lcPH8GECNQA""
  },
  {
    "{": ""      ""Video ID: Vmu7okiiKJk""
  },
  {
    "{": ""      ""Video ID: adiMMYyuKNQ""
  },
  {
    "{": ""      ""Video ID: Kk8Pdd8xkRI""
  },
  {
    "{": ""      ""Video ID: LQoOSx0a0YM""
  },
  {
    "{": ""      ""Video ID: bbNh2G_mkFE""
  },
  {
    "{": ""      ""Video ID: MHFKdQuhx2A""
  },
  {
    "{": ""      ""Video ID: 2KIWgnh8Qzg""
  },
  {
    "{": ""      ""Video ID: Xxfb1OGJbbQ""
  },
  {
    "{": ""      ""Video ID: PTpdy3oUV50""
  },
  {
    "{": ""      ""Video ID: qHvmjZ9STqA""
  },
  {
    "{": ""      ""Video ID: dhs9GDhnj7g""
  },
  {
    "{": ""      ""Video ID: 2brQKwX2Dfw""
  },
  {
    "{": ""      ""Video ID: uL9MBhQk25c""
  },
  {
    "{": ""      ""Video ID: q9Es89zk-dk""
  },
  {
    "{": ""      ""Video ID: HzSKpfeNN-8""
  },
  {
    "{": ""      ""Video ID: hOtM10A4T8Y""
  },
  {
    "{": ""      ""Video ID: -5C4mxE_YVk""
  },
  {
    "{": ""      ""Video ID: 2J1nudfLn-Y""
  },
  {
    "{": ""      ""Video ID: mGDuyKmrWXI""
  },
  {
    "{": ""      ""Video ID: rz8bu0K9JEw""
  },
  {
    "{": ""      ""Video ID: nohNJaBkZI0""
  },
  {
    "{": ""      ""Video ID: cEQZxE1byGI""
  },
  {
    "{": ""      ""Video ID: e1JyhMIJXKE""
  },
  {
    "{": ""      ""Video ID: 9vXcWMdI0IA""
  },
  {
    "{": ""      ""Video ID: P2_wJ3rZU8o""
  },
  {
    "{": ""      ""Video ID: MjrGT-p-UVs""
  },
  {
    "{": ""      ""Video ID: DjGaupI6w0c""
  },
  {
    "{": ""      ""Video ID: Ja9YlQ2wXnM""
  },
  {
    "{": ""      ""Video ID: EGHEtDZoLXI""
  },
  {
    "{": ""      ""Video ID: clkBClOwTsk""
  },
  {
    "{": ""      ""Video ID: aaWGXIJFMaU""
  },
  {
    "{": ""      ""Video ID: GX-EUff234Q""
  },
  {
    "{": ""      ""Video ID: f8g20usbubM""
  },
  {
    "{": ""      ""Video ID: EDlC7oG_2W4""
  },
  {
    "{": ""      ""Video ID: RiV_ue-PbL4""
  },
  {
    "{": ""      ""Video ID: 7U89om0zqIc""
  },
  {
    "{": ""      ""Video ID: UUXBCdt5IPg""
  },
  {
    "{": ""      ""Video ID: T64bFq_0xjk""
  },
  {
    "{": ""      ""Video ID: saovOvNfekM""
  },
  {
    "{": ""      ""Video ID: qe2C2Em-LOg""
  },
  {
    "{": ""      ""Video ID: ZlqZ0YycdzQ""
  },
  {
    "{": ""      ""Video ID: TsdvYk7PWeY""
  },
  {
    "{": ""      ""Video ID: HUfRokK7QE4""
  },
  {
    "{": ""      ""Video ID: xKz_3kikbzg""
  },
  {
    "{": ""      ""Video ID: GDACOyymPv0""
  },
  {
    "{": ""      ""Video ID: c26gs2mPN-o""
  },
  {
    "{": ""      ""Video ID: 7L7xFGtYCr4""
  },
  {
    "{": ""      ""Video ID: iXjNSmOgMvY""
  },
  {
    "{": ""      ""Video ID: T6YW_Avr9Q8""
  },
  {
    "{": ""      ""Video ID: eLb2OB76gw4""
  },
  {
    "{": ""      ""Video ID: 2i0JZPWykkI""
  },
  {
    "{": ""      ""Video ID: EF4F0RpACCg""
  },
  {
    "{": ""      ""Video ID: utwsFEb5iNA""
  },
  {
    "{": ""      ""Video ID: WCCo9799dWo""
  },
  {
    "{": ""      ""Video ID: KYpv6D3_6o8""
  },
  {
    "{": ""      ""Video ID: UKeU95Mi63E""
  },
  {
    "{": ""      ""Video ID: 6GuO5ddcs1k""
  },
  {
    "{": ""      ""Video ID: cDTSalVum34""
  },
  {
    "{": ""      ""Video ID: jOW4cBr_0_E""
  },
  {
    "{": ""      ""Video ID: SfYJwvG4OhE""
  },
  {
    "{": ""      ""Video ID: x5NB6LUQIGM""
  },
  {
    "{": ""      ""Video ID: aFO9p2SyE0Y""
  },
  {
    "{": ""      ""Video ID: l0azEi_-Qao""
  },
  {
    "{": ""      ""Video ID: ExPv1zsnH0Q""
  },
  {
    "{": ""      ""Video ID: SXONkT-IBAI""
  },
  {
    "{": ""      ""Video ID: zPlK0nKwP6s""
  },
  {
    "{": ""      ""Video ID: 7mnbxHNJpu0""
  },
  {
    "{": ""      ""Video ID: -jd-8ugwDPc""
  },
  {
    "{": ""      ""Video ID: KKKEnQptNhc""
  },
  {
    "{": ""      ""Video ID: HplOMedipUY""
  },
  {
    "{": ""      ""Video ID: waXSjvTvgnM""
  },
  {
    "{": ""      ""Video ID: OeT12G-Dfsg""
  },
  {
    "{": ""      ""Video ID: 5mA4ReTz_Pk""
  },
  {
    "{": ""      ""Video ID: PgMZ9tJ31Vc""
  },
  {
    "{": ""      ""Video ID: ldt7jkJqaxU""
  },
  {
    "{": ""      ""Video ID: FE7Mnzqzxik""
  },
  {
    "{": ""      ""Video ID: 49heq3a0oog""
  },
  {
    "{": ""      ""Video ID: mRZ1zaHiHM8""
  },
  {
    "{": ""      ""Video ID: rf4Q0bP6R4I""
  },
  {
    "{": ""      ""Video ID: 1f0g5YEYQmc""
  },
  {
    "{": ""      ""Video ID: K92NzGRVG7U""
  },
  {
    "{": ""      ""Video ID: LwvP96U5mF4""
  },
  {
    "{": ""      ""Video ID: LRbjjiZhDdM""
  },
  {
    "{": ""      ""Video ID: RVQPxlaHLac""
  },
  {
    "{": ""      ""Video ID: xVDI31yAYxc""
  },
  {
    "{": ""      ""Video ID: QIc4QrcAOrg""
  },
  {
    "{": ""      ""Video ID: GoCkNBp7YIU""
  },
  {
    "{": ""      ""Video ID: DRmhd2ybiDQ""
  },
  {
    "{": ""      ""Video ID: -KwoqmuK-Uw""
  },
  {
    "{": ""      ""Video ID: bKZjbxCuPqs""
  },
  {
    "{": ""      ""Video ID: KCUlu6-OuOM""
  },
  {
    "{": ""      ""Video ID: bdxIZBGEbfA""
  },
  {
    "{": ""      ""Video ID: p7D7E8mwBbs""
  },
  {
    "{": ""      ""Video ID: vqQes0kv-uo""
  },
  {
    "{": ""      ""Video ID: vJEmBzsxVMQ""
  },
  {
    "{": ""      ""Video ID: SPdSoaYgohI""
  },
  {
    "{": ""      ""Video ID: LEKq3chrw9M""
  },
  {
    "{": ""      ""Video ID: eovwidIVXZ4""
  },
  {
    "{": ""      ""Video ID: 5MLnDeUuu5s""
  },
  {
    "{": ""      ""Video ID: MayCqtfXN7g""
  },
  {
    "{": ""      ""Video ID: N0vhCGk7kWE""
  },
  {
    "{": ""      ""Video ID: RsRmMWWWGOY""
  },
  {
    "{": ""      ""Video ID: dM0cn6EWy9w""
  },
  {
    "{": ""      ""Video ID: Bs1dqmPgO0s""
  },
  {
    "{": ""      ""Video ID: kpPC2lDbOAY""
  },
  {
    "{": ""      ""Video ID: fiEi_jXKdVA""
  },
  {
    "{": ""      ""Video ID: _7XwlXiDR-U""
  },
  {
    "{": ""      ""Video ID: QED6Tk1R-aQ""
  },
  {
    "{": ""      ""Video ID: 0qVrj0yhCzg""
  },
  {
    "{": ""      ""Video ID: NvlTeQyJQ4o""
  },
  {
    "{": ""      ""Video ID: _S8aOE_ngro""
  },
  {
    "{": ""      ""Video ID: nNZUB6Te204""
  },
  {
    "{": ""      ""Video ID: KcMkPbrvDUE""
  },
  {
    "{": ""      ""Video ID: 5zXY6rpFxWs""
  },
  {
    "{": ""      ""Video ID: GzQnCi8SWS0""
  },
  {
    "{": ""      ""Video ID: Y0zH7A9hYcg""
  },
  {
    "{": ""      ""Video ID: eU8ugbR1Jr0""
  },
  {
    "{": ""      ""Video ID: tPoMGGp1DQM""
  },
  {
    "{": ""      ""Video ID: koH0sDec2-k""
  },
  {
    "{": ""      ""Video ID: Eh-cQ3XHzTE""
  },
  {
    "{": ""      ""Video ID: Wsds-Y0Ua1M""
  },
  {
    "{": ""      ""Video ID: suEdKcFq4-w""
  },
  {
    "{": ""      ""Video ID: 9YmaTlniogs""
  },
  {
    "{": ""      ""Video ID: _arXV_3tzt8""
  },
  {
    "{": ""      ""Video ID: e6LnOOc-p_o""
  },
  {
    "{": ""      ""Video ID: bTC22WA2gJk""
  },
  {
    "{": ""      ""Video ID: p-j0PxrTci4""
  },
  {
    "{": ""      ""Video ID: hL-MhvYXEUA""
  },
  {
    "{": ""      ""Video ID: uiONjrculpw""
  },
  {
    "{": ""      ""Video ID: g3BNjGyLc-c""
  },
  {
    "{": ""      ""Video ID: eJmZk9J-9uM""
  },
  {
    "{": ""      ""Video ID: xCyvzI2aVUo""
  },
  {
    "{": ""      ""Video ID: 4-zGbcr1eWw""
  },
  {
    "{": ""      ""Video ID: fP0g5dL6OV8""
  },
  {
    "{": ""      ""Video ID: do0hy4hfDaM""
  },
  {
    "{": ""      ""Video ID: vUnqjmdSoOM""
  },
  {
    "{": ""      ""Video ID: fkTv19GVY98""
  },
  {
    "{": ""      ""Video ID: ysljQBhfN_0""
  },
  {
    "{": ""      ""Video ID: hJGO3E-0qLM""
  },
  {
    "{": ""      ""Video ID: j693iJl48d4""
  },
  {
    "{": ""      ""Video ID: o74L3s7L-zM""
  },
  {
    "{": ""      ""Video ID: wOMMReTd_Jg""
  },
  {
    "{": ""      ""Video ID: PKRiAxPg-Zc""
  },
  {
    "{": ""      ""Video ID: rcAizNJNVU4""
  },
  {
    "{": ""      ""Video ID: J0SIGDKorP8""
  },
  {
    "{": ""      ""Video ID: m7Zd4kburpA""
  },
  {
    "{": ""      ""Video ID: ZyoQ7KVYhTM""
  },
  {
    "{": ""      ""Video ID: 3zGWsRYaJ5E""
  },
  {
    "{": ""      ""Video ID: fj9Sztm_wu8""
  },
  {
    "{": ""      ""Video ID: r8RIbD9S5II""
  },
  {
    "{": ""      ""Video ID: NDKKl4Kd3mc""
  },
  {
    "{": ""      ""Video ID: pVPrhBj_7JA""
  },
  {
    "{": ""      ""Video ID: cuNp4tgc96E""
  },
  {
    "{": ""      ""Video ID: Tx_htrGnrwo""
  },
  {
    "{": ""      ""Video ID: 1WeDOI8W5KA""
  },
  {
    "{": ""      ""Video ID: hXUZlPg6DiI""
  },
  {
    "{": ""      ""Video ID: 1iAB70NMNUA""
  },
  {
    "{": ""      ""Video ID: PRjJa9RcV-M""
  },
  {
    "{": ""      ""Video ID: fyKMWz1L11s""
  },
  {
    "{": ""      ""Video ID: d0BcysJ9VU0""
  },
  {
    "{": ""      ""Video ID: tw1L0fd9nVA""
  },
  {
    "{": ""      ""Video ID: NnQhWOYVGMQ""
  },
  {
    "{": ""      ""Video ID: ObtPA7LtoAo""
  },
  {
    "{": ""      ""Video ID: agQT2lBnWCg""
  },
  {
    "{": ""      ""Video ID: CsiTlGq0UX4""
  },
  {
    "{": ""      ""Video ID: jrLiDk98QuE""
  },
  {
    "{": ""      ""Video ID: nyguUcwvzvQ""
  },
  {
    "{": ""      ""Video ID: Aj12PjXdx6o""
  },
  {
    "{": ""      ""Video ID: WyYFAPbA4sk""
  },
  {
    "{": ""      ""Video ID: Nir4ZyJhYG0""
  },
  {
    "{": ""      ""Video ID: CSXxAnAcVhU""
  },
  {
    "{": ""      ""Video ID: _VvwItcGXfM""
  },
  {
    "{": ""      ""Video ID: 1UZwi6Kw-eo""
  },
  {
    "{": ""      ""Video ID: IP6c6oswQSA""
  },
  {
    "{": ""      ""Video ID: LMpiQzuwQ3Q""
  },
  {
    "{": ""      ""Video ID: dXVI93es5-4""
  },
  {
    "{": ""      ""Video ID: FC_QW0tEzf0""
  },
  {
    "{": ""      ""Video ID: Dni3E7IMzGo""
  },
  {
    "{": ""      ""Video ID: vgcO2Lg4RyM""
  },
  {
    "{": ""      ""Video ID: kbBIaI2XtTM""
  },
  {
    "{": ""      ""Video ID: qz_qByS-q34""
  },
  {
    "{": ""      ""Video ID: DN9wF3rsX5Q""
  },
  {
    "{": ""      ""Video ID: HPjf-PpAjQY""
  },
  {
    "{": ""      ""Video ID: qp4EnI7Llgs""
  },
  {
    "{": ""      ""Video ID: fyybsigvQiA""
  },
  {
    "{": ""      ""Video ID: QShMmtKU4Io""
  },
  {
    "{": ""      ""Video ID: c7uTaAlHhr8""
  },
  {
    "{": ""      ""Video ID: WNAxVpn207M""
  },
  {
    "{": ""      ""Video ID: R-XHAVigovM""
  },
  {
    "{": ""      ""Video ID: 2eeEa4jQbxw""
  },
  {
    "{": ""      ""Video ID: 3l3mFlBvRgs""
  },
  {
    "{": ""      ""Video ID: S6-4FKorQr0""
  },
  {
    "{": ""      ""Video ID: Zi1GDpBdI6I""
  },
  {
    "{": ""      ""Video ID: xbIDAJJOGA0""
  },
  {
    "{": ""      ""Video ID: sSUIIPoo3NY""
  },
  {
    "{": ""      ""Video ID: xtVrIlFJwks""
  },
  {
    "{": ""      ""Video ID: AAQwLisIdU8""
  },
  {
    "{": ""      ""Video ID: TZNPnEJ6dCU""
  },
  {
    "{": ""      ""Video ID: egKSzCXQjA4""
  },
  {
    "{": ""      ""Video ID: Nt7U5EHRo50""
  },
  {
    "{": ""      ""Video ID: FPs1hKq5I14""
  },
  {
    "{": ""      ""Video ID: p_soUf29bmE""
  },
  {
    "{": ""      ""Video ID: YuY7uN58IZM""
  },
  {
    "{": ""      ""Video ID: rBoXgYo_nBM""
  },
  {
    "{": ""      ""Video ID: swTsGnfakFo""
  },
  {
    "{": ""      ""Video ID: Rl5Y14z5ANs""
  },
  {
    "{": ""      ""Video ID: _QmON9EKX-Y""
  },
  {
    "{": ""      ""Video ID: d8QpKQeYKVg""
  },
  {
    "{": ""      ""Video ID: gfPY2dg0wzE""
  },
  {
    "{": ""      ""Video ID: NrWDBah_GMY""
  },
  {
    "{": ""      ""Video ID: j4S69kP3nBE""
  },
  {
    "{": ""      ""Video ID: fY6icg4O3QA""
  },
  {
    "{": ""      ""Video ID: -mVqCaL5UlM""
  },
  {
    "{": ""      ""Video ID: R5pnGAwZ7eY""
  },
  {
    "{": ""      ""Video ID: KrMWUkZejWc""
  },
  {
    "{": ""      ""Video ID: n9oPp9A-xwg""
  },
  {
    "{": ""      ""Video ID: 26AXx8jaN1g""
  },
  {
    "{": ""      ""Video ID: Q4Sxq_MkCdc""
  },
  {
    "{": ""      ""Video ID: khCUquyHrQE""
  },
  {
    "{": ""      ""Video ID: 1D7Dy2-6dr0""
  },
  {
    "{": ""      ""Video ID: 0bU6nwF1rI4""
  },
  {
    "{": ""      ""Video ID: UbMh-b_PymI""
  },
  {
    "{": ""      ""Video ID: ldaR6y0fZbk""
  },
  {
    "{": ""      ""Video ID: PrytvE2lMro""
  },
  {
    "{": ""      ""Video ID: ywR5EnK5S20""
  },
  {
    "{": ""      ""Video ID: bkP5wMofzbQ""
  },
  {
    "{": ""      ""Video ID: fz-Hu7y5jNc""
  },
  {
    "{": ""      ""Video ID: pSXC0xjMHYc""
  },
  {
    "{": ""      ""Video ID: wWsCbvU_6WU""
  },
  {
    "{": ""      ""Video ID: _Hfcvr3KJ30""
  },
  {
    "{": ""      ""Video ID: B_JsB2Pgoso""
  },
  {
    "{": ""      ""Video ID: iUE0dGyHric""
  },
  {
    "{": ""      ""Video ID: YRuSLmbyrOI""
  },
  {
    "{": ""      ""Video ID: vhzVJ-I06hU""
  },
  {
    "{": ""      ""Video ID: v9zzRJKRt0Y""
  },
  {
    "{": ""      ""Video ID: OOXTf5L0Wdk""
  },
  {
    "{": ""      ""Video ID: tU08wGTalhs""
  },
  {
    "{": ""      ""Video ID: EJsC12oV8_s""
  },
  {
    "{": ""      ""Video ID: ZAqo0Mnz1qM""
  },
  {
    "{": ""      ""Video ID: WvApqDaxXwQ""
  },
  {
    "{": ""      ""Video ID: sd33JB5nSqs""
  },
  {
    "{": ""      ""Video ID: T01XEATJIFs""
  },
  {
    "{": ""      ""Video ID: DKJDEWv2x2k""
  },
  {
    "{": ""      ""Video ID: Dvr7ccRAIqA""
  },
  {
    "{": ""      ""Video ID: 8GUHdxUoiJ4""
  },
  {
    "{": ""      ""Video ID: kkeZKYHpjcQ""
  },
  {
    "{": ""      ""Video ID: ygZtzxp-C3A""
  },
  {
    "{": ""      ""Video ID: haiKcsr1krE""
  },
  {
    "{": ""      ""Video ID: m8ag1BH0pC8""
  },
  {
    "{": ""      ""Video ID: sYMzTselj18""
  },
  {
    "{": ""      ""Video ID: qfaRnoxL4bs""
  },
  {
    "{": ""      ""Video ID: 5QYkZVAH4eU""
  },
  {
    "{": ""      ""Video ID: 2qgCPJFw4jg""
  },
  {
    "{": ""      ""Video ID: vgF5PPVkhi4""
  },
  {
    "{": ""      ""Video ID: R-FBMvifr8M""
  },
  {
    "{": ""      ""Video ID: TVvD_D1wilc""
  },
  {
    "{": ""      ""Video ID: 1tWAh96Unhg""
  },
  {
    "{": ""      ""Video ID: Re3BOKn4D-w""
  },
  {
    "{": ""      ""Video ID: G1PIdZ7t2dE""
  },
  {
    "{": ""      ""Video ID: lqv8zTCCKyE""
  },
  {
    "{": ""      ""Video ID: 5UfooIFJym8""
  },
  {
    "{": ""      ""Video ID: GXTU-DCBb4A""
  },
  {
    "{": ""      ""Video ID: Cby07VP4CjY""
  },
  {
    "{": ""      ""Video ID: C01iolpMz9o""
  },
  {
    "{": ""      ""Video ID: XVWcaTMW5j4""
  },
  {
    "{": ""      ""Video ID: 7dZX8j8K6Mc""
  },
  {
    "{": ""      ""Video ID: zZacptZtHRU""
  },
  {
    "{": ""      ""Video ID: dOvfXdI32yE""
  },
  {
    "{": ""      ""Video ID: _6rlTGssKBE""
  },
  {
    "{": ""      ""Video ID: zIVLtgqtf9Q""
  },
  {
    "{": ""      ""Video ID: 71KXnxfkMVc""
  },
  {
    "{": ""      ""Video ID: vItDbWNAX6Y""
  },
  {
    "{": ""      ""Video ID: _RQYrLpC_fA""
  },
  {
    "{": ""      ""Video ID: 4Jr-952OOcw""
  },
  {
    "{": ""      ""Video ID: j5BwD_fjwEs""
  },
  {
    "{": ""      ""Video ID: WtgBibmYuF0""
  },
  {
    "{": ""      ""Video ID: hu8VMsNVkX0""
  },
  {
    "{": ""      ""Video ID: SyJycfsHRSM""
  },
  {
    "{": ""      ""Video ID: dDYgbdFQFjM""
  },
  {
    "{": ""      ""Video ID: irGgjlItSqA""
  },
  {
    "{": ""      ""Video ID: sLZrhs9NWxs""
  },
  {
    "{": ""      ""Video ID: OWwEuVVUp0E""
  },
  {
    "{": ""      ""Video ID: dt-lQHmzXPM""
  },
  {
    "{": ""      ""Video ID: pr-2NbkPcCw""
  },
  {
    "{": ""      ""Video ID: 7I1Q_fWROjM""
  },
  {
    "{": ""      ""Video ID: A7C4arfrgOI""
  },
  {
    "{": ""      ""Video ID: BTIBDx7O34I""
  },
  {
    "{": ""      ""Video ID: Pgo5H-oHYjE""
  },
  {
    "{": ""      ""Video ID: fp0v6cVKLXM""
  },
  {
    "{": ""      ""Video ID: fJswlQsy8W4""
  },
  {
    "{": ""      ""Video ID: fNWJIZi4EDk""
  },
  {
    "{": ""      ""Video ID: UExNGnG8oOU""
  },
  {
    "{": ""      ""Video ID: jq-MwRnxMIY""
  },
  {
    "{": ""      ""Video ID: VPuhGagGpX8""
  },
  {
    "{": ""      ""Video ID: Ln71G-Xjm8Y""
  },
  {
    "{": ""      ""Video ID: 96csjMKf-08""
  },
  {
    "{": ""      ""Video ID: zP8GG1TFGls""
  },
  {
    "{": ""      ""Video ID: qvvEJbFpyAU""
  },
  {
    "{": ""      ""Video ID: ziBf-gAVId8""
  },
  {
    "{": ""      ""Video ID: Er-agIt5-jg""
  },
  {
    "{": ""      ""Video ID: dSXNxieRyXM""
  },
  {
    "{": ""      ""Video ID: aVwqmEIzd9U""
  },
  {
    "{": ""      ""Video ID: -ZST7CE7v-M""
  },
  {
    "{": ""      ""Video ID: LiNhzycdUK4""
  },
  {
    "{": ""      ""Video ID: Yy4TYk6CWkk""
  },
  {
    "{": ""      ""Video ID: hFRHQ3u7nPA""
  },
  {
    "{": ""      ""Video ID: iqkgQqPf-uE""
  },
  {
    "{": ""      ""Video ID: co6G-vyAlII""
  },
  {
    "{": ""      ""Video ID: lvRJEWHzGTo""
  },
  {
    "{": ""      ""Video ID: VSZg9hTQ9D8""
  },
  {
    "{": ""      ""Video ID: lDDSOfRROks""
  },
  {
    "{": ""      ""Video ID: N1fUvo_mqF8""
  },
  {
    "{": ""      ""Video ID: -umKXRjfCbI""
  },
  {
    "{": ""      ""Video ID: jqh6mfaH4AY""
  },
  {
    "{": ""      ""Video ID: HuKLrRKGKoM""
  },
  {
    "{": ""      ""Video ID: Q4hYRv7IhWQ""
  },
  {
    "{": ""      ""Video ID: mwM5nR3khU0""
  },
  {
    "{": ""      ""Video ID: 5N5GaB6r0UE""
  },
  {
    "{": ""      ""Video ID: 7a4nYaJ4Apg""
  },
  {
    "{": ""      ""Video ID: eElRy81L2VE""
  },
  {
    "{": ""      ""Video ID: kfonicgQiv8""
  },
  {
    "{": ""      ""Video ID: JjMl6z1PZX4""
  },
  {
    "{": ""      ""Video ID: LesBD-w04zI""
  },
  {
    "{": ""      ""Video ID: wyDS-9uuqX4""
  },
  {
    "{": ""      ""Video ID: FNhGQYo4yZs""
  },
  {
    "{": ""      ""Video ID: 35f5sxGa5NY""
  },
  {
    "{": ""      ""Video ID: pDjI3O_M2EE""
  },
  {
    "{": ""      ""Video ID: VNoD0ACuDso""
  },
  {
    "{": ""      ""Video ID: YSBHDhWzhGk""
  },
  {
    "{": ""      ""Video ID: 32U8wSrv7UY""
  },
  {
    "{": ""      ""Video ID: kBScjF2BHUA""
  },
  {
    "{": ""      ""Video ID: CgVNQgN-Vvc""
  },
  {
    "{": ""      ""Video ID: JNyRE-4ek-M""
  },
  {
    "{": ""      ""Video ID: AAzWE8nPa2Y""
  },
  {
    "{": ""      ""Video ID: uEBmRHrskGE""
  },
  {
    "{": ""      ""Video ID: LS6_TG0D9uM""
  },
  {
    "{": ""      ""Video ID: Bk6CVlvh_dA""
  },
  {
    "{": ""      ""Video ID: PMstA9uOP7c""
  },
  {
    "{": ""      ""Video ID: TDM-Zmj4i5c""
  },
  {
    "{": ""      ""Video ID: 1pjpoV09TK4""
  },
  {
    "{": ""      ""Video ID: DSBtYAGtpKw""
  },
  {
    "{": ""      ""Video ID: ZQMSfA83bEs""
  },
  {
    "{": ""      ""Video ID: IFTzdx0TdFY""
  },
  {
    "{": ""      ""Video ID: RKC7chsbj2M""
  },
  {
    "{": ""      ""Video ID: DZ_F_3oBwxE""
  },
  {
    "{": ""      ""Video ID: IaW5mKV_-6o""
  },
  {
    "{": ""      ""Video ID: L3PvmReclJw""
  },
  {
    "{": ""      ""Video ID: M0OCutAjdOU""
  },
  {
    "{": ""      ""Video ID: KcNoryVVzoE""
  },
  {
    "{": ""      ""Video ID: vpzcWVCwing""
  },
  {
    "{": ""      ""Video ID: diD2lr_BGcU""
  },
  {
    "{": ""      ""Video ID: f4DAbiIiU_I""
  },
  {
    "{": ""      ""Video ID: x90TUhYnVyQ""
  },
  {
    "{": ""      ""Video ID: Kih8i9F9WLk""
  },
  {
    "{": ""      ""Video ID: qR4mD6tCLmQ""
  },
  {
    "{": ""      ""Video ID: S1p7UaEVEjE""
  },
  {
    "{": ""      ""Video ID: GkV29vf5ME0""
  },
  {
    "{": ""      ""Video ID: btCpR8iI3ds""
  },
  {
    "{": ""      ""Video ID: _QiFESLGtXc""
  },
  {
    "{": ""      ""Video ID: 5TD2F-Q7HT8""
  },
  {
    "{": ""      ""Video ID: 5KP2bOJcnJg""
  },
  {
    "{": ""      ""Video ID: 8c1P7U5qzpU""
  },
  {
    "{": ""      ""Video ID: Wrh8kk38ed0""
  },
  {
    "{": ""      ""Video ID: UgMiGqA6xtA""
  },
  {
    "{": ""      ""Video ID: mS1mtTFWzx4""
  },
  {
    "{": ""      ""Video ID: uuouvflt0Gc""
  },
  {
    "{": ""      ""Video ID: CPpMGbNskj4""
  },
  {
    "{": ""      ""Video ID: ze8oQR_1UaQ""
  },
  {
    "{": ""      ""Video ID: y7fGzCDwYGA""
  },
  {
    "{": ""      ""Video ID: ilXMNXg2JKU""
  },
  {
    "{": ""      ""Video ID: d-m7lEGbnyY""
  },
  {
    "{": ""      ""Video ID: TRTrnNIrN3M""
  },
  {
    "{": ""      ""Video ID: aciSrdkVoLM""
  },
  {
    "{": ""      ""Video ID: vK0nluB7DTQ""
  },
  {
    "{": ""      ""Video ID: bETvlUv2eT4""
  },
  {
    "{": ""      ""Video ID: dnLb9s9ADmw""
  },
  {
    "{": ""      ""Video ID: XvnI7BRqTkM""
  },
  {
    "{": ""      ""Video ID: lm3JUPYtT08""
  },
  {
    "{": ""      ""Video ID: _GBOaJ_88xs""
  },
  {
    "{": ""      ""Video ID: i-q64R3UDCg""
  },
  {
    "{": ""      ""Video ID: xZ8agDnNJeo""
  },
  {
    "{": ""      ""Video ID: MnD1phh3epc""
  },
  {
    "{": ""      ""Video ID: 0uvxDJxid_U""
  },
  {
    "{": ""      ""Video ID: WMmSzUdwtG8""
  },
  {
    "{": ""      ""Video ID: 6nH4psCYYZI""
  },
  {
    "{": ""      ""Video ID: a-W7FtRb_YE""
  },
  {
    "{": ""      ""Video ID: Ggo6DpoX8AI""
  },
  {
    "{": ""      ""Video ID: J9HC-lm46ow""
  },
  {
    "{": ""      ""Video ID: 2PcaoAZZ6Rc""
  },
  {
    "{": ""      ""Video ID: n5zZtUV4npA""
  },
  {
    "{": ""      ""Video ID: lOuj9q0W9v4""
  },
  {
    "{": ""      ""Video ID: EHHzd7XOwJ4""
  },
  {
    "{": ""      ""Video ID: Oc9aqZvyjGo""
  },
  {
    "{": ""      ""Video ID: awU7Dkizof8""
  },
  {
    "{": ""      ""Video ID: a28ilTWQAfU""
  },
  {
    "{": ""      ""Video ID: ZtnYCiR90UA""
  },
  {
    "{": ""      ""Video ID: Orn2WdRe9jE""
  },
  {
    "{": ""      ""Video ID: YCarTchAhXo""
  },
  {
    "{": ""      ""Video ID: NfkJ3X0Fbzc""
  },
  {
    "{": ""      ""Video ID: RvwKQkzSUlM""
  },
  {
    "{": ""      ""Video ID: DdCloYpBom4""
  },
  {
    "{": ""      ""Video ID: udxmoHrcLDg""
  },
  {
    "{": ""      ""Video ID: iHYSa2IY2Xc""
  },
  {
    "{": ""      ""Video ID: qFONmKZdTQo""
  },
  {
    "{": ""      ""Video ID: sXCFqA8sREI""
  },
  {
    "{": ""      ""Video ID: oAdS1-INMmo""
  },
  {
    "{": ""      ""Video ID: o4cyIqlyFBM""
  },
  {
    "{": ""      ""Video ID: V7eMYwzZ32U""
  },
  {
    "{": ""      ""Video ID: 3D1qpX5VS9E""
  },
  {
    "{": ""      ""Video ID: aUTywDDgiME""
  },
  {
    "{": ""      ""Video ID: cSwNDDDyEno""
  },
  {
    "{": ""      ""Video ID: 3DN41gUppAc""
  },
  {
    "{": ""      ""Video ID: 9SeTfcj3UKI""
  },
  {
    "{": ""      ""Video ID: ORdl90W4M1o""
  },
  {
    "{": ""      ""Video ID: I-TkAWUZG4s""
  },
  {
    "{": ""      ""Video ID: 4ewGDd44yro""
  },
  {
    "{": ""      ""Video ID: b83KsPno1JE""
  },
  {
    "{": ""      ""Video ID: NNFTCeb8mA0""
  },
  {
    "{": ""      ""Video ID: hoDtwlhhvHI""
  },
  {
    "{": ""      ""Video ID: SmkNe7vysRY""
  },
  {
    "{": ""      ""Video ID: YjmAYmZAkUI""
  },
  {
    "{": ""      ""Video ID: HkYPL-7qe98""
  },
  {
    "{": ""      ""Video ID: -A2y_NHMOio""
  },
  {
    "{": ""      ""Video ID: J2a1deW-JIo""
  },
  {
    "{": ""      ""Video ID: cnLlkueI5bk""
  },
  {
    "{": ""      ""Video ID: ktFb56ZsvG8""
  },
  {
    "{": ""      ""Video ID: CECSxQGpmNo""
  },
  {
    "{": ""      ""Video ID: O8RCm3Zw9lI""
  },
  {
    "{": ""      ""Video ID: C44HkD0E31o""
  },
  {
    "{": ""      ""Video ID: i6NdubBFdYM""
  },
  {
    "{": ""      ""Video ID: w0YyEm5tNeQ""
  },
  {
    "{": ""      ""Video ID: tyjk_NpuwRo""
  },
  {
    "{": ""      ""Video ID: _hKfFInxbK0""
  },
  {
    "{": ""      ""Video ID: HB7_z0aL7oA""
  },
  {
    "{": ""      ""Video ID: ltmTSn0PhGo""
  },
  {
    "{": ""      ""Video ID: H5MYn5iLBAE""
  },
  {
    "{": ""      ""Video ID: YAJLiexHi9Q""
  },
  {
    "{": ""      ""Video ID: DoyumfnRhIQ""
  },
  {
    "{": ""      ""Video ID: ZfxK5ndRHEk""
  },
  {
    "{": ""      ""Video ID: 5R5kEZwIXQo""
  },
  {
    "{": ""      ""Video ID: l6GpG098YsI""
  },
  {
    "{": ""      ""Video ID: KhxKB8lgkFs""
  },
  {
    "{": ""      ""Video ID: 93im7tNsUM8""
  },
  {
    "{": ""      ""Video ID: rLYIP_DesCE""
  },
  {
    "{": ""      ""Video ID: qFJ6P0Rdghk""
  },
  {
    "{": ""      ""Video ID: otikMMv1mFg""
  },
  {
    "{": ""      ""Video ID: A-tMUqN_5BE""
  },
  {
    "{": ""      ""Video ID: ed6aUNgiY44""
  },
  {
    "{": ""      ""Video ID: m727FafonJY""
  },
  {
    "{": ""      ""Video ID: bWJQYzELxQ8""
  },
  {
    "{": ""      ""Video ID: 8DlB97VSf4Q""
  },
  {
    "{": ""      ""Video ID: jydQ9J-7v9I""
  },
  {
    "{": ""      ""Video ID: mM4Rc68-i-Q""
  },
  {
    "{": ""      ""Video ID: wU48nwDQaBc""
  },
  {
    "{": ""      ""Video ID: nA-u1tDHTfw""
  },
  {
    "{": ""      ""Video ID: 1kzrpsytrGc""
  },
  {
    "{": ""      ""Video ID: W83dDWlPYXU""
  },
  {
    "{": ""      ""Video ID: DXvkOoGBmeI""
  },
  {
    "{": ""      ""Video ID: bHXwQPClTxw""
  },
  {
    "{": ""      ""Video ID: EyCI5IZxnks""
  },
  {
    "{": ""      ""Video ID: Z3ENiX_yMpo""
  },
  {
    "{": ""      ""Video ID: XCYzHYDwbXM""
  },
  {
    "{": ""      ""Video ID: MyRm2pSBdqk""
  },
  {
    "{": ""      ""Video ID: Z77vd4kQCVE""
  },
  {
    "{": ""      ""Video ID: OfwiG6Ktee4""
  },
  {
    "{": ""      ""Video ID: 89PfsPpRYU4""
  },
  {
    "{": ""      ""Video ID: P7Cvz9-ZD9Q""
  },
  {
    "{": ""      ""Video ID: FLNk2ouRh_4""
  },
  {
    "{": ""      ""Video ID: U4AjeJq9kV0""
  },
  {
    "{": ""      ""Video ID: aBR9J4Bf0sw""
  },
  {
    "{": ""      ""Video ID: Kuj54d87xVY""
  },
  {
    "{": ""      ""Video ID: KzhZYAEr1pk""
  },
  {
    "{": ""      ""Video ID: kpSca9cHMq4""
  },
  {
    "{": ""      ""Video ID: X6zSLWBrtFA""
  },
  {
    "{": ""      ""Video ID: DqCkDcx6KIs""
  },
  {
    "{": ""      ""Video ID: _G30E4W3oyU""
  },
  {
    "{": ""      ""Video ID: Ut69WcBvR3c""
  },
  {
    "{": ""      ""Video ID: RUpZZ8Qtl3s""
  },
  {
    "{": ""      ""Video ID: ckgkHNXnvHU""
  },
  {
    "{": ""      ""Video ID: 0xO2gqi_ZjY""
  },
  {
    "{": ""      ""Video ID: 4HtOJwql5Vo""
  },
  {
    "{": ""      ""Video ID: _ludpxi1LFM""
  },
  {
    "{": ""      ""Video ID: 6xSy1WazNfM""
  },
  {
    "{": ""      ""Video ID: 5j0os9Yd434""
  },
  {
    "{": ""      ""Video ID: BQAAta5Mbp8""
  },
  {
    "{": ""      ""Video ID: ZYeF10xwsH8""
  },
  {
    "{": ""      ""Video ID: FDVm8OIP_M0""
  },
  {
    "{": ""      ""Video ID: tlHCleR4ctM""
  },
  {
    "{": ""      ""Video ID: B_8eBQ1JKzA""
  },
  {
    "{": ""      ""Video ID: qn70gPukdtY""
  },
  {
    "{": ""      ""Video ID: GbHUjMFzr-c""
  },
  {
    "{": ""      ""Video ID: LQJ8Wo9lj4k""
  },
  {
    "{": ""      ""Video ID: xVSj44wnDg0""
  },
  {
    "{": ""      ""Video ID: W3GoB7nnc-I""
  },
  {
    "{": ""      ""Video ID: ySR9LKV76hU""
  },
  {
    "{": ""      ""Video ID: SXG3OgrZwSQ""
  },
  {
    "{": ""      ""Video ID: 6YKZNjGaUyM""
  },
  {
    "{": ""      ""Video ID: GWn8Trzl8Ks""
  },
  {
    "{": ""      ""Video ID: fKjLiHURQWo""
  },
  {
    "{": ""      ""Video ID: wDNDRDJy-vo""
  },
  {
    "{": ""      ""Video ID: ssEQDTGKn8E""
  },
  {
    "{": ""      ""Video ID: AzDPXY0DVIg""
  },
  {
    "{": ""      ""Video ID: Gr8BMXL1iAQ""
  },
  {
    "{": ""      ""Video ID: QjfSDTJF9AI""
  },
  {
    "{": ""      ""Video ID: unPBLZaKhg0""
  },
  {
    "{": ""      ""Video ID: cnorc1nVZK0""
  },
  {
    "{": ""      ""Video ID: 5dkGsiJdLxM""
  },
  {
    "{": ""      ""Video ID: Jy42v57CQQ4""
  },
  {
    "{": ""      ""Video ID: bxmYFzJ2G6Q""
  },
  {
    "{": ""      ""Video ID: UMi9vf3XLVI""
  },
  {
    "{": ""      ""Video ID: P_rOZbQUmvk""
  },
  {
    "{": ""      ""Video ID: Yj4GJfPsk6o""
  },
  {
    "{": ""      ""Video ID: sdSw4ngtC-Y""
  },
  {
    "{": ""      ""Video ID: BBi2udFHY-Q""
  },
  {
    "{": ""      ""Video ID: yfPvJ3nyJK4""
  },
  {
    "{": ""      ""Video ID: aDqFQ_Yc4L0""
  },
  {
    "{": ""      ""Video ID: ddCCwkM6Ul0""
  },
  {
    "{": ""      ""Video ID: 9LZFvcOovtU""
  },
  {
    "{": ""      ""Video ID: 9afBnEuTF-Y""
  },
  {
    "{": ""      ""Video ID: kDTjMooYTBE""
  },
  {
    "{": ""      ""Video ID: id1L-nFVlao""
  },
  {
    "{": ""      ""Video ID: BYFJl1ZvRhc""
  },
  {
    "{": ""      ""Video ID: HtkpsrmuTDE""
  },
  {
    "{": ""      ""Video ID: GYtymgxgr-I""
  },
  {
    "{": ""      ""Video ID: K0MFiceafq4""
  },
  {
    "{": ""      ""Video ID: WnwwqiDzcjU""
  },
  {
    "{": ""      ""Video ID: PT-nX25UrsI""
  },
  {
    "{": ""      ""Video ID: GNXP1djL27A""
  },
  {
    "{": ""      ""Video ID: VsZFiMo8TIc""
  },
  {
    "{": ""      ""Video ID: HJEGzZbSxDc""
  },
  {
    "{": ""      ""Video ID: Wc82zjZ0rPk""
  },
  {
    "{": ""      ""Video ID: 19ZufcEeDjo""
  },
  {
    "{": ""      ""Video ID: UKkZqcHQqCU""
  },
  {
    "{": ""      ""Video ID: 17d-SEV5vtk""
  },
  {
    "{": ""      ""Video ID: laEZDpUklU0""
  },
  {
    "{": ""      ""Video ID: 0ECuTFRcQ2s""
  },
  {
    "{": ""      ""Video ID: YYuIkLMsxbU""
  },
  {
    "{": ""      ""Video ID: ZV4NQVWe3VA""
  },
  {
    "{": ""      ""Video ID: 4rmuBELO1KY""
  },
  {
    "{": ""      ""Video ID: OJPYB3RCHq4""
  },
  {
    "{": ""      ""Video ID: xN_YmOVTKSA""
  },
  {
    "{": ""      ""Video ID: PrYW0lQKSA0""
  },
  {
    "{": ""      ""Video ID: niYfZEHfb5w""
  },
  {
    "{": ""      ""Video ID: VPDT_dKry_s""
  },
  {
    "{": ""      ""Video ID: HuiBllZxANs""
  },
  {
    "{": ""      ""Video ID: YEg1n--1bH8""
  },
  {
    "{": ""      ""Video ID: fto8uMsZ39s""
  },
  {
    "{": ""      ""Video ID: gDVaHaCXXmU""
  },
  {
    "{": ""      ""Video ID: OpUjZoQtKCk""
  },
  {
    "{": ""      ""Video ID: A2QRW1jfGPI""
  },
  {
    "{": ""      ""Video ID: xsPsmEkzMQI""
  },
  {
    "{": ""      ""Video ID: UoFbc7eIfJc""
  },
  {
    "{": ""      ""Video ID: -Hwksl1Z_zM""
  },
  {
    "{": ""      ""Video ID: jx8QJCdUR7c""
  },
  {
    "{": ""      ""Video ID: pxfpMJOc3JI""
  },
  {
    "{": ""      ""Video ID: UlZ9y7PNmzE""
  },
  {
    "{": ""      ""Video ID: 9xJ-cJXfpBc""
  },
  {
    "{": ""      ""Video ID: Q0x2vrWsBcA""
  },
  {
    "{": ""      ""Video ID: 5682lEwrYcU""
  },
  {
    "{": ""      ""Video ID: aRgH59DJGNo""
  },
  {
    "{": ""      ""Video ID: OXzvI-zJ1xY""
  },
  {
    "{": ""      ""Video ID: icvkmUhlYI4""
  },
  {
    "{": ""      ""Video ID: lXC88eP7At8""
  },
  {
    "{": ""      ""Video ID: j5n0HeBUg5U""
  },
  {
    "{": ""      ""Video ID: 9916RERQ5o8""
  },
  {
    "{": ""      ""Video ID: rqP_xOc683I""
  },
  {
    "{": ""      ""Video ID: TCJA7CioIks""
  },
  {
    "{": ""      ""Video ID: PJFP7127OLI""
  },
  {
    "{": ""      ""Video ID: qBgSr6uTH14""
  },
  {
    "{": ""      ""Video ID: NW5Vze52dxM""
  },
  {
    "{": ""      ""Video ID: O7XkclPWSyY""
  },
  {
    "{": ""      ""Video ID: O03XDGGDt3E""
  },
  {
    "{": ""      ""Video ID: _BCI646eBlI""
  },
  {
    "{": ""      ""Video ID: MEx_Qk9SSck""
  },
  {
    "{": ""      ""Video ID: A1QJnTgW-As""
  },
  {
    "{": ""      ""Video ID: 6p2sbU2zGPE""
  },
  {
    "{": ""      ""Video ID: F_K7n7zD5aU""
  },
  {
    "{": ""      ""Video ID: bkvmfSzzvRA""
  },
  {
    "{": ""      ""Video ID: SLxhAnquAGU""
  },
  {
    "{": ""      ""Video ID: fFWBmNnpnXs""
  },
  {
    "{": ""      ""Video ID: blcoMZH3aUk""
  },
  {
    "{": ""      ""Video ID: H7DaMB2TEDc""
  },
  {
    "{": ""      ""Video ID: A6IkefZtCIo""
  },
  {
    "{": ""      ""Video ID: hIXCb3a1acA""
  },
  {
    "{": ""      ""Video ID: R-bZ-f-7zZk""
  },
  {
    "{": ""      ""Video ID: lfmh4gwA9Ok""
  },
  {
    "{": ""      ""Video ID: 92xASYyb4WY""
  },
  {
    "{": ""      ""Video ID: PIra9HE15jo""
  },
  {
    "{": ""      ""Video ID: w5-gzzaays0""
  },
  {
    "{": ""      ""Video ID: 54Y3WmChUvo""
  },
  {
    "{": ""      ""Video ID: _06kk0bAG0M""
  },
  {
    "{": ""      ""Video ID: ZCADT94-uCw""
  },
  {
    "{": ""      ""Video ID: t6f6MXtKlbU""
  },
  {
    "{": ""      ""Video ID: FRS79DauAl8""
  },
  {
    "{": ""      ""Video ID: qrHgicnjvV8""
  },
  {
    "{": ""      ""Video ID: Du5w2LM6S_w""
  },
  {
    "{": ""      ""Video ID: YY4aBdwlAb8""
  },
  {
    "{": ""      ""Video ID: HF06jC7YDyA""
  },
  {
    "{": ""      ""Video ID: da3jLaF3JgU""
  },
  {
    "{": ""      ""Video ID: 1ipBCEZwbM0""
  },
  {
    "{": ""      ""Video ID: GrcrmBoHgPU""
  },
  {
    "{": ""      ""Video ID: CfN089ekLqI""
  },
  {
    "{": ""      ""Video ID: ul1l3K6nVgI""
  },
  {
    "{": ""      ""Video ID: CMKHSWJKB40""
  },
  {
    "{": ""      ""Video ID: 5k92R7IVbDs""
  },
  {
    "{": ""      ""Video ID: Invhsa87isk""
  },
  {
    "{": ""      ""Video ID: 7Pdg0hVWUx8""
  },
  {
    "{": ""      ""Video ID: mwsRxxLF1ww""
  },
  {
    "{": ""      ""Video ID: TfRJWos-cPU""
  },
  {
    "{": ""      ""Video ID: PSLU9PiXgRk""
  },
  {
    "{": ""      ""Video ID: Cuu6FQ3mb6A""
  },
  {
    "{": ""      ""Video ID: P9xCwM9osW0""
  },
  {
    "{": ""      ""Video ID: oS6eQ_4PyHk""
  },
  {
    "{": ""      ""Video ID: k7gtugi5SyY""
  },
  {
    "{": ""      ""Video ID: _jpxlIcHI38""
  },
  {
    "{": ""      ""Video ID: yKCBv-XU08s""
  },
  {
    "{": ""      ""Video ID: pwDlyXnlSsw""
  },
  {
    "{": ""      ""Video ID: JDWcubiIvr0""
  },
  {
    "{": ""      ""Video ID: Hm669-HDekw""
  },
  {
    "{": ""      ""Video ID: Gtmu9YqWPhI""
  },
  {
    "{": ""      ""Video ID: umvsgkvF4SE""
  },
  {
    "{": ""      ""Video ID: 0x4hZczko0A""
  },
  {
    "{": ""      ""Video ID: f4xdR53Un8Y""
  },
  {
    "{": ""      ""Video ID: 5syaIo3MFDA""
  },
  {
    "{": ""      ""Video ID: GFRDDkMgpuY""
  },
  {
    "{": ""      ""Video ID: FPwEhfw7buA""
  },
  {
    "{": ""      ""Video ID: davDQSIE-oA""
  },
  {
    "{": ""      ""Video ID: hqDLYhY1SOs""
  },
  {
    "{": ""      ""Video ID: 3vcvcWHJByw""
  },
  {
    "{": ""      ""Video ID: vanH3kVDpUU""
  },
  {
    "{": ""      ""Video ID: 5zDwYUwq5To""
  },
  {
    "{": ""      ""Video ID: VkVgdiXa7PE""
  },
  {
    "{": ""      ""Video ID: tEKbVYOKQy4""
  },
  {
    "{": ""      ""Video ID: JA8JAksrDqI""
  },
  {
    "{": ""      ""Video ID: IEkz0dahsDY""
  },
  {
    "{": ""      ""Video ID: 08i_INg0Mao""
  },
  {
    "{": ""      ""Video ID: eO44WX9LsnA""
  },
  {
    "{": ""      ""Video ID: RhdgTpcqSDU""
  },
  {
    "{": ""      ""Video ID: Lv61m_Z7ozo""
  },
  {
    "{": ""      ""Video ID: Vm6Vkym8xMk""
  },
  {
    "{": ""      ""Video ID: ZOU-DxzKtQA""
  },
  {
    "{": ""      ""Video ID: rpCqrgvT9_U""
  },
  {
    "{": ""      ""Video ID: Y4LE6zbaNi8""
  },
  {
    "{": ""      ""Video ID: qPiwQ3Zy280""
  },
  {
    "{": ""      ""Video ID: z4XtNH15BlQ""
  },
  {
    "{": ""      ""Video ID: A_ayP1nqI9c""
  },
  {
    "{": ""      ""Video ID: qA1m12NcRKI""
  },
  {
    "{": ""      ""Video ID: WKXOTi8hVFc""
  },
  {
    "{": ""      ""Video ID: MxjG9rvBIl8""
  },
  {
    "{": ""      ""Video ID: HD3GGibDobM""
  },
  {
    "{": ""      ""Video ID: liGEHuSdDAc""
  },
  {
    "{": ""      ""Video ID: ph5XNVfWqRI""
  },
  {
    "{": ""      ""Video ID: IpKpbUQn8ws""
  },
  {
    "{": ""      ""Video ID: mNT4wqC4-ig""
  },
  {
    "{": ""      ""Video ID: cLB_Pc5WCCs""
  },
  {
    "{": ""      ""Video ID: e9t8fgDo-vc""
  },
  {
    "{": ""      ""Video ID: _3xa0CUB2Es""
  },
  {
    "{": ""      ""Video ID: XmHhQayfHQI""
  },
  {
    "{": ""      ""Video ID: h57oSbQe12Y""
  },
  {
    "{": ""      ""Video ID: yXgyJgvBWhQ""
  },
  {
    "{": ""      ""Video ID: NFiCY2zj1S0""
  },
  {
    "{": ""      ""Video ID: Z9DsUp2xZbU""
  },
  {
    "{": ""      ""Video ID: qgi_pYPHnXk""
  },
  {
    "{": ""      ""Video ID: Z7mHNfw4tGo""
  },
  {
    "{": ""      ""Video ID: 7hjkr9RsPZI""
  },
  {
    "{": ""      ""Video ID: I9Xwi11mdmA""
  },
  {
    "{": ""      ""Video ID: vfxPWNbmM-E""
  },
  {
    "{": ""      ""Video ID: fVHOcmfLGx4""
  },
  {
    "{": ""      ""Video ID: oTfQI2QSLoA""
  },
  {
    "{": ""      ""Video ID: _fxmuBPl6NE""
  },
  {
    "{": ""      ""Video ID: 6R_3nS0gQTY""
  },
  {
    "{": ""      ""Video ID: H5FReMSPLUs""
  },
  {
    "{": ""      ""Video ID: k9_LVFjdhJQ""
  },
  {
    "{": ""      ""Video ID: EHDXnZ1kuqY""
  },
  {
    "{": ""      ""Video ID: 7c5asvQTtH4""
  },
  {
    "{": ""      ""Video ID: RY9AtYbHfMU""
  },
  {
    "{": ""      ""Video ID: mHfmmbKEGbA""
  },
  {
    "{": ""      ""Video ID: CRsYPiJWXKM""
  },
  {
    "{": ""      ""Video ID: ggE_wj-UfME""
  },
  {
    "{": ""      ""Video ID: VQ1Ri0Esw9o""
  },
  {
    "{": ""      ""Video ID: GIcDPkmtJ-A""
  },
  {
    "{": ""      ""Video ID: eeKp2ER1e3I""
  },
  {
    "{": ""      ""Video ID: X7E8kfANw0o""
  },
  {
    "{": ""      ""Video ID: ObHpvNq7exQ""
  },
  {
    "{": ""      ""Video ID: K1FQRdF0WZw""
  },
  {
    "{": ""      ""Video ID: Dwt0j7FD_sA""
  },
  {
    "{": ""      ""Video ID: 70KXIl4tQZw""
  },
  {
    "{": ""      ""Video ID: dr_BJ9Bp-HM""
  },
  {
    "{": ""      ""Video ID: OBuQDtskFt0""
  },
  {
    "{": ""      ""Video ID: WQaZVq7iZrU""
  },
  {
    "{": ""      ""Video ID: My334K4Nl0U""
  },
  {
    "{": ""      ""Video ID: 483DbIQd7_s""
  },
  {
    "{": ""      ""Video ID: 0A_YHkpB5DI""
  },
  {
    "{": ""      ""Video ID: IF3U2K3-xEE""
  },
  {
    "{": ""      ""Video ID: WN7EI6dEPuE""
  },
  {
    "{": ""      ""Video ID: cDasvO0PWxo""
  },
  {
    "{": ""      ""Video ID: sqgFTddRN7o""
  },
  {
    "{": ""      ""Video ID: GomWb5X-VRU""
  },
  {
    "{": ""      ""Video ID: 07eEY0KbBKg""
  },
  {
    "{": ""      ""Video ID: UGYBqU0XywI""
  },
  {
    "{": ""      ""Video ID: bymkbo6hbn0""
  },
  {
    "{": ""      ""Video ID: dJvYNOC6RZc""
  },
  {
    "{": ""      ""Video ID: s2g14PTq8Ao""
  },
  {
    "{": ""      ""Video ID: xeuzSS-NimA""
  },
  {
    "{": ""      ""Video ID: VrDesMQ0iR8""
  },
  {
    "{": ""      ""Video ID: 8FyHsH3V8Ig""
  },
  {
    "{": ""      ""Video ID: i3JsyLTuTsY""
  },
  {
    "{": ""      ""Video ID: kBBfL0NeZGo""
  },
  {
    "{": ""      ""Video ID: kyEoFGES5eE""
  },
  {
    "{": ""      ""Video ID: C32tpp-YuQU""
  },
  {
    "{": ""      ""Video ID: edJFnElf8tw""
  },
  {
    "{": ""      ""Video ID: UFbqGiy_zik""
  },
  {
    "{": ""      ""Video ID: SiEt7xyJAUs""
  },
  {
    "{": ""      ""Video ID: 41-yX1rXU40""
  },
  {
    "{": ""      ""Video ID: OGDk4-gDo1c""
  },
  {
    "{": ""      ""Video ID: rfMjnajcMKU""
  },
  {
    "{": ""      ""Video ID: 0lJVv7DyCAc""
  },
  {
    "{": ""      ""Video ID: UFYdJ6ztBSg""
  },
  {
    "{": ""      ""Video ID: s3b3Qd_7DnE""
  },
  {
    "{": ""      ""Video ID: PlUu-vFc2dc""
  },
  {
    "{": ""      ""Video ID: 20AMyvyr98M""
  },
  {
    "{": ""      ""Video ID: OSvalWOrOfM""
  },
  {
    "{": ""      ""Video ID: xe2555V-xPQ""
  },
  {
    "{": ""      ""Video ID: wuMKMiTDKE8""
  },
  {
    "{": ""      ""Video ID: 0t_jt5lWqNE""
  },
  {
    "{": ""      ""Video ID: rcHNItlXVKo""
  },
  {
    "{": ""      ""Video ID: mAJZ29D41aY""
  },
  {
    "{": ""      ""Video ID: 3C_MI-aiDZo""
  },
  {
    "{": ""      ""Video ID: 4Qv0eRzCRnU""
  },
  {
    "{": ""      ""Video ID: -YQEl1yZGeE""
  },
  {
    "{": ""      ""Video ID: txlsiXwodW8""
  },
  {
    "{": ""      ""Video ID: 79MmVq2tjDs""
  },
  {
    "{": ""      ""Video ID: Vn6FfVOe-U8""
  },
  {
    "{": ""      ""Video ID: PMX9glSQxTA""
  },
  {
    "{": ""      ""Video ID: Aqjv7RObU70""
  },
  {
    "{": ""      ""Video ID: DpQcJ-qzXLE""
  },
  {
    "{": ""      ""Video ID: _KwLarrJBQQ""
  },
  {
    "{": ""      ""Video ID: 6x-NAq3wKI8""
  },
  {
    "{": ""      ""Video ID: lAxBmM9Om-o""
  },
  {
    "{": ""      ""Video ID: 90ugheFZ9VU""
  },
  {
    "{": ""      ""Video ID: smNXYlZ0pU0""
  },
  {
    "{": ""      ""Video ID: WPIKtDRtjrc""
  },
  {
    "{": ""      ""Video ID: uaOmxUO_608""
  },
  {
    "{": ""      ""Video ID: f39QZzNdE5A""
  },
  {
    "{": ""      ""Video ID: pSXCMHSSepw""
  },
  {
    "{": ""      ""Video ID: WANn-WJjgpM""
  },
  {
    "{": ""      ""Video ID: v0ooT8ZpDxw""
  },
  {
    "{": ""      ""Video ID: nzbBQlQQ3p4""
  },
  {
    "{": ""      ""Video ID: ZRPduT9Jqu0""
  },
  {
    "{": ""      ""Video ID: V6Wcrx3gGHw""
  },
  {
    "{": ""      ""Video ID: QM3vrjDULuY""
  },
  {
    "{": ""      ""Video ID: I5IXIxYI6NI""
  },
  {
    "{": ""      ""Video ID: ceQehhD0eqc""
  },
  {
    "{": ""      ""Video ID: g3Mocj3n6jU""
  },
  {
    "{": ""      ""Video ID: 28zAKKMWVII""
  },
  {
    "{": ""      ""Video ID: WO4Abm_8FiE""
  },
  {
    "{": ""      ""Video ID: TQTpPAtF1Ok""
  },
  {
    "{": ""      ""Video ID: Lht_JH2xi6w""
  },
  {
    "{": ""      ""Video ID: bT0TLrEPqU0""
  },
  {
    "{": ""      ""Video ID: dxYNUu_2egM""
  },
  {
    "{": ""      ""Video ID: BWQY4XkYPZ8""
  },
  {
    "{": ""      ""Video ID: O9bJFUIiGfQ""
  },
  {
    "{": ""      ""Video ID: FzeDc8m4FPg""
  },
  {
    "{": ""      ""Video ID: 0uQ_X6nQ8xk""
  },
  {
    "{": ""      ""Video ID: o34Y3vRnBRw""
  },
  {
    "{": ""      ""Video ID: XMg1nVdycaU""
  },
  {
    "{": ""      ""Video ID: oEziOVgTjB8""
  },
  {
    "{": ""      ""Video ID: z4wfNu_gii4""
  },
  {
    "{": ""      ""Video ID: XUE3HytIUcc""
  },
  {
    "{": ""      ""Video ID: eVRmfcLhDhA""
  },
  {
    "{": ""      ""Video ID: vVrBO_SrX38""
  },
  {
    "{": ""      ""Video ID: 9p77_RWvpAY""
  },
  {
    "{": ""      ""Video ID: zsZnmTQSVJ8""
  },
  {
    "{": ""      ""Video ID: xuiXIK8GzFs""
  },
  {
    "{": ""      ""Video ID: -uH2xLGznG4""
  },
  {
    "{": ""      ""Video ID: aeLp8QiyzBE""
  },
  {
    "{": ""      ""Video ID: _aoIxQnySwM""
  },
  {
    "{": ""      ""Video ID: JQ-kuIPkVas""
  },
  {
    "{": ""      ""Video ID: sHbmu0F54h4""
  },
  {
    "{": ""      ""Video ID: Tk2aZR85iSk""
  },
  {
    "{": ""      ""Video ID: FySEamcsFRQ""
  },
  {
    "{": ""      ""Video ID: eNwzNczqVF8""
  },
  {
    "{": ""      ""Video ID: Sdz8C_c1WyU""
  },
  {
    "{": ""      ""Video ID: iVgkRWNFLA4""
  },
  {
    "{": ""      ""Video ID: b56l4iOjSM8""
  },
  {
    "{": ""      ""Video ID: OuoRj0p85RU""
  },
  {
    "{": ""      ""Video ID: eSlSgKFZQtw""
  },
  {
    "{": ""      ""Video ID: oxKEjFc2amI""
  },
  {
    "{": ""      ""Video ID: hq-l_UO2Ydw""
  },
  {
    "{": ""      ""Video ID: fRpqWDgj5ng""
  },
  {
    "{": ""      ""Video ID: lD7XZX_9kKM""
  },
  {
    "{": ""      ""Video ID: CrgX0U-i22Q""
  },
  {
    "{": ""      ""Video ID: H7itD1wab2Q""
  },
  {
    "{": ""      ""Video ID: YWgBFlieTbM""
  },
  {
    "{": ""      ""Video ID: jUd7ecyYU6s""
  },
  {
    "{": ""      ""Video ID: Wm3yuygUXQ0""
  },
  {
    "{": ""      ""Video ID: 1vybEbACF9w""
  },
  {
    "{": ""      ""Video ID: GmzFHXOEnn8""
  },
  {
    "{": ""      ""Video ID: -TKoot-GUV0""
  },
  {
    "{": ""      ""Video ID: 8g3q7FF_1Js""
  },
  {
    "{": ""      ""Video ID: DtzpG3gCrC4""
  },
  {
    "{": ""      ""Video ID: a6YoXtaWcqE""
  },
  {
    "{": ""      ""Video ID: qmGVYki-oyQ""
  },
  {
    "{": ""      ""Video ID: BfbNKG3lTs8""
  },
  {
    "{": ""      ""Video ID: Nxb77sktuxY""
  },
  {
    "{": ""      ""Video ID: GEO1BpkFDtk""
  },
  {
    "{": ""      ""Video ID: -9ZRIqqGbVw""
  },
  {
    "{": ""      ""Video ID: e8B9DkmUnJg""
  },
  {
    "{": ""      ""Video ID: aVEoiFRYJ10""
  },
  {
    "{": ""      ""Video ID: MEvoy_owET8""
  },
  {
    "{": ""      ""Video ID: KWFaAfZes-c""
  },
  {
    "{": ""      ""Video ID: b3uX5XwdN_8""
  },
  {
    "{": ""      ""Video ID: TnWeWAeD1zY""
  },
  {
    "{": ""      ""Video ID: bWlPSLUT-6U""
  },
  {
    "{": ""      ""Video ID: NiMUYX3rlUo""
  },
  {
    "{": ""      ""Video ID: znkiOA1psoc""
  },
  {
    "{": ""      ""Video ID: PVIXnSQ2I7M""
  },
  {
    "{": ""      ""Video ID: x3fYg7cG1CQ""
  },
  {
    "{": ""      ""Video ID: laXiC8Aj_hI""
  },
  {
    "{": ""      ""Video ID: L0CR0Dwqj4o""
  },
  {
    "{": ""      ""Video ID: S8ZVaOYUUts""
  },
  {
    "{": ""      ""Video ID: hSmTZhdV5YA""
  },
  {
    "{": ""      ""Video ID: Efj-v3ugbbc""
  },
  {
    "{": ""      ""Video ID: vCTffbgTQxg""
  },
  {
    "{": ""      ""Video ID: avx5PFjBQ4U""
  },
  {
    "{": ""      ""Video ID: tmhh1Vd8yaM""
  },
  {
    "{": ""      ""Video ID: 5VHMXG9XNoU""
  },
  {
    "{": ""      ""Video ID: sFo9fkDn6_8""
  },
  {
    "{": ""      ""Video ID: P7Y1zbpLFsg""
  },
  {
    "{": ""      ""Video ID: -EwkJSCOIuE""
  },
  {
    "{": ""      ""Video ID: crAMocJouKY""
  },
  {
    "{": ""      ""Video ID: c4kxMiP6pmg""
  },
  {
    "{": ""      ""Video ID: 5VhvMkirkRs""
  },
  {
    "{": ""      ""Video ID: 5-ElzvEt_xA""
  },
  {
    "{": ""      ""Video ID: shVL-Kn9jiU""
  },
  {
    "{": ""      ""Video ID: drzlp3-GDxI""
  },
  {
    "{": ""      ""Video ID: _MILN4OcxwE""
  },
  {
    "{": ""      ""Video ID: dr2mZ0p_Pm4""
  },
  {
    "{": ""      ""Video ID: V09HYHtkFzE""
  },
  {
    "{": ""      ""Video ID: LLQn5pryrEM""
  },
  {
    "{": ""      ""Video ID: BHkrzPrrJKs""
  },
  {
    "{": ""      ""Video ID: 4ZZY3j_CdlE""
  },
  {
    "{": ""      ""Video ID: LHihmSIJe_8""
  },
  {
    "{": ""      ""Video ID: kSX0w9va92w""
  },
  {
    "{": ""      ""Video ID: ntIdvFkGAfM""
  },
  {
    "{": ""      ""Video ID: M_ELA_O_SS0""
  },
  {
    "{": ""      ""Video ID: Z7olitJ14-k""
  },
  {
    "{": ""      ""Video ID: IubA_LDeB8s""
  },
  {
    "{": ""      ""Video ID: DYO_TWD8X2U""
  },
  {
    "{": ""      ""Video ID: nxax7FoGYno""
  },
  {
    "{": ""      ""Video ID: T5xCG-jD9MA""
  },
  {
    "{": ""      ""Video ID: GqK01pFVg70""
  },
  {
    "{": ""      ""Video ID: er6H94f-kiw""
  },
  {
    "{": ""      ""Video ID: Sc6o4GCv7FA""
  },
  {
    "{": ""      ""Video ID: XluHSB6Hue4""
  },
  {
    "{": ""      ""Video ID: IWnoGIp8hw4""
  },
  {
    "{": ""      ""Video ID: n6YWVmYdfig""
  },
  {
    "{": ""      ""Video ID: SryM8rBlWlc""
  },
  {
    "{": ""      ""Video ID: M96FcyPPoU4""
  },
  {
    "{": ""      ""Video ID: 0MphBygDPmY""
  },
  {
    "{": ""      ""Video ID: 944uqp7qXPU""
  },
  {
    "{": ""      ""Video ID: YIbvED51Tew""
  },
  {
    "{": ""      ""Video ID: u2hvwGTsY-k""
  },
  {
    "{": ""      ""Video ID: 2mLh4mE-SV0""
  },
  {
    "{": ""      ""Video ID: x9yyaAtwIR4""
  },
  {
    "{": ""      ""Video ID: iOIozzuAArQ""
  },
  {
    "{": ""      ""Video ID: FOyRWuklsiQ""
  },
  {
    "{": ""      ""Video ID: uTRZ_EtFQ74""
  },
  {
    "{": ""      ""Video ID: U7_Y_-PbI4s""
  },
  {
    "{": ""      ""Video ID: kXYejBHCENw""
  },
  {
    "{": ""      ""Video ID: cu-XoJBgbfs""
  },
  {
    "{": ""      ""Video ID: aTnpdKb_JfM""
  },
  {
    "{": ""      ""Video ID: S3CA-SQsvwE""
  },
  {
    "{": ""      ""Video ID: qProMEGL5k0""
  },
  {
    "{": ""      ""Video ID: TChO2rHBnlw""
  },
  {
    "{": ""      ""Video ID: -PBTZCMXWMY""
  },
  {
    "{": ""      ""Video ID: coFvmCZwk8I""
  },
  {
    "{": ""      ""Video ID: jmwKdq7NJTA""
  },
  {
    "{": ""      ""Video ID: 13EKLBr2H74""
  },
  {
    "{": ""      ""Video ID: w3z-8QLUEG4""
  },
  {
    "{": ""      ""Video ID: FbGvFG13oQs""
  },
  {
    "{": ""      ""Video ID: _0Wo6KVicic""
  },
  {
    "{": ""      ""Video ID: TWLC8ND0Yy8""
  },
  {
    "{": ""      ""Video ID: X_5xXDZ9SNA""
  },
  {
    "{": ""      ""Video ID: YXFgXmSv4Gk""
  },
  {
    "{": ""      ""Video ID: y-ufRNjoJqw""
  },
  {
    "{": ""      ""Video ID: R1FUcFQVPxQ""
  },
  {
    "{": ""      ""Video ID: Ld_kfDHicSo""
  },
  {
    "{": ""      ""Video ID: S5DYNyRLB-k""
  },
  {
    "{": ""      ""Video ID: w-rcjaBWvx0""
  },
  {
    "{": ""      ""Video ID: vNqjVGhn-ng""
  },
  {
    "{": ""      ""Video ID: X3t8XKtFMlI""
  },
  {
    "{": ""      ""Video ID: SmPDQltgTFo""
  },
  {
    "{": ""      ""Video ID: zzgVy6Mj2Bw""
  },
  {
    "{": ""      ""Video ID: SjiMWoNaSXk""
  },
  {
    "{": ""      ""Video ID: U4fX9a97KkU""
  },
  {
    "{": ""      ""Video ID: CwfZQNWuB2I""
  },
  {
    "{": ""      ""Video ID: 1Ami1_X0kTo""
  },
  {
    "{": ""      ""Video ID: rHpsYfgy1_k""
  },
  {
    "{": ""      ""Video ID: PUUIPRjLdvk""
  },
  {
    "{": ""      ""Video ID: By7MwblZcaU""
  },
  {
    "{": ""      ""Video ID: -R4dAwxL3Ms""
  },
  {
    "{": ""      ""Video ID: dxJzjBtaoJE""
  },
  {
    "{": ""      ""Video ID: yZTA-M27Mjs""
  },
  {
    "{": ""      ""Video ID: rUTPFz0CZLA""
  },
  {
    "{": ""      ""Video ID: 8hPVxUu1stk""
  },
  {
    "{": ""      ""Video ID: ntMopBhgGtM""
  },
  {
    "{": ""      ""Video ID: xtZqQb4FBcA""
  },
  {
    "{": ""      ""Video ID: -o2BMVv24Vc""
  },
  {
    "{": ""      ""Video ID: uNfuX9seIyM""
  },
  {
    "{": ""      ""Video ID: JmfZbUOlJPE""
  },
  {
    "{": ""      ""Video ID: siSe8Qb91wQ""
  },
  {
    "{": ""      ""Video ID: oXdI1GUXBOo""
  },
  {
    "{": ""      ""Video ID: utBMmE277lc""
  },
  {
    "{": ""      ""Video ID: sUKbaUAzoQk""
  },
  {
    "{": ""      ""Video ID: NCFQa6PY22U""
  },
  {
    "{": ""      ""Video ID: p9Dv6aRmHVY""
  },
  {
    "{": ""      ""Video ID: 3kJmypE1DGQ""
  },
  {
    "{": ""      ""Video ID: -Gs0vyf3u5U""
  },
  {
    "{": ""      ""Video ID: vd19_NolCog""
  },
  {
    "{": ""      ""Video ID: uqyoZdPhhuk""
  },
  {
    "{": ""      ""Video ID: pwLDq1SnkGw""
  },
  {
    "{": ""      ""Video ID: Kjo8zd26iuU""
  },
  {
    "{": ""      ""Video ID: CT3RZSVrGVI""
  },
  {
    "{": ""      ""Video ID: lGmVHhCxs4o""
  },
  {
    "{": ""      ""Video ID: -VZifnnPK1c""
  },
  {
    "{": ""      ""Video ID: JiQD_g27X7g""
  },
  {
    "{": ""      ""Video ID: YcPfBQCT40M""
  },
  {
    "{": ""      ""Video ID: NR3BuTdwk48""
  },
  {
    "{": ""      ""Video ID: ajDd492iinY""
  },
  {
    "{": ""      ""Video ID: -EL_fntJnl4""
  },
  {
    "{": ""      ""Video ID: Qrk2AFmvi-I""
  },
  {
    "{": ""      ""Video ID: 0ay_ykrMJL0""
  },
  {
    "{": ""      ""Video ID: VkrS3yHTY7w""
  },
  {
    "{": ""      ""Video ID: fDcnJPMW1sQ""
  },
  {
    "{": ""      ""Video ID: nmNvIKrfqYc""
  },
  {
    "{": ""      ""Video ID: 6um8ix3rvUo""
  },
  {
    "{": ""      ""Video ID: lXs5FUDmm2A""
  },
  {
    "{": ""      ""Video ID: Hq-hkylARiE""
  },
  {
    "{": ""      ""Video ID: lORx9VtJgck""
  },
  {
    "{": ""      ""Video ID: TDy16Nap2e4""
  },
  {
    "{": ""      ""Video ID: EAQF7g6r8sE""
  },
  {
    "{": ""      ""Video ID: taimx_t0RbE""
  },
  {
    "{": ""      ""Video ID: s6D7iO1YLe8""
  },
  {
    "{": ""      ""Video ID: TpZZGTGVePE""
  },
  {
    "{": ""      ""Video ID: V8sAKjwp7Vo""
  },
  {
    "{": ""      ""Video ID: sTNcEl9Bhjg""
  },
  {
    "{": ""      ""Video ID: 6hZ6xz00xhk""
  },
  {
    "{": ""      ""Video ID: kqr4Kfz-FwI""
  },
  {
    "{": ""      ""Video ID: B1MGi12RspA""
  },
  {
    "{": ""      ""Video ID: AEVsXlI1wWM""
  },
  {
    "{": ""      ""Video ID: O7RLBUt1coU""
  },
  {
    "{": ""      ""Video ID: MSTTosTP9MU""
  },
  {
    "{": ""      ""Video ID: Bg6cO88_XvE""
  },
  {
    "{": ""      ""Video ID: Ya1VqJkLC5M""
  },
  {
    "{": ""      ""Video ID: 41hvHYKmjQ8""
  },
  {
    "{": ""      ""Video ID: zhzDYh30C5s""
  },
  {
    "{": ""      ""Video ID: MuWBt1VZqHg""
  },
  {
    "{": ""      ""Video ID: KvpfYwKR6lo""
  },
  {
    "{": ""      ""Video ID: tJXNGm1H-LU""
  },
  {
    "{": ""      ""Video ID: rz7UNxnOI3M""
  },
  {
    "{": ""      ""Video ID: OXIgkmYejJg""
  },
  {
    "{": ""      ""Video ID: JxeYlJRp8aA""
  },
  {
    "{": ""      ""Video ID: QAHwP3MaSmE""
  },
  {
    "{": ""      ""Video ID: jWcEjsxzBr4""
  },
  {
    "{": ""      ""Video ID: PC5sT3ETX78""
  },
  {
    "{": ""      ""Video ID: H2KZi066moM""
  },
  {
    "{": ""      ""Video ID: ghxyVNfuqxk""
  },
  {
    "{": ""      ""Video ID: o25FiglIujU""
  },
  {
    "{": ""      ""Video ID: oRcRH1dip-g""
  },
  {
    "{": ""      ""Video ID: UInoDHGdTO8""
  },
  {
    "{": ""      ""Video ID: qxK2f04eQGU""
  },
  {
    "{": ""      ""Video ID: NrZb7duCTfU""
  },
  {
    "{": ""      ""Video ID: _eKIm6zrhp0""
  },
  {
    "{": ""      ""Video ID: n_HOBiTb6jI""
  },
  {
    "{": ""      ""Video ID: DggGZqYebrQ""
  },
  {
    "{": ""      ""Video ID: 64UsHZXr71M""
  },
  {
    "{": ""      ""Video ID: 7_O3MNJcls8""
  },
  {
    "{": ""      ""Video ID: BPCQb-qg_3A""
  },
  {
    "{": ""      ""Video ID: UuPUFRusOBo""
  },
  {
    "{": ""      ""Video ID: AFfdB5OzlyQ""
  },
  {
    "{": ""      ""Video ID: l_bRQl-UYUY""
  },
  {
    "{": ""      ""Video ID: vr_lWtVVRTo""
  },
  {
    "{": ""      ""Video ID: c0VxG5tL-wg""
  },
  {
    "{": ""      ""Video ID: FBpdK2fPvZk""
  },
  {
    "{": ""      ""Video ID: uAEZ-jWLYj0""
  },
  {
    "{": ""      ""Video ID: kDjExoLqsa8""
  },
  {
    "{": ""      ""Video ID: SHcq0j16s-M""
  },
  {
    "{": ""      ""Video ID: vuvbfVjc3C4""
  },
  {
    "{": ""      ""Video ID: L0_glXhLCls""
  },
  {
    "{": ""      ""Video ID: uw5wlOtldC4""
  },
  {
    "{": ""      ""Video ID: qYWWBwf2wHE""
  },
  {
    "{": ""      ""Video ID: bnU3G-HCf9w""
  },
  {
    "{": ""      ""Video ID: rOmtUK8Hb7w""
  },
  {
    "{": ""      ""Video ID: 57GOsJNjRkY""
  },
  {
    "{": ""      ""Video ID: rQLMdHKcK9E""
  },
  {
    "{": ""      ""Video ID: 9Ei6aoq-sno""
  },
  {
    "{": ""      ""Video ID: 4xe61TGH2CY""
  },
  {
    "{": ""      ""Video ID: T3M6A3NyC34""
  },
  {
    "{": ""      ""Video ID: GlBkmh54YPw""
  },
  {
    "{": ""      ""Video ID: GoNMG5-a15k""
  },
  {
    "{": ""      ""Video ID: lTXEWh2yT_g""
  },
  {
    "{": ""      ""Video ID: 4DdB1BAZqZQ""
  },
  {
    "{": ""      ""Video ID: ceoCx_wTDUg""
  },
  {
    "{": ""      ""Video ID: 87zLW04zee8""
  },
  {
    "{": ""      ""Video ID: GqBrVBUGhFQ""
  },
  {
    "{": ""      ""Video ID: nMJ3WrooXbY""
  },
  {
    "{": ""      ""Video ID: t6VZAuVezuk""
  },
  {
    "{": ""      ""Video ID: HTh-jhcI51c""
  },
  {
    "{": ""      ""Video ID: Np4Sx8pPLCI""
  },
  {
    "{": ""      ""Video ID: -iguBYzvPX0""
  },
  {
    "{": ""      ""Video ID: S7QUftErt_M""
  },
  {
    "{": ""      ""Video ID: kGJo8JCAIn4""
  },
  {
    "{": ""      ""Video ID: SoVcBemW9xM""
  },
  {
    "{": ""      ""Video ID: 5Gz5JC8QcNU""
  },
  {
    "{": ""      ""Video ID: Oh8LPE8OPSk""
  },
  {
    "{": ""      ""Video ID: X_htQD2dgwg""
  },
  {
    "{": ""      ""Video ID: f0wWI44DhrI""
  },
  {
    "{": ""      ""Video ID: C_zQPhveWv8""
  },
  {
    "{": ""      ""Video ID: Jr_Xorc6KnY""
  },
  {
    "{": ""      ""Video ID: axlBWgZ8F9M""
  },
  {
    "{": ""      ""Video ID: _L-mU3diaq8""
  },
  {
    "{": ""      ""Video ID: a14d89aoEXs""
  },
  {
    "{": ""      ""Video ID: BHe8N5hL0Wo""
  },
  {
    "{": ""      ""Video ID: ty3ZwuLeaj0""
  },
  {
    "{": ""      ""Video ID: Yt3tcYaLY8Q""
  },
  {
    "{": ""      ""Video ID: waVPwBxJUC0""
  },
  {
    "{": ""      ""Video ID: 8lEfkFn9sFs""
  },
  {
    "{": ""      ""Video ID: 0LmztRFiH_g""
  },
  {
    "{": ""      ""Video ID: l7jGbQCEYFc""
  },
  {
    "{": ""      ""Video ID: WDxeNDH7G-A""
  },
  {
    "{": ""      ""Video ID: 5_r3uJJ_cuY""
  },
  {
    "{": ""      ""Video ID: SqQ6PYcKseM""
  },
  {
    "{": ""      ""Video ID: zmyBar8Lweo""
  },
  {
    "{": ""      ""Video ID: -tapSgwcsw8""
  },
  {
    "{": ""      ""Video ID: OBmQpa1RWOE""
  },
  {
    "{": ""      ""Video ID: 0x-LLyXMu30""
  },
  {
    "{": ""      ""Video ID: 9Z4SiIkOphk""
  },
  {
    "{": ""      ""Video ID: wETmxrgpFhk""
  },
  {
    "{": ""      ""Video ID: jwkHFfO7hG8""
  },
  {
    "{": ""      ""Video ID: zXFbGirn_88""
  },
  {
    "{": ""      ""Video ID: FIp1LttpxCc""
  },
  {
    "{": ""      ""Video ID: 1PzPzl7LWhE""
  },
  {
    "{": ""      ""Video ID: Lc2oXPkhZdw""
  },
  {
    "{": ""      ""Video ID: msIpvb8OrhY""
  },
  {
    "{": ""      ""Video ID: TtQxyaweiYQ""
  },
  {
    "{": ""      ""Video ID: usq7h3n8GUw""
  },
  {
    "{": ""      ""Video ID: JtvH3TUX2Eg""
  },
  {
    "{": ""      ""Video ID: 9tgQsEdYLTw""
  },
  {
    "{": ""      ""Video ID: 7F1oRcsEJEc""
  },
  {
    "{": ""      ""Video ID: --eVRYFd7kg""
  },
  {
    "{": ""      ""Video ID: c53NhRWgK6c""
  },
  {
    "{": ""      ""Video ID: Rky6tNZjLOA""
  },
  {
    "{": ""      ""Video ID: qrjy6TVNsxY""
  },
  {
    "{": ""      ""Video ID: 3Ad-_b5oMNU""
  },
  {
    "{": ""      ""Video ID: Ci6KiFkrf18""
  },
  {
    "{": ""      ""Video ID: DHHbHxCzw1Y""
  },
  {
    "{": ""      ""Video ID: fV2Y7MbKdAQ""
  },
  {
    "{": ""      ""Video ID: TodElS9Y9ZY""
  },
  {
    "{": ""      ""Video ID: SR6-k2_B9MU""
  },
  {
    "{": ""      ""Video ID: pMQM4L6pPrE""
  },
  {
    "{": ""      ""Video ID: OG_YbDzQsLc""
  },
  {
    "{": ""      ""Video ID: DyGNozUNzUU""
  },
  {
    "{": ""      ""Video ID: BFlnXeo4mKQ""
  },
  {
    "{": ""      ""Video ID: LQ-mL_iIoss""
  },
  {
    "{": ""      ""Video ID: xD_R6T2Yug0""
  },
  {
    "{": ""      ""Video ID: 7Op8fMbtAlw""
  },
  {
    "{": ""      ""Video ID: bkL4-pz2FVU""
  },
  {
    "{": ""      ""Video ID: K36hSRoHBPg""
  },
  {
    "{": ""      ""Video ID: 4xEWptc9TT8""
  },
  {
    "{": ""      ""Video ID: KIrh6ZfAFw4""
  },
  {
    "{": ""      ""Video ID: EvXJGx9LbAo""
  },
  {
    "{": ""      ""Video ID: jaDPmrj1Pfc""
  },
  {
    "{": ""      ""Video ID: QiQGItUB8r4""
  },
  {
    "{": ""      ""Video ID: eQBtRW6sfqM""
  },
  {
    "{": ""      ""Video ID: 21ko-1Hrnek""
  },
  {
    "{": ""      ""Video ID: EbtF7c2Jbgk""
  },
  {
    "{": ""      ""Video ID: bWO6TDwQZWE""
  },
  {
    "{": ""      ""Video ID: Nqy9QyJVg7U""
  },
  {
    "{": ""      ""Video ID: xQTrdzSb1c4""
  },
  {
    "{": ""      ""Video ID: zdDSK9DIdrU""
  },
  {
    "{": ""      ""Video ID: pNk8eJAbspg""
  },
  {
    "{": ""      ""Video ID: OPBIHJYgdGM""
  },
  {
    "{": ""      ""Video ID: xEJvnZafBzc""
  },
  {
    "{": ""      ""Video ID: d0QV1bsIU5c""
  },
  {
    "{": ""      ""Video ID: e_J8Qd8LHDw""
  },
  {
    "{": ""      ""Video ID: aMKM3oOfjM8""
  },
  {
    "{": ""      ""Video ID: Ad0_ZpEAzMs""
  },
  {
    "{": ""      ""Video ID: vDaiikxFcdU""
  },
  {
    "{": ""      ""Video ID: uS9_ngRLctY""
  },
  {
    "{": ""      ""Video ID: 6fUWZsxKraw""
  },
  {
    "{": ""      ""Video ID: Y2As2a0RyVI""
  },
  {
    "{": ""      ""Video ID: jCfRdIWlds8""
  },
  {
    "{": ""      ""Video ID: H9oja6Gq7Ak""
  },
  {
    "{": ""      ""Video ID: vZPlTwFV7OE""
  },
  {
    "{": ""      ""Video ID: d6xzq7oOdW8""
  },
  {
    "{": ""      ""Video ID: dHLdC3Mrj0k""
  },
  {
    "{": ""      ""Video ID: yXeDIiy1wIA""
  },
  {
    "{": ""      ""Video ID: 11q6vssAFUg""
  },
  {
    "{": ""      ""Video ID: 7yeu8Kqaq8Y""
  },
  {
    "{": ""      ""Video ID: JQorM0zncsI""
  },
  {
    "{": ""      ""Video ID: ghVfxb9cP5E""
  },
  {
    "{": ""      ""Video ID: 8ixNRKdRPag""
  },
  {
    "{": ""      ""Video ID: EpdPX9avs1M""
  },
  {
    "{": ""      ""Video ID: TkHWMeWHayg""
  },
  {
    "{": ""      ""Video ID: 8oPsARBQQj4""
  },
  {
    "{": ""      ""Video ID: DThZFot19hU""
  },
  {
    "{": ""      ""Video ID: _FXyPVFNGBE""
  },
  {
    "{": ""      ""Video ID: OlOWssPvgJI""
  },
  {
    "{": ""      ""Video ID: tMoFq8usQHI""
  },
  {
    "{": ""      ""Video ID: xoW0XFVZs2g""
  },
  {
    "{": ""      ""Video ID: FGOaOZVbtzY""
  },
  {
    "{": ""      ""Video ID: UdRDt7NWenM""
  },
  {
    "{": ""      ""Video ID: 031zwj35s-U""
  },
  {
    "{": ""      ""Video ID: qCyRPCojb2Q""
  },
  {
    "{": ""      ""Video ID: PWkTjlS5R0E""
  },
  {
    "{": ""      ""Video ID: 5DTkmMsl_1Y""
  },
  {
    "{": ""      ""Video ID: FvpEFwnfgdY""
  },
  {
    "{": ""      ""Video ID: GvWrDsMphoE""
  },
  {
    "{": ""      ""Video ID: 6xSPuJx5maw""
  },
  {
    "{": ""      ""Video ID: DWk4qKUWSpU""
  },
  {
    "{": ""      ""Video ID: Drje7Q7RCPk""
  },
  {
    "{": ""      ""Video ID: 9DSmcPee6cc""
  },
  {
    "{": ""      ""Video ID: EyzW2cAl0gQ""
  },
  {
    "{": ""      ""Video ID: 0ezilop74fM""
  },
  {
    "{": ""      ""Video ID: 8_Zy-VK2JSM""
  },
  {
    "{": ""      ""Video ID: xcozhIHMq3U""
  },
  {
    "{": ""      ""Video ID: iMFz1SveI8c""
  },
  {
    "{": ""      ""Video ID: mr_WSKfDqAM""
  },
  {
    "{": ""      ""Video ID: gbHZHLfs6Tc""
  },
  {
    "{": ""      ""Video ID: -C9kP6wz5l4""
  },
  {
    "{": ""      ""Video ID: svL_2lv5x14""
  },
  {
    "{": ""      ""Video ID: jeVEEtXFnEE""
  },
  {
    "{": ""      ""Video ID: wFAixPJq4lE""
  },
  {
    "{": ""      ""Video ID: kzGnodqMV1o""
  },
  {
    "{": ""      ""Video ID: ZveOiSwDBjg""
  },
  {
    "{": ""      ""Video ID: ksCA0yR_lzE""
  },
  {
    "{": ""      ""Video ID: 0pz2TV4OfNU""
  },
  {
    "{": ""      ""Video ID: 7b5RUJPXG9E""
  },
  {
    "{": ""      ""Video ID: rPUMGoqpha0""
  },
  {
    "{": ""      ""Video ID: E__D-CZ0fi4""
  },
  {
    "{": ""      ""Video ID: eqcxsZMwjqQ""
  },
  {
    "{": ""      ""Video ID: RnpNNIZuqSs""
  },
  {
    "{": ""      ""Video ID: kDQwa6-KJsI""
  },
  {
    "{": ""      ""Video ID: G3YbeM1FqAM""
  },
  {
    "{": ""      ""Video ID: DN91BZ5V0Yg""
  },
  {
    "{": ""      ""Video ID: Tj61Ez5wnY0""
  },
  {
    "{": ""      ""Video ID: QDeN3b0_fNo""
  },
  {
    "{": ""      ""Video ID: nfeSaIMnYKA""
  },
  {
    "{": ""      ""Video ID: kPtgwIbpROQ""
  },
  {
    "{": ""      ""Video ID: p-xgof01thA""
  },
  {
    "{": ""      ""Video ID: eFNHXZ-g6ks""
  },
  {
    "{": ""      ""Video ID: 8z1MplgLcAI""
  },
  {
    "{": ""      ""Video ID: ULpRyC_ChpA""
  },
  {
    "{": ""      ""Video ID: H96re3-Be20""
  },
  {
    "{": ""      ""Video ID: wfxO_KmfJfc""
  },
  {
    "{": ""      ""Video ID: WB6bZyy4PXk""
  },
  {
    "{": ""      ""Video ID: ouU5d3u-NsA""
  },
  {
    "{": ""      ""Video ID: vLqnAvxiS5Q""
  },
  {
    "{": ""      ""Video ID: hxyABa09yYs""
  },
  {
    "{": ""      ""Video ID: ihaiXS0ALU0""
  },
  {
    "{": ""      ""Video ID: 3RhnHo3RDfg""
  },
  {
    "{": ""      ""Video ID: ceo7yISzd1k""
  },
  {
    "{": ""      ""Video ID: zUbA-vz0Py0""
  },
  {
    "{": ""      ""Video ID: xVVlZzCGJmo""
  },
  {
    "{": ""      ""Video ID: 5ebj3sXUFGg""
  },
  {
    "{": ""      ""Video ID: gFKfMbbaqGM""
  },
  {
    "{": ""      ""Video ID: SPtdX503hds""
  },
  {
    "{": ""      ""Video ID: Eq_No1U9igw""
  },
  {
    "{": ""      ""Video ID: 9l9awnPFZ6A""
  },
  {
    "{": ""      ""Video ID: FR1_NI9OiXI""
  },
  {
    "{": ""      ""Video ID: evk-wyyTQFE""
  },
  {
    "{": ""      ""Video ID: G03cgipFKis""
  },
  {
    "{": ""      ""Video ID: 1qFWIZ6uLjI""
  },
  {
    "{": ""      ""Video ID: m5IIORtdqFg""
  },
  {
    "{": ""      ""Video ID: zp_XHfylwPU""
  },
  {
    "{": ""      ""Video ID: ULqSbOdtaRs""
  },
  {
    "{": ""      ""Video ID: MpHCOZYiyOY""
  },
  {
    "{": ""      ""Video ID: FZ3lQ-vzU5s""
  },
  {
    "{": ""      ""Video ID: 3xP0bGAJWqs""
  },
  {
    "{": ""      ""Video ID: qI82d5ZkePU""
  },
  {
    "{": ""      ""Video ID: Exsaow2LWYg""
  },
  {
    "{": ""      ""Video ID: 7bLK3yPTBx0""
  },
  {
    "{": ""      ""Video ID: NbakN7SLdbk""
  },
  {
    "{": ""      ""Video ID: 0vETFKvU2rQ""
  },
  {
    "{": ""      ""Video ID: p7YyURmPKC8""
  },
  {
    "{": ""      ""Video ID: bTCPHpT-Jb4""
  },
  {
    "{": ""      ""Video ID: -HInQ2KMJe4""
  },
  {
    "{": ""      ""Video ID: O3K6yiReOls""
  },
  {
    "{": ""      ""Video ID: 2WVZJ6gVksY""
  },
  {
    "{": ""      ""Video ID: c34-m9p0Y3s""
  },
  {
    "{": ""      ""Video ID: mWGpNvK-__w""
  },
  {
    "{": ""      ""Video ID: fwmvz5S6r3w""
  },
  {
    "{": ""      ""Video ID: 1ostgqhDjIo""
  },
  {
    "{": ""      ""Video ID: pZcOiIx4xZk""
  },
  {
    "{": ""      ""Video ID: fbXVFJhFFsM""
  },
  {
    "{": ""      ""Video ID: fjVYfkqUTzw""
  },
  {
    "{": ""      ""Video ID: nM9Ou5noW18""
  },
  {
    "{": ""      ""Video ID: A8AWfprUZRc""
  },
  {
    "{": ""      ""Video ID: 4_PdeKwCzO8""
  },
  {
    "{": ""      ""Video ID: mhfp6Z8z1cI""
  },
  {
    "{": ""      ""Video ID: waoEBhpURgk""
  },
  {
    "{": ""      ""Video ID: EiK2fwmW6pU""
  },
  {
    "{": ""      ""Video ID: oDBRWCykzC0""
  },
  {
    "{": ""      ""Video ID: Nxo3L0LRwMQ""
  },
  {
    "{": ""      ""Video ID: 6q1MtEDOvlg""
  },
  {
    "{": ""      ""Video ID: 00rFqqOh_XI""
  },
  {
    "{": ""      ""Video ID: s3SE41Z9C1w""
  },
  {
    "{": ""      ""Video ID: pTQjA5g960Q""
  },
  {
    "{": ""      ""Video ID: N0Vr_o96lnM""
  },
  {
    "{": ""      ""Video ID: 6rTuGWUOTLk""
  },
  {
    "{": ""      ""Video ID: kxQWNcR6g7w""
  },
  {
    "{": ""      ""Video ID: eWgvpQn1Gm0""
  },
  {
    "{": ""      ""Video ID: 9hLN8pZKOGA""
  },
  {
    "{": ""      ""Video ID: G90wfGDAMiU""
  },
  {
    "{": ""      ""Video ID: PtFzvWv-WdY""
  },
  {
    "{": ""      ""Video ID: 7Bcsq7L5vZM""
  },
  {
    "{": ""      ""Video ID: oVL9MBsonS8""
  },
  {
    "{": ""      ""Video ID: oW-mUdwAQls""
  },
  {
    "{": ""      ""Video ID: 7uQl76yHPD8""
  },
  {
    "{": ""      ""Video ID: iJwBWT6c9NU""
  },
  {
    "{": ""      ""Video ID: 4UfXuLAK0aQ""
  },
  {
    "{": ""      ""Video ID: YAEI15bkoqo""
  },
  {
    "{": ""      ""Video ID: Alc2kKJFlyc""
  },
  {
    "{": ""      ""Video ID: ob6MPntLXWI""
  },
  {
    "{": ""      ""Video ID: vE7Qyk5KOGI""
  },
  {
    "{": ""      ""Video ID: ESARBMvPJ4M""
  },
  {
    "{": ""      ""Video ID: BgWioq7a0kM""
  },
  {
    "{": ""      ""Video ID: GE_mJGEmDJM""
  },
  {
    "{": ""      ""Video ID: 8aYuG1i2e4o""
  },
  {
    "{": ""      ""Video ID: bC4EJ8Jlck0""
  },
  {
    "{": ""      ""Video ID: 4ziZga4MQcA""
  },
  {
    "{": ""      ""Video ID: Yb5VImRI5Ag""
  },
  {
    "{": ""      ""Video ID: nqemvF9ORY4""
  },
  {
    "{": ""      ""Video ID: Hr5t9bEbSuw""
  },
  {
    "{": ""      ""Video ID: Gr5NvRKRiOA""
  },
  {
    "{": ""      ""Video ID: hsknWg-1wVI""
  },
  {
    "{": ""      ""Video ID: vt-1BqQcD3E""
  },
  {
    "{": ""      ""Video ID: zNMFBeUKLJ4""
  },
  {
    "{": ""      ""Video ID: eYdN0IrfN7s""
  },
  {
    "{": ""      ""Video ID: VjJ3_n60d18""
  },
  {
    "{": ""      ""Video ID: iKVPlPfZM6I""
  },
  {
    "{": ""      ""Video ID: tv6cvcoaccA""
  },
  {
    "{": ""      ""Video ID: LHTWTBt95K0""
  },
  {
    "{": ""      ""Video ID: nNOvxdn1S7E""
  },
  {
    "{": ""      ""Video ID: WfVYj1qkrpc""
  },
  {
    "{": ""      ""Video ID: qiAJd0h8xAE""
  },
  {
    "{": ""      ""Video ID: y-XXNI2o6V8""
  },
  {
    "{": ""      ""Video ID: ITG-IbHEYEE""
  },
  {
    "{": ""      ""Video ID: z0LEj8IPHGU""
  },
  {
    "{": ""      ""Video ID: ZwTBJQEpt-w""
  },
  {
    "{": ""      ""Video ID: zMS-0A3c2dY""
  },
  {
    "{": ""      ""Video ID: h2goTVC5g3M""
  },
  {
    "{": ""      ""Video ID: lZ8IHt2hEag""
  },
  {
    "{": ""      ""Video ID: HPTC5prUcng""
  },
  {
    "{": ""      ""Video ID: 9yAc5nz3iXc""
  },
  {
    "{": ""      ""Video ID: oy880cLxRvw""
  },
  {
    "{": ""      ""Video ID: lSiGyGS6u8M""
  },
  {
    "{": ""      ""Video ID: ZnhpFvutxNk""
  },
  {
    "{": ""      ""Video ID: sdDcnseDJns""
  },
  {
    "{": ""      ""Video ID: dOeF9LW2QcY""
  },
  {
    "{": ""      ""Video ID: fTSNf4JI8Yg""
  },
  {
    "{": ""      ""Video ID: NiRraaWKI1c""
  },
  {
    "{": ""      ""Video ID: IXLyeh80YhE""
  },
  {
    "{": ""      ""Video ID: PpIyDwISxPw""
  },
  {
    "{": ""      ""Video ID: nEcqOUxQtCA""
  },
  {
    "{": ""      ""Video ID: gmuW8K6DOw8""
  },
  {
    "{": ""      ""Video ID: trWcqxrQgcc""
  },
  {
    "{": ""      ""Video ID: jWkHmJhKF7g""
  },
  {
    "{": ""      ""Video ID: t3kI8LNTqNo""
  },
  {
    "{": ""      ""Video ID: jGcAzX9E3qU""
  },
  {
    "{": ""      ""Video ID: K-0LmH7BfOk""
  },
  {
    "{": ""      ""Video ID: 8f-7vAiZ4dg""
  },
  {
    "{": ""      ""Video ID: l8zbw80FOxU""
  },
  {
    "{": ""      ""Video ID: 0WqSah4dxRA""
  },
  {
    "{": ""      ""Video ID: Uw9T7RAkps8""
  },
  {
    "{": ""      ""Video ID: oYRbkJsCGks""
  },
  {
    "{": ""      ""Video ID: 8RV46fsmx6E""
  },
  {
    "{": ""      ""Video ID: kcrF346sS_I""
  },
  {
    "{": ""      ""Video ID: 58xyjOFkpxk""
  },
  {
    "{": ""      ""Video ID: l9ijLulwUTY""
  },
  {
    "{": ""      ""Video ID: 85WxlT6CPGg""
  },
  {
    "{": ""      ""Video ID: TKR4kryBDdk""
  },
  {
    "{": ""      ""Video ID: Ktr7fLbZFK4""
  },
  {
    "{": ""      ""Video ID: 30TAmBltTk4""
  },
  {
    "{": ""      ""Video ID: 28q430Vps9s""
  },
  {
    "{": ""      ""Video ID: o5u6BX1xq14""
  },
  {
    "{": ""      ""Video ID: kBsMBsfy2vQ""
  },
  {
    "{": ""      ""Video ID: dAHmzL9iuyI""
  },
  {
    "{": ""      ""Video ID: BdT9UR7QL8U""
  },
  {
    "{": ""      ""Video ID: E8DSBvSRl-8""
  },
  {
    "{": ""      ""Video ID: Yoj4v4CKUkA""
  },
  {
    "{": ""      ""Video ID: BC_B3OBmb0Y""
  },
  {
    "{": ""      ""Video ID: qYVZp1ZFtmU""
  },
  {
    "{": ""      ""Video ID: wflJixZQYnQ""
  },
  {
    "{": ""      ""Video ID: 5ZYmCQu5oyk""
  },
  {
    "{": ""      ""Video ID: D0HEKayNFZQ""
  },
  {
    "{": ""      ""Video ID: ULNDQd809ag""
  },
  {
    "{": ""      ""Video ID: belzgoxfayo""
  },
  {
    "{": ""      ""Video ID: 9h5UZrmyzz4""
  },
  {
    "{": ""      ""Video ID: fRsgw-O6qeU""
  },
  {
    "{": ""      ""Video ID: A_7HNqdEWwo""
  },
  {
    "{": ""      ""Video ID: IkaWp_9AAeg""
  },
  {
    "{": ""      ""Video ID: OwydwDOwyp8""
  },
  {
    "{": ""      ""Video ID: KUiQPxumS78""
  },
  {
    "{": ""      ""Video ID: dWHwVVneUlM""
  },
  {
    "{": ""      ""Video ID: z7g-9Cd6Z2I""
  },
  {
    "{": ""      ""Video ID: SlTCL8-uvec""
  },
  {
    "{": ""      ""Video ID: maUfhiFRe48""
  },
  {
    "{": ""      ""Video ID: iYrgkTNJcfo""
  },
  {
    "{": ""      ""Video ID: JiGvPz6Duac""
  },
  {
    "{": ""      ""Video ID: KoUMBZUukas""
  },
  {
    "{": ""      ""Video ID: BbQeVFiTlUA""
  },
  {
    "{": ""      ""Video ID: OX4wqvl69VM""
  },
  {
    "{": ""      ""Video ID: 6tPdzbbmiuA""
  },
  {
    "{": ""      ""Video ID: Mv-ABihs-W4""
  },
  {
    "{": ""      ""Video ID: uO_vGCiZW_A""
  },
  {
    "{": ""      ""Video ID: LKedkJKZP74""
  },
  {
    "{": ""      ""Video ID: Jg_3ZaMkm4A""
  },
  {
    "{": ""      ""Video ID: mZ20qqg-SCg""
  },
  {
    "{": ""      ""Video ID: kKZWof1Vp0M""
  },
  {
    "{": ""      ""Video ID: Or9ANvNqt3o""
  },
  {
    "{": ""      ""Video ID: xEAo7JnDm_I""
  },
  {
    "{": ""      ""Video ID: _MD9yKW-S1k""
  },
  {
    "{": ""      ""Video ID: XPydvZMCC0k""
  },
  {
    "{": ""      ""Video ID: n-uSYHYr3Ts""
  },
  {
    "{": ""      ""Video ID: lE-4hhhXkIQ""
  },
  {
    "{": ""      ""Video ID: Ad1x0b4GBmE""
  },
  {
    "{": ""      ""Video ID: uVrSmNXZYYg""
  },
  {
    "{": ""      ""Video ID: rUo3rR88Dsg""
  },
  {
    "{": ""      ""Video ID: v1mPKsTo8hk""
  },
  {
    "{": ""      ""Video ID: YJuvfODXjI4""
  },
  {
    "{": ""      ""Video ID: jBJbMZ_QHz0""
  },
  {
    "{": ""      ""Video ID: W5tLi_jA7eQ""
  },
  {
    "{": ""      ""Video ID: zwW9-trDMDk""
  },
  {
    "{": ""      ""Video ID: cd5aA_kIDzY""
  },
  {
    "{": ""      ""Video ID: YfVXF84fK48""
  },
  {
    "{": ""      ""Video ID: og0EinKrAVE""
  },
  {
    "{": ""      ""Video ID: ZH-CJechOJ4""
  },
  {
    "{": ""      ""Video ID: -jXZu3ia278""
  },
  {
    "{": ""      ""Video ID: lfbMaNqzkJQ""
  },
  {
    "{": ""      ""Video ID: tWaKcvuh1os""
  },
  {
    "{": ""      ""Video ID: M1xAFoQC_vo""
  },
  {
    "{": ""      ""Video ID: _TILeFYYpKI""
  },
  {
    "{": ""      ""Video ID: adg4A9r-GmA""
  },
  {
    "{": ""      ""Video ID: 5v2HFjesOdU""
  },
  {
    "{": ""      ""Video ID: uPMRNmqb1I8""
  },
  {
    "{": ""      ""Video ID: qbwrK5QKzMs""
  },
  {
    "{": ""      ""Video ID: Bo8qH0DGjQk""
  },
  {
    "{": ""      ""Video ID: QcIALHrN22Y""
  },
  {
    "{": ""      ""Video ID: UPZav-Ut0NY""
  },
  {
    "{": ""      ""Video ID: PmrDRQNjF-U""
  },
  {
    "{": ""      ""Video ID: fRLW1J-XWxQ""
  },
  {
    "{": ""      ""Video ID: kbb6RgSvKDc""
  },
  {
    "{": ""      ""Video ID: fqbspkwFf8c""
  },
  {
    "{": ""      ""Video ID: 7qZFrsFHedA""
  },
  {
    "{": ""      ""Video ID: lZIRnamXz7I""
  },
  {
    "{": ""      ""Video ID: 2N1W6IpDRsc""
  },
  {
    "{": ""      ""Video ID: vVI99g7adR8""
  },
  {
    "{": ""      ""Video ID: cyGoXKYFIl0""
  },
  {
    "{": ""      ""Video ID: JODb29e7Ids""
  },
  {
    "{": ""      ""Video ID: brXX7ax_Tmg""
  },
  {
    "{": ""      ""Video ID: AatvMtXUNDA""
  },
  {
    "{": ""      ""Video ID: HJUjsxNj84o""
  },
  {
    "{": ""      ""Video ID: C_wWkvbGQKQ""
  },
  {
    "{": ""      ""Video ID: JRIBM6HQ1OI""
  },
  {
    "{": ""      ""Video ID: 8zfwF4bzf74""
  },
  {
    "{": ""      ""Video ID: D-GIWGmSVOc""
  },
  {
    "{": ""      ""Video ID: BDvqMOncvpE""
  },
  {
    "{": ""      ""Video ID: mVrSc0mH_KU""
  },
  {
    "{": ""      ""Video ID: AHnPvsjBSDU""
  },
  {
    "{": ""      ""Video ID: JWkBcPzva9Y""
  },
  {
    "{": ""      ""Video ID: Ihl61RQSq2M""
  },
  {
    "{": ""      ""Video ID: K8PHOeb0qGo""
  },
  {
    "{": ""      ""Video ID: yVac56e3x1s""
  },
  {
    "{": ""      ""Video ID: erVOzVnjOAg""
  },
  {
    "{": ""      ""Video ID: aRd5YxgyYQQ""
  },
  {
    "{": ""      ""Video ID: nB37PHzesZ0""
  },
  {
    "{": ""      ""Video ID: SS--YJhOQsA""
  },
  {
    "{": ""      ""Video ID: 26yN342jhKA""
  },
  {
    "{": ""      ""Video ID: bdRFKTOFh8U""
  },
  {
    "{": ""      ""Video ID: _s0ZxAVAcDw""
  },
  {
    "{": ""      ""Video ID: hk_ZW_ojvGQ""
  },
  {
    "{": ""      ""Video ID: zpuyOjEUmas""
  },
  {
    "{": ""      ""Video ID: wqXW-OMvpP0""
  },
  {
    "{": ""      ""Video ID: cSJoOLNbQBo""
  },
  {
    "{": ""      ""Video ID: 5hWYKmrLaRw""
  },
  {
    "{": ""      ""Video ID: JLmwZDmc0Ns""
  },
  {
    "{": ""      ""Video ID: 1jun0YU2TxI""
  },
  {
    "{": ""      ""Video ID: 51GinSJAFNc""
  },
  {
    "{": ""      ""Video ID: eqXp65lW-SE""
  },
  {
    "{": ""      ""Video ID: o3EZEPV8Sxc""
  },
  {
    "{": ""      ""Video ID: UW6lqGcjdlA""
  },
  {
    "{": ""      ""Video ID: x81SIPpnnF0""
  },
  {
    "{": ""      ""Video ID: bmI-mKR3EXk""
  },
  {
    "{": ""      ""Video ID: JzRfvpzVOh4""
  },
  {
    "{": ""      ""Video ID: FGhsMP30jZw""
  },
  {
    "{": ""      ""Video ID: 61sX4p94rTI""
  },
  {
    "{": ""      ""Video ID: czNVQMRr9O8""
  },
  {
    "{": ""      ""Video ID: ORm4jhitPxM""
  },
  {
    "{": ""      ""Video ID: PbFH8ZbPm5o""
  },
  {
    "{": ""      ""Video ID: tCy7q8HpOEs""
  },
  {
    "{": ""      ""Video ID: 7qoUJRIJ3CA""
  },
  {
    "{": ""      ""Video ID: zlFIxwHt9kg""
  },
  {
    "{": ""      ""Video ID: GbE4wcEkKnM""
  },
  {
    "{": ""      ""Video ID: aeXhaFbxpA8""
  },
  {
    "{": ""      ""Video ID: XXYB9WI5tyU""
  },
  {
    "{": ""      ""Video ID: e6TOJwxZnvY""
  },
  {
    "{": ""      ""Video ID: xFkGhxqXiWM""
  },
  {
    "{": ""      ""Video ID: gGQ8ZVDvP_k""
  },
  {
    "{": ""      ""Video ID: xt-cR_YJSl4""
  },
  {
    "{": ""      ""Video ID: ZYpxQEPzpJk""
  },
  {
    "{": ""      ""Video ID: TbRKx2XmNhQ""
  },
  {
    "{": ""      ""Video ID: zHB192OeWaU""
  },
  {
    "{": ""      ""Video ID: SjsXeCsCybE""
  },
  {
    "{": ""      ""Video ID: cFLRqhgdvlU""
  },
  {
    "{": ""      ""Video ID: gDxQ4WakI9k""
  },
  {
    "{": ""      ""Video ID: PFOIPXFs_Ug""
  },
  {
    "{": ""      ""Video ID: -BGlpMxp98I""
  },
  {
    "{": ""      ""Video ID: ke69dglYLqY""
  },
  {
    "{": ""      ""Video ID: -UnI1QHmxik""
  },
  {
    "{": ""      ""Video ID: 21KZ1RrML54""
  },
  {
    "{": ""      ""Video ID: AyDKqDKgaoc""
  },
  {
    "{": ""      ""Video ID: 4QLMp5EUdy0""
  },
  {
    "{": ""      ""Video ID: XueopdCcaCY""
  },
  {
    "{": ""      ""Video ID: jjqjmgyCoCM""
  },
  {
    "{": ""      ""Video ID: v9xXYA9oa74""
  },
  {
    "{": ""      ""Video ID: 8yDnlol_w_U""
  },
  {
    "{": ""      ""Video ID: 0MWK4KhZhWQ""
  },
  {
    "{": ""      ""Video ID: GHqlL3lW2LI""
  },
  {
    "{": ""      ""Video ID: eMnwUL1xVgM""
  },
  {
    "{": ""      ""Video ID: WQ4UuhdU17o""
  },
  {
    "{": ""      ""Video ID: bSO-u6tcdSY""
  },
  {
    "{": ""      ""Video ID: Mc3e0CPmTAk""
  },
  {
    "{": ""      ""Video ID: MiF2fGvEGx0""
  },
  {
    "{": ""      ""Video ID: pxYiGymUHQM""
  },
  {
    "{": ""      ""Video ID: nzSW3KcBGGY""
  },
  {
    "{": ""      ""Video ID: 6Brb3JlZyQ4""
  },
  {
    "{": ""      ""Video ID: qxFoPYpjWUw""
  },
  {
    "{": ""      ""Video ID: pgtSEfiVrVM""
  },
  {
    "{": ""      ""Video ID: AaOg2bq3oNk""
  },
  {
    "{": ""      ""Video ID: avth1C3F_zA""
  },
  {
    "{": ""      ""Video ID: 78BFTtWOKqU""
  },
  {
    "{": ""      ""Video ID: 3z4LMNgLGhM""
  },
  {
    "{": ""      ""Video ID: L_-rz6VkKYY""
  },
  {
    "{": ""      ""Video ID: _vOIz4hLrfk""
  },
  {
    "{": ""      ""Video ID: OT8NbBZ9m40""
  },
  {
    "{": ""      ""Video ID: GGFj3gkutnY""
  },
  {
    "{": ""      ""Video ID: gSb-A3dRDzY""
  },
  {
    "{": ""      ""Video ID: fHN7-B4C7Po""
  },
  {
    "{": ""      ""Video ID: 2JVA7jFnmBI""
  },
  {
    "{": ""      ""Video ID: 2ClGk0amMPU""
  },
  {
    "{": ""      ""Video ID: Sadh1zLTJn0""
  },
  {
    "{": ""      ""Video ID: fDmBVHEkFMs""
  },
  {
    "{": ""      ""Video ID: VPy3IpYzrHY""
  },
  {
    "{": ""      ""Video ID: zoaBbcuhCPg""
  },
  {
    "{": ""      ""Video ID: nPBMa8Cq-pE""
  },
  {
    "{": ""      ""Video ID: esKI1Vp7g7A""
  },
  {
    "{": ""      ""Video ID: 6JWCfQR966g""
  },
  {
    "{": ""      ""Video ID: EVPhiums6Ho""
  },
  {
    "{": ""      ""Video ID: ws1Zcwa5Wns""
  },
  {
    "{": ""      ""Video ID: IhCWlB3GhO0""
  },
  {
    "{": ""      ""Video ID: wHqBykKwj_I""
  },
  {
    "{": ""      ""Video ID: T9AhZjo62Fo""
  },
  {
    "{": ""      ""Video ID: 8OXQs-gWnpQ""
  },
  {
    "{": ""      ""Video ID: HDRNMaxNBVw""
  },
  {
    "{": ""      ""Video ID: idtXbmO4XcM""
  },
  {
    "{": ""      ""Video ID: BScWG5rK29o""
  },
  {
    "{": ""      ""Video ID: Ngh-I3mbV0U""
  },
  {
    "{": ""      ""Video ID: gWHCw-i2wYk""
  },
  {
    "{": ""      ""Video ID: 3Y1IpLB0gfw""
  },
  {
    "{": ""      ""Video ID: SIqS2SgPZhY""
  },
  {
    "{": ""      ""Video ID: q-n1JVGOvPo""
  },
  {
    "{": ""      ""Video ID: NBqLoDPMj8c""
  },
  {
    "{": ""      ""Video ID: YbZTzutK2jM""
  },
  {
    "{": ""      ""Video ID: Z_XTB8l3Tzg""
  },
  {
    "{": ""      ""Video ID: QqIu047Vx8s""
  },
  {
    "{": ""      ""Video ID: hzmbUg_z4Tg""
  },
  {
    "{": ""      ""Video ID: hDGZ6Tgy3rA""
  },
  {
    "{": ""      ""Video ID: uOqu87VlC-w""
  },
  {
    "{": ""      ""Video ID: KR_2x8UUI44""
  },
  {
    "{": ""      ""Video ID: 4vAMEM6dJXI""
  },
  {
    "{": ""      ""Video ID: GhZeYjpSXCQ""
  },
  {
    "{": ""      ""Video ID: VGurfyISnN8""
  },
  {
    "{": ""      ""Video ID: xSZ1xPlLm3U""
  },
  {
    "{": ""      ""Video ID: aIsS9L9nqvY""
  },
  {
    "{": ""      ""Video ID: X4Ua8xO60VE""
  },
  {
    "{": ""      ""Video ID: Z6mC_q3YI70""
  },
  {
    "{": ""      ""Video ID: 9QKorf4M0SQ""
  },
  {
    "{": ""      ""Video ID: jKd8FxQpVY4""
  },
  {
    "{": ""      ""Video ID: mkw33tZG-Hw""
  },
  {
    "{": ""      ""Video ID: 9kuu2edvI4Q""
  },
  {
    "{": ""      ""Video ID: TkArz9YLq0o""
  },
  {
    "{": ""      ""Video ID: ERcRSp9XOdI""
  },
  {
    "{": ""      ""Video ID: NJ12263ThU4""
  },
  {
    "{": ""      ""Video ID: JE-c0DlYW1w""
  },
  {
    "{": ""      ""Video ID: U0t9GP8-cao""
  },
  {
    "{": ""      ""Video ID: pDNxd344h9c""
  },
  {
    "{": ""      ""Video ID: F1qOpdKpwJg""
  },
  {
    "{": ""      ""Video ID: QuD-ewJiBm8""
  },
  {
    "{": ""      ""Video ID: 7fgUJ6PivfQ""
  },
  {
    "{": ""      ""Video ID: I0MdQHww6CM""
  },
  {
    "{": ""      ""Video ID: A3FCIskWObQ""
  },
  {
    "{": ""      ""Video ID: QuJErrjlKqQ""
  },
  {
    "{": ""      ""Video ID: KKnFkVdc95c""
  },
  {
    "{": ""      ""Video ID: DMAAM3ox7Vc""
  },
  {
    "{": ""      ""Video ID: epk9Yzme-No""
  },
  {
    "{": ""      ""Video ID: A-NpdoGkaEc""
  },
  {
    "{": ""      ""Video ID: ccogAV0n-Ak""
  },
  {
    "{": ""      ""Video ID: EotM7FH8uQg""
  },
  {
    "{": ""      ""Video ID: CHKF3kKca-A""
  },
  {
    "{": ""      ""Video ID: 32m4QiTEBMM""
  },
  {
    "{": ""      ""Video ID: VdJb7iWcoR0""
  },
  {
    "{": ""      ""Video ID: u1IccBFXYzA""
  },
  {
    "{": ""      ""Video ID: 2fj-J4bJ-ZU""
  },
  {
    "{": ""      ""Video ID: 2YVBkalr9Zw""
  },
  {
    "{": ""      ""Video ID: NuVaosgPT7Q""
  },
  {
    "{": ""      ""Video ID: iXMhrGg8EEw""
  },
  {
    "{": ""      ""Video ID: efIwlc3hUXQ""
  },
  {
    "{": ""      ""Video ID: jJ-GUpiV4Yk""
  },
  {
    "{": ""      ""Video ID: KEO0vLrDvtY""
  },
  {
    "{": ""      ""Video ID: GxtaOmKs1tQ""
  },
  {
    "{": ""      ""Video ID: Yez4t9TKRoI""
  },
  {
    "{": ""      ""Video ID: rs7ASfZ2cSQ""
  },
  {
    "{": ""      ""Video ID: W1IkMx5-XYw""
  },
  {
    "{": ""      ""Video ID: dkis07L-O-g""
  },
  {
    "{": ""      ""Video ID: gIJA6pTex_Y""
  },
  {
    "{": ""      ""Video ID: TJCOr_dEqPg""
  },
  {
    "{": ""      ""Video ID: j8vPgXSVbRI""
  },
  {
    "{": ""      ""Video ID: ACcIdICAsGE""
  },
  {
    "{": ""      ""Video ID: -FwBiVK4LF8""
  },
  {
    "{": ""      ""Video ID: xLhWXSgkUTw""
  },
  {
    "{": ""      ""Video ID: gSBQeWO_b8s""
  },
  {
    "{": ""      ""Video ID: Zn-RsYbcLHk""
  },
  {
    "{": ""      ""Video ID: srTsw-5mcok""
  },
  {
    "{": ""      ""Video ID: Je0SUq8cnyw""
  },
  {
    "{": ""      ""Video ID: Zk8ki4x-6uU""
  },
  {
    "{": ""      ""Video ID: kM8_Eh80NW8""
  },
  {
    "{": ""      ""Video ID: 6jpqHBaF_dQ""
  },
  {
    "{": ""      ""Video ID: pJqYUKdK01Y""
  },
  {
    "{": ""      ""Video ID: 38LXsvGNZ14""
  },
  {
    "{": ""      ""Video ID: lroxnnZLZ_g""
  },
  {
    "{": ""      ""Video ID: 7yuwuWNXpic""
  },
  {
    "{": ""      ""Video ID: FG1ZGOzBSNQ""
  },
  {
    "{": ""      ""Video ID: VHGyTqScN7w""
  },
  {
    "{": ""      ""Video ID: eSuWO0_IHEc""
  },
  {
    "{": ""      ""Video ID: zU3KVo_slFQ""
  },
  {
    "{": ""      ""Video ID: 9dtiGn_w0bY""
  },
  {
    "{": ""      ""Video ID: CXqUU-oYSpY""
  },
  {
    "{": ""      ""Video ID: -wfm5zVvo30""
  },
  {
    "{": ""      ""Video ID: Q_Rr3oHJIRw""
  },
  {
    "{": ""      ""Video ID: ZwfhJIHWYTg""
  },
  {
    "{": ""      ""Video ID: fLwifqYVsQc""
  },
  {
    "{": ""      ""Video ID: EcdgD27CYDA""
  },
  {
    "{": ""      ""Video ID: ifDHMeegTLY""
  },
  {
    "{": ""      ""Video ID: Q1QK_iCgnyQ""
  },
  {
    "{": ""      ""Video ID: xvYBkE50Ib0""
  },
  {
    "{": ""      ""Video ID: M8TNl37D5Fk""
  },
  {
    "{": ""      ""Video ID: --NjiDX9vtw""
  },
  {
    "{": ""      ""Video ID: 4VU8-yIn1Ws""
  },
  {
    "{": ""      ""Video ID: TZofhLqcVKg""
  },
  {
    "{": ""      ""Video ID: yLx_Zaw6RAY""
  },
  {
    "{": ""      ""Video ID: HFH19wfGg8Q""
  },
  {
    "{": ""      ""Video ID: tKdXb8c4eNk""
  },
  {
    "{": ""      ""Video ID: tlNs6-NNbCI""
  },
  {
    "{": ""      ""Video ID: kT7oBURyzLE""
  },
  {
    "{": ""      ""Video ID: odglY01uojo""
  },
  {
    "{": ""      ""Video ID: zqTWscyGnK0""
  },
  {
    "{": ""      ""Video ID: AeH3141d9fc""
  },
  {
    "{": ""      ""Video ID: qizs0XdFwPk""
  },
  {
    "{": ""      ""Video ID: YHhpItFMyF8""
  },
  {
    "{": ""      ""Video ID: U77a_wK7qls""
  },
  {
    "{": ""      ""Video ID: WOOaCT_Yj1U""
  },
  {
    "{": ""      ""Video ID: fPG02HGdrjk""
  },
  {
    "{": ""      ""Video ID: 6IzOgL1NKhY""
  },
  {
    "{": ""      ""Video ID: ZjjY1rRHSRY""
  },
  {
    "{": ""      ""Video ID: LF86tJwh5XY""
  },
  {
    "{": ""      ""Video ID: -1DKa0g5hFg""
  },
  {
    "{": ""      ""Video ID: gWd3OVi0Jbs""
  },
  {
    "{": ""      ""Video ID: Hm1Qkvj8puc""
  },
  {
    "{": ""      ""Video ID: gQ9Lg7DP4No""
  },
  {
    "{": ""      ""Video ID: Od-MYorauQQ""
  },
  {
    "{": ""      ""Video ID: KOMtG-srrYA""
  },
  {
    "{": ""      ""Video ID: FS3sldknCRg""
  },
  {
    "{": ""      ""Video ID: OcXbzMP7y94""
  },
  {
    "{": ""      ""Video ID: rRs5NqhC5SQ""
  },
  {
    "{": ""      ""Video ID: HAmEToWjT9U""
  },
  {
    "{": ""      ""Video ID: zjgGZ9BGu5U""
  },
  {
    "{": ""      ""Video ID: wKgYeiiUkOg""
  },
  {
    "{": ""      ""Video ID: 6oSfW84SfEY""
  },
  {
    "{": ""      ""Video ID: Mna_GqVvOdY""
  },
  {
    "{": ""      ""Video ID: XBxHHLTZ7b0""
  },
  {
    "{": ""      ""Video ID: HezTIk9ye1Q""
  },
  {
    "{": ""      ""Video ID: 4GlmxBZKfnI""
  },
  {
    "{": ""      ""Video ID: B3qfduHMtqc""
  },
  {
    "{": ""      ""Video ID: 22QEK1RewfI""
  },
  {
    "{": ""      ""Video ID: Mhsi77ZYisI""
  },
  {
    "{": ""      ""Video ID: xSOjp5wkILA""
  },
  {
    "{": ""      ""Video ID: EaCdQwSzZrc""
  },
  {
    "{": ""      ""Video ID: W9VVVWE1UfU""
  },
  {
    "{": ""      ""Video ID: ID2-bvki1M0""
  },
  {
    "{": ""      ""Video ID: SEWtJQ4coOc""
  },
  {
    "{": ""      ""Video ID: IWpE8syet00""
  },
  {
    "{": ""      ""Video ID: ZNBLJIYoxKY""
  },
  {
    "{": ""      ""Video ID: In_UPQzRYts""
  },
  {
    "{": ""      ""Video ID: KT0ICCcb8Hw""
  },
  {
    "{": ""      ""Video ID: zcS0aWG7qIo""
  },
  {
    "{": ""      ""Video ID: H2IrPyix_Ag""
  },
  {
    "{": ""      ""Video ID: o_7QQP1h2N8""
  },
  {
    "{": ""      ""Video ID: SZ0voWYH5QA""
  },
  {
    "{": ""      ""Video ID: 6J05cByqBg4""
  },
  {
    "{": ""      ""Video ID: 9zVdCRF3_PU""
  },
  {
    "{": ""      ""Video ID: b7N_hbUt4lw""
  },
  {
    "{": ""      ""Video ID: Xi6Ghpv40mA""
  },
  {
    "{": ""      ""Video ID: PnfHRlRYyW4""
  },
  {
    "{": ""      ""Video ID: 1cP9QRsJ9kg""
  },
  {
    "{": ""      ""Video ID: JZsZjr5LGJw""
  },
  {
    "{": ""      ""Video ID: 5GSjjrdwacI""
  },
  {
    "{": ""      ""Video ID: E1uTFUxw2aM""
  },
  {
    "{": ""      ""Video ID: gojTt_JfOWs""
  },
  {
    "{": ""      ""Video ID: ixC2rxN7FdE""
  },
  {
    "{": ""      ""Video ID: PAZ5g1QXBok""
  },
  {
    "{": ""      ""Video ID: ozWFBr9ikjY""
  },
  {
    "{": ""      ""Video ID: 49NvXkWolSU""
  },
  {
    "{": ""      ""Video ID: poBOxS9b39w""
  },
  {
    "{": ""      ""Video ID: KRT1_a3HjDs""
  },
  {
    "{": ""      ""Video ID: GmnqdJNe2Ho""
  },
  {
    "{": ""      ""Video ID: KSAg3jZKMC8""
  },
  {
    "{": ""      ""Video ID: 8_47537kxCE""
  },
  {
    "{": ""      ""Video ID: 5a1CXWo1yNU""
  },
  {
    "{": ""      ""Video ID: Vlpp6LMjEBo""
  },
  {
    "{": ""      ""Video ID: 75wn0VZ6GSk""
  },
  {
    "{": ""      ""Video ID: lsRWksQPHJk""
  },
  {
    "{": ""      ""Video ID: fk7Kr3-Ynpk""
  },
  {
    "{": ""      ""Video ID: 7J2HVAAQusk""
  },
  {
    "{": ""      ""Video ID: d0nSuK7-1gE""
  },
  {
    "{": ""      ""Video ID: vMmUVcncEV0""
  },
  {
    "{": ""      ""Video ID: s68EaWcIMHg""
  },
  {
    "{": ""      ""Video ID: mlBOeekEO8E""
  },
  {
    "{": ""      ""Video ID: NkH4zS-PcwY""
  },
  {
    "{": ""      ""Video ID: eQvxplevYUE""
  },
  {
    "{": ""      ""Video ID: CQKvzONLHvo""
  },
  {
    "{": ""      ""Video ID: RthfzzuGFsY""
  },
  {
    "{": ""      ""Video ID: 2DVorjObO2s""
  },
  {
    "{": ""      ""Video ID: d3g7G5fz09k""
  },
  {
    "{": ""      ""Video ID: NLpygcE-oTc""
  },
  {
    "{": ""      ""Video ID: dvS5CuQYHFE""
  },
  {
    "{": ""      ""Video ID: Q_Lyo5z8_Qo""
  },
  {
    "{": ""      ""Video ID: 2Q1CHyO23w0""
  },
  {
    "{": ""      ""Video ID: it6o95zetps""
  },
  {
    "{": ""      ""Video ID: aCBAendOnxo""
  },
  {
    "{": ""      ""Video ID: Wh3TjqCeRQg""
  },
  {
    "{": ""      ""Video ID: RzbsLkiJlGo""
  },
  {
    "{": ""      ""Video ID: DWxaO8NyWdI""
  },
  {
    "{": ""      ""Video ID: RLhGwx41IvM""
  },
  {
    "{": ""      ""Video ID: IliWk0gIGXQ""
  },
  {
    "{": ""      ""Video ID: Q4gg6fwrVQo""
  },
  {
    "{": ""      ""Video ID: B64K0HNMYqg""
  },
  {
    "{": ""      ""Video ID: FDILepD8Reo""
  },
  {
    "{": ""      ""Video ID: 9CsUWHRfpVU""
  },
  {
    "{": ""      ""Video ID: ArZ67A4KZsY""
  },
  {
    "{": ""      ""Video ID: 3Ut-n-e__0E""
  },
  {
    "{": ""      ""Video ID: VFigBpfqaXU""
  },
  {
    "{": ""      ""Video ID: 6lr6d92nW9M""
  },
  {
    "{": ""      ""Video ID: D97qHtEgNgs""
  },
  {
    "{": ""      ""Video ID: U0wDPyLo7dY""
  },
  {
    "{": ""      ""Video ID: WG85Ko2FyLA""
  },
  {
    "{": ""      ""Video ID: 8EofI-g2lwY""
  },
  {
    "{": ""      ""Video ID: uzZVWQz9H0w""
  },
  {
    "{": ""      ""Video ID: hBNM5Tc59aM""
  },
  {
    "{": ""      ""Video ID: 5lzRtajg0Gc""
  },
  {
    "{": ""      ""Video ID: p4g05tfSfuo""
  },
  {
    "{": ""      ""Video ID: n6-A1ZDLiXs""
  },
  {
    "{": ""      ""Video ID: YY22225bzEY""
  },
  {
    "{": ""      ""Video ID: FInSRuafLDM""
  },
  {
    "{": ""      ""Video ID: cLMHHES0TH0""
  },
  {
    "{": ""      ""Video ID: hBvJmZQPSOo""
  },
  {
    "{": ""      ""Video ID: EnTaaUI0LUQ""
  },
  {
    "{": ""      ""Video ID: BoQGlEq_WzU""
  },
  {
    "{": ""      ""Video ID: mdRaI597HKA""
  },
  {
    "{": ""      ""Video ID: DGkszzt5IqM""
  },
  {
    "{": ""      ""Video ID: 1SyUId9bOcg""
  },
  {
    "{": ""      ""Video ID: 9_ZAoniaJGs""
  },
  {
    "{": ""      ""Video ID: XkH_JGZbrT8""
  },
  {
    "{": ""      ""Video ID: s2DUO49FRoM""
  },
  {
    "{": ""      ""Video ID: b4vKFDZgIkc""
  },
  {
    "{": ""      ""Video ID: 1mcsrp2uqNc""
  },
  {
    "{": ""      ""Video ID: 8ctIifEt2nI""
  },
  {
    "{": ""      ""Video ID: tmyQI8MjO90""
  },
  {
    "{": ""      ""Video ID: A12qtprly-Q""
  },
  {
    "{": ""      ""Video ID: hx0CdwasJeg""
  },
  {
    "{": ""      ""Video ID: jsUkCkr2raE""
  },
  {
    "{": ""      ""Video ID: C1MzdJOMnd0""
  },
  {
    "{": ""      ""Video ID: Et0ZiyMOYUM""
  },
  {
    "{": ""      ""Video ID: w97Vjqgv5iA""
  },
  {
    "{": ""      ""Video ID: D9uz9p1v-h4""
  },
  {
    "{": ""      ""Video ID: KyN1r6s56ms""
  },
  {
    "{": ""      ""Video ID: roPEKXpzYkk""
  },
  {
    "{": ""      ""Video ID: _W3RUdJ1F6I""
  },
  {
    "{": ""      ""Video ID: vfJlkImPVx8""
  },
  {
    "{": ""      ""Video ID: 6LP2KtE1VVU""
  },
  {
    "{": ""      ""Video ID: GvYnHC-ukI0""
  },
  {
    "{": ""      ""Video ID: a0X5JIeCUnY""
  },
  {
    "{": ""      ""Video ID: HgfUuGRQno8""
  },
  {
    "{": ""      ""Video ID: hjUHaG_K5fg""
  },
  {
    "{": ""      ""Video ID: dVXm2yjPscA""
  },
  {
    "{": ""      ""Video ID: 4Wzd7rUHQzo""
  },
  {
    "{": ""      ""Video ID: z2JctYLzVJk""
  },
  {
    "{": ""      ""Video ID: Vy9DBxjo_Ow""
  },
  {
    "{": ""      ""Video ID: -Ti1hKsRzDA""
  },
  {
    "{": ""      ""Video ID: gASQ1_HEEHA""
  },
  {
    "{": ""      ""Video ID: iGOFESqcyVc""
  },
  {
    "{": ""      ""Video ID: 6nMKcc0X4Kk""
  },
  {
    "{": ""      ""Video ID: DfceF6IVoz0""
  },
  {
    "{": ""      ""Video ID: KukmM8f2Oro""
  },
  {
    "{": ""      ""Video ID: Ha2haXYiq64""
  },
  {
    "{": ""      ""Video ID: 1Z17ZPQP60E""
  },
  {
    "{": ""      ""Video ID: ruXej7LMRX4""
  },
  {
    "{": ""      ""Video ID: ocnQDQU6FbE""
  },
  {
    "{": ""      ""Video ID: 6PCcpIPjJxo""
  },
  {
    "{": ""      ""Video ID: oPupb_VcGM8""
  },
  {
    "{": ""      ""Video ID: tQm3u_ztHrY""
  },
  {
    "{": ""      ""Video ID: L3wk5LoLewQ""
  },
  {
    "{": ""      ""Video ID: wTslKKXBBAs""
  },
  {
    "{": ""      ""Video ID: hG9ILia535Q""
  },
  {
    "{": ""      ""Video ID: gdq7yfpj0Yg""
  },
  {
    "{": ""      ""Video ID: Rixo0aHGMzk""
  },
  {
    "{": ""      ""Video ID: Iy712w55m_o""
  },
  {
    "{": ""      ""Video ID: Pt1mMJc8VvM""
  },
  {
    "{": ""      ""Video ID: ZbBHkC6FLlQ""
  },
  {
    "{": ""      ""Video ID: BB84zlk3cO8""
  },
  {
    "{": ""      ""Video ID: gaIlO-hPrYE""
  },
  {
    "{": ""      ""Video ID: 68clIoBR9aM""
  },
  {
    "{": ""      ""Video ID: f6zpDTlPIdY""
  },
  {
    "{": ""      ""Video ID: nu2Bx8OhS40""
  },
  {
    "{": ""      ""Video ID: r39MoThESaY""
  },
  {
    "{": ""      ""Video ID: belq28zQQ6c""
  },
  {
    "{": ""      ""Video ID: AG1cIHYgXuU""
  },
  {
    "{": ""      ""Video ID: bCo9yQt751A""
  },
  {
    "{": ""      ""Video ID: Y9sHAitW1Ao""
  },
  {
    "{": ""      ""Video ID: ycc9Va-6sNM""
  },
  {
    "{": ""      ""Video ID: OIiQ0BivtNc""
  },
  {
    "{": ""      ""Video ID: cY3TzxNKsKM""
  },
  {
    "{": ""      ""Video ID: 6cM5y5utht8""
  },
  {
    "{": ""      ""Video ID: Fw0_V0V1q7o""
  },
  {
    "{": ""      ""Video ID: AQisA7VNHD4""
  },
  {
    "{": ""      ""Video ID: NaxQHl8lJK0""
  },
  {
    "{": ""      ""Video ID: TV7bCxoOEik""
  },
  {
    "{": ""      ""Video ID: rFvNWiI8aKU""
  },
  {
    "{": ""      ""Video ID: CInYCFvPTZk""
  },
  {
    "{": ""      ""Video ID: WeVpbRlWU-M""
  },
  {
    "{": ""      ""Video ID: H7XJg0FH8TM""
  },
  {
    "{": ""      ""Video ID: Hl4OqFwgxtA""
  },
  {
    "{": ""      ""Video ID: -hURjCJv1_c""
  },
  {
    "{": ""      ""Video ID: jIgYLedanF4""
  },
  {
    "{": ""      ""Video ID: LZu-iyNIdYY""
  },
  {
    "{": ""      ""Video ID: Jbbb6KKXJOw""
  },
  {
    "{": ""      ""Video ID: hFUg7bRIIJM""
  },
  {
    "{": ""      ""Video ID: CESBR4G_NtI""
  },
  {
    "{": ""      ""Video ID: doSll8KoJPQ""
  },
  {
    "{": ""      ""Video ID: 2kJqQ7DJWg8""
  },
  {
    "{": ""      ""Video ID: PO5OQ3xlvmo""
  },
  {
    "{": ""      ""Video ID: gF5JA5BtXzc""
  },
  {
    "{": ""      ""Video ID: Io0N7_QEu3U""
  },
  {
    "{": ""      ""Video ID: GgR6YN6PxDM""
  },
  {
    "{": ""      ""Video ID: WBU8uzuLCK4""
  },
  {
    "{": ""      ""Video ID: Ts8ugJXt4Jw""
  },
  {
    "{": ""      ""Video ID: PidYNBHPJhY""
  },
  {
    "{": ""      ""Video ID: Y0mkBIsDlOc""
  },
  {
    "{": ""      ""Video ID: 3Y5pgyw5eIk""
  },
  {
    "{": ""      ""Video ID: ooCdWp2dTCk""
  },
  {
    "{": ""      ""Video ID: yDSJ5mpvwgw""
  },
  {
    "{": ""      ""Video ID: LwGiCFMW7gM""
  },
  {
    "{": ""      ""Video ID: q02Nnjsd1vo""
  },
  {
    "{": ""      ""Video ID: R7chGtam0F8""
  },
  {
    "{": ""      ""Video ID: fe9pMA0khlQ""
  },
  {
    "{": ""      ""Video ID: rGv0PGBBneM""
  },
  {
    "{": ""      ""Video ID: khYp2BLDezY""
  },
  {
    "{": ""      ""Video ID: V45ozSJIVxk""
  },
  {
    "{": ""      ""Video ID: 3V456cTGF2E""
  },
  {
    "{": ""      ""Video ID: ShrhGsXhCyQ""
  },
  {
    "{": ""      ""Video ID: w6C6eBNpBJU""
  },
  {
    "{": ""      ""Video ID: x01x9xEuceY""
  },
  {
    "{": ""      ""Video ID: 2X2IUQQHiig""
  },
  {
    "{": ""      ""Video ID: hv2zGjVTBP8""
  },
  {
    "{": ""      ""Video ID: c9Ze5RG8L3k""
  },
  {
    "{": ""      ""Video ID: C3oBDEEK1fo""
  },
  {
    "{": ""      ""Video ID: C2YZfm-RoYI""
  },
  {
    "{": ""      ""Video ID: 7CDsuuYdiY0""
  },
  {
    "{": ""      ""Video ID: cX-jdjeQmDo""
  },
  {
    "{": ""      ""Video ID: TOGsGD-f6RM""
  },
  {
    "{": ""      ""Video ID: HSbu9ZmUIMc""
  },
  {
    "{": ""      ""Video ID: A2vmoqX_OMM""
  },
  {
    "{": ""      ""Video ID: 2N6CCP25HjM""
  },
  {
    "{": ""      ""Video ID: yUGzf5ZWnx8""
  },
  {
    "{": ""      ""Video ID: keXfuSx-Dh4""
  },
  {
    "{": ""      ""Video ID: WhEG9x4dVIo""
  },
  {
    "{": ""      ""Video ID: p9eCJVpPS6I""
  },
  {
    "{": ""      ""Video ID: xPjtmLkstVs""
  },
  {
    "{": ""      ""Video ID: mY6uRpiD2TE""
  },
  {
    "{": ""      ""Video ID: PhXRZj5TdRM""
  },
  {
    "{": ""      ""Video ID: -BsyWByAK4k""
  },
  {
    "{": ""      ""Video ID: S9ZazjWpSB0""
  },
  {
    "{": ""      ""Video ID: dY8oPNN10Rs""
  },
  {
    "{": ""      ""Video ID: 5uJFZcn2cxo""
  },
  {
    "{": ""      ""Video ID: gwv0Px3MRvk""
  },
  {
    "{": ""      ""Video ID: qoZfQ7wHUVI""
  },
  {
    "{": ""      ""Video ID: ryu3_ckLaZk""
  },
  {
    "{": ""      ""Video ID: huEljRAJO98""
  },
  {
    "{": ""      ""Video ID: fyIHvlFmJnU""
  },
  {
    "{": ""      ""Video ID: ShegCNHaH_4""
  },
  {
    "{": ""      ""Video ID: Qr-6sNI28Tg""
  },
  {
    "{": ""      ""Video ID: _LArDIxtfyk""
  },
  {
    "{": ""      ""Video ID: B7qJC6tsADI""
  },
  {
    "{": ""      ""Video ID: BwO6wf3VHJQ""
  },
  {
    "{": ""      ""Video ID: -002Yr_r-b8""
  },
  {
    "{": ""      ""Video ID: 3S6cPoZV7XM""
  },
  {
    "{": ""      ""Video ID: KKVzl-fihck""
  },
  {
    "{": ""      ""Video ID: X0frjwsmx1I""
  },
  {
    "{": ""      ""Video ID: raEJ2zConMg""
  },
  {
    "{": ""      ""Video ID: whhbPVrb5KM""
  },
  {
    "{": ""      ""Video ID: uyCoDbFVaJ8""
  },
  {
    "{": ""      ""Video ID: Zgh_53_eaqc""
  },
  {
    "{": ""      ""Video ID: hNK26-o-IS8""
  },
  {
    "{": ""      ""Video ID: qX7L647LYHk""
  },
  {
    "{": ""      ""Video ID: Qt5Et3vT_ng""
  },
  {
    "{": ""      ""Video ID: i0HXEglXD5U""
  },
  {
    "{": ""      ""Video ID: cjylvNNo7zc""
  },
  {
    "{": ""      ""Video ID: 9LZyHoAPL3M""
  },
  {
    "{": ""      ""Video ID: uQNWHmiGj-k""
  },
  {
    "{": ""      ""Video ID: 8BB3NrSpRGE""
  },
  {
    "{": ""      ""Video ID: PjiGNqmDCSI""
  },
  {
    "{": ""      ""Video ID: l5ZXM3h4jig""
  },
  {
    "{": ""      ""Video ID: UabYW6QtCfM""
  },
  {
    "{": ""      ""Video ID: 522bNo6hFMw""
  },
  {
    "{": ""      ""Video ID: cXhqsu3YOfE""
  },
  {
    "{": ""      ""Video ID: zlF2YcnWUio""
  },
  {
    "{": ""      ""Video ID: dKeBwMuzKK0""
  },
  {
    "{": ""      ""Video ID: MyvVQYf6XWk""
  },
  {
    "{": ""      ""Video ID: EgK-evWJtWU""
  },
  {
    "{": ""      ""Video ID: _8fr3bauSyM""
  },
  {
    "{": ""      ""Video ID: pwJKGfAWQUo""
  },
  {
    "{": ""      ""Video ID: 9fZWNzx0ouw""
  },
  {
    "{": ""      ""Video ID: E-DdsRh_v-s""
  },
  {
    "{": ""      ""Video ID: zODSOBkpiV0""
  },
  {
    "{": ""      ""Video ID: RgX9SZDhPic""
  },
  {
    "{": ""      ""Video ID: VuC8oDQpkGU""
  },
  {
    "{": ""      ""Video ID: D9HdsBzJRdc""
  },
  {
    "{": ""      ""Video ID: G5ruQT-1-uY""
  },
  {
    "{": ""      ""Video ID: mN9IXLT_UFo""
  },
  {
    "{": ""      ""Video ID: q5-pi8bnuh0""
  },
  {
    "{": ""      ""Video ID: UQIlNVbttuM""
  },
  {
    "{": ""      ""Video ID: V4af9Q0Fa4Q""
  },
  {
    "{": ""      ""Video ID: Ju1Dr89xbZ4""
  },
  {
    "{": ""      ""Video ID: MvFCPkvNMY4""
  },
  {
    "{": ""      ""Video ID: 33ZjcnWf9hA""
  },
  {
    "{": ""      ""Video ID: jr8RMYxhqbw""
  },
  {
    "{": ""      ""Video ID: LcO9tRDg4NI""
  },
  {
    "{": ""      ""Video ID: QKjhNa6PGLk""
  },
  {
    "{": ""      ""Video ID: Z7vZnIE8c68""
  },
  {
    "{": ""      ""Video ID: dZIbQLiBv4Q""
  },
  {
    "{": ""      ""Video ID: oybBROcYWcA""
  },
  {
    "{": ""      ""Video ID: l2MOpkriXb4""
  },
  {
    "{": ""      ""Video ID: 82XvG-gvqSo""
  },
  {
    "{": ""      ""Video ID: zjB4yUb2Eu0""
  },
  {
    "{": ""      ""Video ID: 6Uk6izT3AtQ""
  },
  {
    "{": ""      ""Video ID: v7ZG8ohlZvE""
  },
  {
    "{": ""      ""Video ID: Y9DuCyJikSE""
  },
  {
    "{": ""      ""Video ID: 6afjdjjG1mI""
  },
  {
    "{": ""      ""Video ID: U0VOrLOhhbo""
  },
  {
    "{": ""      ""Video ID: 7TblCRd8fkA""
  },
  {
    "{": ""      ""Video ID: f777edriEkI""
  },
  {
    "{": ""      ""Video ID: 53x4zozLcV4""
  },
  {
    "{": ""      ""Video ID: ejoIItxUXTI""
  },
  {
    "{": ""      ""Video ID: J036bTqOb2A""
  },
  {
    "{": ""      ""Video ID: KloETuVJx2c""
  },
  {
    "{": ""      ""Video ID: IPx_bX5_T70""
  },
  {
    "{": ""      ""Video ID: Iho7UvmsdhI""
  },
  {
    "{": ""      ""Video ID: z8LHkje1lIs""
  },
  {
    "{": ""      ""Video ID: Vs_GJrovHSs""
  },
  {
    "{": ""      ""Video ID: KyW7y0hq8XQ""
  },
  {
    "{": ""      ""Video ID: 3XlPU5rUeI0""
  },
  {
    "{": ""      ""Video ID: SA1f2MefsMM""
  },
  {
    "{": ""      ""Video ID: GrVsLdTtepM""
  },
  {
    "{": ""      ""Video ID: btCmQJXTyTw""
  },
  {
    "{": ""      ""Video ID: 2TKtWegS1DY""
  },
  {
    "{": ""      ""Video ID: aroN2uRbIMc""
  },
  {
    "{": ""      ""Video ID: s1UT2Ms5E2k""
  },
  {
    "{": ""      ""Video ID: a7wh_yhedd8""
  },
  {
    "{": ""      ""Video ID: CwKsflSFpv4""
  },
  {
    "{": ""      ""Video ID: nqcrQixAKJc""
  },
  {
    "{": ""      ""Video ID: KSZq1Wkanxg""
  },
  {
    "{": ""      ""Video ID: lWLwJyc0ZqI""
  },
  {
    "{": ""      ""Video ID: msMQlZu2c0o""
  },
  {
    "{": ""      ""Video ID: _PAURdVu0zo""
  },
  {
    "{": ""      ""Video ID: bUvWK_xJXiU""
  },
  {
    "{": ""      ""Video ID: 3LeHSRiUbUs""
  },
  {
    "{": ""      ""Video ID: cZbAwrycIc0""
  },
  {
    "{": ""      ""Video ID: gBMdN4nl7x0""
  },
  {
    "{": ""      ""Video ID: gagcykr4pZ4""
  },
  {
    "{": ""      ""Video ID: onnmXHsXfaU""
  },
  {
    "{": ""      ""Video ID: GxE9D6mIO7o""
  },
  {
    "{": ""      ""Video ID: orn4hc5ZBZs""
  },
  {
    "{": ""      ""Video ID: 3F5VWaCZvaM""
  },
  {
    "{": ""      ""Video ID: ipjhC0WfL9Q""
  },
  {
    "{": ""      ""Video ID: qJzSiAPXTiQ""
  },
  {
    "{": ""      ""Video ID: ejQkFKYK6a8""
  },
  {
    "{": ""      ""Video ID: CIrTfVuT52o""
  },
  {
    "{": ""      ""Video ID: EIbjBOtWBHg""
  },
  {
    "{": ""      ""Video ID: 1ASBuh72Re8""
  },
  {
    "{": ""      ""Video ID: TIiBzX7b1og""
  },
  {
    "{": ""      ""Video ID: pXBjwQqdqI4""
  },
  {
    "{": ""      ""Video ID: 9e75lQUT_OY""
  },
  {
    "{": ""      ""Video ID: STLR6tFP4S4""
  },
  {
    "{": ""      ""Video ID: Tq2Q848P0h8""
  },
  {
    "{": ""      ""Video ID: D6SfmXigHpE""
  },
  {
    "{": ""      ""Video ID: USSAEQl0XMM""
  },
  {
    "{": ""      ""Video ID: bImMxtAX5Ic""
  },
  {
    "{": ""      ""Video ID: XWdz1pnAFUA""
  },
  {
    "{": ""      ""Video ID: 1Ylk69fDO4U""
  },
  {
    "{": ""      ""Video ID: 4NZfeHN7DxQ""
  },
  {
    "{": ""      ""Video ID: ob7SyWw1jHQ""
  },
  {
    "{": ""      ""Video ID: IIBPGvK7Pg0""
  },
  {
    "{": ""      ""Video ID: 3ajC0Wl116I""
  },
  {
    "{": ""      ""Video ID: 5gFrPAnht6o""
  },
  {
    "{": ""      ""Video ID: rmUHDujLBNQ""
  },
  {
    "{": ""      ""Video ID: EgphbC2rOxg""
  },
  {
    "{": ""      ""Video ID: kPm9HPmxLh4""
  },
  {
    "{": ""      ""Video ID: RKtoA7ezx_Y""
  },
  {
    "{": ""      ""Video ID: osNvnNO5LrI""
  },
  {
    "{": ""      ""Video ID: _wCdULj6fOQ""
  },
  {
    "{": ""      ""Video ID: maJz0kTQJyI""
  },
  {
    "{": ""      ""Video ID: eSLm9NrWXVc""
  },
  {
    "{": ""      ""Video ID: NaCYEGSSpEA""
  },
  {
    "{": ""      ""Video ID: npbpK4yQ4tg""
  },
  {
    "{": ""      ""Video ID: X2xcF7b9x_U""
  },
  {
    "{": ""      ""Video ID: ut-VciIZQFY""
  },
  {
    "{": ""      ""Video ID: BFVDkr4rR4E""
  },
  {
    "{": ""      ""Video ID: xKBM8Q_w0wg""
  },
  {
    "{": ""      ""Video ID: RbaLeU1Ht1w""
  },
  {
    "{": ""      ""Video ID: 15Auogh_AZc""
  },
  {
    "{": ""      ""Video ID: l3kaK2_CrEw""
  },
  {
    "{": ""      ""Video ID: 6wBWjwqG318""
  },
  {
    "{": ""      ""Video ID: 3MMLozhEYPA""
  },
  {
    "{": ""      ""Video ID: GlYMNW4rqYU""
  },
  {
    "{": ""      ""Video ID: zmyvEhU-gmw""
  },
  {
    "{": ""      ""Video ID: c3KFFFXvbXY""
  },
  {
    "{": ""      ""Video ID: AoFWRXzNc7U""
  },
  {
    "{": ""      ""Video ID: SaEjnIguMIU""
  },
  {
    "{": ""      ""Video ID: 7pT85npMef0""
  },
  {
    "{": ""      ""Video ID: fJPyX6eIvwY""
  },
  {
    "{": ""      ""Video ID: FkRjWKgvqpI""
  },
  {
    "{": ""      ""Video ID: t387PcnvPZE""
  },
  {
    "{": ""      ""Video ID: NqM4EVmpA04""
  },
  {
    "{": ""      ""Video ID: C9xM1Cpubk0""
  },
  {
    "{": ""      ""Video ID: p62zMaMO-1s""
  },
  {
    "{": ""      ""Video ID: fmALOxE2bZI""
  },
  {
    "{": ""      ""Video ID: ai47ETebgso""
  },
  {
    "{": ""      ""Video ID: WylfwfEYxCw""
  },
  {
    "{": ""      ""Video ID: MNKmxGHfEXs""
  },
  {
    "{": ""      ""Video ID: yny7xVNgeFQ""
  },
  {
    "{": ""      ""Video ID: NmA-dWdaI5k""
  },
  {
    "{": ""      ""Video ID: 6epCVUppjJM""
  },
  {
    "{": ""      ""Video ID: StIPhBHghU0""
  },
  {
    "{": ""      ""Video ID: lnlKgQP6Afw""
  },
  {
    "{": ""      ""Video ID: mMpqSDM6SRo""
  },
  {
    "{": ""      ""Video ID: LjLMAQiIRyU""
  },
  {
    "{": ""      ""Video ID: rQ5zHzfnGT4""
  },
  {
    "{": ""      ""Video ID: MEu5sqac99M""
  },
  {
    "{": ""      ""Video ID: -ClwicFzAcM""
  },
  {
    "{": ""      ""Video ID: wwU8O6tc0kI""
  },
  {
    "{": ""      ""Video ID: WcmB9xWr0XY""
  },
  {
    "{": ""      ""Video ID: cGNeCARNKuA""
  },
  {
    "{": ""      ""Video ID: jEkJ8Mow4_M""
  },
  {
    "{": ""      ""Video ID: I1UIDqAiXMQ""
  },
  {
    "{": ""      ""Video ID: K_mNMGtHBSU""
  },
  {
    "{": ""      ""Video ID: hWiBt-pqp0E""
  },
  {
    "{": ""      ""Video ID: -ELn-IdLwUs""
  },
  {
    "{": ""      ""Video ID: j4_O-Zd1bec""
  },
  {
    "{": ""      ""Video ID: Jpnajrx7FGM""
  },
  {
    "{": ""      ""Video ID: EDModrMBQ3k""
  },
  {
    "{": ""      ""Video ID: zP5uIPyYDlQ""
  },
  {
    "{": ""      ""Video ID: wekzQrQfacg""
  },
  {
    "{": ""      ""Video ID: DAt6Pf7jZjA""
  },
  {
    "{": ""      ""Video ID: uNQv5YSg_YA""
  },
  {
    "{": ""      ""Video ID: oSPqto796Lc""
  },
  {
    "{": ""      ""Video ID: YPvYCodKdSk""
  },
  {
    "{": ""      ""Video ID: p7HtgtzLo-E""
  },
  {
    "{": ""      ""Video ID: LK6_gr2ulHg""
  },
  {
    "{": ""      ""Video ID: 3MrKZVi04yU""
  },
  {
    "{": ""      ""Video ID: 0akLTXxpl60""
  },
  {
    "{": ""      ""Video ID: lq_gRMDR4Y0""
  },
  {
    "{": ""      ""Video ID: nwDzATryei8""
  },
  {
    "{": ""      ""Video ID: Vzb81oVEcpA""
  },
  {
    "{": ""      ""Video ID: FmKwlE3fO-Y""
  },
  {
    "{": ""      ""Video ID: 4k3UvFnirlk""
  },
  {
    "{": ""      ""Video ID: nNumEm2NzQA""
  },
  {
    "{": ""      ""Video ID: MrACUZjNtDA""
  },
  {
    "{": ""      ""Video ID: KsBLN4eP2Y8""
  },
  {
    "{": ""      ""Video ID: rcpaEXHzpiQ""
  },
  {
    "{": ""      ""Video ID: ovUJgm6FicI""
  },
  {
    "{": ""      ""Video ID: 1ptU2GzwOMs""
  },
  {
    "{": ""      ""Video ID: ExQfZC9E6j0""
  },
  {
    "{": ""      ""Video ID: LIIHNvt__34""
  },
  {
    "{": ""      ""Video ID: hhzlEX9GQAE""
  },
  {
    "{": ""      ""Video ID: wHJm0kO914Q""
  },
  {
    "{": ""      ""Video ID: GhKyD7kKlJg""
  },
  {
    "{": ""      ""Video ID: -3fDFSPSoyo""
  },
  {
    "{": ""      ""Video ID: t5LvylbVEE8""
  },
  {
    "{": ""      ""Video ID: ongBGCMyT5o""
  },
  {
    "{": ""      ""Video ID: vaCYEEO-58I""
  },
  {
    "{": ""      ""Video ID: GahDESc5zFw""
  },
  {
    "{": ""      ""Video ID: VmgEbRjdCmw""
  },
  {
    "{": ""      ""Video ID: nY2NXPl625A""
  },
  {
    "{": ""      ""Video ID: _FIh_ipMERs""
  },
  {
    "{": ""      ""Video ID: zJ6YiZgHei8""
  },
  {
    "{": ""      ""Video ID: yrGNNZnz8EI""
  },
  {
    "{": ""      ""Video ID: LbiHpDnpoRc""
  },
  {
    "{": ""      ""Video ID: U_vLTSWpQcY""
  },
  {
    "{": ""      ""Video ID: f0p8LepIuVM""
  },
  {
    "{": ""      ""Video ID: LnCjYagqtMo""
  },
  {
    "{": ""      ""Video ID: lkKbE9qCzQo""
  },
  {
    "{": ""      ""Video ID: cr7vG0pnZCc""
  },
  {
    "{": ""      ""Video ID: _yvRZoM-2r8""
  },
  {
    "{": ""      ""Video ID: hfXavRTM4Fg""
  },
  {
    "{": ""      ""Video ID: gAcxGD6-c-E""
  },
  {
    "{": ""      ""Video ID: 309MCU8TonE""
  },
  {
    "{": ""      ""Video ID: vVkFb26u9g8""
  },
  {
    "{": ""      ""Video ID: 7tABE4tAlrM""
  },
  {
    "{": ""      ""Video ID: rC720Cl3N-0""
  },
  {
    "{": ""      ""Video ID: lBZne09Gf5A""
  },
  {
    "{": ""      ""Video ID: 7_E4N5YIycI""
  },
  {
    "{": ""      ""Video ID: KeZB2EsPqGE""
  },
  {
    "{": ""      ""Video ID: SjUrib_Gh0Y""
  },
  {
    "{": ""      ""Video ID: _BVNN1wqw3k""
  },
  {
    "{": ""      ""Video ID: XmzailhVl-U""
  },
  {
    "{": ""      ""Video ID: u8PuLnZFz6Q""
  },
  {
    "{": ""      ""Video ID: BGHXksHIakw""
  },
  {
    "{": ""      ""Video ID: EBZ81hmZuNk""
  },
  {
    "{": ""      ""Video ID: 2Lk7ZPC4Z6M""
  },
  {
    "{": ""      ""Video ID: WhLaa5pNeok""
  },
  {
    "{": ""      ""Video ID: zlXQTfjAh-Y""
  },
  {
    "{": ""      ""Video ID: thWVIOKAv18""
  },
  {
    "{": ""      ""Video ID: K0nBNJM0fBo""
  },
  {
    "{": ""      ""Video ID: 6wztMqkWGnc""
  },
  {
    "{": ""      ""Video ID: ybRz91eimTg""
  },
  {
    "{": ""      ""Video ID: jiv0oy9JW7k""
  },
  {
    "{": ""      ""Video ID: lPx1ITNhdC8""
  },
  {
    "{": ""      ""Video ID: iyYeSn6bfus""
  },
  {
    "{": ""      ""Video ID: pMTDaVpBPR0""
  },
  {
    "{": ""      ""Video ID: 9pLZPw2vUMs""
  },
  {
    "{": ""      ""Video ID: _YwQdSS0S1M""
  },
  {
    "{": ""      ""Video ID: qQ3-Xa2Ivxg""
  },
  {
    "{": ""      ""Video ID: iH4jXpd09nQ""
  },
  {
    "{": ""      ""Video ID: Q8APprYhK2g""
  },
  {
    "{": ""      ""Video ID: HTkPYnNmOBM""
  },
  {
    "{": ""      ""Video ID: Xb0jJYYXjpQ""
  },
  {
    "{": ""      ""Video ID: 7NHDtTykjKU""
  },
  {
    "{": ""      ""Video ID: 9ru9bKzyAzY""
  },
  {
    "{": ""      ""Video ID: GbPetrK_6Lc""
  },
  {
    "{": ""      ""Video ID: GWtFofq3Ask""
  },
  {
    "{": ""      ""Video ID: dVMDqqNzryA""
  },
  {
    "{": ""      ""Video ID: KUBERI7umAU""
  },
  {
    "{": ""      ""Video ID: m5NrM7-r5sc""
  },
  {
    "{": ""      ""Video ID: KAclPkC4Mzg""
  },
  {
    "{": ""      ""Video ID: MhyyYefB4xg""
  },
  {
    "{": ""      ""Video ID: mrSgOfGD7CA""
  },
  {
    "{": ""      ""Video ID: G0ybKkxfB2o""
  },
  {
    "{": ""      ""Video ID: Sgveu4UNySI""
  },
  {
    "{": ""      ""Video ID: gX_B026yJSE""
  },
  {
    "{": ""      ""Video ID: oSPb-7S8-2o""
  },
  {
    "{": ""      ""Video ID: 8YVTNPP40ZY""
  },
  {
    "{": ""      ""Video ID: bo7mS0W0rgc""
  },
  {
    "{": ""      ""Video ID: Qx00Q_u8SbM""
  },
  {
    "{": ""      ""Video ID: -Md1JSB-IWc""
  },
  {
    "{": ""      ""Video ID: qw_CfGoN8bE""
  },
  {
    "{": ""      ""Video ID: pdP6sl2Zg2c""
  },
  {
    "{": ""      ""Video ID: Fq-JiWDOwB4""
  },
  {
    "{": ""      ""Video ID: NBSs5qzNq2Q""
  },
  {
    "{": ""      ""Video ID: S5VaUzbEl3Q""
  },
  {
    "{": ""      ""Video ID: Z0wn_PIolNE""
  },
  {
    "{": ""      ""Video ID: PV5a5d55Y-8""
  },
  {
    "{": ""      ""Video ID: ZsIUNWLaroM""
  },
  {
    "{": ""      ""Video ID: Hfe65WSONCw""
  },
  {
    "{": ""      ""Video ID: dWmG_I5rUXI""
  },
  {
    "{": ""      ""Video ID: F4_0cwDWRzo""
  },
  {
    "{": ""      ""Video ID: NqKk2T2FMqY""
  },
  {
    "{": ""      ""Video ID: CBtL3NIcAvU""
  },
  {
    "{": ""      ""Video ID: TSSwsPByGYE""
  },
  {
    "{": ""      ""Video ID: AsrDBTDmrBw""
  },
  {
    "{": ""      ""Video ID: t2rVMZBFa-U""
  },
  {
    "{": ""      ""Video ID: IUgFyy1lPTI""
  },
  {
    "{": ""      ""Video ID: 6J6dDXW8_TQ""
  },
  {
    "{": ""      ""Video ID: 8kg69IsdTFw""
  },
  {
    "{": ""      ""Video ID: 4ft9QapA9Xk""
  },
  {
    "{": ""      ""Video ID: tgCjT1lQRdQ""
  },
  {
    "{": ""      ""Video ID: isFh-niPHhQ""
  },
  {
    "{": ""      ""Video ID: _nJAB3yaumw""
  },
  {
    "{": ""      ""Video ID: PY2Ng8MYMnQ""
  },
  {
    "{": ""      ""Video ID: -W3y-rDepCc""
  },
  {
    "{": ""      ""Video ID: r31w3MnrldM""
  },
  {
    "{": ""      ""Video ID: UJjLuXwt3YU""
  },
  {
    "{": ""      ""Video ID: KfHwv9L41ZQ""
  },
  {
    "{": ""      ""Video ID: Lho0OyKy8JU""
  },
  {
    "{": ""      ""Video ID: 6YNt8NG6prc""
  },
  {
    "{": ""      ""Video ID: exRmYPZgnu8""
  },
  {
    "{": ""      ""Video ID: pvqNugxc0I8""
  },
  {
    "{": ""      ""Video ID: Bsghy35O_wY""
  },
  {
    "{": ""      ""Video ID: aqPDxyTI_xQ""
  },
  {
    "{": ""      ""Video ID: sfWONxylXmU""
  },
  {
    "{": ""      ""Video ID: ETzbAUpMii8""
  },
  {
    "{": ""      ""Video ID: QlQRt5an0tQ""
  },
  {
    "{": ""      ""Video ID: l--EmxXz4yA""
  },
  {
    "{": ""      ""Video ID: SpBTSBT_RW0""
  },
  {
    "{": ""      ""Video ID: vf0cTadzjDA""
  },
  {
    "{": ""      ""Video ID: IcLOgyjJEdk""
  },
  {
    "{": ""      ""Video ID: aa4EOnt4uOc""
  },
  {
    "{": ""      ""Video ID: 1G_6V8BDKMk""
  },
  {
    "{": ""      ""Video ID: zIz_ObG_tlo""
  },
  {
    "{": ""      ""Video ID: LWZ8hBWNHKs""
  },
  {
    "{": ""      ""Video ID: m44Xr448Mjs""
  },
  {
    "{": ""      ""Video ID: qIEtob9-IoY""
  },
  {
    "{": ""      ""Video ID: esCtQ2G3geo""
  },
  {
    "{": ""      ""Video ID: lldIEP7vLGU""
  },
  {
    "{": ""      ""Video ID: 04Qf90IpJpU""
  },
  {
    "{": ""      ""Video ID: s31nWSiminI""
  },
  {
    "{": ""      ""Video ID: l41Zf6pzDF8""
  },
  {
    "{": ""      ""Video ID: h0D-jtiSFCM""
  },
  {
    "{": ""      ""Video ID: qxwsi74tz3o""
  },
  {
    "{": ""      ""Video ID: c_e4G2To2ps""
  },
  {
    "{": ""      ""Video ID: T5WWdA1KgYM""
  },
  {
    "{": ""      ""Video ID: l4BNx8o2aeI""
  },
  {
    "{": ""      ""Video ID: LR19O7WaqTA""
  },
  {
    "{": ""      ""Video ID: iAkhpYOp7pE""
  },
  {
    "{": ""      ""Video ID: 3fqI5krjPFY""
  },
  {
    "{": ""      ""Video ID: YQa4PpIkOZU""
  },
  {
    "{": ""      ""Video ID: jk6ILZAaAMI""
  },
  {
    "{": ""      ""Video ID: XUuUAvoiTsI""
  },
  {
    "{": ""      ""Video ID: 6o3cVm9pqrw""
  },
  {
    "{": ""      ""Video ID: B8o7ptR4dnQ""
  },
  {
    "{": ""      ""Video ID: bosnjuVt3l8""
  },
  {
    "{": ""      ""Video ID: LTWjptNXa1Q""
  },
  {
    "{": ""      ""Video ID: yf7vVPaJsrE""
  },
  {
    "{": ""      ""Video ID: VWMHIej1bB0""
  },
  {
    "{": ""      ""Video ID: u-CLSHAaEgs""
  },
  {
    "{": ""      ""Video ID: 5b2mO1c9RKI""
  },
  {
    "{": ""      ""Video ID: 8-bMZ_clS4M""
  },
  {
    "{": ""      ""Video ID: B2Ih3IWrbgo""
  },
  {
    "{": ""      ""Video ID: 5kKnBJt4ePs""
  },
  {
    "{": ""      ""Video ID: FXOKI934BZU""
  },
  {
    "{": ""      ""Video ID: hUx3SHrh-G0""
  },
  {
    "{": ""      ""Video ID: rIndiifvkXg""
  },
  {
    "{": ""      ""Video ID: bw_ec7O9Vs0""
  },
  {
    "{": ""      ""Video ID: Y8a1YwEZFiQ""
  },
  {
    "{": ""      ""Video ID: R8VX5Zd4vcQ""
  },
  {
    "{": ""      ""Video ID: R5j2E5SEpuM""
  },
  {
    "{": ""      ""Video ID: IbasQ2D10u0""
  },
  {
    "{": ""      ""Video ID: _z36Ghqh-0A""
  },
  {
    "{": ""      ""Video ID: xv_Gu6ttqw8""
  },
  {
    "{": ""      ""Video ID: O5GeAJLxyzU""
  },
  {
    "{": ""      ""Video ID: F276pUaHMq0""
  },
  {
    "{": ""      ""Video ID: Q-9EOmyqqxA""
  },
  {
    "{": ""      ""Video ID: Lb7rTiP6dnE""
  },
  {
    "{": ""      ""Video ID: LeTFgFdIU2Y""
  },
  {
    "{": ""      ""Video ID: WWJ9uTEBZ9U""
  },
  {
    "{": ""      ""Video ID: MjKAIQntnsQ""
  },
  {
    "{": ""      ""Video ID: 3s3L9rp8zSE""
  },
  {
    "{": ""      ""Video ID: UbegH4HMafQ""
  },
  {
    "{": ""      ""Video ID: qUOItuKm5UE""
  },
  {
    "{": ""      ""Video ID: ZGrYndBurq8""
  },
  {
    "{": ""      ""Video ID: Gsh6JmaKJBA""
  },
  {
    "{": ""      ""Video ID: awgv62If1z4""
  },
  {
    "{": ""      ""Video ID: 3Vrge-8F6rw""
  },
  {
    "{": ""      ""Video ID: NpeIs5MFTYU""
  },
  {
    "{": ""      ""Video ID: BaI-9Hsi89I""
  },
  {
    "{": ""      ""Video ID: CB6_QMHf0Uk""
  },
  {
    "{": ""      ""Video ID: lHgUN5dUc9w""
  },
  {
    "{": ""      ""Video ID: RsV2oWL0bK0""
  },
  {
    "{": ""      ""Video ID: VAJgJg-rfJ8""
  },
  {
    "{": ""      ""Video ID: QavlsCL79k8""
  },
  {
    "{": ""      ""Video ID: 9O0KCfLqMZo""
  },
  {
    "{": ""      ""Video ID: 7P8DmDNqh9g""
  },
  {
    "{": ""      ""Video ID: rRmxB8j1niM""
  },
  {
    "{": ""      ""Video ID: L6Y_RtMGRoE""
  },
  {
    "{": ""      ""Video ID: qItN1REsxH4""
  },
  {
    "{": ""      ""Video ID: EWyQXH5D8PA""
  },
  {
    "{": ""      ""Video ID: 5s1ueuoYOSY""
  },
  {
    "{": ""      ""Video ID: GNgyThraJ8A""
  },
  {
    "{": ""      ""Video ID: AQpRC3VKUXo""
  },
  {
    "{": ""      ""Video ID: 2WdYt9VkVek""
  },
  {
    "{": ""      ""Video ID: 04TiiZV0FAA""
  },
  {
    "{": ""      ""Video ID: U0-ZVPffN40""
  },
  {
    "{": ""      ""Video ID: vyFNl47zaDU""
  },
  {
    "{": ""      ""Video ID: eMZex70tAJI""
  },
  {
    "{": ""      ""Video ID: XQzcLqblLUw""
  },
  {
    "{": ""      ""Video ID: FQsI9kmnLVU""
  },
  {
    "{": ""      ""Video ID: _A72m57Dsz4""
  },
  {
    "{": ""      ""Video ID: XWj086rdpxE""
  },
  {
    "{": ""      ""Video ID: vok7NLflAQM""
  },
  {
    "{": ""      ""Video ID: Ryrs3UVAQK0""
  },
  {
    "{": ""      ""Video ID: kEbvbul8iqQ""
  },
  {
    "{": ""      ""Video ID: zOocG_EzzbM""
  },
  {
    "{": ""      ""Video ID: kMP7aw8OflM""
  },
  {
    "{": ""      ""Video ID: j-HSuqbvvbw""
  },
  {
    "{": ""      ""Video ID: LELcpFEsrFc""
  },
  {
    "{": ""      ""Video ID: 4PctzLJ18Mg""
  },
  {
    "{": ""      ""Video ID: dhoG_heyv08""
  },
  {
    "{": ""      ""Video ID: 67yMasXc2FE""
  },
  {
    "{": ""      ""Video ID: 14tZRDdwggU""
  },
  {
    "{": ""      ""Video ID: KTi1OsEKRfU""
  },
  {
    "{": ""      ""Video ID: jf3tZCArF3k""
  },
  {
    "{": ""      ""Video ID: Lri1sqHpYAk""
  },
  {
    "{": ""      ""Video ID: rk6CDGA3RtY""
  },
  {
    "{": ""      ""Video ID: 70g5wU5wJf0""
  },
  {
    "{": ""      ""Video ID: Cc-jAeRvhdg""
  },
  {
    "{": ""      ""Video ID: uwq-ELljnao""
  },
  {
    "{": ""      ""Video ID: 6oAAtByRIQo""
  },
  {
    "{": ""      ""Video ID: IWTOrQCsLk8""
  },
  {
    "{": ""      ""Video ID: ILiT-cl6BD8""
  },
  {
    "{": ""      ""Video ID: 1AFkM809Gq8""
  },
  {
    "{": ""      ""Video ID: kSlt0_8HwMk""
  },
  {
    "{": ""      ""Video ID: MolT3LHPHAw""
  },
  {
    "{": ""      ""Video ID: UIx57sfxGCk""
  },
  {
    "{": ""      ""Video ID: XvNS2bfN_Zg""
  },
  {
    "{": ""      ""Video ID: hpLIY1XMkG8""
  },
  {
    "{": ""      ""Video ID: VYdaKhH8gzM""
  },
  {
    "{": ""      ""Video ID: z2xbGALQiM0""
  },
  {
    "{": ""      ""Video ID: zWbx_2gs1Sw""
  },
  {
    "{": ""      ""Video ID: -3VQAGDJML8""
  },
  {
    "{": ""      ""Video ID: A7Rc9o81uis""
  },
  {
    "{": ""      ""Video ID: 4dOvLIRSU_M""
  },
  {
    "{": ""      ""Video ID: rrsvAxH8brw""
  },
  {
    "{": ""      ""Video ID: DL1MYtvVye0""
  },
  {
    "{": ""      ""Video ID: ryN0WSDK7oA""
  },
  {
    "{": ""      ""Video ID: MtA2zlc24lY""
  },
  {
    "{": ""      ""Video ID: YOdjJMKET0A""
  },
  {
    "{": ""      ""Video ID: rjLuPAEAJJg""
  },
  {
    "{": ""      ""Video ID: NpkrVj-rhmg""
  },
  {
    "{": ""      ""Video ID: W6weNAh2UZE""
  },
  {
    "{": ""      ""Video ID: AKu7Qn-HQvk""
  },
  {
    "{": ""      ""Video ID: YQvAlGlPbxU""
  },
  {
    "{": ""      ""Video ID: adgte0BubaM""
  },
  {
    "{": ""      ""Video ID: hzueYX4KqVs""
  },
  {
    "{": ""      ""Video ID: u-OZbV3eJmE""
  },
  {
    "{": ""      ""Video ID: GYfNnlWeGic""
  },
  {
    "{": ""      ""Video ID: wNqJKIPy1BU""
  },
  {
    "{": ""      ""Video ID: VzUicyfMd5I""
  },
  {
    "{": ""      ""Video ID: MEo2GUM4SFI""
  },
  {
    "{": ""      ""Video ID: RukkWFZWECs""
  },
  {
    "{": ""      ""Video ID: dOW626xUWTs""
  },
  {
    "{": ""      ""Video ID: fbOC0uoKYtU""
  },
  {
    "{": ""      ""Video ID: n3REuen54jA""
  },
  {
    "{": ""      ""Video ID: wcuYWR-RWIU""
  },
  {
    "{": ""      ""Video ID: UuCHoC55EKM""
  },
  {
    "{": ""      ""Video ID: tazsCMtkxA8""
  },
  {
    "{": ""      ""Video ID: XgoNGgpQc6Y""
  },
  {
    "{": ""      ""Video ID: 3YvyBzkzpwA""
  },
  {
    "{": ""      ""Video ID: 9INufFwAiPE""
  },
  {
    "{": ""      ""Video ID: C2hKLbhvhns""
  },
  {
    "{": ""      ""Video ID: uK879xxF75I""
  },
  {
    "{": ""      ""Video ID: X1si2o4SSEI""
  },
  {
    "{": ""      ""Video ID: raxreyd8eyg""
  },
  {
    "{": ""      ""Video ID: Grxs4u4vTn4""
  },
  {
    "{": ""      ""Video ID: oNX7iXEr74U""
  },
  {
    "{": ""      ""Video ID: 02H0boY5W_w""
  },
  {
    "{": ""      ""Video ID: LH3t4_hmOtY""
  },
  {
    "{": ""      ""Video ID: 9sx-Ua93AUo""
  },
  {
    "{": ""      ""Video ID: BRWHAQYCDdA""
  },
  {
    "{": ""      ""Video ID: gcEqM8z1wgA""
  },
  {
    "{": ""      ""Video ID: j0PDGp1hL4w""
  },
  {
    "{": ""      ""Video ID: YzXTxGtgGJ8""
  },
  {
    "{": ""      ""Video ID: SGF0ko1DrUE""
  },
  {
    "{": ""      ""Video ID: bI_2RW2fyUA""
  },
  {
    "{": ""      ""Video ID: i0zFWZJJV7o""
  },
  {
    "{": ""      ""Video ID: nWk4JhIf8Bw""
  },
  {
    "{": ""      ""Video ID: L_1PiLvqLi8""
  },
  {
    "{": ""      ""Video ID: 50yRd7lNiD8""
  },
  {
    "{": ""      ""Video ID: NLYqpYPaNrE""
  },
  {
    "{": ""      ""Video ID: CkjeO_nUN9Y""
  },
  {
    "{": ""      ""Video ID: EbqK68yzTNc""
  },
  {
    "{": ""      ""Video ID: d5aayQz0sEw""
  },
  {
    "{": ""      ""Video ID: 2rqch9i8m1Y""
  },
  {
    "{": ""      ""Video ID: Pmoy0wN7g50""
  },
  {
    "{": ""      ""Video ID: GsT3_ZfaHxQ""
  },
  {
    "{": ""      ""Video ID: 5ys_o3Z-Cms""
  },
  {
    "{": ""      ""Video ID: Ar90_mMNsJ0""
  },
  {
    "{": ""      ""Video ID: weGB_Tvnd5E""
  },
  {
    "{": ""      ""Video ID: ZmrY9JAV044""
  },
  {
    "{": ""      ""Video ID: uYd1Sv7QinY""
  },
  {
    "{": ""      ""Video ID: t3wk03SeLTY""
  },
  {
    "{": ""      ""Video ID: g0b_lTEgICw""
  },
  {
    "{": ""      ""Video ID: eyAbo_mutNc""
  },
  {
    "{": ""      ""Video ID: q6AYhT8X7wE""
  },
  {
    "{": ""      ""Video ID: xWaBLGaTyTI""
  },
  {
    "{": ""      ""Video ID: Q5YP0tcn1WE""
  },
  {
    "{": ""      ""Video ID: bzz0QcBmbQU""
  },
  {
    "{": ""      ""Video ID: exWiVYbm_ZU""
  },
  {
    "{": ""      ""Video ID: kZE7Vauexh4""
  },
  {
    "{": ""      ""Video ID: uvdnxtpspL0""
  },
  {
    "{": ""      ""Video ID: oFjJ90B-Rcs""
  },
  {
    "{": ""      ""Video ID: KHAEZy1VIv0""
  },
  {
    "{": ""      ""Video ID: ieEFUjnwy00""
  },
  {
    "{": ""      ""Video ID: pezGrZQn3ZM""
  },
  {
    "{": ""      ""Video ID: VjfaLgkJUMg""
  },
  {
    "{": ""      ""Video ID: zySSH6KC-n8""
  },
  {
    "{": ""      ""Video ID: g-6Yl18XP74""
  },
  {
    "{": ""      ""Video ID: NQ74eKbWKX4""
  },
  {
    "{": ""      ""Video ID: XpbUsGINtCE""
  },
  {
    "{": ""      ""Video ID: wz_HXdfK13c""
  },
  {
    "{": ""      ""Video ID: 98Nyzs0btVw""
  },
  {
    "{": ""      ""Video ID: NPHIoFp2n3U""
  },
  {
    "{": ""      ""Video ID: hWau42p0tfk""
  },
  {
    "{": ""      ""Video ID: mtYSix9t0P4""
  },
  {
    "{": ""      ""Video ID: n4ccnEurTFU""
  },
  {
    "{": ""      ""Video ID: XHCzlBlkAr4""
  },
  {
    "{": ""      ""Video ID: EW9SI59mlzQ""
  },
  {
    "{": ""      ""Video ID: EUktQ59rx68""
  },
  {
    "{": ""      ""Video ID: j8zvV8e9yhk""
  },
  {
    "{": ""      ""Video ID: 8OW5oyWkybI""
  },
  {
    "{": ""      ""Video ID: D-xAXngf0Yk""
  },
  {
    "{": ""      ""Video ID: 0ihfKQHvlpY""
  },
  {
    "{": ""      ""Video ID: DgYxYTOAC0w""
  },
  {
    "{": ""      ""Video ID: E2fVIKBNtLY""
  },
  {
    "{": ""      ""Video ID: TQ44Fw0M6UQ""
  },
  {
    "{": ""      ""Video ID: skT1h1wkOHI""
  },
  {
    "{": ""      ""Video ID: zT6vx8h0ddI""
  },
  {
    "{": ""      ""Video ID: ZLQEX2kk49s""
  },
  {
    "{": ""      ""Video ID: PiuqcBtMc8Y""
  },
  {
    "{": ""      ""Video ID: yKUG5p1juXY""
  },
  {
    "{": ""      ""Video ID: uwLZoPYc1bQ""
  },
  {
    "{": ""      ""Video ID: amLikeyn6zQ""
  },
  {
    "{": ""      ""Video ID: o-fL-daPwGE""
  },
  {
    "{": ""      ""Video ID: DhhOcaBFJjs""
  },
  {
    "{": ""      ""Video ID: y87-UkJh9kU""
  },
  {
    "{": ""      ""Video ID: HGcEiBQwErc""
  },
  {
    "{": ""      ""Video ID: ivdJuwyzSwg""
  },
  {
    "{": ""      ""Video ID: X85eRqtOKaU""
  },
  {
    "{": ""      ""Video ID: BaN2ttSW_XM""
  },
  {
    "{": ""      ""Video ID: p5_y8r1y3mY""
  },
  {
    "{": ""      ""Video ID: oHsEhR49lE8""
  },
  {
    "{": ""      ""Video ID: 4HbVEtd7kM0""
  },
  {
    "{": ""      ""Video ID: fx3SrhmqOtQ""
  },
  {
    "{": ""      ""Video ID: b8dIxHSxeUk""
  },
  {
    "{": ""      ""Video ID: s4sMSxHbyR4""
  },
  {
    "{": ""      ""Video ID: bB2hzW1T9XA""
  },
  {
    "{": ""      ""Video ID: ZK8KVYgg3BA""
  },
  {
    "{": ""      ""Video ID: QDpXjkcaN0U""
  },
  {
    "{": ""      ""Video ID: t_yWlVEkOeY""
  },
  {
    "{": ""      ""Video ID: nJgRQ-LPsVA""
  },
  {
    "{": ""      ""Video ID: T5UC3wMC4_8""
  },
  {
    "{": ""      ""Video ID: 8NOfL3o8908""
  },
  {
    "{": ""      ""Video ID: XMAhJwkt9FM""
  },
  {
    "{": ""      ""Video ID: UDVOGqUvkmk""
  },
  {
    "{": ""      ""Video ID: mxAhqIZdMpI""
  },
  {
    "{": ""      ""Video ID: 8otioaz12gE""
  },
  {
    "{": ""      ""Video ID: iqhBJnpxNvE""
  },
  {
    "{": ""      ""Video ID: Ls3PL_66u8Q""
  },
  {
    "{": ""      ""Video ID: yO72seZKgu0""
  },
  {
    "{": ""      ""Video ID: WiWI-6Sm8bk""
  },
  {
    "{": ""      ""Video ID: RJQ2jJaKZo4""
  },
  {
    "{": ""      ""Video ID: 4BQx_EDdT8M""
  },
  {
    "{": ""      ""Video ID: hAQSkw_rj8w""
  },
  {
    "{": ""      ""Video ID: EHvrFClZeoM""
  },
  {
    "{": ""      ""Video ID: jCKexTKlmnc""
  },
  {
    "{": ""      ""Video ID: zsLKtfv6wE8""
  },
  {
    "{": ""      ""Video ID: CrKMErJS7SU""
  },
  {
    "{": ""      ""Video ID: -CgNrVGZ7yg""
  },
  {
    "{": ""      ""Video ID: a2XGq8f_zks""
  },
  {
    "{": ""      ""Video ID: qOtl8Qv0jwQ""
  },
  {
    "{": ""      ""Video ID: jqjvJ_V1liw""
  },
  {
    "{": ""      ""Video ID: X28PW6jx2yY""
  },
  {
    "{": ""      ""Video ID: af2bs4gF1L0""
  },
  {
    "{": ""      ""Video ID: FM-SW1TeHe0""
  },
  {
    "{": ""      ""Video ID: tYfz5e6MNUM""
  },
  {
    "{": ""      ""Video ID: 4j8EowdLA3I""
  },
  {
    "{": ""      ""Video ID: 66E_gq-OGto""
  },
  {
    "{": ""      ""Video ID: 0RSNTaR7GUc""
  },
  {
    "{": ""      ""Video ID: YZdTV54-vto""
  },
  {
    "{": ""      ""Video ID: uNa9YmZPDlA""
  },
  {
    "{": ""      ""Video ID: Kyd5OJ8Hm14""
  },
  {
    "{": ""      ""Video ID: 1Of3rxFXOSA""
  },
  {
    "{": ""      ""Video ID: 37AQCFvfKjc""
  },
  {
    "{": ""      ""Video ID: ynF0Bi_F2Rc""
  },
  {
    "{": ""      ""Video ID: I8V9zf3iMpQ""
  },
  {
    "{": ""      ""Video ID: 7bQtEbzlHeE""
  },
  {
    "{": ""      ""Video ID: y-C6MqXw4HQ""
  },
  {
    "{": ""      ""Video ID: XT9aRRHN4E0""
  },
  {
    "{": ""      ""Video ID: InLsspo8BZs""
  },
  {
    "{": ""      ""Video ID: -MuZPnLxKig""
  },
  {
    "{": ""      ""Video ID: WC8OzCL0N3E""
  },
  {
    "{": ""      ""Video ID: 63CRFi8fl78""
  },
  {
    "{": ""      ""Video ID: Os6AXn9q7mM""
  },
  {
    "{": ""      ""Video ID: NwAYZDlmhvU""
  },
  {
    "{": ""      ""Video ID: 0iC4B9Alaek""
  },
  {
    "{": ""      ""Video ID: vvU0olb86kw""
  },
  {
    "{": ""      ""Video ID: Oo5T74X3VEU""
  },
  {
    "{": ""      ""Video ID: ycAUfhgIabI""
  },
  {
    "{": ""      ""Video ID: 1nnL2p061_0""
  },
  {
    "{": ""      ""Video ID: YEElydQ5mw0""
  },
  {
    "{": ""      ""Video ID: Nr3ECpR4HhM""
  },
  {
    "{": ""      ""Video ID: 9LGle8L2jcA""
  },
  {
    "{": ""      ""Video ID: Vkt9heaAuaM""
  },
  {
    "{": ""      ""Video ID: GSwGPBHwsRQ""
  },
  {
    "{": ""      ""Video ID: lKjAS6oYNyk""
  },
  {
    "{": ""      ""Video ID: wCAC7lWwUw0""
  },
  {
    "{": ""      ""Video ID: gG6QMJ3rvrY""
  },
  {
    "{": ""      ""Video ID: eZGh-y0kkT8""
  },
  {
    "{": ""      ""Video ID: MpkBjOUTOHA""
  },
  {
    "{": ""      ""Video ID: pxTdMBE1oak""
  },
  {
    "{": ""      ""Video ID: wm4d_EiC4rQ""
  },
  {
    "{": ""      ""Video ID: HGSJYsssCLQ""
  },
  {
    "{": ""      ""Video ID: uaT3ZgKcLS8""
  },
  {
    "{": ""      ""Video ID: TB4YyV0kzKI""
  },
  {
    "{": ""      ""Video ID: k3rehC-Borw""
  },
  {
    "{": ""      ""Video ID: eB39GJVQWVY""
  },
  {
    "{": ""      ""Video ID: BojbqCQUCxw""
  },
  {
    "{": ""      ""Video ID: CL0BYnu7-Fo""
  },
  {
    "{": ""      ""Video ID: L2pFqSjo6Dg""
  },
  {
    "{": ""      ""Video ID: XakmuUfHTcI""
  },
  {
    "{": ""      ""Video ID: amut2GKYgJ0""
  },
  {
    "{": ""      ""Video ID: KlLUXHLsq50""
  },
  {
    "{": ""      ""Video ID: YVU8ALzHa9g""
  },
  {
    "{": ""      ""Video ID: HicElm2PIGQ""
  },
  {
    "{": ""      ""Video ID: eaDfAEigzTU""
  },
  {
    "{": ""      ""Video ID: 3u5svpwujyo""
  },
  {
    "{": ""      ""Video ID: AHPRRZoHeBA""
  },
  {
    "{": ""      ""Video ID: uPphoPNWR8s""
  },
  {
    "{": ""      ""Video ID: CO-ftWVKvog""
  },
  {
    "{": ""      ""Video ID: xAEMVwb6Y5k""
  },
  {
    "{": ""      ""Video ID: INEM20WOej0""
  },
  {
    "{": ""      ""Video ID: Z72_-yAPhlc""
  },
  {
    "{": ""      ""Video ID: iZslZK_Brbw""
  },
  {
    "{": ""      ""Video ID: 9ciH3RSSO1g""
  },
  {
    "{": ""      ""Video ID: 346-B080N28""
  },
  {
    "{": ""      ""Video ID: _4SHP4igfbI""
  },
  {
    "{": ""      ""Video ID: azbolVrSOO0""
  },
  {
    "{": ""      ""Video ID: JGFMLDg7gm8""
  },
  {
    "{": ""      ""Video ID: -fePOPgpJzk""
  },
  {
    "{": ""      ""Video ID: RYfvPV6PGfM""
  },
  {
    "{": ""      ""Video ID: y-qnq4L0RpI""
  },
  {
    "{": ""      ""Video ID: BRXfpIhEF6s""
  },
  {
    "{": ""      ""Video ID: QoNWKyiOIFE""
  },
  {
    "{": ""      ""Video ID: xIBAjGGXX2A""
  },
  {
    "{": ""      ""Video ID: 0MLxnLgVKto""
  },
  {
    "{": ""      ""Video ID: D4xPnHnnJ6o""
  },
  {
    "{": ""      ""Video ID: HMajrjJ5Q5I""
  },
  {
    "{": ""      ""Video ID: ZZFn6VaHurU""
  },
  {
    "{": ""      ""Video ID: -oaD9oM4xQo""
  },
  {
    "{": ""      ""Video ID: _YnurFvWtQQ""
  },
  {
    "{": ""      ""Video ID: 3TeQgA9EzWw""
  },
  {
    "{": ""      ""Video ID: TsQ25Iobf5k""
  },
  {
    "{": ""      ""Video ID: 7-W4GWjN2kg""
  },
  {
    "{": ""      ""Video ID: 5BP0Otf2Qd4""
  },
  {
    "{": ""      ""Video ID: oPYwRcgYU_g""
  },
  {
    "{": ""      ""Video ID: j4ybRLYTSwc""
  },
  {
    "{": ""      ""Video ID: AE9wPOFAfGY""
  },
  {
    "{": ""      ""Video ID: 9lXSZQZlpbg""
  },
  {
    "{": ""      ""Video ID: WaCaiiMFLv0""
  },
  {
    "{": ""      ""Video ID: gYaybeSkdpU""
  },
  {
    "{": ""      ""Video ID: h5cnU_rIpCM""
  },
  {
    "{": ""      ""Video ID: oCgx4pvvkbk""
  },
  {
    "{": ""      ""Video ID: TlL62xGA2qs""
  },
  {
    "{": ""      ""Video ID: zDlzQR8LVDk""
  },
  {
    "{": ""      ""Video ID: 9nOGnY0n0aQ""
  },
  {
    "{": ""      ""Video ID: r4nWeUr3ROw""
  },
  {
    "{": ""      ""Video ID: GIopxOEKXt0""
  },
  {
    "{": ""      ""Video ID: 1rJApkVuuJE""
  },
  {
    "{": ""      ""Video ID: hS65KMOPB4I""
  },
  {
    "{": ""      ""Video ID: uUbooZFMvoQ""
  },
  {
    "{": ""      ""Video ID: _nPky2vpM-0""
  },
  {
    "{": ""      ""Video ID: _BGyWYtee18""
  },
  {
    "{": ""      ""Video ID: itN3pzbs5-4""
  },
  {
    "{": ""      ""Video ID: APESLPdb5uE""
  },
  {
    "{": ""      ""Video ID: 0Z9_rzYrFhI""
  },
  {
    "{": ""      ""Video ID: pT8EiFmBg6s""
  },
  {
    "{": ""      ""Video ID: BdKzGb_dUzQ""
  },
  {
    "{": ""      ""Video ID: 2YcXgvVkEWQ""
  },
  {
    "{": ""      ""Video ID: 57dXFXRDRJc""
  },
  {
    "{": ""      ""Video ID: Qjp2JK2b-sM""
  },
  {
    "{": ""      ""Video ID: xQaNgG6tyMU""
  },
  {
    "{": ""      ""Video ID: WHzOWTSQgr8""
  },
  {
    "{": ""      ""Video ID: SG5u04Gbg0A""
  },
  {
    "{": ""      ""Video ID: yzhhtmu4tLY""
  },
  {
    "{": ""      ""Video ID: FVvwcgQpyqU""
  },
  {
    "{": ""      ""Video ID: VeXnkh64Qkw""
  },
  {
    "{": ""      ""Video ID: r6nRIIYMHjE""
  },
  {
    "{": ""      ""Video ID: MIqQqaP2yTo""
  },
  {
    "{": ""      ""Video ID: QzDha6Yrfuk""
  },
  {
    "{": ""      ""Video ID: NE2XLbVcLxI""
  },
  {
    "{": ""      ""Video ID: nmO9J3WO-9Y""
  },
  {
    "{": ""      ""Video ID: zA8WA16YzTI""
  },
  {
    "{": ""      ""Video ID: k3SPGQnjG9Y""
  },
  {
    "{": ""      ""Video ID: 3oRa-VJC67Y""
  },
  {
    "{": ""      ""Video ID: oooyweDGrVk""
  },
  {
    "{": ""      ""Video ID: -az_Ihpukec""
  },
  {
    "{": ""      ""Video ID: rkOJm_ic3s0""
  },
  {
    "{": ""      ""Video ID: bRdS_T9Hp3g""
  },
  {
    "{": ""      ""Video ID: hVFJ1uzgPS4""
  },
  {
    "{": ""      ""Video ID: -CONwFr-Hww""
  },
  {
    "{": ""      ""Video ID: W2PFm6LkrcA""
  },
  {
    "{": ""      ""Video ID: kXcCtXTFjzI""
  },
  {
    "{": ""      ""Video ID: XQrzq8RoARk""
  },
  {
    "{": ""      ""Video ID: 8KRWRnlP3-8""
  },
  {
    "{": ""      ""Video ID: CFVeYDRwyMw""
  },
  {
    "{": ""      ""Video ID: RBwTPvpAy98""
  },
  {
    "{": ""      ""Video ID: -yqTW4KefnY""
  },
  {
    "{": ""      ""Video ID: U2eaCFnfQ1k""
  },
  {
    "{": ""      ""Video ID: DCBwnhhK3Sg""
  },
  {
    "{": ""      ""Video ID: faewHOiSX6I""
  },
  {
    "{": ""      ""Video ID: dAV3FhYzilE""
  },
  {
    "{": ""      ""Video ID: vxHuby0Dh-0""
  },
  {
    "{": ""      ""Video ID: mOdfM4XV2lo""
  },
  {
    "{": ""      ""Video ID: AEGi8iS01B8""
  },
  {
    "{": ""      ""Video ID: g6ahxjQ5ZU0""
  },
  {
    "{": ""      ""Video ID: y8ue4n3wbkw""
  },
  {
    "{": ""      ""Video ID: I2tc61M1iEg""
  },
  {
    "{": ""      ""Video ID: ga2Z5eryZYE""
  },
  {
    "{": ""      ""Video ID: VkRx-PLT_rY""
  },
  {
    "{": ""      ""Video ID: 8c9E1swx_xA""
  },
  {
    "{": ""      ""Video ID: b4CwrsBzWn0""
  },
  {
    "{": ""      ""Video ID: 2GnZ1n7no3M""
  },
  {
    "{": ""      ""Video ID: 0XgmrMZ0h54""
  },
  {
    "{": ""      ""Video ID: dbSek274iIY""
  },
  {
    "{": ""      ""Video ID: adadYN2IHPU""
  },
  {
    "{": ""      ""Video ID: 2_vpEyE6rug""
  },
  {
    "{": ""      ""Video ID: 2ElPSalb-Z8""
  },
  {
    "{": ""      ""Video ID: HqY5OpiVxdM""
  },
  {
    "{": ""      ""Video ID: syDjYGHQqyc""
  },
  {
    "{": ""      ""Video ID: uXYeKKcbdLc""
  },
  {
    "{": ""      ""Video ID: 0krnQ3G_IVc""
  },
  {
    "{": ""      ""Video ID: T1lKtgokAaw""
  },
  {
    "{": ""      ""Video ID: eLoQteiJNOU""
  },
  {
    "{": ""      ""Video ID: E_k7wKHLzsk""
  },
  {
    "{": ""      ""Video ID: rJlUfXwUG24""
  },
  {
    "{": ""      ""Video ID: xsXHcg7EWu0""
  },
  {
    "{": ""      ""Video ID: TVPm9TXvbw8""
  },
  {
    "{": ""      ""Video ID: dqKaU0aFW40""
  },
  {
    "{": ""      ""Video ID: acaMWkj5MfY""
  },
  {
    "{": ""      ""Video ID: NIeAothI8GE""
  },
  {
    "{": ""      ""Video ID: et91CIaNhWc""
  },
  {
    "{": ""      ""Video ID: yGYf4fEFS3g""
  },
  {
    "{": ""      ""Video ID: 5QPA1dxpw9k""
  },
  {
    "{": ""      ""Video ID: vknjU1-uWG8""
  },
  {
    "{": ""      ""Video ID: 0KDR5XBCZG4""
  },
  {
    "{": ""      ""Video ID: XUn8HH_V0sk""
  },
  {
    "{": ""      ""Video ID: 6Xt9KcR28Q4""
  },
  {
    "{": ""      ""Video ID: XdJ3ks1h25A""
  },
  {
    "{": ""      ""Video ID: uoHp_igk1Gk""
  },
  {
    "{": ""      ""Video ID: 5uso31yzrLU""
  },
  {
    "{": ""      ""Video ID: BRgJxf0p3Ic""
  },
  {
    "{": ""      ""Video ID: ARBeZ9jtCaE""
  },
  {
    "{": ""      ""Video ID: TPjHhTxq0wA""
  },
  {
    "{": ""      ""Video ID: sMtpFHqVJDo""
  },
  {
    "{": ""      ""Video ID: 3ZCwA7-0M4k""
  },
  {
    "{": ""      ""Video ID: qLnT-HolC9w""
  },
  {
    "{": ""      ""Video ID: 3VPk8RAdV98""
  },
  {
    "{": ""      ""Video ID: 92gL3u3ckyw""
  },
  {
    "{": ""      ""Video ID: V1S9_iLCVTM""
  },
  {
    "{": ""      ""Video ID: ZxbxA_jlKy0""
  },
  {
    "{": ""      ""Video ID: BcuN-yce1m4""
  },
  {
    "{": ""      ""Video ID: ypzOyIOULOU""
  },
  {
    "{": ""      ""Video ID: tD04jTanGUg""
  },
  {
    "{": ""      ""Video ID: D3fiIyh771w""
  },
  {
    "{": ""      ""Video ID: 2CawSyN6ky4""
  },
  {
    "{": ""      ""Video ID: pwjapvApwmM""
  },
  {
    "{": ""      ""Video ID: aSTjk15vSbA""
  },
  {
    "{": ""      ""Video ID: M6bnp-evhR8""
  },
  {
    "{": ""      ""Video ID: mxNOYHNkiZs""
  },
  {
    "{": ""      ""Video ID: -eYetOXPsT8""
  },
  {
    "{": ""      ""Video ID: rPY_1pHy0u8""
  },
  {
    "{": ""      ""Video ID: _ILQAsTh--w""
  },
  {
    "{": ""      ""Video ID: 7SO1zpsMrHw""
  },
  {
    "{": ""      ""Video ID: XNsHE7dX5cY""
  },
  {
    "{": ""      ""Video ID: JWVXlV5WoH0""
  },
  {
    "{": ""      ""Video ID: Pbt9QNarEbk""
  },
  {
    "{": ""      ""Video ID: ZiQVCPTa0ys""
  },
  {
    "{": ""      ""Video ID: go8mjvXWSc4""
  },
  {
    "{": ""      ""Video ID: 8KtxM34WnDg""
  },
  {
    "{": ""      ""Video ID: xW-VkFNEQkM""
  },
  {
    "{": ""      ""Video ID: p7rnjXrwiaE""
  },
  {
    "{": ""      ""Video ID: Au6LFZGs2Ic""
  },
  {
    "{": ""      ""Video ID: So6XjSV6-kE""
  },
  {
    "{": ""      ""Video ID: Ne5qQcW4W0c""
  },
  {
    "{": ""      ""Video ID: bge6a0oImGM""
  },
  {
    "{": ""      ""Video ID: vW2Y8Zudia8""
  },
  {
    "{": ""      ""Video ID: o97YruBgg6g""
  },
  {
    "{": ""      ""Video ID: 8OEhGOaojVQ""
  },
  {
    "{": ""      ""Video ID: jlvd3GBmbNU""
  },
  {
    "{": ""      ""Video ID: 7uqGQS4bDK0""
  },
  {
    "{": ""      ""Video ID: I7X4LV97FVY""
  },
  {
    "{": ""      ""Video ID: wd8EV0tb1SY""
  },
  {
    "{": ""      ""Video ID: t7fnlpqXzgE""
  },
  {
    "{": ""      ""Video ID: VbSWzK4nKQA""
  },
  {
    "{": ""      ""Video ID: arEjv6NaXHI""
  },
  {
    "{": ""      ""Video ID: 1KMwBtR-yGQ""
  },
  {
    "{": ""      ""Video ID: 4XKGTMU0Ceo""
  },
  {
    "{": ""      ""Video ID: Qti9Md1OngU""
  },
  {
    "{": ""      ""Video ID: 1yZA4CkEbjY""
  },
  {
    "{": ""      ""Video ID: LtrJG2rUSLA""
  },
  {
    "{": ""      ""Video ID: NfUzKvrz4Xg""
  },
  {
    "{": ""      ""Video ID: Vn4esPALgB4""
  },
  {
    "{": ""      ""Video ID: vfoIEWx1cKY""
  },
  {
    "{": ""      ""Video ID: k971Y4lcFT4""
  },
  {
    "{": ""      ""Video ID: 6PhfsXAdQIQ""
  },
  {
    "{": ""      ""Video ID: kWPaUIk37bY""
  },
  {
    "{": ""      ""Video ID: HNXQN0OtgIw""
  },
  {
    "{": ""      ""Video ID: K2FCF5ptuRE""
  },
  {
    "{": ""      ""Video ID: MjXJl0l2viA""
  },
  {
    "{": ""      ""Video ID: S69CP-FnnmU""
  },
  {
    "{": ""      ""Video ID: JAdTv7gx9EQ""
  },
  {
    "{": ""      ""Video ID: F8t54xXvLIo""
  },
  {
    "{": ""      ""Video ID: CFgA49tZPSo""
  },
  {
    "{": ""      ""Video ID: CgeJ-Y__dCI""
  },
  {
    "{": ""      ""Video ID: Dj0hrVUKCDw""
  },
  {
    "{": ""      ""Video ID: ngLIsKlfr8U""
  },
  {
    "{": ""      ""Video ID: P-ckYhRqYSw""
  },
  {
    "{": ""      ""Video ID: k8aRMD8GaAA""
  },
  {
    "{": ""      ""Video ID: zrYcpIh0GME""
  },
  {
    "{": ""      ""Video ID: dPwKRUBjUMk""
  },
  {
    "{": ""      ""Video ID: KGpE3V8mXCU""
  },
  {
    "{": ""      ""Video ID: YhKI4AlBjzk""
  },
  {
    "{": ""      ""Video ID: k_5v4aTiS1M""
  },
  {
    "{": ""      ""Video ID: IYNLgflvn-E""
  },
  {
    "{": ""      ""Video ID: y3NRLtVV-As""
  },
  {
    "{": ""      ""Video ID: WJzMSS6hdUc""
  },
  {
    "{": ""      ""Video ID: 11awJZxHuz0""
  },
  {
    "{": ""      ""Video ID: q5oMw2mC7EE""
  },
  {
    "{": ""      ""Video ID: BAUGVqV88Yk""
  },
  {
    "{": ""      ""Video ID: GygjY0H8BMI""
  },
  {
    "{": ""      ""Video ID: vb-1WJ3mliY""
  },
  {
    "{": ""      ""Video ID: NDUuHOzcBt0""
  },
  {
    "{": ""      ""Video ID: vrj4Q_5Qzj0""
  },
  {
    "{": ""      ""Video ID: kcShah5tFW4""
  },
  {
    "{": ""      ""Video ID: P8QyEKrV_6o""
  },
  {
    "{": ""      ""Video ID: mWaBkSZaUYE""
  },
  {
    "{": ""      ""Video ID: qVGE488nNcs""
  },
  {
    "{": ""      ""Video ID: r71av-sl9ng""
  },
  {
    "{": ""      ""Video ID: XvXbVcAl30c""
  },
  {
    "{": ""      ""Video ID: -ffyod5Wwzc""
  },
  {
    "{": ""      ""Video ID: j6KIHrynvU4""
  },
  {
    "{": ""      ""Video ID: OAL6xk1QD_Q""
  },
  {
    "{": ""      ""Video ID: JGoucViSFz0""
  },
  {
    "{": ""      ""Video ID: JdpyuStEtps""
  },
  {
    "{": ""      ""Video ID: kncnk4ABo-E""
  },
  {
    "{": ""      ""Video ID: ruBkQR_Cgf0""
  },
  {
    "{": ""      ""Video ID: NlR1UIJOO7k""
  },
  {
    "{": ""      ""Video ID: KuD3bfhC6ek""
  },
  {
    "{": ""      ""Video ID: IhLiiIDLN4U""
  },
  {
    "{": ""      ""Video ID: VekF8njQhlI""
  },
  {
    "{": ""      ""Video ID: DqKEbo0zahk""
  },
  {
    "{": ""      ""Video ID: HEZFB4wMpEo""
  },
  {
    "{": ""      ""Video ID: YyIaEO-lTuE""
  },
  {
    "{": ""      ""Video ID: aB-EZjThcWs""
  },
  {
    "{": ""      ""Video ID: FRZ7drWLUx4""
  },
  {
    "{": ""      ""Video ID: mmIuW6XfQrQ""
  },
  {
    "{": ""      ""Video ID: tCS0plZ3l8c""
  },
  {
    "{": ""      ""Video ID: 8nweC-a2FZY""
  },
  {
    "{": ""      ""Video ID: Iw114M4MqwM""
  },
  {
    "{": ""      ""Video ID: 6a4HPuyQwWQ""
  },
  {
    "{": ""      ""Video ID: UCGvv91wEf8""
  },
  {
    "{": ""      ""Video ID: Wx7IyKIMxUE""
  },
  {
    "{": ""      ""Video ID: UXcBg9btaFE""
  },
  {
    "{": ""      ""Video ID: GSaOaWd5asA""
  },
  {
    "{": ""      ""Video ID: 3h-kA4CyJgk""
  },
  {
    "{": ""      ""Video ID: C1I0AwnOI6Y""
  },
  {
    "{": ""      ""Video ID: XDyheKhwWf8""
  },
  {
    "{": ""      ""Video ID: cvWFOvGfbH8""
  },
  {
    "{": ""      ""Video ID: Wiqm_5-RqiQ""
  },
  {
    "{": ""      ""Video ID: ENjiQdDNEYQ""
  },
  {
    "{": ""      ""Video ID: 2J4lQ2VOuvs""
  },
  {
    "{": ""      ""Video ID: jr-fn1SwtNg""
  },
  {
    "{": ""      ""Video ID: yPNKskTd6pQ""
  },
  {
    "{": ""      ""Video ID: hQzzS86SmRc""
  },
  {
    "{": ""      ""Video ID: lmo_GAfGU8M""
  },
  {
    "{": ""      ""Video ID: eezrxdOo5IY""
  },
  {
    "{": ""      ""Video ID: fvdfATDJKvM""
  },
  {
    "{": ""      ""Video ID: n9Xkh9wKqn8""
  },
  {
    "{": ""      ""Video ID: 2gmmKemd2-Q""
  },
  {
    "{": ""      ""Video ID: SNmHgMYrDFo""
  },
  {
    "{": ""      ""Video ID: h5zOu0UFXC4""
  },
  {
    "{": ""      ""Video ID: GS24miW6jQc""
  },
  {
    "{": ""      ""Video ID: evKbgl5LFHY""
  },
  {
    "{": ""      ""Video ID: UdJ84tr-64Q""
  },
  {
    "{": ""      ""Video ID: wInnNbRa7qM""
  },
  {
    "{": ""      ""Video ID: y0EBAOEqaeI""
  },
  {
    "{": ""      ""Video ID: MhhVgVzFZDo""
  },
  {
    "{": ""      ""Video ID: ueZs8puIvkg""
  },
  {
    "{": ""      ""Video ID: DVRQnXse1MM""
  },
  {
    "{": ""      ""Video ID: MKOhHYXDD20""
  },
  {
    "{": ""      ""Video ID: IEFwFWaZzHQ""
  },
  {
    "{": ""      ""Video ID: LtxeypCaVfI""
  },
  {
    "{": ""      ""Video ID: cxvZdGShDW8""
  },
  {
    "{": ""      ""Video ID: ziHZPDRS_NQ""
  },
  {
    "{": ""      ""Video ID: FaIf28f5LoQ""
  },
  {
    "{": ""      ""Video ID: IqgYtvQdpEM""
  },
  {
    "{": ""      ""Video ID: G-ZHAZv8Xk4""
  },
  {
    "{": ""      ""Video ID: iaBKGoasjGI""
  },
  {
    "{": ""      ""Video ID: vgiRdJ1tvoI""
  },
  {
    "{": ""      ""Video ID: r8_51g448hw""
  },
  {
    "{": ""      ""Video ID: ygJrWqaHqQ8""
  },
  {
    "{": ""      ""Video ID: 8NZVWGRYcIM""
  },
  {
    "{": ""      ""Video ID: yAmXZPuS7L0""
  },
  {
    "{": ""      ""Video ID: peR8Hs9s_wY""
  },
  {
    "{": ""      ""Video ID: lEhEAnc5wYk""
  },
  {
    "{": ""      ""Video ID: 6NPg20GdNxk""
  },
  {
    "{": ""      ""Video ID: fcfJVExb1NI""
  },
  {
    "{": ""      ""Video ID: TaDuA6AhVkw""
  },
  {
    "{": ""      ""Video ID: cRz8JDO7oXs""
  },
  {
    "{": ""      ""Video ID: gH_J28JplJY""
  },
  {
    "{": ""      ""Video ID: 9y6NniSreMc""
  },
  {
    "{": ""      ""Video ID: dbcEbidQdVI""
  },
  {
    "{": ""      ""Video ID: opqtpNT1Hdo""
  },
  {
    "{": ""      ""Video ID: 7oFcEiKNSEk""
  },
  {
    "{": ""      ""Video ID: uppoGphvXf8""
  },
  {
    "{": ""      ""Video ID: 9O2atpo1RXY""
  },
  {
    "{": ""      ""Video ID: HmbGoxIDJnA""
  },
  {
    "{": ""      ""Video ID: MS2ortKnA2c""
  },
  {
    "{": ""      ""Video ID: ZjtUzAp2ED0""
  },
  {
    "{": ""      ""Video ID: cUrYIqk9YaI""
  },
  {
    "{": ""      ""Video ID: ryrqlUqmPJY""
  },
  {
    "{": ""      ""Video ID: mpo802OkHOE""
  },
  {
    "{": ""      ""Video ID: STjAkPW89EE""
  },
  {
    "{": ""      ""Video ID: U1OvsK0QlD8""
  },
  {
    "{": ""      ""Video ID: cTgssKkXh_Y""
  },
  {
    "{": ""      ""Video ID: 6tpD8rxnHtY""
  },
  {
    "{": ""      ""Video ID: rNofmmV6aNo""
  },
  {
    "{": ""      ""Video ID: KVDlKgnp9ps""
  },
  {
    "{": ""      ""Video ID: CMRY4ouxt8s""
  },
  {
    "{": ""      ""Video ID: 1cIE0NNwQyc""
  },
  {
    "{": ""      ""Video ID: 9Tt7Phq6Te8""
  },
  {
    "{": ""      ""Video ID: GTLJKl0TWrU""
  },
  {
    "{": ""      ""Video ID: AVpktlo8Ins""
  },
  {
    "{": ""      ""Video ID: S8dAziFqZog""
  },
  {
    "{": ""      ""Video ID: 7SsBq_Exxfc""
  },
  {
    "{": ""      ""Video ID: W9OrquGcR6E""
  },
  {
    "{": ""      ""Video ID: QnHK4DqY2Y8""
  },
  {
    "{": ""      ""Video ID: dYQu8pLslEE""
  },
  {
    "{": ""      ""Video ID: 3atepKCIHXk""
  },
  {
    "{": ""      ""Video ID: vOFnZNeQMvQ""
  },
  {
    "{": ""      ""Video ID: AKOVPLKwhvI""
  },
  {
    "{": ""      ""Video ID: S74m-FmrSuk""
  },
  {
    "{": ""      ""Video ID: bPIbfQGuaek""
  },
  {
    "{": ""      ""Video ID: _fslSH6AfiE""
  },
  {
    "{": ""      ""Video ID: 6VA0oqbIIKs""
  },
  {
    "{": ""      ""Video ID: BiZWTZ2u7sE""
  },
  {
    "{": ""      ""Video ID: HoLGlShukZ8""
  },
  {
    "{": ""      ""Video ID: iH6o8LgCbKE""
  },
  {
    "{": ""      ""Video ID: 553rhOO0UzA""
  },
  {
    "{": ""      ""Video ID: -PrJdZ4UON0""
  },
  {
    "{": ""      ""Video ID: SA2T0GVC0-M""
  },
  {
    "{": ""      ""Video ID: aJic0P8PhX0""
  },
  {
    "{": ""      ""Video ID: ffduTqOvAb4""
  },
  {
    "{": ""      ""Video ID: 9cWrZ1dZMDQ""
  },
  {
    "{": ""      ""Video ID: jqfzDj41Weo""
  },
  {
    "{": ""      ""Video ID: ImiCFiE7rUw""
  },
  {
    "{": ""      ""Video ID: 4_e4kd5-Hug""
  },
  {
    "{": ""      ""Video ID: GgX8gWBGsII""
  },
  {
    "{": ""      ""Video ID: 6d8LVZXHJMM""
  },
  {
    "{": ""      ""Video ID: mpLbbxHB49Q""
  },
  {
    "{": ""      ""Video ID: zBQtShQy4Co""
  },
  {
    "{": ""      ""Video ID: EGu8WcC2Jcw""
  },
  {
    "{": ""      ""Video ID: 6Upqb9UVAY8""
  },
  {
    "{": ""      ""Video ID: cJVYvcCEbmA""
  },
  {
    "{": ""      ""Video ID: QKc_Owy8SiQ""
  },
  {
    "{": ""      ""Video ID: Px6ETiOh-EE""
  },
  {
    "{": ""      ""Video ID: UpWrr9J5AM8""
  },
  {
    "{": ""      ""Video ID: zVw9PGODUc8""
  },
  {
    "{": ""      ""Video ID: 7sbt-tPN7nU""
  },
  {
    "{": ""      ""Video ID: BTY4XCf0Rec""
  },
  {
    "{": ""      ""Video ID: m9-3TquLnsI""
  },
  {
    "{": ""      ""Video ID: mF9BIDeMR6U""
  },
  {
    "{": ""      ""Video ID: reP8JL8nhcA""
  },
  {
    "{": ""      ""Video ID: pq6OPKVKiv8""
  },
  {
    "{": ""      ""Video ID: xMQwbiiDs9M""
  },
  {
    "{": ""      ""Video ID: g2fT6hyiqzE""
  },
  {
    "{": ""      ""Video ID: v2QRkQGD7PA""
  },
  {
    "{": ""      ""Video ID: _d8TeKzPfxI""
  },
  {
    "{": ""      ""Video ID: 0Pw8Fqiny6Y""
  },
  {
    "{": ""      ""Video ID: mJaQJw1Wf2s""
  },
  {
    "{": ""      ""Video ID: ns9oAGnK9CU""
  },
  {
    "{": ""      ""Video ID: Dj1gIW7BcdI""
  },
  {
    "{": ""      ""Video ID: yu8aKf6GKIU""
  },
  {
    "{": ""      ""Video ID: IpVnr_8Ar9g""
  },
  {
    "{": ""      ""Video ID: hXI3_f9a-Do""
  },
  {
    "{": ""      ""Video ID: xFXvB2DrcWI""
  },
  {
    "{": ""      ""Video ID: sVLuv8ZfCeo""
  },
  {
    "{": ""      ""Video ID: 1wFwEBfETc4""
  },
  {
    "{": ""      ""Video ID: Sj8fECk3rDQ""
  },
  {
    "{": ""      ""Video ID: t_i3qoE0R3c""
  },
  {
    "{": ""      ""Video ID: Zb1R3jtgxBQ""
  },
  {
    "{": ""      ""Video ID: wWxC3me37Yk""
  },
  {
    "{": ""      ""Video ID: YmM5EpM7dHI""
  },
  {
    "{": ""      ""Video ID: lxNOB-1IHJM""
  },
  {
    "{": ""      ""Video ID: tuXBf7QrbM8""
  },
  {
    "{": ""      ""Video ID: -Kn8O1xmEbY""
  },
  {
    "{": ""      ""Video ID: UDqvrANxvFU""
  },
  {
    "{": ""      ""Video ID: bIGdgxjqago""
  },
  {
    "{": ""      ""Video ID: ADAzird1_sI""
  },
  {
    "{": ""      ""Video ID: HL_v5a8JkIk""
  },
  {
    "{": ""      ""Video ID: R1nJNh91KAk""
  },
  {
    "{": ""      ""Video ID: BT6C-QFH-NQ""
  },
  {
    "{": ""      ""Video ID: bef1Gu0t6iE""
  },
  {
    "{": ""      ""Video ID: 7Zv3Z8MISA8""
  },
  {
    "{": ""      ""Video ID: V4pzTRiZwBw""
  },
  {
    "{": ""      ""Video ID: LDESJzHQpDU""
  },
  {
    "{": ""      ""Video ID: 4Tv8wRnSD1M""
  },
  {
    "{": ""      ""Video ID: gXckFGk9tVo""
  },
  {
    "{": ""      ""Video ID: P8RMZCXguE0""
  },
  {
    "{": ""      ""Video ID: ILo2f9EGt1c""
  },
  {
    "{": ""      ""Video ID: 8VuIymB2vXk""
  },
  {
    "{": ""      ""Video ID: 5KcOAIYKtpc""
  },
  {
    "{": ""      ""Video ID: 5ZgO7beIUzg""
  },
  {
    "{": ""      ""Video ID: kSEpCXADMxY""
  },
  {
    "{": ""      ""Video ID: n08iJNNvEik""
  },
  {
    "{": ""      ""Video ID: -Je661Yx_Hg""
  },
  {
    "{": ""      ""Video ID: 7iMbx0RbDY4""
  },
  {
    "{": ""      ""Video ID: wBtq1DTBSn0""
  },
  {
    "{": ""      ""Video ID: X8KFbWZOm48""
  },
  {
    "{": ""      ""Video ID: 803Ut4SbeIM""
  },
  {
    "{": ""      ""Video ID: rQDrzhSQunE""
  },
  {
    "{": ""      ""Video ID: _pu7JSJiYl8""
  },
  {
    "{": ""      ""Video ID: jzrzYoxfz5U""
  },
  {
    "{": ""      ""Video ID: 51D6VZ_WhXo""
  },
  {
    "{": ""      ""Video ID: VmxsBvEaCYw""
  },
  {
    "{": ""      ""Video ID: FExqG6LdWHU""
  },
  {
    "{": ""      ""Video ID: iD2GubKwjew""
  },
  {
    "{": ""      ""Video ID: KaaOwEZrERs""
  },
  {
    "{": ""      ""Video ID: r72BfbGGihU""
  },
  {
    "{": ""      ""Video ID: QM7y7CQ3yC0""
  },
  {
    "{": ""      ""Video ID: SuzFd2aBoHI""
  },
  {
    "{": ""      ""Video ID: n9l35JfNAbI""
  },
  {
    "{": ""      ""Video ID: TJ6qsP6zTUw""
  },
  {
    "{": ""      ""Video ID: DVDUcQETmtQ""
  },
  {
    "{": ""      ""Video ID: SCAiW_UvhHM""
  },
  {
    "{": ""      ""Video ID: 3TI8_IZ2v7I""
  },
  {
    "{": ""      ""Video ID: VcBNcxqTXC0""
  },
  {
    "{": ""      ""Video ID: 5AlZfW6xwcE""
  },
  {
    "{": ""      ""Video ID: 6cbxp1nQ0TA""
  },
  {
    "{": ""      ""Video ID: s6ukoIaHsZA""
  },
  {
    "{": ""      ""Video ID: gxlGZ8LFzKA""
  },
  {
    "{": ""      ""Video ID: 13KfLCich34""
  },
  {
    "{": ""      ""Video ID: pTnpxdTw4SE""
  },
  {
    "{": ""      ""Video ID: 5KmqbSPrDe8""
  },
  {
    "{": ""      ""Video ID: OVmp9-DZZdQ""
  },
  {
    "{": ""      ""Video ID: i9kAuNH087Q""
  },
  {
    "{": ""      ""Video ID: TXNlV4MdSDM""
  },
  {
    "{": ""      ""Video ID: MqySp7Nq5j0""
  },
  {
    "{": ""      ""Video ID: Ti_bUHeHx6Q""
  },
  {
    "{": ""      ""Video ID: KfPirXS39as""
  },
  {
    "{": ""      ""Video ID: JSPAeUSqzyw""
  },
  {
    "{": ""      ""Video ID: 1Ed2TJdfBqo""
  },
  {
    "{": ""      ""Video ID: ynJaug6mw20""
  },
  {
    "{": ""      ""Video ID: czAkynzIy_A""
  },
  {
    "{": ""      ""Video ID: 8r0W23qEb5k""
  },
  {
    "{": ""      ""Video ID: VxOExPJd2E4""
  },
  {
    "{": ""      ""Video ID: mIxJ9nXyc24""
  },
  {
    "{": ""      ""Video ID: QF9b7mdEPng""
  },
  {
    "{": ""      ""Video ID: 9LsPemf908c""
  },
  {
    "{": ""      ""Video ID: SQyWSqgJGZM""
  },
  {
    "{": ""      ""Video ID: hKk96kOAnLg""
  },
  {
    "{": ""      ""Video ID: ZWArtIXY5WA""
  },
  {
    "{": ""      ""Video ID: oaGwItPeMgQ""
  },
  {
    "{": ""      ""Video ID: FlSaXCzLW6w""
  },
  {
    "{": ""      ""Video ID: Y2UoUDXyUk8""
  },
  {
    "{": ""      ""Video ID: z07yGyA17NA""
  },
  {
    "{": ""      ""Video ID: mOKJ5ZPzF0Y""
  },
  {
    "{": ""      ""Video ID: Pj80puAydw8""
  },
  {
    "{": ""      ""Video ID: 2_7i8YWYmgs""
  },
  {
    "{": ""      ""Video ID: hejr73jMyDk""
  },
  {
    "{": ""      ""Video ID: kUdDwHBr2J4""
  },
  {
    "{": ""      ""Video ID: 8Za6u613jUQ""
  },
  {
    "{": ""      ""Video ID: OyGxhwRk8VM""
  },
  {
    "{": ""      ""Video ID: PskQwaun5Ik""
  },
  {
    "{": ""      ""Video ID: iiDb42-0QRI""
  },
  {
    "{": ""      ""Video ID: zaTzJSFwqwI""
  },
  {
    "{": ""      ""Video ID: cSOJEm888gY""
  },
  {
    "{": ""      ""Video ID: YZnuldw8j80""
  },
  {
    "{": ""      ""Video ID: FfxqMaqjhAk""
  },
  {
    "{": ""      ""Video ID: JKU-Wlg9Wz4""
  },
  {
    "{": ""      ""Video ID: 92p3qJm-yrg""
  },
  {
    "{": ""      ""Video ID: -hfPiqbGcgs""
  },
  {
    "{": ""      ""Video ID: Ws8pgiijtUE""
  },
  {
    "{": ""      ""Video ID: w8g9bFBiSTI""
  },
  {
    "{": ""      ""Video ID: dJapBPcULvc""
  },
  {
    "{": ""      ""Video ID: IyisJfvrouM""
  },
  {
    "{": ""      ""Video ID: SlDd3Yipk2c""
  },
  {
    "{": ""      ""Video ID: 0n1ouu1cnXM""
  },
  {
    "{": ""      ""Video ID: b1DzRb4DHGw""
  },
  {
    "{": ""      ""Video ID: jGNgcRwKW4Q""
  },
  {
    "{": ""      ""Video ID: 2xAoG4TcMnQ""
  },
  {
    "{": ""      ""Video ID: ROuKXO5tGYc""
  },
  {
    "{": ""      ""Video ID: oAalYg53V30""
  },
  {
    "{": ""      ""Video ID: A9qyeUOoAZU""
  },
  {
    "{": ""      ""Video ID: hdtGlge-ATE""
  },
  {
    "{": ""      ""Video ID: l-_r1EvJ6q4""
  },
  {
    "{": ""      ""Video ID: 3cGcRdURXus""
  },
  {
    "{": ""      ""Video ID: 3xiLMnZoi-Y""
  },
  {
    "{": ""      ""Video ID: EJ-_eBlXdlM""
  },
  {
    "{": ""      ""Video ID: vcVUO2Q1LxM""
  },
  {
    "{": ""      ""Video ID: pAzZ0GVlmwM""
  },
  {
    "{": ""      ""Video ID: wa0C1sX5d_k""
  },
  {
    "{": ""      ""Video ID: NuYcA9sZ97I""
  },
  {
    "{": ""      ""Video ID: art6cxKvBAs""
  },
  {
    "{": ""      ""Video ID: RfUUZCWKLZs""
  },
  {
    "{": ""      ""Video ID: GibND8wOiA0""
  },
  {
    "{": ""      ""Video ID: RavNZlHU1YU""
  },
  {
    "{": ""      ""Video ID: dAGRhcofPdc""
  },
  {
    "{": ""      ""Video ID: CdVU8nBpQtc""
  },
  {
    "{": ""      ""Video ID: 1yxFSEg9bws""
  },
  {
    "{": ""      ""Video ID: 0-El-LApJ-U""
  },
  {
    "{": ""      ""Video ID: ORjtvS_O3Ac""
  },
  {
    "{": ""      ""Video ID: SMjaI5TTmTY""
  },
  {
    "{": ""      ""Video ID: 1MrbgjLbvwo""
  },
  {
    "{": ""      ""Video ID: ii7GRFuow5w""
  },
  {
    "{": ""      ""Video ID: FqinziCcygM""
  },
  {
    "{": ""      ""Video ID: FKWgvemUhVM""
  },
  {
    "{": ""      ""Video ID: DCdZwASSKuk""
  },
  {
    "{": ""      ""Video ID: BaRcQWVeUQc""
  },
  {
    "{": ""      ""Video ID: fFFK-LLaeVo""
  },
  {
    "{": ""      ""Video ID: 47bOMvdk4MM""
  },
  {
    "{": ""      ""Video ID: 9IQGmpi3K2Q""
  },
  {
    "{": ""      ""Video ID: BVJ6OWqU9Tg""
  },
  {
    "{": ""      ""Video ID: s2bnKeUvKG0""
  },
  {
    "{": ""      ""Video ID: 0zrcjwAYzPk""
  },
  {
    "{": ""      ""Video ID: l2VWzia4t_w""
  },
  {
    "{": ""      ""Video ID: SN9XCLDJSqA""
  },
  {
    "{": ""      ""Video ID: YVDPSZe21KI""
  },
  {
    "{": ""      ""Video ID: Wx3NqvMYMAM""
  },
  {
    "{": ""      ""Video ID: qP1iP4V_jqc""
  },
  {
    "{": ""      ""Video ID: 4ESRWwinXno""
  },
  {
    "{": ""      ""Video ID: qjc1TREntDc""
  },
  {
    "{": ""      ""Video ID: H6oKKFrOnKY""
  },
  {
    "{": ""      ""Video ID: R0ks1U2C6aI""
  },
  {
    "{": ""      ""Video ID: ytuB1RTMg9g""
  },
  {
    "{": ""      ""Video ID: Rlb_jrRODbo""
  },
  {
    "{": ""      ""Video ID: e3MbnnU9tBo""
  },
  {
    "{": ""      ""Video ID: zP1v-2q_Mhc""
  },
  {
    "{": ""      ""Video ID: JvRikfTBCH4""
  },
  {
    "{": ""      ""Video ID: pn12JDri8eY""
  },
  {
    "{": ""      ""Video ID: 3AiPvmtNZaE""
  },
  {
    "{": ""      ""Video ID: XCwlI72lNZ8""
  },
  {
    "{": ""      ""Video ID: 5SqB9vn_CPc""
  },
  {
    "{": ""      ""Video ID: OHi4zSbecw8""
  },
  {
    "{": ""      ""Video ID: kSa-gYvs_Qo""
  },
  {
    "{": ""      ""Video ID: bSsO5p9tnI8""
  },
  {
    "{": ""      ""Video ID: 13FPL5cYMGM""
  },
  {
    "{": ""      ""Video ID: zIDOSTw2G4A""
  },
  {
    "{": ""      ""Video ID: K91yLhO2vt0""
  },
  {
    "{": ""      ""Video ID: 4wSkQo8oPkg""
  },
  {
    "{": ""      ""Video ID: 09GjH9WhesU""
  },
  {
    "{": ""      ""Video ID: uFKTpvS8wfM""
  },
  {
    "{": ""      ""Video ID: imgNkyXJ3sQ""
  },
  {
    "{": ""      ""Video ID: dAalG1_8K8U""
  },
  {
    "{": ""      ""Video ID: 5Xi3hbJaxr8""
  },
  {
    "{": ""      ""Video ID: yGuJRuZGNGc""
  },
  {
    "{": ""      ""Video ID: iLQYwoPaTb4""
  },
  {
    "{": ""      ""Video ID: 7_SQqXXZE2w""
  },
  {
    "{": ""      ""Video ID: 0boAhvmiI44""
  },
  {
    "{": ""      ""Video ID: FFPzDguv9gM""
  },
  {
    "{": ""      ""Video ID: DWi1Y0SmUlM""
  },
  {
    "{": ""      ""Video ID: 0LNAyTeoQxE""
  },
  {
    "{": ""      ""Video ID: LXvz98jrTa0""
  },
  {
    "{": ""      ""Video ID: kgG_Zv7_vok""
  },
  {
    "{": ""      ""Video ID: rE3xz6ZxI0A""
  },
  {
    "{": ""      ""Video ID: _HOcORgcizE""
  },
  {
    "{": ""      ""Video ID: poJfWSq_L_g""
  },
  {
    "{": ""      ""Video ID: Xe15md7VFQQ""
  },
  {
    "{": ""      ""Video ID: RjIFPVqOVPQ""
  },
  {
    "{": ""      ""Video ID: s0se9v3n9Gs""
  },
  {
    "{": ""      ""Video ID: vUdXFo-KNXM""
  },
  {
    "{": ""      ""Video ID: tcSWbRZ3y5w""
  },
  {
    "{": ""      ""Video ID: mF2vw9I-_wk""
  },
  {
    "{": ""      ""Video ID: I-z268TK-Ok""
  },
  {
    "{": ""      ""Video ID: U7b3j9pFNyw""
  },
  {
    "{": ""      ""Video ID: YgR7CmKFXdA""
  },
  {
    "{": ""      ""Video ID: xw0ibZcK-aM""
  },
  {
    "{": ""      ""Video ID: laBko8hNeDk""
  },
  {
    "{": ""      ""Video ID: iimMKWF7SK0""
  },
  {
    "{": ""      ""Video ID: A_iJr8mTg_Y""
  },
  {
    "{": ""      ""Video ID: svM3I4eXyCo""
  },
  {
    "{": ""      ""Video ID: mU5GCdhT0Q0""
  },
  {
    "{": ""      ""Video ID: KT-Q0aVOvHY""
  },
  {
    "{": ""      ""Video ID: 0d-JFLoZI3E""
  },
  {
    "{": ""      ""Video ID: DYwTyK_OcKA""
  },
  {
    "{": ""      ""Video ID: TO6-8ehtf_o""
  },
  {
    "{": ""      ""Video ID: 7Lq5UYv_V_8""
  },
  {
    "{": ""      ""Video ID: OLbMloO6wXM""
  },
  {
    "{": ""      ""Video ID: KR2TZrsa8xQ""
  },
  {
    "{": ""      ""Video ID: TdAPdGzwDdA""
  },
  {
    "{": ""      ""Video ID: -TiX09DmflE""
  },
  {
    "{": ""      ""Video ID: GlanmnOelvg""
  },
  {
    "{": ""      ""Video ID: hVWo5pQpYaw""
  },
  {
    "{": ""      ""Video ID: NjwpT0oj-do""
  },
  {
    "{": ""      ""Video ID: WQ_cI0bhX6c""
  },
  {
    "{": ""      ""Video ID: GTzi9RjV7Fg""
  },
  {
    "{": ""      ""Video ID: 2Byg_Cf5Xtg""
  },
  {
    "{": ""      ""Video ID: KGmUBDB1Otg""
  },
  {
    "{": ""      ""Video ID: 6JNE4IOTju8""
  },
  {
    "{": ""      ""Video ID: ofZyD7uAlgA""
  },
  {
    "{": ""      ""Video ID: S0ECl8_XL2c""
  },
  {
    "{": ""      ""Video ID: dQKJUKPO17Q""
  },
  {
    "{": ""      ""Video ID: Ydnqpf1svkU""
  },
  {
    "{": ""      ""Video ID: ZFoR-mJGjlE""
  },
  {
    "{": ""      ""Video ID: SWaxfiya0kw""
  },
  {
    "{": ""      ""Video ID: ko0LE0l-5T4""
  },
  {
    "{": ""      ""Video ID: fw6qPVZ5lmE""
  },
  {
    "{": ""      ""Video ID: kvhLAeHzMwk""
  },
  {
    "{": ""      ""Video ID: -wEloVJYl9c""
  },
  {
    "{": ""      ""Video ID: ypb4yO_1VeM""
  },
  {
    "{": ""      ""Video ID: U8wsHQUi2e4""
  },
  {
    "{": ""      ""Video ID: V_OU3Ajk7VI""
  },
  {
    "{": ""      ""Video ID: 9a3pmcCiJd0""
  },
  {
    "{": ""      ""Video ID: MWzFOMCPfII""
  },
  {
    "{": ""      ""Video ID: XLlJkZ4H2fs""
  },
  {
    "{": ""      ""Video ID: wCgENwOytuA""
  },
  {
    "{": ""      ""Video ID: s7QGu9M04hU""
  },
  {
    "{": ""      ""Video ID: rLYtOZFO7Ns""
  },
  {
    "{": ""      ""Video ID: YqJmDEWIFA8""
  },
  {
    "{": ""      ""Video ID: tmISXzooFzk""
  },
  {
    "{": ""      ""Video ID: 4_Rwsz1clPM""
  },
  {
    "{": ""      ""Video ID: 7cEHKtDw8ks""
  },
  {
    "{": ""      ""Video ID: JsVGKHzn2UA""
  },
  {
    "{": ""      ""Video ID: cm86Q5iiecw""
  },
  {
    "{": ""      ""Video ID: tBJYYU12tI8""
  },
  {
    "{": ""      ""Video ID: sVK-Ql_0syU""
  },
  {
    "{": ""      ""Video ID: Lv-_4JA_Rgc""
  },
  {
    "{": ""      ""Video ID: _homXEeP1Fc""
  },
  {
    "{": ""      ""Video ID: a8wc2X1BBzk""
  },
  {
    "{": ""      ""Video ID: CSGjraup38s""
  },
  {
    "{": ""      ""Video ID: mxjO3obmFR8""
  },
  {
    "{": ""      ""Video ID: c9eefm3qVU4""
  },
  {
    "{": ""      ""Video ID: Wleao2UGMhw""
  },
  {
    "{": ""      ""Video ID: pS3CH_F5zl4""
  },
  {
    "{": ""      ""Video ID: jLFc7D7CsLQ""
  },
  {
    "{": ""      ""Video ID: OWL-5f1HVOM""
  },
  {
    "{": ""      ""Video ID: ywd3IHWK4A8""
  },
  {
    "{": ""      ""Video ID: 7uHjvVW9s1I""
  },
  {
    "{": ""      ""Video ID: IoDJxTq5xJw""
  },
  {
    "{": ""      ""Video ID: Jd9nXrGd-h0""
  },
  {
    "{": ""      ""Video ID: OKLGOk1j9YE""
  },
  {
    "{": ""      ""Video ID: 9bP2RvD46FA""
  },
  {
    "{": ""      ""Video ID: uapx6_q5juE""
  },
  {
    "{": ""      ""Video ID: jJdXRlKz5S0""
  },
  {
    "{": ""      ""Video ID: Uwb5q_mJ_10""
  },
  {
    "{": ""      ""Video ID: pn_3ZXEdQqI""
  },
  {
    "{": ""      ""Video ID: cpQVtXfICB8""
  },
  {
    "{": ""      ""Video ID: Gf1nrbTEmDQ""
  },
  {
    "{": ""      ""Video ID: wZa-Ja0CMDE""
  },
  {
    "{": ""      ""Video ID: Sm8wZDAAaMg""
  },
  {
    "{": ""      ""Video ID: GjSpHAqb2Nc""
  },
  {
    "{": ""      ""Video ID: NJmOpoxR_Fo""
  },
  {
    "{": ""      ""Video ID: OIej9QgljkI""
  },
  {
    "{": ""      ""Video ID: 7SjhEQ0LxGY""
  },
  {
    "{": ""      ""Video ID: Ieo3Ro46DNY""
  },
  {
    "{": ""      ""Video ID: PPNYW0Lt40c""
  },
  {
    "{": ""      ""Video ID: vct-K0ijRS4""
  },
  {
    "{": ""      ""Video ID: l__8SqmZWZ4""
  },
  {
    "{": ""      ""Video ID: 1NE5ZCajIP0""
  },
  {
    "{": ""      ""Video ID: 2-b6mBME_Ng""
  },
  {
    "{": ""      ""Video ID: cAu7I4AiAts""
  },
  {
    "{": ""      ""Video ID: UUXsuKWHOSo""
  },
  {
    "{": ""      ""Video ID: WpRsgzURnvU""
  },
  {
    "{": ""      ""Video ID: QA3TS8u8RWU""
  },
  {
    "{": ""      ""Video ID: yxA4zdy8--o""
  },
  {
    "{": ""      ""Video ID: nLx0sJymw-Q""
  },
  {
    "{": ""      ""Video ID: 6BaRJpZNZrE""
  },
  {
    "{": ""      ""Video ID: 43UWxYRxDrI""
  },
  {
    "{": ""      ""Video ID: TV74PsUo1dc""
  },
  {
    "{": ""      ""Video ID: OJS8Z6dZWNQ""
  },
  {
    "{": ""      ""Video ID: uj6kiNJppEc""
  },
  {
    "{": ""      ""Video ID: xvQk944WQzQ""
  },
  {
    "{": ""      ""Video ID: 4xyQIZDzbxA""
  },
  {
    "{": ""      ""Video ID: eA6A873Rbjs""
  },
  {
    "{": ""      ""Video ID: aGXL-sLCT5Q""
  },
  {
    "{": ""      ""Video ID: zsJHxEs7Tk4""
  },
  {
    "{": ""      ""Video ID: jaFE9UfngIs""
  },
  {
    "{": ""      ""Video ID: 8K_JM9-GJoI""
  },
  {
    "{": ""      ""Video ID: 8lNZjtBnITM""
  },
  {
    "{": ""      ""Video ID: w1eZJZPoV2g""
  },
  {
    "{": ""      ""Video ID: 7-QQ1k5G784""
  },
  {
    "{": ""      ""Video ID: hXzDJF8Omc8""
  },
  {
    "{": ""      ""Video ID: LkafEQcACzQ""
  },
  {
    "{": ""      ""Video ID: Klh3zPtXrfU""
  },
  {
    "{": ""      ""Video ID: LZjl6R4EK9I""
  },
  {
    "{": ""      ""Video ID: waeN-keNRUU""
  },
  {
    "{": ""      ""Video ID: l5y1i4_BWG4""
  },
  {
    "{": ""      ""Video ID: mSzxyGQliT8""
  },
  {
    "{": ""      ""Video ID: Qb_wZqc_VZY""
  },
  {
    "{": ""      ""Video ID: obUEfSBIJJA""
  },
  {
    "{": ""      ""Video ID: -gLFyzH7pXk""
  },
  {
    "{": ""      ""Video ID: TWDUXizjhiM""
  },
  {
    "{": ""      ""Video ID: psZgRo1ABIE""
  },
  {
    "{": ""      ""Video ID: 0TLA_f7S0cw""
  },
  {
    "{": ""      ""Video ID: thtVspJFL58""
  },
  {
    "{": ""      ""Video ID: ixjnnPweYXY""
  },
  {
    "{": ""      ""Video ID: DWGdE0gT7PM""
  },
  {
    "{": ""      ""Video ID: ubASLyBMZIA""
  },
  {
    "{": ""      ""Video ID: 7FzIfk9b9IA""
  },
  {
    "{": ""      ""Video ID: qtVjoqPCSzA""
  },
  {
    "{": ""      ""Video ID: ctR35kwW4aQ""
  },
  {
    "{": ""      ""Video ID: jbRy-_Tmldg""
  },
  {
    "{": ""      ""Video ID: HbXLIniGz24""
  },
  {
    "{": ""      ""Video ID: 2xGZnRgfTCo""
  },
  {
    "{": ""      ""Video ID: PYce_R9mBVM""
  },
  {
    "{": ""      ""Video ID: y09NZUQN4rI""
  },
  {
    "{": ""      ""Video ID: 9pTPBv2l5X0""
  },
  {
    "{": ""      ""Video ID: vZFr4LNXyrs""
  },
  {
    "{": ""      ""Video ID: 3F5emj8srAo""
  },
  {
    "{": ""      ""Video ID: dQkF8LUoyVE""
  },
  {
    "{": ""      ""Video ID: MzXhyoEVzsg""
  },
  {
    "{": ""      ""Video ID: SHX9pLIh1QM""
  },
  {
    "{": ""      ""Video ID: BTRgbRIyL3c""
  },
  {
    "{": ""      ""Video ID: iUlAcRbtQx0""
  },
  {
    "{": ""      ""Video ID: rTuaM2h5rqk""
  },
  {
    "{": ""      ""Video ID: XrDmGGO39T4""
  },
  {
    "{": ""      ""Video ID: 07w6vN4Uiwk""
  },
  {
    "{": ""      ""Video ID: NsbYNVzOvWs""
  },
  {
    "{": ""      ""Video ID: y00Goj4opUg""
  },
  {
    "{": ""      ""Video ID: PxIkS1aSwss""
  },
  {
    "{": ""      ""Video ID: vBi775zLh2Y""
  },
  {
    "{": ""      ""Video ID: IUJictR2ejQ""
  },
  {
    "{": ""      ""Video ID: neow_g5F7yI""
  },
  {
    "{": ""      ""Video ID: xnAFXazFtaQ""
  },
  {
    "{": ""      ""Video ID: 8LAza0IRj1Y""
  },
  {
    "{": ""      ""Video ID: mw4Btgj1DPk""
  },
  {
    "{": ""      ""Video ID: H8bLmZypFHU""
  },
  {
    "{": ""      ""Video ID: aOgC9NhH5n8""
  },
  {
    "{": ""      ""Video ID: 1fciRDE_WMo""
  },
  {
    "{": ""      ""Video ID: zJV45MPJQ2Q""
  },
  {
    "{": ""      ""Video ID: _QJJOtT32C0""
  },
  {
    "{": ""      ""Video ID: wsh5GItvWJ4""
  },
  {
    "{": ""      ""Video ID: iTCWgljr8tY""
  },
  {
    "{": ""      ""Video ID: ZbeAPwKzAOM""
  },
  {
    "{": ""      ""Video ID: jimfffbqZCI""
  },
  {
    "{": ""      ""Video ID: -ywCjJr5PUk""
  },
  {
    "{": ""      ""Video ID: dF_aKLydmqI""
  },
  {
    "{": ""      ""Video ID: D9V2FPmLbnI""
  },
  {
    "{": ""      ""Video ID: WhgyGMWxbkA""
  },
  {
    "{": ""      ""Video ID: VTaNR7nwghw""
  },
  {
    "{": ""      ""Video ID: BZMcHzgBwC8""
  },
  {
    "{": ""      ""Video ID: aeioASVTErk""
  },
  {
    "{": ""      ""Video ID: DGQiRoFThsw""
  },
  {
    "{": ""      ""Video ID: jHCLgmh1R-k""
  },
  {
    "{": ""      ""Video ID: kYACWwnVdS4""
  },
  {
    "{": ""      ""Video ID: guIJKDeG7_I""
  },
  {
    "{": ""      ""Video ID: PadztlSQZig""
  },
  {
    "{": ""      ""Video ID: Wcqomq4KuiA""
  },
  {
    "{": ""      ""Video ID: t4mZXfRMI0U""
  },
  {
    "{": ""      ""Video ID: rQzR5wYS7Fc""
  },
  {
    "{": ""      ""Video ID: t93h2E3QURo""
  },
  {
    "{": ""      ""Video ID: Ztc9hbZpj4g""
  },
  {
    "{": ""      ""Video ID: UG9LJdOAsrw""
  },
  {
    "{": ""      ""Video ID: 8cP3wmB_dlE""
  },
  {
    "{": ""      ""Video ID: aMfUkCbQ5S8""
  },
  {
    "{": ""      ""Video ID: 2N1SM0xOgh8""
  },
  {
    "{": ""      ""Video ID: OKHSTpAwfpU""
  },
  {
    "{": ""      ""Video ID: sDPsSyaZNIw""
  },
  {
    "{": ""      ""Video ID: gmsis-motuY""
  },
  {
    "{": ""      ""Video ID: HRwAojLnA6A""
  },
  {
    "{": ""      ""Video ID: Id5vYdIkSMQ""
  },
  {
    "{": ""      ""Video ID: r6yu0d766nA""
  },
  {
    "{": ""      ""Video ID: QCfx2gRbOTA""
  },
  {
    "{": ""      ""Video ID: Z5h-VKlnMLU""
  },
  {
    "{": ""      ""Video ID: 6p-AZ_axbUU""
  },
  {
    "{": ""      ""Video ID: Zx0JajPjtHY""
  },
  {
    "{": ""      ""Video ID: TbqOgPAdPWw""
  },
  {
    "{": ""      ""Video ID: vGXu1EBWzlA""
  },
  {
    "{": ""      ""Video ID: KmckBc0aG3M""
  },
  {
    "{": ""      ""Video ID: dp3Wxia6XAU""
  },
  {
    "{": ""      ""Video ID: zHhsnqQXXVQ""
  },
  {
    "{": ""      ""Video ID: mclzXciU5OA""
  },
  {
    "{": ""      ""Video ID: auu8R1kxSUM""
  },
  {
    "{": ""      ""Video ID: 964QHmjLqa0""
  },
  {
    "{": ""      ""Video ID: g477AgN1k0Q""
  },
  {
    "{": ""      ""Video ID: kqh5N48fB48""
  },
  {
    "{": ""      ""Video ID: 132x5VWVJ44""
  },
  {
    "{": ""      ""Video ID: 0uvr3dmptvg""
  },
  {
    "{": ""      ""Video ID: y_DXXTQRSk0""
  },
  {
    "{": ""      ""Video ID: bLfjENpqiiA""
  },
  {
    "{": ""      ""Video ID: daEdot_kM8o""
  },
  {
    "{": ""      ""Video ID: trqEqll6-iE""
  },
  {
    "{": ""      ""Video ID: gsfB6oJ55wM""
  },
  {
    "{": ""      ""Video ID: UBwrx6J41FA""
  },
  {
    "{": ""      ""Video ID: YA3pLCQhOCM""
  },
  {
    "{": ""      ""Video ID: p7nx7r2NJx8""
  },
  {
    "{": ""      ""Video ID: DT9QbIG41_g""
  },
  {
    "{": ""      ""Video ID: bDsIFspVzfI""
  },
  {
    "{": ""      ""Video ID: tjOAvegLKvM""
  },
  {
    "{": ""      ""Video ID: v4tqsQktE2w""
  },
  {
    "{": ""      ""Video ID: oi_gc4XDfZs""
  },
  {
    "{": ""      ""Video ID: FAmwpa52jxo""
  },
  {
    "{": ""      ""Video ID: 5r2uJ7XZjTE""
  },
  {
    "{": ""      ""Video ID: cb50-ouA-IA""
  },
  {
    "{": ""      ""Video ID: RARSvBF6xDk""
  },
  {
    "{": ""      ""Video ID: LYEhV_CYE3w""
  },
  {
    "{": ""      ""Video ID: kz6EUv8Biss""
  },
  {
    "{": ""      ""Video ID: w1xAyN9kNas""
  },
  {
    "{": ""      ""Video ID: IVY_TL1iB1g""
  },
  {
    "{": ""      ""Video ID: oYolp7mUWD8""
  },
  {
    "{": ""      ""Video ID: HwmS5oQsvaI""
  },
  {
    "{": ""      ""Video ID: 6ZYO98LPhoU""
  },
  {
    "{": ""      ""Video ID: V5TafXFYCYg""
  },
  {
    "{": ""      ""Video ID: IHdy-di5nNo""
  },
  {
    "{": ""      ""Video ID: TX7I8SQkyxk""
  },
  {
    "{": ""      ""Video ID: SEuzbUeRl00""
  },
  {
    "{": ""      ""Video ID: KZPqbjQbGUk""
  },
  {
    "{": ""      ""Video ID: _pv1IyTQ2tQ""
  },
  {
    "{": ""      ""Video ID: DTsSdZYgzog""
  },
  {
    "{": ""      ""Video ID: ALQzTAnHn9g""
  },
  {
    "{": ""      ""Video ID: W_7g3HyKocY""
  },
  {
    "{": ""      ""Video ID: aTrX1DBPl7E""
  },
  {
    "{": ""      ""Video ID: odRUGt6BISM""
  },
  {
    "{": ""      ""Video ID: K5OOEdZ2pb0""
  },
  {
    "{": ""      ""Video ID: NEu4pO8zh3E""
  },
  {
    "{": ""      ""Video ID: q3SznJR6VXk""
  },
  {
    "{": ""      ""Video ID: zQaQy0HMKJU""
  },
  {
    "{": ""      ""Video ID: g3h0S9ucw7I""
  },
  {
    "{": ""      ""Video ID: 5-2OsdMzr08""
  },
  {
    "{": ""      ""Video ID: uxJrSXePGVs""
  },
  {
    "{": ""      ""Video ID: aFKbBqGT31Y""
  },
  {
    "{": ""      ""Video ID: EwZt6bvyMqI""
  },
  {
    "{": ""      ""Video ID: 2XA_qLD7rxE""
  },
  {
    "{": ""      ""Video ID: bKBXdHn5gXg""
  },
  {
    "{": ""      ""Video ID: rhxsM6NDZGc""
  },
  {
    "{": ""      ""Video ID: nF2ThweUj8U""
  },
  {
    "{": ""      ""Video ID: UH9NHuQ-RhM""
  },
  {
    "{": ""      ""Video ID: _WEdZbw4C30""
  },
  {
    "{": ""      ""Video ID: pSXAH7LxjuY""
  },
  {
    "{": ""      ""Video ID: FtDazS9d0EY""
  },
  {
    "{": ""      ""Video ID: zVHdxIXlpXw""
  },
  {
    "{": ""      ""Video ID: vud8vkeU-2E""
  },
  {
    "{": ""      ""Video ID: G3kiJbg_b0o""
  },
  {
    "{": ""      ""Video ID: fyQlQLMHafE""
  },
  {
    "{": ""      ""Video ID: K0P9RknIoc8""
  },
  {
    "{": ""      ""Video ID: z89AoOSEce8""
  },
  {
    "{": ""      ""Video ID: UnlyEtM6pV4""
  },
  {
    "{": ""      ""Video ID: hJhIlaE2fRc""
  },
  {
    "{": ""      ""Video ID: 6DI6RbxpTDI""
  },
  {
    "{": ""      ""Video ID: Wgqggc4v8xY""
  },
  {
    "{": ""      ""Video ID: 43te9NWpV5Q""
  },
  {
    "{": ""      ""Video ID: oQ-h0lYAt9w""
  },
  {
    "{": ""      ""Video ID: DO0NcjexN3Q""
  },
  {
    "{": ""      ""Video ID: QVg3wNXu_nc""
  },
  {
    "{": ""      ""Video ID: FMM0oNfImmU""
  },
  {
    "{": ""      ""Video ID: DMwnHCSM-bk""
  },
  {
    "{": ""      ""Video ID: JPJQbyS4_rU""
  },
  {
    "{": ""      ""Video ID: _VL6dE-RrvY""
  },
  {
    "{": ""      ""Video ID: QaWON2Q1A7M""
  },
  {
    "{": ""      ""Video ID: Jvc48SRIabE""
  },
  {
    "{": ""      ""Video ID: 7OOrSs1ogno""
  },
  {
    "{": ""      ""Video ID: C9QVVgld8fk""
  },
  {
    "{": ""      ""Video ID: zpYpH_BbrfY""
  },
  {
    "{": ""      ""Video ID: mhE_lzLHzMY""
  },
  {
    "{": ""      ""Video ID: yVoIEkM0DF0""
  },
  {
    "{": ""      ""Video ID: YGVROWkRF-s""
  },
  {
    "{": ""      ""Video ID: HphZlEASCF8""
  },
  {
    "{": ""      ""Video ID: 7eEQEsf7bLU""
  },
  {
    "{": ""      ""Video ID: YHWzNAZxrkw""
  },
  {
    "{": ""      ""Video ID: JahB9VY92uw""
  },
  {
    "{": ""      ""Video ID: JgZLyVLbU3E""
  },
  {
    "{": ""      ""Video ID: c39jYgsvUOY""
  },
  {
    "{": ""      ""Video ID: f-bB0yCO-E0""
  },
  {
    "{": ""      ""Video ID: bffyfVadZ14""
  },
  {
    "{": ""      ""Video ID: 6J1FcO27VjE""
  },
  {
    "{": ""      ""Video ID: leBXXzuzOYc""
  },
  {
    "{": ""      ""Video ID: RNTa2wjd7jk""
  },
  {
    "{": ""      ""Video ID: m4anw3z88wM""
  },
  {
    "{": ""      ""Video ID: rSmvfTlRxjc""
  },
  {
    "{": ""      ""Video ID: INg5V-DDYeI""
  },
  {
    "{": ""      ""Video ID: VZOdM0fDi4s""
  },
  {
    "{": ""      ""Video ID: ceUI6Fr4wPU""
  },
  {
    "{": ""      ""Video ID: bnKl02keyHk""
  },
  {
    "{": ""      ""Video ID: YMuzVltM9e0""
  },
  {
    "{": ""      ""Video ID: Ecv-xf5i7as""
  },
  {
    "{": ""      ""Video ID: E3ayDJAbO3k""
  },
  {
    "{": ""      ""Video ID: A5ionNPvcj8""
  },
  {
    "{": ""      ""Video ID: brc91BGocFs""
  },
  {
    "{": ""      ""Video ID: ep-xe9VlCKA""
  },
  {
    "{": ""      ""Video ID: gQokzuVBzSM""
  },
  {
    "{": ""      ""Video ID: qPOnx1ucV7w""
  },
  {
    "{": ""      ""Video ID: HWzqqqB2u6Q""
  },
  {
    "{": ""      ""Video ID: _0WkEqgRs00""
  },
  {
    "{": ""      ""Video ID: uf-oqJ1gfrk""
  },
  {
    "{": ""      ""Video ID: 331IPIRQeBU""
  },
  {
    "{": ""      ""Video ID: ZtjubKYwf9o""
  },
  {
    "{": ""      ""Video ID: gSZMeeB3dnk""
  },
  {
    "{": ""      ""Video ID: ReJfEwt-zZk""
  },
  {
    "{": ""      ""Video ID: M8A2rQuJD8k""
  },
  {
    "{": ""      ""Video ID: 1HVqGk7ngxM""
  },
  {
    "{": ""      ""Video ID: idzipprCNwM""
  },
  {
    "{": ""      ""Video ID: HpCMMtyy594""
  },
  {
    "{": ""      ""Video ID: R1iiJzHHoAo""
  },
  {
    "{": ""      ""Video ID: hUFpNOsAig8""
  },
  {
    "{": ""      ""Video ID: -b8VKyTzGQ4""
  },
  {
    "{": ""      ""Video ID: xKxtKUWzA2s""
  },
  {
    "{": ""      ""Video ID: SPXgd6gHU2U""
  },
  {
    "{": ""      ""Video ID: pmdRbBTDiTI""
  },
  {
    "{": ""      ""Video ID: 9NdcNjXvTrQ""
  },
  {
    "{": ""      ""Video ID: tiQQp95CNbo""
  },
  {
    "{": ""      ""Video ID: s58XrBu7mNo""
  },
  {
    "{": ""      ""Video ID: L_UXJ10pWy0""
  },
  {
    "{": ""      ""Video ID: BK3F35YJV3U""
  },
  {
    "{": ""      ""Video ID: aVlplW-pfSU""
  },
  {
    "{": ""      ""Video ID: 3oZiwcbBd5M""
  },
  {
    "{": ""      ""Video ID: 48PFwS70CcU""
  },
  {
    "{": ""      ""Video ID: NkCo5MiH1aI""
  },
  {
    "{": ""      ""Video ID: pW7t6W6GGYY""
  },
  {
    "{": ""      ""Video ID: OwV30fKHnMM""
  },
  {
    "{": ""      ""Video ID: YIJw_83h9R8""
  },
  {
    "{": ""      ""Video ID: pGApmivy_jo""
  },
  {
    "{": ""      ""Video ID: VNEJEi56XEI""
  },
  {
    "{": ""      ""Video ID: fThs68I81lQ""
  },
  {
    "{": ""      ""Video ID: BY6Sbrjy3ao""
  },
  {
    "{": ""      ""Video ID: jcVzcPOP0Sw""
  },
  {
    "{": ""      ""Video ID: ixYjlhBcFpE""
  },
  {
    "{": ""      ""Video ID: mOpQQYwawGU""
  },
  {
    "{": ""      ""Video ID: korlItQ0Yy0""
  },
  {
    "{": ""      ""Video ID: tpAjC38lhk8""
  },
  {
    "{": ""      ""Video ID: jJ-L9krWwEI""
  },
  {
    "{": ""      ""Video ID: _p56kRj8R4U""
  },
  {
    "{": ""      ""Video ID: lhwCY1BBBhY""
  },
  {
    "{": ""      ""Video ID: rfAr-DYG-kw""
  },
  {
    "{": ""      ""Video ID: 0e0mPIj1kLw""
  },
  {
    "{": ""      ""Video ID: rChotQQT0bg""
  },
  {
    "{": ""      ""Video ID: v3Gem6_5juI""
  },
  {
    "{": ""      ""Video ID: -ugKvB_r43o""
  },
  {
    "{": ""      ""Video ID: YXcXW39KrGo""
  },
  {
    "{": ""      ""Video ID: d0B0yqIPs34""
  },
  {
    "{": ""      ""Video ID: 4SlOLM6x77A""
  },
  {
    "{": ""      ""Video ID: 83mCeOIVmk0""
  },
  {
    "{": ""      ""Video ID: f-R4elEehfw""
  },
  {
    "{": ""      ""Video ID: yd1Qod15BzU""
  },
  {
    "{": ""      ""Video ID: x7NVH9CJ60c""
  },
  {
    "{": ""      ""Video ID: GiSt7GSAGQA""
  },
  {
    "{": ""      ""Video ID: RdkNu6Lan5E""
  },
  {
    "{": ""      ""Video ID: u0P6r4uTQ5Q""
  },
  {
    "{": ""      ""Video ID: PmgwUY6eNt0""
  },
  {
    "{": ""      ""Video ID: SuCajiXZCFg""
  },
  {
    "{": ""      ""Video ID: swncNY4HlbU""
  },
  {
    "{": ""      ""Video ID: Zd14gB2oMVw""
  },
  {
    "{": ""      ""Video ID: nsKxdx4rvZI""
  },
  {
    "{": ""      ""Video ID: a-JlucinwT8""
  },
  {
    "{": ""      ""Video ID: D5u2L6CMB6A""
  },
  {
    "{": ""      ""Video ID: PEtEOHqZclQ""
  },
  {
    "{": ""      ""Video ID: DbjBYQxNxbQ""
  },
  {
    "{": ""      ""Video ID: X1L6nTweq08""
  },
  {
    "{": ""      ""Video ID: GX_BPsipu-c""
  },
  {
    "{": ""      ""Video ID: 5RnOsx8529E""
  },
  {
    "{": ""      ""Video ID: PrJEFsK-sO8""
  },
  {
    "{": ""      ""Video ID: 8dprK_9z0Qc""
  },
  {
    "{": ""      ""Video ID: SgzCTbkveGg""
  },
  {
    "{": ""      ""Video ID: ufrV9h7kW24""
  },
  {
    "{": ""      ""Video ID: ufaL9B3DClY""
  },
  {
    "{": ""      ""Video ID: NTUZ-TiTK5E""
  },
  {
    "{": ""      ""Video ID: 8kmeTg-tm6c""
  },
  {
    "{": ""      ""Video ID: c8qbXoeaOOE""
  },
  {
    "{": ""      ""Video ID: oBp2_9wYxVQ""
  },
  {
    "{": ""      ""Video ID: 0kFe0JVt14Y""
  },
  {
    "{": ""      ""Video ID: wkOd3dFhjVc""
  },
  {
    "{": ""      ""Video ID: kzZF3hxthZE""
  },
  {
    "{": ""      ""Video ID: ytafHBoQrPc""
  },
  {
    "{": ""      ""Video ID: gDu0Rs2Hc98""
  },
  {
    "{": ""      ""Video ID: 67cum04P2kI""
  },
  {
    "{": ""      ""Video ID: 7l8mWGCeBu8""
  },
  {
    "{": ""      ""Video ID: wn9sShRbuuM""
  },
  {
    "{": ""      ""Video ID: qndZKzNHpwc""
  },
  {
    "{": ""      ""Video ID: V1RnMTAoV5U""
  },
  {
    "{": ""      ""Video ID: q8VaIu0vuIA""
  },
  {
    "{": ""      ""Video ID: 7pv9x4rhSlY""
  },
  {
    "{": ""      ""Video ID: JG4zV0euo1E""
  },
  {
    "{": ""      ""Video ID: 5d4CaV5W8JU""
  },
  {
    "{": ""      ""Video ID: YVmyZ2gtuwM""
  },
  {
    "{": ""      ""Video ID: acROvuObr-Q""
  },
  {
    "{": ""      ""Video ID: _qzqSwB68Tc""
  },
  {
    "{": ""      ""Video ID: LTRvcROcWHg""
  },
  {
    "{": ""      ""Video ID: n4GHQg0UkVQ""
  },
  {
    "{": ""      ""Video ID: kLiCOf0OXrA""
  },
  {
    "{": ""      ""Video ID: e81g4hBl19g""
  },
  {
    "{": ""      ""Video ID: opUeuFUdYFg""
  },
  {
    "{": ""      ""Video ID: BuiBrRnoDj0""
  },
  {
    "{": ""      ""Video ID: auNYvfBLHGQ""
  },
  {
    "{": ""      ""Video ID: kFDi1GIJXFQ""
  },
  {
    "{": ""      ""Video ID: 9YQycn4TpCY""
  },
  {
    "{": ""      ""Video ID: zwuHCWvQDfA""
  },
  {
    "{": ""      ""Video ID: J8OYvHPpGDY""
  },
  {
    "{": ""      ""Video ID: IrIn0ldCVCE""
  },
  {
    "{": ""      ""Video ID: hVNyfkrVT48""
  },
  {
    "{": ""      ""Video ID: S-bz4mO7TaU""
  },
  {
    "{": ""      ""Video ID: IVssQncboy4""
  },
  {
    "{": ""      ""Video ID: CezoQ0AF6xA""
  },
  {
    "{": ""      ""Video ID: e9tnQ3kKifE""
  },
  {
    "{": ""      ""Video ID: UMwa3ZwTwyA""
  },
  {
    "{": ""      ""Video ID: utkBu-mqi-c""
  },
  {
    "{": ""      ""Video ID: fKMqySX9AUc""
  },
  {
    "{": ""      ""Video ID: 4MUuDFeoyvM""
  },
  {
    "{": ""      ""Video ID: t-PvUI9dI68""
  },
  {
    "{": ""      ""Video ID: ScGSglqHtzc""
  },
  {
    "{": ""      ""Video ID: 2iQA-_d1Hvw""
  },
  {
    "{": ""      ""Video ID: srjI1dUYNdI""
  },
  {
    "{": ""      ""Video ID: o451Ct3fczg""
  },
  {
    "{": ""      ""Video ID: zxUaadrxuDk""
  },
  {
    "{": ""      ""Video ID: Kon4czfAHu4""
  },
  {
    "{": ""      ""Video ID: bUXNi6302ww""
  },
  {
    "{": ""      ""Video ID: s9cxsUf2XV0""
  },
  {
    "{": ""      ""Video ID: m_Lub8LRbLo""
  },
  {
    "{": ""      ""Video ID: B2lhR2aBpo0""
  },
  {
    "{": ""      ""Video ID: E3w-Xn-KY10""
  },
  {
    "{": ""      ""Video ID: HvT03pxhe58""
  },
  {
    "{": ""      ""Video ID: 1UXr4-YDJqk""
  },
  {
    "{": ""      ""Video ID: 77iAuECnq-Q""
  },
  {
    "{": ""      ""Video ID: BBtr2bG3XME""
  },
  {
    "{": ""      ""Video ID: Ml9KZnaJUds""
  },
  {
    "{": ""      ""Video ID: l3SstB-En-E""
  },
  {
    "{": ""      ""Video ID: hEzjM_uXm9Q""
  },
  {
    "{": ""      ""Video ID: wISmf4s_EZs""
  },
  {
    "{": ""      ""Video ID: wk6XudbEg-I""
  },
  {
    "{": ""      ""Video ID: ht42weIj2Jk""
  },
  {
    "{": ""      ""Video ID: iY49Dp8Kap8""
  },
  {
    "{": ""      ""Video ID: kGMF3cn7T10""
  },
  {
    "{": ""      ""Video ID: UEKhj7J2LQQ""
  },
  {
    "{": ""      ""Video ID: L0eMNQOqo5c""
  },
  {
    "{": ""      ""Video ID: YfNbPQJ5Fdc""
  },
  {
    "{": ""      ""Video ID: kc-lMg4rm2Y""
  },
  {
    "{": ""      ""Video ID: Cfmdl9-tnSU""
  },
  {
    "{": ""      ""Video ID: eSAnGy5gwIg""
  },
  {
    "{": ""      ""Video ID: LSw11L2z9Kg""
  },
  {
    "{": ""      ""Video ID: mGHP74tpqwk""
  },
  {
    "{": ""      ""Video ID: cvZ2pSiko1o""
  },
  {
    "{": ""      ""Video ID: nAWRBezzdO8""
  },
  {
    "{": ""      ""Video ID: zABKYBgzVqE""
  },
  {
    "{": ""      ""Video ID: jw_I7UVYnOQ""
  },
  {
    "{": ""      ""Video ID: li-BHb9DqZU""
  },
  {
    "{": ""      ""Video ID: Ds8INeClixc""
  },
  {
    "{": ""      ""Video ID: XlG9wTtutFo""
  },
  {
    "{": ""      ""Video ID: wdDldH9IHco""
  },
  {
    "{": ""      ""Video ID: NSSyTBr4Lnw""
  },
  {
    "{": ""      ""Video ID: PpT7Au54_SU""
  },
  {
    "{": ""      ""Video ID: D2YlXOX1eeE""
  },
  {
    "{": ""      ""Video ID: _3MSxoW3DC0""
  },
  {
    "{": ""      ""Video ID: z7IHQYC7vPs""
  },
  {
    "{": ""      ""Video ID: DCxx27zu_hE""
  },
  {
    "{": ""      ""Video ID: _q4SRTyFD8g""
  },
  {
    "{": ""      ""Video ID: 7IaPtrmGCHA""
  },
  {
    "{": ""      ""Video ID: tsMXqORX4Ds""
  },
  {
    "{": ""      ""Video ID: YJ8R0Wh0zAY""
  },
  {
    "{": ""      ""Video ID: WJ0icWqJdtY""
  },
  {
    "{": ""      ""Video ID: yDc7esDw7BE""
  },
  {
    "{": ""      ""Video ID: TJJYhK1FcjU""
  },
  {
    "{": ""      ""Video ID: WXrSxIp4Skw""
  },
  {
    "{": ""      ""Video ID: Y_ez7EuNGZg""
  },
  {
    "{": ""      ""Video ID: XpXwyWKi910""
  },
  {
    "{": ""      ""Video ID: FHMTsKMRXjg""
  },
  {
    "{": ""      ""Video ID: v27tN1HUG24""
  },
  {
    "{": ""      ""Video ID: i1Qgdt9tTlk""
  },
  {
    "{": ""      ""Video ID: ILylRW-XQ1w""
  },
  {
    "{": ""      ""Video ID: wU5thqp-eIU""
  },
  {
    "{": ""      ""Video ID: XXntOl5L4vg""
  },
  {
    "{": ""      ""Video ID: gb3HuJM1wgw""
  },
  {
    "{": ""      ""Video ID: rJUAh-K92Hg""
  },
  {
    "{": ""      ""Video ID: QOKuXJJ_RrA""
  },
  {
    "{": ""      ""Video ID: n6Vnk_kFUPY""
  },
  {
    "{": ""      ""Video ID: ITJ7ypOIz20""
  },
  {
    "{": ""      ""Video ID: 4gyTyraFxFY""
  },
  {
    "{": ""      ""Video ID: -4NdBA3bv6A""
  },
  {
    "{": ""      ""Video ID: oc6g7ZnkGzI""
  },
  {
    "{": ""      ""Video ID: xpflsAS8VOU""
  },
  {
    "{": ""      ""Video ID: spIsdrwUgPI""
  },
  {
    "{": ""      ""Video ID: fa0caW2jOq8""
  },
  {
    "{": ""      ""Video ID: gMqfYHtpYqw""
  },
  {
    "{": ""      ""Video ID: y-5XK-2Ufd4""
  },
  {
    "{": ""      ""Video ID: 4zNK5kKG0n4""
  },
  {
    "{": ""      ""Video ID: XOdllt8L5tk""
  },
  {
    "{": ""      ""Video ID: JMPxTwiIoD4""
  },
  {
    "{": ""      ""Video ID: 0AMxS6ym7Sw""
  },
  {
    "{": ""      ""Video ID: FBr_HIhtaN0""
  },
  {
    "{": ""      ""Video ID: eHlsglPBZDU""
  },
  {
    "{": ""      ""Video ID: sN8grtFUQYs""
  },
  {
    "{": ""      ""Video ID: siBoLc9vxac""
  },
  {
    "{": ""      ""Video ID: 83iw6rGVXqQ""
  },
  {
    "{": ""      ""Video ID: SojqfX-OQRA""
  },
  {
    "{": ""      ""Video ID: gdwwOIFCfFM""
  },
  {
    "{": ""      ""Video ID: grFbjP49zn0""
  },
  {
    "{": ""      ""Video ID: zMCeIVAmm-M""
  },
  {
    "{": ""      ""Video ID: 2ZclUmQMDBY""
  },
  {
    "{": ""      ""Video ID: kXrzVNh-x_o""
  },
  {
    "{": ""      ""Video ID: EZYQSEIMkXw""
  },
  {
    "{": ""      ""Video ID: Vtm-jbQdF6k""
  },
  {
    "{": ""      ""Video ID: R0DwAWut3b8""
  },
  {
    "{": ""      ""Video ID: ko9vR2_ptlA""
  },
  {
    "{": ""      ""Video ID: 5j_QnEuH96w""
  },
  {
    "{": ""      ""Video ID: rwQqtf86qOc""
  },
  {
    "{": ""      ""Video ID: iMGI10JpfVY""
  },
  {
    "{": ""      ""Video ID: pvUInZm4NfY""
  },
  {
    "{": ""      ""Video ID: Ey7-5vfZ9U8""
  },
  {
    "{": ""      ""Video ID: fmYTbDaMcxE""
  },
  {
    "{": ""      ""Video ID: dxJlmdzruM8""
  },
  {
    "{": ""      ""Video ID: BuXry6V8Rjc""
  },
  {
    "{": ""      ""Video ID: Q-WO-sorNkA""
  },
  {
    "{": ""      ""Video ID: UZW9S21NXBw""
  },
  {
    "{": ""      ""Video ID: UgfKSrqxbqM""
  },
  {
    "{": ""      ""Video ID: XUkLBFeFpBY""
  },
  {
    "{": ""      ""Video ID: 8i9u-EltOVs""
  },
  {
    "{": ""      ""Video ID: DJEH9P0hgCw""
  },
  {
    "{": ""      ""Video ID: McHViMSzQdI""
  },
  {
    "{": ""      ""Video ID: 9JmhJaQH6tc""
  },
  {
    "{": ""      ""Video ID: G_M9iFVYWBI""
  },
  {
    "{": ""      ""Video ID: cKNwifg7uBE""
  },
  {
    "{": ""      ""Video ID: W5r1npU3FJ4""
  },
  {
    "{": ""      ""Video ID: Qpvdl6HaXOk""
  },
  {
    "{": ""      ""Video ID: wNHIZe9PfRg""
  },
  {
    "{": ""      ""Video ID: _lVCBLfwA5A""
  },
  {
    "{": ""      ""Video ID: Lzb1BM1iKkk""
  },
  {
    "{": ""      ""Video ID: VgchCe6qm1U""
  },
  {
    "{": ""      ""Video ID: klJIrCTDIY4""
  },
  {
    "{": ""      ""Video ID: TE-S_jzmQOQ""
  },
  {
    "{": ""      ""Video ID: hWLmZ_mF2V4""
  },
  {
    "{": ""      ""Video ID: Njq0DNCiGFQ""
  },
  {
    "{": ""      ""Video ID: aDHJ_bNoxA8""
  },
  {
    "{": ""      ""Video ID: ciHf4WXKY4E""
  },
  {
    "{": ""      ""Video ID: vQ6E-51QedA""
  },
  {
    "{": ""      ""Video ID: yZaHKycAqks""
  },
  {
    "{": ""      ""Video ID: yUZtSchaVzM""
  },
  {
    "{": ""      ""Video ID: A2oTGk8jvuw""
  },
  {
    "{": ""      ""Video ID: npVmypDPGXc""
  },
  {
    "{": ""      ""Video ID: bwmaP6PIxB8""
  },
  {
    "{": ""      ""Video ID: gizJlFP1MTg""
  },
  {
    "{": ""      ""Video ID: eUeNmb7CSBE""
  },
  {
    "{": ""      ""Video ID: 1gjtvx2UfIc""
  },
  {
    "{": ""      ""Video ID: uIoe7XVQrBs""
  },
  {
    "{": ""      ""Video ID: 7Xy3OZmjWcU""
  },
  {
    "{": ""      ""Video ID: Bnuu0BZn_Uo""
  },
  {
    "{": ""      ""Video ID: gskQdUY5syo""
  },
  {
    "{": ""      ""Video ID: _LJn3nRufv8""
  },
  {
    "{": ""      ""Video ID: RaJXl7Rr-l4""
  },
  {
    "{": ""      ""Video ID: v9OoD7luJ9w""
  },
  {
    "{": ""      ""Video ID: RGwctqQF56k""
  },
  {
    "{": ""      ""Video ID: ch7iAX76mOc""
  },
  {
    "{": ""      ""Video ID: y0gJoWWMVkE""
  },
  {
    "{": ""      ""Video ID: WaXoqDbJEPY""
  },
  {
    "{": ""      ""Video ID: RTDC7hJEqT4""
  },
  {
    "{": ""      ""Video ID: oYtfviYA38Q""
  },
  {
    "{": ""      ""Video ID: 2xhlBvZn-Uk""
  },
  {
    "{": ""      ""Video ID: S2paoWQbZT0""
  },
  {
    "{": ""      ""Video ID: gYnrUHUhOZU""
  },
  {
    "{": ""      ""Video ID: 17BpCCQXsTQ""
  },
  {
    "{": ""      ""Video ID: 8z1QLPXWDrw""
  },
  {
    "{": ""      ""Video ID: Tfm2-bfMlbI""
  },
  {
    "{": ""      ""Video ID: UceMw4hfZN8""
  },
  {
    "{": ""      ""Video ID: 7hW0_UMtsb4""
  },
  {
    "{": ""      ""Video ID: OhO0UUPiVjs""
  },
  {
    "{": ""      ""Video ID: 5wrd-T75Pos""
  },
  {
    "{": ""      ""Video ID: WvT4y2vBXzk""
  },
  {
    "{": ""      ""Video ID: YyhGpqx4bEE""
  },
  {
    "{": ""      ""Video ID: czTTmD4wxfw""
  },
  {
    "{": ""      ""Video ID: pO5RZn26clY""
  },
  {
    "{": ""      ""Video ID: U9OcsbWw8og""
  },
  {
    "{": ""      ""Video ID: nIFyUM3pZ4A""
  },
  {
    "{": ""      ""Video ID: LdP5MmwRYXk""
  },
  {
    "{": ""      ""Video ID: hcOSXK9tZ7Y""
  },
  {
    "{": ""      ""Video ID: GYevZoMCC7A""
  },
  {
    "{": ""      ""Video ID: fYWIT9TSJPE""
  },
  {
    "{": ""      ""Video ID: Ge0kYHjXHL0""
  },
  {
    "{": ""      ""Video ID: 3N_pVwxBRjk""
  },
  {
    "{": ""      ""Video ID: j4UmYU7cCkE""
  },
  {
    "{": ""      ""Video ID: 94d-KVorSHM""
  },
  {
    "{": ""      ""Video ID: 8UVyFdWprrs""
  },
  {
    "{": ""      ""Video ID: PIEIeonrpJQ""
  },
  {
    "{": ""      ""Video ID: VIjanhKqVC4""
  },
  {
    "{": ""      ""Video ID: hWWNLvgU4MI""
  },
  {
    "{": ""      ""Video ID: KTIMzJS9DHY""
  },
  {
    "{": ""      ""Video ID: sCSp61GV1NI""
  },
  {
    "{": ""      ""Video ID: Fu_4CjA2x4I""
  },
  {
    "{": ""      ""Video ID: eTb-UUVFvYY""
  },
  {
    "{": ""      ""Video ID: jS0e_jj0Bf8""
  },
  {
    "{": ""      ""Video ID: 5bKvF7xNbRs""
  },
  {
    "{": ""      ""Video ID: Q3y8uwtxrHo""
  },
  {
    "{": ""      ""Video ID: qPVP12DnBvU""
  },
  {
    "{": ""      ""Video ID: uoGuDDw0c9k""
  },
  {
    "{": ""      ""Video ID: 5NFOnQQMnx4""
  },
  {
    "{": ""      ""Video ID: UTXxobCHY4c""
  },
  {
    "{": ""      ""Video ID: IQQe2HDz03c""
  },
  {
    "{": ""      ""Video ID: a9J1b3MqiX8""
  },
  {
    "{": ""      ""Video ID: qttQIDBuW5k""
  },
  {
    "{": ""      ""Video ID: WUIM5BMlXSY""
  },
  {
    "{": ""      ""Video ID: B0fZK3m7bDc""
  },
  {
    "{": ""      ""Video ID: RxjyCksUcAw""
  },
  {
    "{": ""      ""Video ID: _4C8YC7miLk""
  },
  {
    "{": ""      ""Video ID: 04fX9dez564""
  },
  {
    "{": ""      ""Video ID: GREk8pdh1uw""
  },
  {
    "{": ""      ""Video ID: qNjFCnigTe0""
  },
  {
    "{": ""      ""Video ID: FwNBu22QWwc""
  },
  {
    "{": ""      ""Video ID: fx4wnv92Rzo""
  },
  {
    "{": ""      ""Video ID: qJS4VJ9kIr4""
  },
  {
    "{": ""      ""Video ID: jQ_Q9zCHQ5U""
  },
  {
    "{": ""      ""Video ID: vYMuMKLhyeE""
  },
  {
    "{": ""      ""Video ID: r3VOL5zIDAw""
  },
  {
    "{": ""      ""Video ID: us8epXXicq4""
  },
  {
    "{": ""      ""Video ID: f-6LmHYRaJQ""
  },
  {
    "{": ""      ""Video ID: TWooYHUuQhg""
  },
  {
    "{": ""      ""Video ID: KfRW7YRhB_E""
  },
  {
    "{": ""      ""Video ID: PUuMjXzr5yI""
  },
  {
    "{": ""      ""Video ID: I27ZgkkLvXI""
  },
  {
    "{": ""      ""Video ID: _hm4OS4UXCo""
  },
  {
    "{": ""      ""Video ID: qRESyp9wWBA""
  },
  {
    "{": ""      ""Video ID: Ll54UHW420Y""
  },
  {
    "{": ""      ""Video ID: HojWaEdu3xw""
  },
  {
    "{": ""      ""Video ID: zM_AMsmydG0""
  },
  {
    "{": ""      ""Video ID: 4gBJX2wK1II""
  },
  {
    "{": ""      ""Video ID: HNELm929QYc""
  },
  {
    "{": ""      ""Video ID: PLxClEu0Ysk""
  },
  {
    "{": ""      ""Video ID: c-XhDez2Nxo""
  },
  {
    "{": ""      ""Video ID: 1SrIr66HCmo""
  },
  {
    "{": ""      ""Video ID: Ed1MiIPvHqE""
  },
  {
    "{": ""      ""Video ID: 2mZMrz4NuXA""
  },
  {
    "{": ""      ""Video ID: oatoZrPm6W0""
  },
  {
    "{": ""      ""Video ID: EXgq-AZpuOo""
  },
  {
    "{": ""      ""Video ID: 3Et_LsxlX8Y""
  },
  {
    "{": ""      ""Video ID: moE3l9wKlFw""
  },
  {
    "{": ""      ""Video ID: PVtD-MrawGc""
  },
  {
    "{": ""      ""Video ID: kdcFPmXti9U""
  },
  {
    "{": ""      ""Video ID: yC-YXLWzS40""
  },
  {
    "{": ""      ""Video ID: I4lYtSEkiLc""
  },
  {
    "{": ""      ""Video ID: YPZhrdfjvOM""
  },
  {
    "{": ""      ""Video ID: OhLkvzTQd0o""
  },
  {
    "{": ""      ""Video ID: 6cnU3nvAsOE""
  },
  {
    "{": ""      ""Video ID: J3CSn2zn47c""
  },
  {
    "{": ""      ""Video ID: 6Q6OQlX_sFg""
  },
  {
    "{": ""      ""Video ID: q7diFpgBz8Y""
  },
  {
    "{": ""      ""Video ID: 5jdAjaaw26Y""
  },
  {
    "{": ""      ""Video ID: sYHaNfkc_lI""
  },
  {
    "{": ""      ""Video ID: S9jaiJJbKd8""
  },
  {
    "{": ""      ""Video ID: YE81V1YjrGg""
  },
  {
    "{": ""      ""Video ID: 7yvgjuZctnc""
  },
  {
    "{": ""      ""Video ID: LyPlfryoOjQ""
  },
  {
    "{": ""      ""Video ID: 1G0ZNzx0Ayo""
  },
  {
    "{": ""      ""Video ID: EmtcZk4EtN0""
  },
  {
    "{": ""      ""Video ID: 504a-bzwVLo""
  },
  {
    "{": ""      ""Video ID: Mj2UL2MfQzA""
  },
  {
    "{": ""      ""Video ID: kMSVg6Vbb98""
  },
  {
    "{": ""      ""Video ID: GZ175fINOzs""
  },
  {
    "{": ""      ""Video ID: qIyt_-UuiZQ""
  },
  {
    "{": ""      ""Video ID: Wg2htO0QXHw""
  },
  {
    "{": ""      ""Video ID: W_wQhUi2kPI""
  },
  {
    "{": ""      ""Video ID: dRncDLufxWQ""
  },
  {
    "{": ""      ""Video ID: hXEVjeqBt2Y""
  },
  {
    "{": ""      ""Video ID: aBCA9GpGZ5I""
  },
  {
    "{": ""      ""Video ID: CmFisT05Xmk""
  },
  {
    "{": ""      ""Video ID: UOgE3uUObT8""
  },
  {
    "{": ""      ""Video ID: _JWqTfmGp4I""
  },
  {
    "{": ""      ""Video ID: lkbXsDaGj-g""
  },
  {
    "{": ""      ""Video ID: WFpcxgRsKHg""
  },
  {
    "{": ""      ""Video ID: QAuL8M4u-7Y""
  },
  {
    "{": ""      ""Video ID: nf4UPQts-vA""
  },
  {
    "{": ""      ""Video ID: fTZ0Hxloa1E""
  },
  {
    "{": ""      ""Video ID: o0kasxIp3v0""
  },
  {
    "{": ""      ""Video ID: cwxW64pqqzI""
  },
  {
    "{": ""      ""Video ID: nLwTIWUPVgs""
  },
  {
    "{": ""      ""Video ID: liyFOeInxiY""
  },
  {
    "{": ""      ""Video ID: a8yKb7wWagM""
  },
  {
    "{": ""      ""Video ID: _vLl3K8yzOk""
  },
  {
    "{": ""      ""Video ID: qstj5BG4loI""
  },
  {
    "{": ""      ""Video ID: h9R131hl4zI""
  },
  {
    "{": ""      ""Video ID: JJXn4mupmzc""
  },
  {
    "{": ""      ""Video ID: LijS7XP4vp8""
  },
  {
    "{": ""      ""Video ID: TaotlzBIf5k""
  },
  {
    "{": ""      ""Video ID: yYxIlnW9Ymw""
  },
  {
    "{": ""      ""Video ID: Fr_SVPnWlxs""
  },
  {
    "{": ""      ""Video ID: dufJhHW9LdI""
  },
  {
    "{": ""      ""Video ID: kKyugpFQAtg""
  },
  {
    "{": ""      ""Video ID: wd5bcL2APZI""
  },
  {
    "{": ""      ""Video ID: 5cFp_fElzY4""
  },
  {
    "{": ""      ""Video ID: mcm-cAr9ktI""
  },
  {
    "{": ""      ""Video ID: Itq8PUzIJpw""
  },
  {
    "{": ""      ""Video ID: Gxi3Z4lvlVU""
  },
  {
    "{": ""      ""Video ID: iNiDbiW5aGk""
  },
  {
    "{": ""      ""Video ID: OtoMHls3kJg""
  },
  {
    "{": ""      ""Video ID: VRSNT_9ru2U""
  },
  {
    "{": ""      ""Video ID: uN1RDYluKNk""
  },
  {
    "{": ""      ""Video ID: g69ykl5uaXQ""
  },
  {
    "{": ""      ""Video ID: 2pw9ttqg9_M""
  },
  {
    "{": ""      ""Video ID: -j2LSmtDPjI""
  },
  {
    "{": ""      ""Video ID: C4lpIaSraPE""
  },
  {
    "{": ""      ""Video ID: Yo7lfHHEu4c""
  },
  {
    "{": ""      ""Video ID: CtoPerY_X0w""
  },
  {
    "{": ""      ""Video ID: wul1l9ZwQFk""
  },
  {
    "{": ""      ""Video ID: UlMNZtPTyQM""
  },
  {
    "{": ""      ""Video ID: R5PmnBHZQAE""
  },
  {
    "{": ""      ""Video ID: ObWeKaHwEo8""
  },
  {
    "{": ""      ""Video ID: R1ou3ikP0N0""
  },
  {
    "{": ""      ""Video ID: vJ8BUD9D1K0""
  },
  {
    "{": ""      ""Video ID: F_ikVBkwmZ4""
  },
  {
    "{": ""      ""Video ID: YJO6JL4435U""
  },
  {
    "{": ""      ""Video ID: UorNMMNvPDc""
  },
  {
    "{": ""      ""Video ID: Z24IMXGxcK4""
  },
  {
    "{": ""      ""Video ID: iqhXuyWnvf0""
  },
  {
    "{": ""      ""Video ID: pAXm5-nktHg""
  },
  {
    "{": ""      ""Video ID: rbZNeX9X0Gs""
  },
  {
    "{": ""      ""Video ID: QcVs_bUebrI""
  },
  {
    "{": ""      ""Video ID: sJQSD8E6niQ""
  },
  {
    "{": ""      ""Video ID: sgbIm1NP3F4""
  },
  {
    "{": ""      ""Video ID: FvGyqw3ZeLs""
  },
  {
    "{": ""      ""Video ID: mXAQgjdyI3I""
  },
  {
    "{": ""      ""Video ID: s_Q-6vnyZVg""
  },
  {
    "{": ""      ""Video ID: eX7UKH3_xuA""
  },
  {
    "{": ""      ""Video ID: h9jJ8fXVhjE""
  },
  {
    "{": ""      ""Video ID: 5e9y6-LRDPY""
  },
  {
    "{": ""      ""Video ID: pphoNerNRU4""
  },
  {
    "{": ""      ""Video ID: 1NX81Yd6cyI""
  },
  {
    "{": ""      ""Video ID: egJRWM9nErM""
  },
  {
    "{": ""      ""Video ID: VYxr6nhqtfk""
  },
  {
    "{": ""      ""Video ID: u4nQ7bJidRs""
  },
  {
    "{": ""      ""Video ID: 6HQhNlQqN1k""
  },
  {
    "{": ""      ""Video ID: emoS2NOSPG8""
  },
  {
    "{": ""      ""Video ID: bT1B5EV4slA""
  },
  {
    "{": ""      ""Video ID: tQRDrvsLKV8""
  },
  {
    "{": ""      ""Video ID: IBWcQws3B9E""
  },
  {
    "{": ""      ""Video ID: w9SwLZshjz0""
  },
  {
    "{": ""      ""Video ID: C0lEvSPT10A""
  },
  {
    "{": ""      ""Video ID: YH-m2__WXxk""
  },
  {
    "{": ""      ""Video ID: DL1u4tczaCM""
  },
  {
    "{": ""      ""Video ID: -SoqDnaJkXQ""
  },
  {
    "{": ""      ""Video ID: EHV_lAcDYuM""
  },
  {
    "{": ""      ""Video ID: QPsAoCu_yyM""
  },
  {
    "{": ""      ""Video ID: F1oB6Ve1KEk""
  },
  {
    "{": ""      ""Video ID: uhqrWue42pg""
  },
  {
    "{": ""      ""Video ID: KIojtF7liJI""
  },
  {
    "{": ""      ""Video ID: X3I1-A5umn0""
  },
  {
    "{": ""      ""Video ID: jK4j7Ypod4s""
  },
  {
    "{": ""      ""Video ID: yvfJgQKCS2M""
  },
  {
    "{": ""      ""Video ID: uQKwGA9wtFc""
  },
  {
    "{": ""      ""Video ID: 6Z7U12JGlOQ""
  },
  {
    "{": ""      ""Video ID: 20jSUVC0G0Q""
  },
  {
    "{": ""      ""Video ID: hHKOT4K7hO4""
  },
  {
    "{": ""      ""Video ID: _XCt43GIeEc""
  },
  {
    "{": ""      ""Video ID: DQkksAVBezc""
  },
  {
    "{": ""      ""Video ID: ubbjgLDKGyk""
  },
  {
    "{": ""      ""Video ID: oZi1Mk2Njtg""
  },
  {
    "{": ""      ""Video ID: fJlHBT1r3EU""
  },
  {
    "{": ""      ""Video ID: QkxnQXsCiVM""
  },
  {
    "{": ""      ""Video ID: JPTgZ0acjfI""
  },
  {
    "{": ""      ""Video ID: CDAWszeZtNg""
  },
  {
    "{": ""      ""Video ID: KXN9r6tPgHU""
  },
  {
    "{": ""      ""Video ID: sXldafIl5DQ""
  },
  {
    "{": ""      ""Video ID: _CimES10UL4""
  },
  {
    "{": ""      ""Video ID: e3fqE01YYWs""
  },
  {
    "{": ""      ""Video ID: -xBAN1nwNvQ""
  },
  {
    "{": ""      ""Video ID: zRRTQW3t56g""
  },
  {
    "{": ""      ""Video ID: yfvgx-mz2-8""
  },
  {
    "{": ""      ""Video ID: 8JwkOOHgp_E""
  },
  {
    "{": ""      ""Video ID: h4bYnG5b4ck""
  },
  {
    "{": ""      ""Video ID: 6DsSouaW78I""
  },
  {
    "{": ""      ""Video ID: MzYXaAioFD8""
  },
  {
    "{": ""      ""Video ID: jl8LvfrSsss""
  },
  {
    "{": ""      ""Video ID: Uwh7UoxbLMk""
  },
  {
    "{": ""      ""Video ID: Z6rdwC1xfrk""
  },
  {
    "{": ""      ""Video ID: iDmz-fv_oEM""
  },
  {
    "{": ""      ""Video ID: YK0LgQTyPvs""
  },
  {
    "{": ""      ""Video ID: UxAuZijwyMM""
  },
  {
    "{": ""      ""Video ID: OzVjnhab9Ss""
  },
  {
    "{": ""      ""Video ID: ncvLAFUHl1Y""
  },
  {
    "{": ""      ""Video ID: zx8fOrDYyEQ""
  },
  {
    "{": ""      ""Video ID: JMMOkNxh1zw""
  },
  {
    "{": ""      ""Video ID: ZHEac6pCLFk""
  },
  {
    "{": ""      ""Video ID: YAPMWkaZZf8""
  },
  {
    "{": ""      ""Video ID: l22ijt0rOkM""
  },
  {
    "{": ""      ""Video ID: 4-rT3eZkjoo""
  },
  {
    "{": ""      ""Video ID: 07EmY67Q9Y0""
  },
  {
    "{": ""      ""Video ID: kGxIrxLwibQ""
  },
  {
    "{": ""      ""Video ID: mR4M7kbxwro""
  },
  {
    "{": ""      ""Video ID: iJerXU_VOIk""
  },
  {
    "{": ""      ""Video ID: 9KhZwsYtNDE""
  },
  {
    "{": ""      ""Video ID: QUH4fu4NheQ""
  },
  {
    "{": ""      ""Video ID: O1753V-0K5k""
  },
  {
    "{": ""      ""Video ID: lCZffO_JxtQ""
  },
  {
    "{": ""      ""Video ID: nFVKnPcJAww""
  },
  {
    "{": ""      ""Video ID: vrn6IdNdZyE""
  },
  {
    "{": ""      ""Video ID: -If0bzyZlNE""
  },
  {
    "{": ""      ""Video ID: Loo1hHhgP5k""
  },
  {
    "{": ""      ""Video ID: Zu8k3z2fMoA""
  },
  {
    "{": ""      ""Video ID: 9JzunZnQeLw""
  },
  {
    "{": ""      ""Video ID: jd7YgLNCExM""
  },
  {
    "{": ""      ""Video ID: Gtd0SQJ989o""
  },
  {
    "{": ""      ""Video ID: d7A3jcX2PDk""
  },
  {
    "{": ""      ""Video ID: Vv50sk-_oB0""
  },
  {
    "{": ""      ""Video ID: 50CfOTxR-aA""
  },
  {
    "{": ""      ""Video ID: 7xWIrpf7dik""
  },
  {
    "{": ""      ""Video ID: CMAIMS-jqpg""
  },
  {
    "{": ""      ""Video ID: 55_5cywPqvs""
  },
  {
    "{": ""      ""Video ID: V9JxZo1U0g0""
  },
  {
    "{": ""      ""Video ID: PbD9yB0bIrI""
  },
  {
    "{": ""      ""Video ID: PdE1Z-j2LGw""
  },
  {
    "{": ""      ""Video ID: HDIvH4bjeCc""
  },
  {
    "{": ""      ""Video ID: dCluP2cTj80""
  },
  {
    "{": ""      ""Video ID: x8joRhJkMc8""
  },
  {
    "{": ""      ""Video ID: NBSkgm43XKQ""
  },
  {
    "{": ""      ""Video ID: ivdcW-2vPuk""
  },
  {
    "{": ""      ""Video ID: soMO7aapwUk""
  },
  {
    "{": ""      ""Video ID: CVcY1JJiDZ4""
  },
  {
    "{": ""      ""Video ID: g8IsZLf7P9k""
  },
  {
    "{": ""      ""Video ID: z_VFD9Xhiic""
  },
  {
    "{": ""      ""Video ID: 3zx0_b7XjNk""
  },
  {
    "{": ""      ""Video ID: XqMf3towVVI""
  },
  {
    "{": ""      ""Video ID: G2WnpqWD6FE""
  },
  {
    "{": ""      ""Video ID: 3-e11ckQz_o""
  },
  {
    "{": ""      ""Video ID: 1y6TnhR6EXs""
  },
  {
    "{": ""      ""Video ID: RxNAaHmjvIE""
  },
  {
    "{": ""      ""Video ID: JDhnvg06rHM""
  },
  {
    "{": ""      ""Video ID: bsLxXV9OI2M""
  },
  {
    "{": ""      ""Video ID: MbeOwlK5Dhg""
  },
  {
    "{": ""      ""Video ID: 97gOAp_v8u4""
  },
  {
    "{": ""      ""Video ID: Cxa3SMd2wcA""
  },
  {
    "{": ""      ""Video ID: IVbgSwuU8xY""
  },
  {
    "{": ""      ""Video ID: Hv-UtDBb0_c""
  },
  {
    "{": ""      ""Video ID: zGNryrsT7OI""
  },
  {
    "{": ""      ""Video ID: plHY-5tr83o""
  },
  {
    "{": ""      ""Video ID: 0zv9E86L148""
  },
  {
    "{": ""      ""Video ID: 8ShbFl0kUmE""
  },
  {
    "{": ""      ""Video ID: m06GxCzytyM""
  },
  {
    "{": ""      ""Video ID: NMnvPgw3dc8""
  },
  {
    "{": ""      ""Video ID: cO_aUtJkBes""
  },
  {
    "{": ""      ""Video ID: NkN0T2rn5WA""
  },
  {
    "{": ""      ""Video ID: OmwSAhrZgbQ""
  },
  {
    "{": ""      ""Video ID: E2UoVSxo4ow""
  },
  {
    "{": ""      ""Video ID: zpUpWEjEN_U""
  },
  {
    "{": ""      ""Video ID: nHI_0i4hvxU""
  },
  {
    "{": ""      ""Video ID: 8QWpfyqm_yo""
  },
  {
    "{": ""      ""Video ID: Wt1Lo-WPDQg""
  },
  {
    "{": ""      ""Video ID: pIreWMvuqN4""
  },
  {
    "{": ""      ""Video ID: WFw5B9qg2QI""
  },
  {
    "{": ""      ""Video ID: OnxjMRw75E8""
  },
  {
    "{": ""      ""Video ID: sABpGFzxebQ""
  },
  {
    "{": ""      ""Video ID: DF6ywgm1yBU""
  },
  {
    "{": ""      ""Video ID: E0xO8MgphhA""
  },
  {
    "{": ""      ""Video ID: feyRjZ3_xBA""
  },
  {
    "{": ""      ""Video ID: T87tdVUtLV4""
  },
  {
    "{": ""      ""Video ID: 0lyJKNPU2wE""
  },
  {
    "{": ""      ""Video ID: eeTnYCGv_hU""
  },
  {
    "{": ""      ""Video ID: hEuzbr0eSMw""
  },
  {
    "{": ""      ""Video ID: kZDj1cgZjEg""
  },
  {
    "{": ""      ""Video ID: 2I4NYYIZJ1s""
  },
  {
    "{": ""      ""Video ID: VwHOE8hlGV0""
  },
  {
    "{": ""      ""Video ID: 521NIVPIxWs""
  },
  {
    "{": ""      ""Video ID: yvG02lUFrIQ""
  },
  {
    "{": ""      ""Video ID: SZEXzHj0XUo""
  },
  {
    "{": ""      ""Video ID: 4U8Visy7Wio""
  },
  {
    "{": ""      ""Video ID: -1mXSF6D-PI""
  },
  {
    "{": ""      ""Video ID: CgpKB8nnHTQ""
  },
  {
    "{": ""      ""Video ID: g-4SMz2DhVk""
  },
  {
    "{": ""      ""Video ID: 8iBTIsMmmNU""
  },
  {
    "{": ""      ""Video ID: t8shVDvMdo4""
  },
  {
    "{": ""      ""Video ID: I2fuwVhwEG0""
  },
  {
    "{": ""      ""Video ID: F59KmOrnFco""
  },
  {
    "{": ""      ""Video ID: jTQwGkG_AWU""
  },
  {
    "{": ""      ""Video ID: yTdjlofgOJo""
  },
  {
    "{": ""      ""Video ID: KkpX9q0MZgs""
  },
  {
    "{": ""      ""Video ID: rPX5G3_4H_g""
  },
  {
    "{": ""      ""Video ID: lFoC5sNHdNs""
  },
  {
    "{": ""      ""Video ID: XYDIGYrA-bc""
  },
  {
    "{": ""      ""Video ID: 1I70yBTHMw4""
  },
  {
    "{": ""      ""Video ID: HDZBF4mlZK0""
  },
  {
    "{": ""      ""Video ID: A9zUt5UKJ6M""
  },
  {
    "{": ""      ""Video ID: JGbiR6mvE9c""
  },
  {
    "{": ""      ""Video ID: I91MLRtPvu8""
  },
  {
    "{": ""      ""Video ID: 8FSHNRXQnek""
  },
  {
    "{": ""      ""Video ID: jTwUg76BCNE""
  },
  {
    "{": ""      ""Video ID: 2Vc06unznlo""
  },
  {
    "{": ""      ""Video ID: tKZzFTLrNvc""
  },
  {
    "{": ""      ""Video ID: Eom5uGLwolY""
  },
  {
    "{": ""      ""Video ID: XfmVFOetFwI""
  },
  {
    "{": ""      ""Video ID: _dYJ4KQvzIw""
  },
  {
    "{": ""      ""Video ID: 5GBq4MGBEgM""
  },
  {
    "{": ""      ""Video ID: Q6jJ3VA518k""
  },
  {
    "{": ""      ""Video ID: uZ3PsQ1XCYM""
  },
  {
    "{": ""      ""Video ID: sokLXXmG0vQ""
  },
  {
    "{": ""      ""Video ID: UDPZdRNXXDo""
  },
  {
    "{": ""      ""Video ID: R50fbBXeNoU""
  },
  {
    "{": ""      ""Video ID: 9S30XLds5gc""
  },
  {
    "{": ""      ""Video ID: DwEMTpjWUQA""
  },
  {
    "{": ""      ""Video ID: ovZ9fPxrCdA""
  },
  {
    "{": ""      ""Video ID: YSLVyP515jo""
  },
  {
    "{": ""      ""Video ID: f3MKo7HE8WU""
  },
  {
    "{": ""      ""Video ID: d84-2YPaDEc""
  },
  {
    "{": ""      ""Video ID: mXoL4WdszLQ""
  },
  {
    "{": ""      ""Video ID: dB83z10MDbE""
  },
  {
    "{": ""      ""Video ID: p4E_ZJ1kp74""
  },
  {
    "{": ""      ""Video ID: RZhheuPDsyQ""
  },
  {
    "{": ""      ""Video ID: I5htQgVROAE""
  },
  {
    "{": ""      ""Video ID: Z4Tx6ZemM_c""
  },
  {
    "{": ""      ""Video ID: Qnsl3dOuZRM""
  },
  {
    "{": ""      ""Video ID: MBvgFmpfu8E""
  },
  {
    "{": ""      ""Video ID: SzX17dqfMmo""
  },
  {
    "{": ""      ""Video ID: 4iJdVmU3Vuo""
  },
  {
    "{": ""      ""Video ID: citzK49qa3w""
  },
  {
    "{": ""      ""Video ID: WmUU00Umm0g""
  },
  {
    "{": ""      ""Video ID: a9PeQZrBY80""
  },
  {
    "{": ""      ""Video ID: K3WomWPQQY0""
  },
  {
    "{": ""      ""Video ID: 7bIvFg5fXUM""
  },
  {
    "{": ""      ""Video ID: Qe1Mt1ozlTY""
  },
  {
    "{": ""      ""Video ID: dv0yqkfhMmA""
  },
  {
    "{": ""      ""Video ID: _rqFHB_1VUQ""
  },
  {
    "{": ""      ""Video ID: 23EGqaSlhEE""
  },
  {
    "{": ""      ""Video ID: mZs0qP3WZ-w""
  },
  {
    "{": ""      ""Video ID: PWnppgFa6kY""
  },
  {
    "{": ""      ""Video ID: 9GFT85ccSW0""
  },
  {
    "{": ""      ""Video ID: e3KphwZyocw""
  },
  {
    "{": ""      ""Video ID: 9mraHQw9_Zc""
  },
  {
    "{": ""      ""Video ID: N3Aw9dsTDu0""
  },
  {
    "{": ""      ""Video ID: -O73M3LPuYM""
  },
  {
    "{": ""      ""Video ID: A7wiLiHSOYs""
  },
  {
    "{": ""      ""Video ID: 6HmoKn0ARSM""
  },
  {
    "{": ""      ""Video ID: wb9rMVGR0nY""
  },
  {
    "{": ""      ""Video ID: CJwNX8Z2U5U""
  },
  {
    "{": ""      ""Video ID: gbJBPFEbh54""
  },
  {
    "{": ""      ""Video ID: fak1v_Euv3A""
  },
  {
    "{": ""      ""Video ID: aWxSJ4cevcM""
  },
  {
    "{": ""      ""Video ID: N3y_XyBTjZc""
  },
  {
    "{": ""      ""Video ID: uNdJWG8IjhU""
  },
  {
    "{": ""      ""Video ID: cmrSHJy2vJE""
  },
  {
    "{": ""      ""Video ID: 9hC4FXdZcOg""
  },
  {
    "{": ""      ""Video ID: F44BcGjIbAA""
  },
  {
    "{": ""      ""Video ID: d4324hOvwsA""
  },
  {
    "{": ""      ""Video ID: 10qLYy6hiFQ""
  },
  {
    "{": ""      ""Video ID: EQ-JyAGUsys""
  },
  {
    "{": ""      ""Video ID: -axOgiuo8Ec""
  },
  {
    "{": ""      ""Video ID: 1PFgBl25AHQ""
  },
  {
    "{": ""      ""Video ID: yQoZmYUuvXw""
  },
  {
    "{": ""      ""Video ID: aKKGYMg6ez0""
  },
  {
    "{": ""      ""Video ID: mMl-sNOOEIw""
  },
  {
    "{": ""      ""Video ID: 7IAZLsg_6SY""
  },
  {
    "{": ""      ""Video ID: rARMAvSAvcQ""
  },
  {
    "{": ""      ""Video ID: OQjaE3z4Wi0""
  },
  {
    "{": ""      ""Video ID: 2XuSxLRSECk""
  },
  {
    "{": ""      ""Video ID: 5QLtB6JJiMk""
  },
  {
    "{": ""      ""Video ID: XnamP4-M9ko""
  },
  {
    "{": ""      ""Video ID: y_b3LMoQUJ0""
  },
  {
    "{": ""      ""Video ID: UvPufQqo3yI""
  },
  {
    "{": ""      ""Video ID: SMI0v9zhsvI""
  },
  {
    "{": ""      ""Video ID: q6Qe818ie-4""
  },
  {
    "{": ""      ""Video ID: QGiat_6BFI0""
  },
  {
    "{": ""      ""Video ID: p069Ddy-9yo""
  },
  {
    "{": ""      ""Video ID: jNW4pfeJLb8""
  },
  {
    "{": ""      ""Video ID: _eAHvfW16qo""
  },
  {
    "{": ""      ""Video ID: GvNiBfkuWEo""
  },
  {
    "{": ""      ""Video ID: bLZHTHpD8EE""
  },
  {
    "{": ""      ""Video ID: 3gdy4iVMa8M""
  },
  {
    "{": ""      ""Video ID: 4A_OPgtBnsc""
  },
  {
    "{": ""      ""Video ID: o_ueajf8JZo""
  },
  {
    "{": ""      ""Video ID: Q7Ez5VdORTc""
  },
  {
    "{": ""      ""Video ID: -59mcxFNLHQ""
  },
  {
    "{": ""      ""Video ID: m4Y3t_pygOg""
  },
  {
    "{": ""      ""Video ID: g5K3lGLDudI""
  },
  {
    "{": ""      ""Video ID: nnuXJxv0tWc""
  },
  {
    "{": ""      ""Video ID: z4i1t_lxJcw""
  },
  {
    "{": ""      ""Video ID: -iSJHBsdkhk""
  },
  {
    "{": ""      ""Video ID: A0XYRZqE4z4""
  },
  {
    "{": ""      ""Video ID: jiYE2BiwDB0""
  },
  {
    "{": ""      ""Video ID: PZnj6k7QQZM""
  },
  {
    "{": ""      ""Video ID: HeVKhxHkR2U""
  },
  {
    "{": ""      ""Video ID: y7HQR8wJrUI""
  },
  {
    "{": ""      ""Video ID: B-Tne0Brdic""
  },
  {
    "{": ""      ""Video ID: OwSOsfa1064""
  },
  {
    "{": ""      ""Video ID: BJtOCs5crns""
  },
  {
    "{": ""      ""Video ID: szZu-OKjqpo""
  },
  {
    "{": ""      ""Video ID: YgYDJorzMYs""
  },
  {
    "{": ""      ""Video ID: KEeUyA8-XIQ""
  },
  {
    "{": ""      ""Video ID: yCVD3i-86jM""
  },
  {
    "{": ""      ""Video ID: hs9ViKuXogY""
  },
  {
    "{": ""      ""Video ID: Irlrm_xvuF0""
  },
  {
    "{": ""      ""Video ID: nXlujTM9NyE""
  },
  {
    "{": ""      ""Video ID: NaasH5cjG4I""
  },
  {
    "{": ""      ""Video ID: kKV5oirFSpE""
  },
  {
    "{": ""      ""Video ID: 3oCURtAXfWs""
  },
  {
    "{": ""      ""Video ID: 5HOn8cMhJM8""
  },
  {
    "{": ""      ""Video ID: kiZC_WrCqKk""
  },
  {
    "{": ""      ""Video ID: VhLysEyHoBE""
  },
  {
    "{": ""      ""Video ID: _GwmSHnF08E""
  },
  {
    "{": ""      ""Video ID: hcyw9QJwfY0""
  },
  {
    "{": ""      ""Video ID: UgxinEBj1xQ""
  },
  {
    "{": ""      ""Video ID: DPoGfKiNd3I""
  },
  {
    "{": ""      ""Video ID: YXCWaRSIl1Y""
  },
  {
    "{": ""      ""Video ID: O6NTJzIb4NQ""
  },
  {
    "{": ""      ""Video ID: MpvI8Grnl2w""
  },
  {
    "{": ""      ""Video ID: B14zObkPoIg""
  },
  {
    "{": ""      ""Video ID: plFJcF7hV_c""
  },
  {
    "{": ""      ""Video ID: DeMLsu8fDBk""
  },
  {
    "{": ""      ""Video ID: E7ho54jJtAY""
  },
  {
    "{": ""      ""Video ID: 1FijKc4_0NQ""
  },
  {
    "{": ""      ""Video ID: x9gYDnC9jNs""
  },
  {
    "{": ""      ""Video ID: dGgNoLB-MHI""
  },
  {
    "{": ""      ""Video ID: 8GJMCurbiFw""
  },
  {
    "{": ""      ""Video ID: QahDhc0WQao""
  },
  {
    "{": ""      ""Video ID: P9gE-SH5Bsg""
  },
  {
    "{": ""      ""Video ID: TuHo_eYKJA8""
  },
  {
    "{": ""      ""Video ID: wSFuxF6Q_xc""
  },
  {
    "{": ""      ""Video ID: _ykusARrWXc""
  },
  {
    "{": ""      ""Video ID: -Sv4PCUNz7E""
  },
  {
    "{": ""      ""Video ID: QVUI66Nfbiw""
  },
  {
    "{": ""      ""Video ID: 46AnrxVMhTQ""
  },
  {
    "{": ""      ""Video ID: gCYfPwDLc48""
  },
  {
    "{": ""      ""Video ID: SPwh_TgKLnA""
  },
  {
    "{": ""      ""Video ID: _Gj8WPnYdNg""
  },
  {
    "{": ""      ""Video ID: eEA1HuKvzHQ""
  },
  {
    "{": ""      ""Video ID: kvIqJGxfvdM""
  },
  {
    "{": ""      ""Video ID: USxEawBrkA4""
  },
  {
    "{": ""      ""Video ID: b-ZLouxYCbo""
  },
  {
    "{": ""      ""Video ID: vjaBR-8UWlk""
  },
  {
    "{": ""      ""Video ID: 6QIPIKOfMaM""
  },
  {
    "{": ""      ""Video ID: Pn9xhz3A_Zo""
  },
  {
    "{": ""      ""Video ID: xOXl83hPByE""
  },
  {
    "{": ""      ""Video ID: KU7OAHY4oYY""
  },
  {
    "{": ""      ""Video ID: vIC4IprMgTM""
  },
  {
    "{": ""      ""Video ID: jqU06v9cyYE""
  },
  {
    "{": ""      ""Video ID: Al3L8N140Xg""
  },
  {
    "{": ""      ""Video ID: mDjUrCbH1yo""
  },
  {
    "{": ""      ""Video ID: Br7N6ITeO5w""
  },
  {
    "{": ""      ""Video ID: ooH80diDEXk""
  },
  {
    "{": ""      ""Video ID: iMbx27eRDEo""
  },
  {
    "{": ""      ""Video ID: rfEhvdcOeUo""
  },
  {
    "{": ""      ""Video ID: I__3n9GqbBs""
  },
  {
    "{": ""      ""Video ID: hKhKd8E9xnU""
  },
  {
    "{": ""      ""Video ID: NDXhbFDLjmQ""
  },
  {
    "{": ""      ""Video ID: XppwWakzkkU""
  },
  {
    "{": ""      ""Video ID: oS_racAIjDI""
  },
  {
    "{": ""      ""Video ID: 8uk2wBWFptY""
  },
  {
    "{": ""      ""Video ID: G-9muHdgemI""
  },
  {
    "{": ""      ""Video ID: yRWlyw7Z-bU""
  },
  {
    "{": ""      ""Video ID: aJeBfcpT3HE""
  },
  {
    "{": ""      ""Video ID: vmQfO6NdVTk""
  },
  {
    "{": ""      ""Video ID: 2rryIZ93cyE""
  },
  {
    "{": ""      ""Video ID: up-F6Ztstgk""
  },
  {
    "{": ""      ""Video ID: 5y070jbJuVs""
  },
  {
    "{": ""      ""Video ID: VZXGHVlUsdA""
  },
  {
    "{": ""      ""Video ID: fkzNOEiW4M8""
  },
  {
    "{": ""      ""Video ID: GMc2RdFuOxI""
  },
  {
    "{": ""      ""Video ID: vvTF6B5XKxQ""
  },
  {
    "{": ""      ""Video ID: Ed9CYDt99tA""
  },
  {
    "{": ""      ""Video ID: XVo9GKAvmOw""
  },
  {
    "{": ""      ""Video ID: AeKKeiXTBos""
  },
  {
    "{": ""      ""Video ID: 4ai0KGSOWXk""
  },
  {
    "{": ""      ""Video ID: Mvh7J-sFtAc""
  },
  {
    "{": ""      ""Video ID: Xhr6_7z_YPI""
  },
  {
    "{": ""      ""Video ID: q8mUlfV5mIs""
  },
  {
    "{": ""      ""Video ID: lDwAo32GiR4""
  },
  {
    "{": ""      ""Video ID: Rxv8SS1XU_8""
  },
  {
    "{": ""      ""Video ID: jJQvok-LXMg""
  },
  {
    "{": ""      ""Video ID: _F9TvIJA2cw""
  },
  {
    "{": ""      ""Video ID: dzm1FUfdBgA""
  },
  {
    "{": ""      ""Video ID: 6dHcdSSvT6c""
  },
  {
    "{": ""      ""Video ID: 7KLiUrbi76k""
  },
  {
    "{": ""      ""Video ID: 7aL8JbELarg""
  },
  {
    "{": ""      ""Video ID: n1VO7Demm4c""
  },
  {
    "{": ""      ""Video ID: P4f0atGC_0o""
  },
  {
    "{": ""      ""Video ID: myYby1E0wWk""
  },
  {
    "{": ""      ""Video ID: jjyUXrNXpsw""
  },
  {
    "{": ""      ""Video ID: Brx73lv2l1A""
  },
  {
    "{": ""      ""Video ID: FIeZWbQGrqY""
  },
  {
    "{": ""      ""Video ID: Wmz5Ke80vZ8""
  },
  {
    "{": ""      ""Video ID: j-mHlMH6rBE""
  },
  {
    "{": ""      ""Video ID: ALqVNUHs-30""
  },
  {
    "{": ""      ""Video ID: DUZxy04rSK0""
  },
  {
    "{": ""      ""Video ID: qmqX8__xGiE""
  },
  {
    "{": ""      ""Video ID: 9ddYCZ_7_Xo""
  },
  {
    "{": ""      ""Video ID: LmNTr5hWCPY""
  },
  {
    "{": ""      ""Video ID: -DJYofEbdKI""
  },
  {
    "{": ""      ""Video ID: oweLOqYsIZc""
  },
  {
    "{": ""      ""Video ID: rQRCFXKIw6w""
  },
  {
    "{": ""      ""Video ID: s5pgVh1Hodk""
  },
  {
    "{": ""      ""Video ID: eoHyf_J6JZ4""
  },
  {
    "{": ""      ""Video ID: lWbsCLrEaZ4""
  },
  {
    "{": ""      ""Video ID: mmzd-RM0tX0""
  },
  {
    "{": ""      ""Video ID: FkD1XZA7qRA""
  },
  {
    "{": ""      ""Video ID: v-ZuGRWyBJE""
  },
  {
    "{": ""      ""Video ID: qEMtphIwbg0""
  },
  {
    "{": ""      ""Video ID: QdGlhoI68Kg""
  },
  {
    "{": ""      ""Video ID: CmsL5JEYCtQ""
  },
  {
    "{": ""      ""Video ID: fhZr5rs2Z3o""
  },
  {
    "{": ""      ""Video ID: vmjteg0tjKA""
  },
  {
    "{": ""      ""Video ID: uc8ZDzyQZCk""
  },
  {
    "{": ""      ""Video ID: cwTb_RgEE9g""
  },
  {
    "{": ""      ""Video ID: G_C65chapxo""
  },
  {
    "{": ""      ""Video ID: fLWNWEsk5Gc""
  },
  {
    "{": ""      ""Video ID: dpwIqwIC_mU""
  },
  {
    "{": ""      ""Video ID: I6PuZwJwato""
  },
  {
    "{": ""      ""Video ID: wIECny0iPvU""
  },
  {
    "{": ""      ""Video ID: SZ82eS_TlF4""
  },
  {
    "{": ""      ""Video ID: hBvs4k7a3GQ""
  },
  {
    "{": ""      ""Video ID: qc0sTncVXnk""
  },
  {
    "{": ""      ""Video ID: jy7Hm6ApX48""
  },
  {
    "{": ""      ""Video ID: f_0UaInDjU0""
  },
  {
    "{": ""      ""Video ID: tBSYt5XQwA4""
  },
  {
    "{": ""      ""Video ID: 0qVDvw6hXiI""
  },
  {
    "{": ""      ""Video ID: hVx8wFMUD3E""
  },
  {
    "{": ""      ""Video ID: GyncFUv-S8A""
  },
  {
    "{": ""      ""Video ID: IQx7IoVY4Sc""
  },
  {
    "{": ""      ""Video ID: wcTPQbJlamM""
  },
  {
    "{": ""      ""Video ID: _GIIz_VhVzM""
  },
  {
    "{": ""      ""Video ID: GArO6v09F4E""
  },
  {
    "{": ""      ""Video ID: gii7lTynsWE""
  },
  {
    "{": ""      ""Video ID: 1EjSInJbKZM""
  },
  {
    "{": ""      ""Video ID: gIlCkl4ZZfQ""
  },
  {
    "{": ""      ""Video ID: EzA7RnLxoQY""
  },
  {
    "{": ""      ""Video ID: 8-gpSqbxM4Y""
  },
  {
    "{": ""      ""Video ID: FyMYL9BUG5M""
  },
  {
    "{": ""      ""Video ID: 8WzKnNQEeI8""
  },
  {
    "{": ""      ""Video ID: SxeFScZkNHk""
  },
  {
    "{": ""      ""Video ID: 6efQ_GyQW3o""
  },
  {
    "{": ""      ""Video ID: TbA0_5ERhZs""
  },
  {
    "{": ""      ""Video ID: OPcfkJj36nc""
  },
  {
    "{": ""      ""Video ID: _-crLQfA3_Q""
  },
  {
    "{": ""      ""Video ID: dHURlzV5FEc""
  },
  {
    "{": ""      ""Video ID: aSZ567BPH3E""
  },
  {
    "{": ""      ""Video ID: OOqOWhfFW2U""
  },
  {
    "{": ""      ""Video ID: 54xF8QL8GzA""
  },
  {
    "{": ""      ""Video ID: Ld8q-3UHrW8""
  },
  {
    "{": ""      ""Video ID: Waol3RjY9L0""
  },
  {
    "{": ""      ""Video ID: L_ZoPwHjamc""
  },
  {
    "{": ""      ""Video ID: hqsVXIhwAzA""
  },
  {
    "{": ""      ""Video ID: e-O9KXXw2oE""
  },
  {
    "{": ""      ""Video ID: lVbe8AK6_58""
  },
  {
    "{": ""      ""Video ID: dSzYd7nAySo""
  },
  {
    "{": ""      ""Video ID: JcdNX8_KjlI""
  },
  {
    "{": ""      ""Video ID: XdOm19CAkYc""
  },
  {
    "{": ""      ""Video ID: pzQal2UwNlU""
  },
  {
    "{": ""      ""Video ID: HJWp_1kVM7g""
  },
  {
    "{": ""      ""Video ID: 5MIXfNhJ_8s""
  },
  {
    "{": ""      ""Video ID: 9MtKjIqLtgc""
  },
  {
    "{": ""      ""Video ID: hnwS6ctsJ7E""
  },
  {
    "{": ""      ""Video ID: DzxOK21kXms""
  },
  {
    "{": ""      ""Video ID: O6FOHfHcEM4""
  },
  {
    "{": ""      ""Video ID: n-5YsB2MwpI""
  },
  {
    "{": ""      ""Video ID: VGH5uiR5DhU""
  },
  {
    "{": ""      ""Video ID: 3nZt4-A7Ftk""
  },
  {
    "{": ""      ""Video ID: wzWP11y_qME""
  },
  {
    "{": ""      ""Video ID: wjzli1rApRw""
  },
  {
    "{": ""      ""Video ID: M3DKAj_GV54""
  },
  {
    "{": ""      ""Video ID: Znfa561GOBs""
  },
  {
    "{": ""      ""Video ID: uA37wIafUz8""
  },
  {
    "{": ""      ""Video ID: gxh-lAgzcgg""
  },
  {
    "{": ""      ""Video ID: aySJEwlXB3Q""
  },
  {
    "{": ""      ""Video ID: UekFnp_f01o""
  },
  {
    "{": ""      ""Video ID: L6JLsNVaees""
  },
  {
    "{": ""      ""Video ID: CSWUu3e581o""
  },
  {
    "{": ""      ""Video ID: vT6vtvqu_Kc""
  },
  {
    "{": ""      ""Video ID: waM7mW1g4Lw""
  },
  {
    "{": ""      ""Video ID: qtt3EJ2WEtM""
  },
  {
    "{": ""      ""Video ID: mrlTDIaICQI""
  },
  {
    "{": ""      ""Video ID: -HzxOb9YSrY""
  },
  {
    "{": ""      ""Video ID: KtqVXo_80VA""
  },
  {
    "{": ""      ""Video ID: fXmcoMm6Hg8""
  },
  {
    "{": ""      ""Video ID: a-nAOFgTfQM""
  },
  {
    "{": ""      ""Video ID: 2d-S4S-16EM""
  },
  {
    "{": ""      ""Video ID: gORJFfyAEHA""
  },
  {
    "{": ""      ""Video ID: JRVOt5As9Hk""
  },
  {
    "{": ""      ""Video ID: 3GaredpYGyc""
  },
  {
    "{": ""      ""Video ID: ZND3ErUJtuc""
  },
  {
    "{": ""      ""Video ID: -6qopxtoApo""
  },
  {
    "{": ""      ""Video ID: lmUGJ3Jh7fc""
  },
  {
    "{": ""      ""Video ID: 8ipTPOd-PKA""
  },
  {
    "{": ""      ""Video ID: cTfHmwWT4kM""
  },
  {
    "{": ""      ""Video ID: QFtvY0E9QJ8""
  },
  {
    "{": ""      ""Video ID: oeZQ737o2gI""
  },
  {
    "{": ""      ""Video ID: BRtHo6VWfn0""
  },
  {
    "{": ""      ""Video ID: Kvo5F-nElDY""
  },
  {
    "{": ""      ""Video ID: H2fmMrAihpc""
  },
  {
    "{": ""      ""Video ID: TyI0wbTQcao""
  },
  {
    "{": ""      ""Video ID: pnFXqGzYIXo""
  },
  {
    "{": ""      ""Video ID: djZaaM2pqyM""
  },
  {
    "{": ""      ""Video ID: lVXq-qdfv1w""
  },
  {
    "{": ""      ""Video ID: fl1SJeKr7S8""
  },
  {
    "{": ""      ""Video ID: St3sNdQWSlY""
  },
  {
    "{": ""      ""Video ID: HGST5pl338k""
  },
  {
    "{": ""      ""Video ID: z1iLwurM-lA""
  },
  {
    "{": ""      ""Video ID: CpncYhTQcb0""
  },
  {
    "{": ""      ""Video ID: KWy9s2TavJw""
  },
  {
    "{": ""      ""Video ID: NrgMjJtIj1g""
  },
  {
    "{": ""      ""Video ID: wAzZ7A7z2Q0""
  },
  {
    "{": ""      ""Video ID: _WrwViLw9xw""
  },
  {
    "{": ""      ""Video ID: fTB1_LcBko0""
  },
  {
    "{": ""      ""Video ID: K3dOMDyCboQ""
  },
  {
    "{": ""      ""Video ID: igcnhhESuas""
  },
  {
    "{": ""      ""Video ID: KFtBySy94ao""
  },
  {
    "{": ""      ""Video ID: OOKPsc6D7js""
  },
  {
    "{": ""      ""Video ID: HoPnGjHesJM""
  },
  {
    "{": ""      ""Video ID: aoKhtmq00js""
  },
  {
    "{": ""      ""Video ID: Wn4kKtvEymY""
  },
  {
    "{": ""      ""Video ID: Ckcacl9zJRI""
  },
  {
    "{": ""      ""Video ID: wu1cMNJe9Mw""
  },
  {
    "{": ""      ""Video ID: 5dSRXS53sdk""
  },
  {
    "{": ""      ""Video ID: XuvTCRqsqjc""
  },
  {
    "{": ""      ""Video ID: dRUhJkZQorI""
  },
  {
    "{": ""      ""Video ID: s8fsY5xTIAw""
  },
  {
    "{": ""      ""Video ID: IZjGwwC8ssc""
  },
  {
    "{": ""      ""Video ID: 23PYDcyBkC0""
  },
  {
    "{": ""      ""Video ID: WS4sz6lRBhg""
  },
  {
    "{": ""      ""Video ID: K7VOb4OD7ok""
  },
  {
    "{": ""      ""Video ID: jFzAsqveT0w""
  },
  {
    "{": ""      ""Video ID: -JlAX3vtivs""
  },
  {
    "{": ""      ""Video ID: gZAxT5Uc7Bs""
  },
  {
    "{": ""      ""Video ID: 7Md6xVb1JlM""
  },
  {
    "{": ""      ""Video ID: B9Z5wLJ7BUE""
  },
  {
    "{": ""      ""Video ID: 90vG3fHwDjA""
  },
  {
    "{": ""      ""Video ID: l-EwctgufVw""
  },
  {
    "{": ""      ""Video ID: qYgx2Ofsthc""
  },
  {
    "{": ""      ""Video ID: WyX80j9P4ng""
  },
  {
    "{": ""      ""Video ID: ZAXz8Is0WqM""
  },
  {
    "{": ""      ""Video ID: 8TvnrbypZYs""
  },
  {
    "{": ""      ""Video ID: zGydbRbndLI""
  },
  {
    "{": ""      ""Video ID: 15TBCg3XX5Q""
  },
  {
    "{": ""      ""Video ID: KZlPB2QUp5k""
  },
  {
    "{": ""      ""Video ID: YkjhL70f6gY""
  },
  {
    "{": ""      ""Video ID: qT0ZTYHg3nc""
  },
  {
    "{": ""      ""Video ID: 2xnQIb9b3IQ""
  },
  {
    "{": ""      ""Video ID: luNM0rJH-hY""
  },
  {
    "{": ""      ""Video ID: KuKM30xg6x8""
  },
  {
    "{": ""      ""Video ID: KDOXN0dlkf8""
  },
  {
    "{": ""      ""Video ID: HNilO4XLkVg""
  },
  {
    "{": ""      ""Video ID: pmE_2YKe3-U""
  },
  {
    "{": ""      ""Video ID: qjlwX-4M3Fc""
  },
  {
    "{": ""      ""Video ID: tRE4UHr9U-8""
  },
  {
    "{": ""      ""Video ID: ZXJF8NKFPzI""
  },
  {
    "{": ""      ""Video ID: kWlJBWWwF_k""
  },
  {
    "{": ""      ""Video ID: FhO2WZWifGA""
  },
  {
    "{": ""      ""Video ID: 9xZWJOK6qqc""
  },
  {
    "{": ""      ""Video ID: Rc4Ex0lOlMc""
  },
  {
    "{": ""      ""Video ID: MZqQNjvdm_w""
  },
  {
    "{": ""      ""Video ID: cKS1cKmsrCI""
  },
  {
    "{": ""      ""Video ID: aEMYL7liciQ""
  },
  {
    "{": ""      ""Video ID: DTxmZACa-cE""
  },
  {
    "{": ""      ""Video ID: BTu5HrxK4X4""
  },
  {
    "{": ""      ""Video ID: GMJoe-H7wps""
  },
  {
    "{": ""      ""Video ID: O7B0hfpCXN4""
  },
  {
    "{": ""      ""Video ID: GCpmnG7FPQY""
  },
  {
    "{": ""      ""Video ID: fa83eHgiF84""
  },
  {
    "{": ""      ""Video ID: bSZ7BBGSMsY""
  },
  {
    "{": ""      ""Video ID: LXFTrddQkk8""
  },
  {
    "{": ""      ""Video ID: _WcuRx-vlrU""
  },
  {
    "{": ""      ""Video ID: g3fEC1_xh-Y""
  },
  {
    "{": ""      ""Video ID: ym-J_g_iDVQ""
  },
  {
    "{": ""      ""Video ID: QrHa3cWv5RE""
  },
  {
    "{": ""      ""Video ID: kSaotRjtAJM""
  },
  {
    "{": ""      ""Video ID: JW7rMEz7aL4""
  },
  {
    "{": ""      ""Video ID: z0YBOgQf1TQ""
  },
  {
    "{": ""      ""Video ID: UIqIuOPs5PQ""
  },
  {
    "{": ""      ""Video ID: zfKNF3pkE70""
  },
  {
    "{": ""      ""Video ID: quMAEBTU7bM""
  },
  {
    "{": ""      ""Video ID: NKGRnmr0qPw""
  },
  {
    "{": ""      ""Video ID: qrjK9byo1wA""
  },
  {
    "{": ""      ""Video ID: z99y3BZQ0Wc""
  },
  {
    "{": ""      ""Video ID: 0VK6jhSpoRE""
  },
  {
    "{": ""      ""Video ID: XPQ9MgVGi2I""
  },
  {
    "{": ""      ""Video ID: _df9yyDAYtQ""
  },
  {
    "{": ""      ""Video ID: _gbhuDdjG_0""
  },
  {
    "{": ""      ""Video ID: A4DsYLqbvGc""
  },
  {
    "{": ""      ""Video ID: etrmZ0fwlJ8""
  },
  {
    "{": ""      ""Video ID: 6iv7zfKYj3Y""
  },
  {
    "{": ""      ""Video ID: kzp7C-4edJw""
  },
  {
    "{": ""      ""Video ID: 001GbymmPss""
  },
  {
    "{": ""      ""Video ID: r5sjRefB7NM""
  },
  {
    "{": ""      ""Video ID: fZhG0jwBUM4""
  },
  {
    "{": ""      ""Video ID: DjP3as-yrJQ""
  },
  {
    "{": ""      ""Video ID: i3s46n7DKAs""
  },
  {
    "{": ""      ""Video ID: kwZ3f27ev1M""
  },
  {
    "{": ""      ""Video ID: Sy8m0Ukq5Zg""
  },
  {
    "{": ""      ""Video ID: LV_A8RwqTac""
  },
  {
    "{": ""      ""Video ID: AyVMgjdsaCI""
  },
  {
    "{": ""      ""Video ID: mAeAWls7MAw""
  },
  {
    "{": ""      ""Video ID: L4xtZ0ov5Gg""
  },
  {
    "{": ""      ""Video ID: 4D4aYNS-4wg""
  },
  {
    "{": ""      ""Video ID: 91eKiCcluFk""
  },
  {
    "{": ""      ""Video ID: urukjceXh_I""
  },
  {
    "{": ""      ""Video ID: rW3hbhTqOVg""
  },
  {
    "{": ""      ""Video ID: OXyVdRMpfq0""
  },
  {
    "{": ""      ""Video ID: NWqyz4DN6Qo""
  },
  {
    "{": ""      ""Video ID: l1ipwPvyPho""
  },
  {
    "{": ""      ""Video ID: 6d9j95Fvo3o""
  },
  {
    "{": ""      ""Video ID: NmgpM1wBmCU""
  },
  {
    "{": ""      ""Video ID: sckFyUSnCk4""
  },
  {
    "{": ""      ""Video ID: 5J19XDEDj-s""
  },
  {
    "{": ""      ""Video ID: nZrw204TmE8""
  },
  {
    "{": ""      ""Video ID: Yq6Q3r1HzFI""
  },
  {
    "{": ""      ""Video ID: XznUU0fEvUI""
  },
  {
    "{": ""      ""Video ID: 5RpmfZLwHE0""
  },
  {
    "{": ""      ""Video ID: FL4Mwrpz1sk""
  },
  {
    "{": ""      ""Video ID: GQjC-PG9UXY""
  },
  {
    "{": ""      ""Video ID: mS_ppOlgx30""
  },
  {
    "{": ""      ""Video ID: ckuvjTAk7lk""
  },
  {
    "{": ""      ""Video ID: QFV_4qoR7kY""
  },
  {
    "{": ""      ""Video ID: EczFOGEVK2Y""
  },
  {
    "{": ""      ""Video ID: MoEcE5AKZSQ""
  },
  {
    "{": ""      ""Video ID: JhDsDNg0mAo""
  },
  {
    "{": ""      ""Video ID: V49VLE8N1lg""
  },
  {
    "{": ""      ""Video ID: d1f4Wf4_g9s""
  },
  {
    "{": ""      ""Video ID: iir2ZQEEbLA""
  },
  {
    "{": ""      ""Video ID: UmOaBU67TWU""
  },
  {
    "{": ""      ""Video ID: b3l7fotSQ6M""
  },
  {
    "{": ""      ""Video ID: UnP7USp2zZM""
  },
  {
    "{": ""      ""Video ID: nCD4i0S7l4Y""
  },
  {
    "{": ""      ""Video ID: JcoUdFIEJbI""
  },
  {
    "{": ""      ""Video ID: DJnUG8FK2xc""
  },
  {
    "{": ""      ""Video ID: rbFIdyENQbo""
  },
  {
    "{": ""      ""Video ID: z0NdrnaFqU0""
  },
  {
    "{": ""      ""Video ID: YwQuYbZvVqs""
  },
  {
    "{": ""      ""Video ID: qHnTtYhCbX4""
  },
  {
    "{": ""      ""Video ID: T4AHjbOod4Q""
  },
  {
    "{": ""      ""Video ID: 8vY0TgU9uiQ""
  },
  {
    "{": ""      ""Video ID: UtWe7WNgf0Q""
  },
  {
    "{": ""      ""Video ID: _i52c09Jp3U""
  },
  {
    "{": ""      ""Video ID: nBQLUd14jUA""
  },
  {
    "{": ""      ""Video ID: 4qhbB_DC59M""
  },
  {
    "{": ""      ""Video ID: _W17UoFYMIc""
  },
  {
    "{": ""      ""Video ID: At1wibQuht8""
  },
  {
    "{": ""      ""Video ID: sxdz9kjEwtI""
  },
  {
    "{": ""      ""Video ID: q98Nxy61yQM""
  },
  {
    "{": ""      ""Video ID: mulIo25fhlk""
  },
  {
    "{": ""      ""Video ID: VyvYKHwC7eU""
  },
  {
    "{": ""      ""Video ID: N4PH7bp15EY""
  },
  {
    "{": ""      ""Video ID: fdzhFEsLb2Q""
  },
  {
    "{": ""      ""Video ID: bmEinAb_LeE""
  },
  {
    "{": ""      ""Video ID: ELQ2iokZQR4""
  },
  {
    "{": ""      ""Video ID: 51rMnTjRXN8""
  },
  {
    "{": ""      ""Video ID: G0TiKxphw9I""
  },
  {
    "{": ""      ""Video ID: BBmKenpHgBY""
  },
  {
    "{": ""      ""Video ID: Twxmr9Za-WY""
  },
  {
    "{": ""      ""Video ID: tYuhzkK_d00""
  },
  {
    "{": ""      ""Video ID: iFZljV-D5BY""
  },
  {
    "{": ""      ""Video ID: zR1odqAG5CY""
  },
  {
    "{": ""      ""Video ID: soxGlmCrTOM""
  },
  {
    "{": ""      ""Video ID: RJ-j1TsMnZA""
  },
  {
    "{": ""      ""Video ID: ELL49Dcvqgg""
  },
  {
    "{": ""      ""Video ID: IwZOXKOdBug""
  },
  {
    "{": ""      ""Video ID: Y2elyw7pckI""
  },
  {
    "{": ""      ""Video ID: t6KDmbq1sc0""
  },
  {
    "{": ""      ""Video ID: RoHR1zveagI""
  },
  {
    "{": ""      ""Video ID: F9eYyDaQwQY""
  },
  {
    "{": ""      ""Video ID: 00BONBEpy84""
  },
  {
    "{": ""      ""Video ID: Tr1qee-bTZI""
  },
  {
    "{": ""      ""Video ID: jx-8WU0fEwY""
  },
  {
    "{": ""      ""Video ID: 2NWfI6Wc8Qk""
  },
  {
    "{": ""      ""Video ID: ngIVF1hhzKA""
  },
  {
    "{": ""      ""Video ID: Qgj1XHeJNsA""
  },
  {
    "{": ""      ""Video ID: eAe6-DlIAlo""
  },
  {
    "{": ""      ""Video ID: I7bhFGOee5s""
  },
  {
    "{": ""      ""Video ID: 6Gj2Zer8iBc""
  },
  {
    "{": ""      ""Video ID: XO-aLeiE_Pg""
  },
  {
    "{": ""      ""Video ID: 72qSFrYhVpA""
  },
  {
    "{": ""      ""Video ID: wYGa1-zB8so""
  },
  {
    "{": ""      ""Video ID: kJ59rvPGe_4""
  },
  {
    "{": ""      ""Video ID: xfHccAAYTrg""
  },
  {
    "{": ""      ""Video ID: UOWKZdJ3g24""
  },
  {
    "{": ""      ""Video ID: alySPq-T9Ng""
  },
  {
    "{": ""      ""Video ID: tZ2ZPeN-6wI""
  },
  {
    "{": ""      ""Video ID: gYFQEC9IGv8""
  },
  {
    "{": ""      ""Video ID: _6tQ1_G7zM8""
  },
  {
    "{": ""      ""Video ID: l3UAgaz-njA""
  },
  {
    "{": ""      ""Video ID: 7SWWiAjPFBM""
  },
  {
    "{": ""      ""Video ID: 9i6TiY0AHlo""
  },
  {
    "{": ""      ""Video ID: ylkyOn_cc14""
  },
  {
    "{": ""      ""Video ID: WrAAvh8REts""
  },
  {
    "{": ""      ""Video ID: JJnaqiSvy60""
  },
  {
    "{": ""      ""Video ID: 3zqHYKuR-gA""
  },
  {
    "{": ""      ""Video ID: eGEBO_L6LKQ""
  },
  {
    "{": ""      ""Video ID: kRePPzY48_E""
  },
  {
    "{": ""      ""Video ID: ReXck-u7E2k""
  },
  {
    "{": ""      ""Video ID: 3W8wDbRMTAc""
  },
  {
    "{": ""      ""Video ID: iPlAObap_J4""
  },
  {
    "{": ""      ""Video ID: mRO6s2U2LyE""
  },
  {
    "{": ""      ""Video ID: V-uqQc4X8Mk""
  },
  {
    "{": ""      ""Video ID: lHZuEAAbEXI""
  },
  {
    "{": ""      ""Video ID: QHZWPlFl_GY""
  },
  {
    "{": ""      ""Video ID: 4LHbq2pAFgM""
  },
  {
    "{": ""      ""Video ID: TUCGVRyZ1ZA""
  },
  {
    "{": ""      ""Video ID: PkX2Us287qs""
  },
  {
    "{": ""      ""Video ID: Lxb_Vc_KvrE""
  },
  {
    "{": ""      ""Video ID: AtyIUQ6-JIM""
  },
  {
    "{": ""      ""Video ID: niuHaMythyQ""
  },
  {
    "{": ""      ""Video ID: C07hfHWCclE""
  },
  {
    "{": ""      ""Video ID: 57I1dCz0hNk""
  },
  {
    "{": ""      ""Video ID: 4ScZ3B_ZC3M""
  },
  {
    "{": ""      ""Video ID: qy1SysZTJ2U""
  },
  {
    "{": ""      ""Video ID: A12z4tp5GHg""
  },
  {
    "{": ""      ""Video ID: dJBxdRIQx7Y""
  },
  {
    "{": ""      ""Video ID: 3yT95uIwEys""
  },
  {
    "{": ""      ""Video ID: q15SidjjS-I""
  },
  {
    "{": ""      ""Video ID: v4zHlgWEY4U""
  },
  {
    "{": ""      ""Video ID: hRCbJIxVRNk""
  },
  {
    "{": ""      ""Video ID: zvgwM2PZkGY""
  },
  {
    "{": ""      ""Video ID: onO6IIgY288""
  },
  {
    "{": ""      ""Video ID: q49tvlNmDvw""
  },
  {
    "{": ""      ""Video ID: 0wn6NJkLGZA""
  },
  {
    "{": ""      ""Video ID: 3RVPyvqrBIE""
  },
  {
    "{": ""      ""Video ID: 6zeWdYP_dUQ""
  },
  {
    "{": ""      ""Video ID: eo038Nsv3UA""
  },
  {
    "{": ""      ""Video ID: 77c-IpCbri4""
  },
  {
    "{": ""      ""Video ID: ECguzO6LoCA""
  },
  {
    "{": ""      ""Video ID: IoY3BJ5O0pc""
  },
  {
    "{": ""      ""Video ID: vMXpSVa3RiE""
  },
  {
    "{": ""      ""Video ID: E_T4N6CX8Q0""
  },
  {
    "{": ""      ""Video ID: PKyqkIuG7Kc""
  },
  {
    "{": ""      ""Video ID: e2RBzVhw5Vs""
  },
  {
    "{": ""      ""Video ID: revjjJBxn_Y""
  },
  {
    "{": ""      ""Video ID: oh8VEirnSnA""
  },
  {
    "{": ""      ""Video ID: 6GHfYMrirtg""
  },
  {
    "{": ""      ""Video ID: MTaMwA59Iy4""
  },
  {
    "{": ""      ""Video ID: 5j40tk9eJN4""
  },
  {
    "{": ""      ""Video ID: T9idg7djO5g""
  },
  {
    "{": ""      ""Video ID: _7lCJvugvXI""
  },
  {
    "{": ""      ""Video ID: U0qsF8Cu1BU""
  },
  {
    "{": ""      ""Video ID: sChxozkHcbw""
  },
  {
    "{": ""      ""Video ID: 066kObsJoqE""
  },
  {
    "{": ""      ""Video ID: fsf6zqzQSk8""
  },
  {
    "{": ""      ""Video ID: IWd3_nfh9c8""
  },
  {
    "{": ""      ""Video ID: GnxMmvlToSc""
  },
  {
    "{": ""      ""Video ID: V_0w5wexGzg""
  },
  {
    "{": ""      ""Video ID: Xhxm67gCP9Q""
  },
  {
    "{": ""      ""Video ID: 0ibwRgfJRb4""
  },
  {
    "{": ""      ""Video ID: KTmyQ84Tt5Q""
  },
  {
    "{": ""      ""Video ID: AqR3k77Vzg8""
  },
  {
    "{": ""      ""Video ID: wZy52y-NyGQ""
  },
  {
    "{": ""      ""Video ID: HhM0xPE7utQ""
  },
  {
    "{": ""      ""Video ID: -1d-xX0oZTU""
  },
  {
    "{": ""      ""Video ID: aSd44lg7sAw""
  },
  {
    "{": ""      ""Video ID: 0zrXm0S4cyg""
  },
  {
    "{": ""      ""Video ID: tlHQQ6uyUhU""
  },
  {
    "{": ""      ""Video ID: 0OSCRQdJboM""
  },
  {
    "{": ""      ""Video ID: nnIidFJk09M""
  },
  {
    "{": ""      ""Video ID: mr9-1hqSjoQ""
  },
  {
    "{": ""      ""Video ID: 44wS8z7CAFY""
  },
  {
    "{": ""      ""Video ID: RTtXkqDlqVU""
  },
  {
    "{": ""      ""Video ID: h91qc3TGXug""
  },
  {
    "{": ""      ""Video ID: gOvE8JA4H7w""
  },
  {
    "{": ""      ""Video ID: C3mq590Fv2k""
  },
  {
    "{": ""      ""Video ID: avUKl_lGolY""
  },
  {
    "{": ""      ""Video ID: 1RNRH2YX5Yk""
  },
  {
    "{": ""      ""Video ID: y7rONLxzAA4""
  },
  {
    "{": ""      ""Video ID: _xTD1QNVZsk""
  },
  {
    "{": ""      ""Video ID: tz_Q59qkGjo""
  },
  {
    "{": ""      ""Video ID: A4afYmsjPJA""
  },
  {
    "{": ""      ""Video ID: XTkCrWNc4x4""
  },
  {
    "{": ""      ""Video ID: BllfooQQcZM""
  },
  {
    "{": ""      ""Video ID: hkAvVM9ekCw""
  },
  {
    "{": ""      ""Video ID: __ZtO3ZOSEU""
  },
  {
    "{": ""      ""Video ID: YTGq1zz3zVU""
  },
  {
    "{": ""      ""Video ID: BfLvhwa2Nt0""
  },
  {
    "{": ""      ""Video ID: wV2raMLN3-4""
  },
  {
    "{": ""      ""Video ID: BYwuW1z4ZoA""
  },
  {
    "{": ""      ""Video ID: GjKejA5IFiU""
  },
  {
    "{": ""      ""Video ID: avPWaH-_F48""
  },
  {
    "{": ""      ""Video ID: F0KaAVVu2No""
  },
  {
    "{": ""      ""Video ID: RiMwL-hkjso""
  },
  {
    "{": ""      ""Video ID: 1NMe5uZxjQo""
  },
  {
    "{": ""      ""Video ID: D-ZIT37XfBg""
  },
  {
    "{": ""      ""Video ID: 41rfox9sbkM""
  },
  {
    "{": ""      ""Video ID: cKGqQU6WsK8""
  },
  {
    "{": ""      ""Video ID: BrRkSebOa1I""
  },
  {
    "{": ""      ""Video ID: RhYC3NTwFhc""
  },
  {
    "{": ""      ""Video ID: WzE1PeemmaU""
  },
  {
    "{": ""      ""Video ID: hHZD0fyI8j0""
  },
  {
    "{": ""      ""Video ID: XsBmV5sjneM""
  },
  {
    "{": ""      ""Video ID: hCl6xrREzSk""
  },
  {
    "{": ""      ""Video ID: VkaC_0OicFU""
  },
  {
    "{": ""      ""Video ID: t7Pnyb3frUg""
  },
  {
    "{": ""      ""Video ID: 5Ud4M7RGF2s""
  },
  {
    "{": ""      ""Video ID: 9v13bVSLdfo""
  },
  {
    "{": ""      ""Video ID: HtBpnu6OiSs""
  },
  {
    "{": ""      ""Video ID: G2SieS3Xfaw""
  },
  {
    "{": ""      ""Video ID: 8tztm9dLyY4""
  },
  {
    "{": ""      ""Video ID: dPzLb02DFHM""
  },
  {
    "{": ""      ""Video ID: 9E1ZmWIXaAE""
  },
  {
    "{": ""      ""Video ID: Rcgt2DDhmmE""
  },
  {
    "{": ""      ""Video ID: OIPZv_Uldhk""
  },
  {
    "{": ""      ""Video ID: CT12K2wI734""
  },
  {
    "{": ""      ""Video ID: Qw4mYkdjZLA""
  },
  {
    "{": ""      ""Video ID: g5nzEax87lw""
  },
  {
    "{": ""      ""Video ID: tz79d9_iFOc""
  },
  {
    "{": ""      ""Video ID: CjTRKbPJjrs""
  },
  {
    "{": ""      ""Video ID: vqCNhNcN0mA""
  },
  {
    "{": ""      ""Video ID: aZjZSQFJeVc""
  },
  {
    "{": ""      ""Video ID: lA7GtTT6u08""
  },
  {
    "{": ""      ""Video ID: -CnImIihIWs""
  },
  {
    "{": ""      ""Video ID: ZExmcRv9vek""
  },
  {
    "{": ""      ""Video ID: d1pLdr_Bg8s""
  },
  {
    "{": ""      ""Video ID: R1PJGJOYhqg""
  },
  {
    "{": ""      ""Video ID: g9R9RnTMw2w""
  },
  {
    "{": ""      ""Video ID: Ez4B75phq-U""
  },
  {
    "{": ""      ""Video ID: wq54zDv8Z84""
  },
  {
    "{": ""      ""Video ID: HSP3mK5W7-g""
  },
  {
    "{": ""      ""Video ID: KBh1LYb1g6E""
  },
  {
    "{": ""      ""Video ID: LR408nP99Io""
  },
  {
    "{": ""      ""Video ID: hl9bJ7u9qlE""
  },
  {
    "{": ""      ""Video ID: 4C-YqkvEvhk""
  },
  {
    "{": ""      ""Video ID: utAfui6ifSg""
  },
  {
    "{": ""      ""Video ID: zg6VM8EWH20""
  },
  {
    "{": ""      ""Video ID: paucykJ6SdA""
  },
  {
    "{": ""      ""Video ID: U8qOEMQ6iA8""
  },
  {
    "{": ""      ""Video ID: V_JDHzq23QY""
  },
  {
    "{": ""      ""Video ID: 1FELSbR3Wbg""
  },
  {
    "{": ""      ""Video ID: upFwpR4lU-4""
  },
  {
    "{": ""      ""Video ID: FrasvwCwVLg""
  },
  {
    "{": ""      ""Video ID: faS3Jb0gyxw""
  },
  {
    "{": ""      ""Video ID: iBjrKxdMPR8""
  },
  {
    "{": ""      ""Video ID: jmsU0egeJBI""
  },
  {
    "{": ""      ""Video ID: I0tzHkuiSGU""
  },
  {
    "{": ""      ""Video ID: nvTOcQOlXLQ""
  },
  {
    "{": ""      ""Video ID: b9-myfkdrpk""
  },
  {
    "{": ""      ""Video ID: TrYzy_UU2Ng""
  },
  {
    "{": ""      ""Video ID: OKcRPQCKLnw""
  },
  {
    "{": ""      ""Video ID: Q0BTrUIhiKk""
  },
  {
    "{": ""      ""Video ID: qQWgdFUhfN8""
  },
  {
    "{": ""      ""Video ID: 0VSFsQMkX4c""
  },
  {
    "{": ""      ""Video ID: czyR0aw_SP0""
  },
  {
    "{": ""      ""Video ID: 6kHlBBbns3U""
  },
  {
    "{": ""      ""Video ID: xQW96SXRiXo""
  },
  {
    "{": ""      ""Video ID: vzkWxn6KSvg""
  },
  {
    "{": ""      ""Video ID: z80S_r3ecZo""
  },
  {
    "{": ""      ""Video ID: 323RSjNBDEM""
  },
  {
    "{": ""      ""Video ID: CuOQ9WfXlWU""
  },
  {
    "{": ""      ""Video ID: 8IFV7neg16s""
  },
  {
    "{": ""      ""Video ID: wCXO7DB7HXo""
  },
  {
    "{": ""      ""Video ID: ZGQxmLwgUCg""
  },
  {
    "{": ""      ""Video ID: 8jIAVBENtR8""
  },
  {
    "{": ""      ""Video ID: HmCGEsxZ_RQ""
  },
  {
    "{": ""      ""Video ID: yMeEy39e4yE""
  },
  {
    "{": ""      ""Video ID: zpyFCPwEVj4""
  },
  {
    "{": ""      ""Video ID: ENfumfhqdeo""
  },
  {
    "{": ""      ""Video ID: PSrCUAcXir0""
  },
  {
    "{": ""      ""Video ID: YjQycqGbXmk""
  },
  {
    "{": ""      ""Video ID: oAAzAtxO1wg""
  },
  {
    "{": ""      ""Video ID: CCg5iMKAc0Y""
  },
  {
    "{": ""      ""Video ID: hLluh7yk9Yc""
  },
  {
    "{": ""      ""Video ID: __ghLE7QtnA""
  },
  {
    "{": ""      ""Video ID: VsgJnkBUUHk""
  },
  {
    "{": ""      ""Video ID: TtbCuan7SwY""
  },
  {
    "{": ""      ""Video ID: eAXZtr4cMjM""
  },
  {
    "{": ""      ""Video ID: 1Qtg0Gmv7J8""
  },
  {
    "{": ""      ""Video ID: D7WU56vvVWY""
  },
  {
    "{": ""      ""Video ID: J3x5Rmn60w0""
  },
  {
    "{": ""      ""Video ID: _CKj01LIWr4""
  },
  {
    "{": ""      ""Video ID: iqxr5OZIdj0""
  },
  {
    "{": ""      ""Video ID: Rv0AI3hjc7k""
  },
  {
    "{": ""      ""Video ID: hjwJl4t-DF8""
  },
  {
    "{": ""      ""Video ID: xuuDEXyDnZI""
  },
  {
    "{": ""      ""Video ID: r0If7gOXWJY""
  },
  {
    "{": ""      ""Video ID: ZH0a6TYWkkY""
  },
  {
    "{": ""      ""Video ID: RoZciw_Nqe0""
  },
  {
    "{": ""      ""Video ID: L3ULR0RROPo""
  },
  {
    "{": ""      ""Video ID: VLKC_shCTq4""
  },
  {
    "{": ""      ""Video ID: ZyRgX_OpgEk""
  },
  {
    "{": ""      ""Video ID: Qe_mS_ucYCM""
  },
  {
    "{": ""      ""Video ID: RPzbBQwKegg""
  },
  {
    "{": ""      ""Video ID: HLt532ClzuI""
  },
  {
    "{": ""      ""Video ID: rijSlGYxEk4""
  },
  {
    "{": ""      ""Video ID: QibDTrZirBE""
  },
  {
    "{": ""      ""Video ID: 1Cou8l_d6Y4""
  },
  {
    "{": ""      ""Video ID: UBWRO0TlCn4""
  },
  {
    "{": ""      ""Video ID: ngWb3oyUSow""
  },
  {
    "{": ""      ""Video ID: QNcJD7O1qUE""
  },
  {
    "{": ""      ""Video ID: UqkJstRAR0Y""
  },
  {
    "{": ""      ""Video ID: ZwBJ8SHB42U""
  },
  {
    "{": ""      ""Video ID: jG-L5g4_dng""
  },
  {
    "{": ""      ""Video ID: FrfQl_T_uTg""
  },
  {
    "{": ""      ""Video ID: B8ifU-trbzI""
  },
  {
    "{": ""      ""Video ID: XGAhXocWGCk""
  },
  {
    "{": ""      ""Video ID: EWDxnayeC8I""
  },
  {
    "{": ""      ""Video ID: PcxPHoJ9il0""
  },
  {
    "{": ""      ""Video ID: srrbvNNUKrA""
  },
  {
    "{": ""      ""Video ID: VD5Ah6ZgVpk""
  },
  {
    "{": ""      ""Video ID: lEXvYqSVNN4""
  },
  {
    "{": ""      ""Video ID: b694exl_oZo""
  },
  {
    "{": ""      ""Video ID: B16LnWPFZ7k""
  },
  {
    "{": ""      ""Video ID: VZdU-d9RL0A""
  },
  {
    "{": ""      ""Video ID: drhoArQAXDg""
  },
  {
    "{": ""      ""Video ID: tuu8FmiXX-4""
  },
  {
    "{": ""      ""Video ID: 4IwXHjQ0pR0""
  },
  {
    "{": ""      ""Video ID: O1o54mAuo6o""
  },
  {
    "{": ""      ""Video ID: QpHLEDBON3k""
  },
  {
    "{": ""      ""Video ID: uFL59k_2AOw""
  },
  {
    "{": ""      ""Video ID: fJXd2KLzb68""
  },
  {
    "{": ""      ""Video ID: hKcShDTYb4Q""
  },
  {
    "{": ""      ""Video ID: QQoP2hcqEdY""
  },
  {
    "{": ""      ""Video ID: iQVH5rrqkFY""
  },
  {
    "{": ""      ""Video ID: l1DTQuUkqCE""
  },
  {
    "{": ""      ""Video ID: UVJCmUPiyEM""
  },
  {
    "{": ""      ""Video ID: 8S4yD8mkbPQ""
  },
  {
    "{": ""      ""Video ID: vnkHXhuFN64""
  },
  {
    "{": ""      ""Video ID: ioNjbsjAZ8k""
  },
  {
    "{": ""      ""Video ID: fcS7-Xu7uP8""
  },
  {
    "{": ""      ""Video ID: lL0CWKk8P9E""
  },
  {
    "{": ""      ""Video ID: 1m9oOJcRNps""
  },
  {
    "{": ""      ""Video ID: 3A0fhzkAJ7E""
  },
  {
    "{": ""      ""Video ID: YVpZz_dx25A""
  },
  {
    "{": ""      ""Video ID: OIqLS3xOuRI""
  },
  {
    "{": ""      ""Video ID: gHnd-04XqY8""
  },
  {
    "{": ""      ""Video ID: YUTMdLBHEuw""
  },
  {
    "{": ""      ""Video ID: OfBk9h3RYnc""
  },
  {
    "{": ""      ""Video ID: 4yyxIUNOlrI""
  },
  {
    "{": ""      ""Video ID: L4UusytMXWA""
  },
  {
    "{": ""      ""Video ID: uM7w-qBtz3U""
  },
  {
    "{": ""      ""Video ID: Wj9_miATMzw""
  },
  {
    "{": ""      ""Video ID: aS1iUd3UzAg""
  },
  {
    "{": ""      ""Video ID: XK3VAAm1GrY""
  },
  {
    "{": ""      ""Video ID: c9IJI5YInF8""
  },
  {
    "{": ""      ""Video ID: DAbpafh2Rjg""
  },
  {
    "{": ""      ""Video ID: icaHyUxR108""
  },
  {
    "{": ""      ""Video ID: MwKzyqYVSOE""
  },
  {
    "{": ""      ""Video ID: aKnZ5Oy5-Ic""
  },
  {
    "{": ""      ""Video ID: 7LTEFt6MwHY""
  },
  {
    "{": ""      ""Video ID: L83eh5-SfZc""
  },
  {
    "{": ""      ""Video ID: ZkG6R7-BchQ""
  },
  {
    "{": ""      ""Video ID: FzlRDQZj5v0""
  },
  {
    "{": ""      ""Video ID: mXKAYeureSA""
  },
  {
    "{": ""      ""Video ID: MFGWfTj-oWA""
  },
  {
    "{": ""      ""Video ID: svTYc1C9uLQ""
  },
  {
    "{": ""      ""Video ID: kMKl1Rh2lIU""
  },
  {
    "{": ""      ""Video ID: z9HGzi6-bl8""
  },
  {
    "{": ""      ""Video ID: 1dAJ7Hw0VAU""
  },
  {
    "{": ""      ""Video ID: EQo06jihwf8""
  },
  {
    "{": ""      ""Video ID: NZHuCj7E_D0""
  },
  {
    "{": ""      ""Video ID: 1_2APhTdPS8""
  },
  {
    "{": ""      ""Video ID: O0d1N8tnJyc""
  },
  {
    "{": ""      ""Video ID: n8eaZ-RSxa8""
  },
  {
    "{": ""      ""Video ID: IAlUVJ4cvIE""
  },
  {
    "{": ""      ""Video ID: iGQdoeoORxM""
  },
  {
    "{": ""      ""Video ID: KBVuNRK9CI0""
  },
  {
    "{": ""      ""Video ID: VGWpUTSnlZU""
  },
  {
    "{": ""      ""Video ID: 7mv2OtGTcsE""
  },
  {
    "{": ""      ""Video ID: dKx8G1KLWAQ""
  },
  {
    "{": ""      ""Video ID: 9Z08iScdM0I""
  },
  {
    "{": ""      ""Video ID: nwoCkBch_7k""
  },
  {
    "{": ""      ""Video ID: W8Qecrp-iNo""
  },
  {
    "{": ""      ""Video ID: lhx_RWVHURY""
  },
  {
    "{": ""      ""Video ID: nD5QwOWj3jE""
  },
  {
    "{": ""      ""Video ID: YTOEzYDGYFI""
  },
  {
    "{": ""      ""Video ID: BshW4vposLk""
  },
  {
    "{": ""      ""Video ID: cPAo3bxT4_Q""
  },
  {
    "{": ""      ""Video ID: wI2R24BLvWY""
  },
  {
    "{": ""      ""Video ID: f7zA_Z6m-DI""
  },
  {
    "{": ""      ""Video ID: R3nqSC-w3Zw""
  },
  {
    "{": ""      ""Video ID: 6J5VyhE6X7A""
  },
  {
    "{": ""      ""Video ID: VgYeFxSLERA""
  },
  {
    "{": ""      ""Video ID: 6KtMLKsLnn0""
  },
  {
    "{": ""      ""Video ID: MsIHTo3RQ2U""
  },
  {
    "{": ""      ""Video ID: vmcYYKZCfaE""
  },
  {
    "{": ""      ""Video ID: bDuAMahtYwA""
  },
  {
    "{": ""      ""Video ID: 2MfOWUKNJic""
  },
  {
    "{": ""      ""Video ID: Hr0IU2GidFw""
  },
  {
    "{": ""      ""Video ID: UJmfd8UKK7Y""
  },
  {
    "{": ""      ""Video ID: kVXj4ULvPJQ""
  },
  {
    "{": ""      ""Video ID: luwu412__Rc""
  },
  {
    "{": ""      ""Video ID: _zNnAtSb4pU""
  },
  {
    "{": ""      ""Video ID: xqLLbpkkP4U""
  },
  {
    "{": ""      ""Video ID: 9lKG402YJg4""
  },
  {
    "{": ""      ""Video ID: 5rZDDAdz9-8""
  },
  {
    "{": ""      ""Video ID: Y-Nn2zr31z4""
  },
  {
    "{": ""      ""Video ID: bgctv7YRmQw""
  },
  {
    "{": ""      ""Video ID: j7gIy47_oAI""
  },
  {
    "{": ""      ""Video ID: _e4dSOIAwLQ""
  },
  {
    "{": ""      ""Video ID: BVW3vQpPF_0""
  },
  {
    "{": ""      ""Video ID: DEZi-APIcro""
  },
  {
    "{": ""      ""Video ID: oPl4FS7WlPw""
  },
  {
    "{": ""      ""Video ID: h37Wdywodqg""
  },
  {
    "{": ""      ""Video ID: PhNiKPZDNNE""
  },
  {
    "{": ""      ""Video ID: OmX3UQIbfXI""
  },
  {
    "{": ""      ""Video ID: MtGlq04PWBc""
  },
  {
    "{": ""      ""Video ID: QWHSvDQcqW8""
  },
  {
    "{": ""      ""Video ID: 3w6FxkYU9qM""
  },
  {
    "{": ""      ""Video ID: RMx10BUgzEM""
  },
  {
    "{": ""      ""Video ID: Zk_Fz0uzukw""
  },
  {
    "{": ""      ""Video ID: 0lOFFZ6vYcw""
  },
  {
    "{": ""      ""Video ID: kNNCxe0GnD0""
  },
  {
    "{": ""      ""Video ID: aKY35k8zjfI""
  },
  {
    "{": ""      ""Video ID: eAXFnKKFpLk""
  },
  {
    "{": ""      ""Video ID: gQITmHoq1D8""
  },
  {
    "{": ""      ""Video ID: keiht9JExT4""
  },
  {
    "{": ""      ""Video ID: gaRuCjreEak""
  },
  {
    "{": ""      ""Video ID: 9IVhzMHBB5c""
  },
  {
    "{": ""      ""Video ID: lZpw1PE7Hy4""
  },
  {
    "{": ""      ""Video ID: b57ApHtZFBI""
  },
  {
    "{": ""      ""Video ID: cYwwplrmUjs""
  },
  {
    "{": ""      ""Video ID: u3O-jac4MTU""
  },
  {
    "{": ""      ""Video ID: kRa8scK_W74""
  },
  {
    "{": ""      ""Video ID: gbBMG8N_QbM""
  },
  {
    "{": ""      ""Video ID: kkOE0rS5E8U""
  },
  {
    "{": ""      ""Video ID: kCVYN6mBm8s""
  },
  {
    "{": ""      ""Video ID: EkhskLTnpgE""
  },
  {
    "{": ""      ""Video ID: efshZGi0tY8""
  },
  {
    "{": ""      ""Video ID: isTNRpH0q9Q""
  },
  {
    "{": ""      ""Video ID: NLYvoQhHQXs""
  },
  {
    "{": ""      ""Video ID: zKQtDT9Ou1I""
  },
  {
    "{": ""      ""Video ID: ixWRVJrpVj8""
  },
  {
    "{": ""      ""Video ID: LC5m-3PV9EE""
  },
  {
    "{": ""      ""Video ID: uByy0bqaB8E""
  },
  {
    "{": ""      ""Video ID: O72CndXVO7E""
  },
  {
    "{": ""      ""Video ID: ggTHKJvOFxc""
  },
  {
    "{": ""      ""Video ID: uSHrIeD9bAs""
  },
  {
    "{": ""      ""Video ID: xkof-BxoLM0""
  },
  {
    "{": ""      ""Video ID: -oliKHpVq2A""
  },
  {
    "{": ""      ""Video ID: vFM-j5T-p_o""
  },
  {
    "{": ""      ""Video ID: dWTzmgm1crU""
  },
  {
    "{": ""      ""Video ID: 2OY-wB21xxY""
  },
  {
    "{": ""      ""Video ID: -lpqB_s2bno""
  },
  {
    "{": ""      ""Video ID: Vf0q6qtThF4""
  },
  {
    "{": ""      ""Video ID: a-h8LLqx66U""
  },
  {
    "{": ""      ""Video ID: rYBNr9vHpeg""
  },
  {
    "{": ""      ""Video ID: jaN-4eWzK4Y""
  },
  {
    "{": ""      ""Video ID: zNNOJzGR6jA""
  },
  {
    "{": ""      ""Video ID: Uh3Z7Ryv6WI""
  },
  {
    "{": ""      ""Video ID: _fS5P5PoiQI""
  },
  {
    "{": ""      ""Video ID: PXdloA0oBcg""
  },
  {
    "{": ""      ""Video ID: zpWrHJt6ljg""
  },
  {
    "{": ""      ""Video ID: qgFPLylzLyU""
  },
  {
    "{": ""      ""Video ID: YGek4wEQ9W8""
  },
  {
    "{": ""      ""Video ID: lLjbOpAvSgg""
  },
  {
    "{": ""      ""Video ID: hw1qywrJrSk""
  },
  {
    "{": ""      ""Video ID: jB4aI47NLNo""
  },
  {
    "{": ""      ""Video ID: P0FidXWnGc8""
  },
  {
    "{": ""      ""Video ID: kXqAcmDtEXc""
  },
  {
    "{": ""      ""Video ID: wVQOGbPevR0""
  },
  {
    "{": ""      ""Video ID: MiMWJ1xBo8w""
  },
  {
    "{": ""      ""Video ID: cBcrTucxiRc""
  },
  {
    "{": ""      ""Video ID: 7LqYBncyKpM""
  },
  {
    "{": ""      ""Video ID: DLeNU3RIm4o""
  },
  {
    "{": ""      ""Video ID: q5ULwLv8Jx4""
  },
  {
    "{": ""      ""Video ID: qUOmRBbmTvU""
  },
  {
    "{": ""      ""Video ID: DvC7DIaPs2o""
  },
  {
    "{": ""      ""Video ID: x88feUkK-Sc""
  },
  {
    "{": ""      ""Video ID: WTJ9g1pIkzM""
  },
  {
    "{": ""      ""Video ID: sdOEzng3_KM""
  },
  {
    "{": ""      ""Video ID: eeFb2YpkUmw""
  },
  {
    "{": ""      ""Video ID: XqayiS3NnuY""
  },
  {
    "{": ""      ""Video ID: EDFUNfwROWk""
  },
  {
    "{": ""      ""Video ID: yyMyyWjDNdU""
  },
  {
    "{": ""      ""Video ID: mgRh_MGxoSs""
  },
  {
    "{": ""      ""Video ID: hvcKYW5ustw""
  },
  {
    "{": ""      ""Video ID: nsBzNYOQWqI""
  },
  {
    "{": ""      ""Video ID: Xs7y6pmgRng""
  },
  {
    "{": ""      ""Video ID: c5DWw-Mk-PQ""
  },
  {
    "{": ""      ""Video ID: kG4203vCb5g""
  },
  {
    "{": ""      ""Video ID: ez_s09xDYEs""
  },
  {
    "{": ""      ""Video ID: qTWfM2UOcLg""
  },
  {
    "{": ""      ""Video ID: Xc3Hd4-s270""
  },
  {
    "{": ""      ""Video ID: 1EPjlZvbnik""
  },
  {
    "{": ""      ""Video ID: r7SnpOiryE8""
  },
  {
    "{": ""      ""Video ID: IjQ6x0rz5B4""
  },
  {
    "{": ""      ""Video ID: 07xqxgmKZj8""
  },
  {
    "{": ""      ""Video ID: iMB8DGUHZkM""
  },
  {
    "{": ""      ""Video ID: _sm74ERKXmQ""
  },
  {
    "{": ""      ""Video ID: Ua4KIZ0WIYI""
  },
  {
    "{": ""      ""Video ID: JROWtJgdHkY""
  },
  {
    "{": ""      ""Video ID: kS9QkRteCuo""
  },
  {
    "{": ""      ""Video ID: 5bQ8RzLeCdI""
  },
  {
    "{": ""      ""Video ID: y4u4MdSGSDo""
  },
  {
    "{": ""      ""Video ID: ju_rG3DtBnM""
  },
  {
    "{": ""      ""Video ID: g_Mtq3k2pjo""
  },
  {
    "{": ""      ""Video ID: -E_DWI7oqAY""
  },
  {
    "{": ""      ""Video ID: 0FcEbP4yLho""
  },
  {
    "{": ""      ""Video ID: zIpiM6ExkRI""
  },
  {
    "{": ""      ""Video ID: tA-l1K01olc""
  },
  {
    "{": ""      ""Video ID: QsrPoDHtuWA""
  },
  {
    "{": ""      ""Video ID: j7uDbXLcuXw""
  },
  {
    "{": ""      ""Video ID: fi0HbrhM2hg""
  },
  {
    "{": ""      ""Video ID: 6G8OArPHyh8""
  },
  {
    "{": ""      ""Video ID: Pj5gjqob5vs""
  },
  {
    "{": ""      ""Video ID: hgYCRUj-f9A""
  },
  {
    "{": ""      ""Video ID: GZ2ELec-Slg""
  },
  {
    "{": ""      ""Video ID: -H7cZjIMKXg""
  },
  {
    "{": ""      ""Video ID: Escqou9n8X8""
  },
  {
    "{": ""      ""Video ID: YGYok-6aSp0""
  },
  {
    "{": ""      ""Video ID: XgWOFndK2FA""
  },
  {
    "{": ""      ""Video ID: FXwK227BBHc""
  },
  {
    "{": ""      ""Video ID: NvwaDd2a6OQ""
  },
  {
    "{": ""      ""Video ID: 4b3a3SrWaME""
  },
  {
    "{": ""      ""Video ID: x1eFqJxUKx4""
  },
  {
    "{": ""      ""Video ID: Q88vtR8ulzc""
  },
  {
    "{": ""      ""Video ID: p3kxUreqD00""
  },
  {
    "{": ""      ""Video ID: K2bRNqcC0OU""
  },
  {
    "{": ""      ""Video ID: 3G5aKAbJ-VM""
  },
  {
    "{": ""      ""Video ID: VXjGLPzI4DU""
  },
  {
    "{": ""      ""Video ID: HF2zmJvs39Q""
  },
  {
    "{": ""      ""Video ID: KUyOGmr6xBQ""
  },
  {
    "{": ""      ""Video ID: dQprT6JD9CY""
  },
  {
    "{": ""      ""Video ID: fuYL-keoGvU""
  },
  {
    "{": ""      ""Video ID: aOj7FPiGh18""
  },
  {
    "{": ""      ""Video ID: jUwaNG8i8vw""
  },
  {
    "{": ""      ""Video ID: 3nsTeoT0QGI""
  },
  {
    "{": ""      ""Video ID: q6JboTeandw""
  },
  {
    "{": ""      ""Video ID: gyQTCeobZlg""
  },
  {
    "{": ""      ""Video ID: PKs9m5ERm-8""
  },
  {
    "{": ""      ""Video ID: EX4PAyP4ZMk""
  },
  {
    "{": ""      ""Video ID: B-FLDr7OVpY""
  },
  {
    "{": ""      ""Video ID: ULtGHlcQzD0""
  },
  {
    "{": ""      ""Video ID: QwJUqj0hLgk""
  },
  {
    "{": ""      ""Video ID: p2vTTbu_6nI""
  },
  {
    "{": ""      ""Video ID: QtPd9iNSFC0""
  },
  {
    "{": ""      ""Video ID: bg-1CPh0DdE""
  },
  {
    "{": ""      ""Video ID: 6vAMbi12b5A""
  },
  {
    "{": ""      ""Video ID: kCwVrJy1rx8""
  },
  {
    "{": ""      ""Video ID: 9e_kiWm6BFg""
  },
  {
    "{": ""      ""Video ID: zICQVvsLsrU""
  },
  {
    "{": ""      ""Video ID: Ic9wzAHL_rM""
  },
  {
    "{": ""      ""Video ID: 88_pL5fJirc""
  },
  {
    "{": ""      ""Video ID: o3VtUUgPhlA""
  },
  {
    "{": ""      ""Video ID: K0AG6iO46T0""
  },
  {
    "{": ""      ""Video ID: eI6J7yPSEuk""
  },
  {
    "{": ""      ""Video ID: BhQb2wJVPTg""
  },
  {
    "{": ""      ""Video ID: Lrk6vsb77xk""
  },
  {
    "{": ""      ""Video ID: z_VaquA7JuM""
  },
  {
    "{": ""      ""Video ID: h2RWrq_eVGQ""
  },
  {
    "{": ""      ""Video ID: 4qvP9GrjdKw""
  },
  {
    "{": ""      ""Video ID: gYKacRc-Hjc""
  },
  {
    "{": ""      ""Video ID: n4f89Jg-TnY""
  },
  {
    "{": ""      ""Video ID: fYFj0OXTFdU""
  },
  {
    "{": ""      ""Video ID: 9g3clVRckEE""
  },
  {
    "{": ""      ""Video ID: A51o88zUpAA""
  },
  {
    "{": ""      ""Video ID: ADkfLfih7OE""
  },
  {
    "{": ""      ""Video ID: XW3oNrWv6vQ""
  },
  {
    "{": ""      ""Video ID: -Y86bI23FGM""
  },
  {
    "{": ""      ""Video ID: Gz7FOJwvs6M""
  },
  {
    "{": ""      ""Video ID: NXkYyK35mvc""
  },
  {
    "{": ""      ""Video ID: mQmBecSIliQ""
  },
  {
    "{": ""      ""Video ID: g0WKKDuj2Wc""
  },
  {
    "{": ""      ""Video ID: UyExFeb8IGM""
  },
  {
    "{": ""      ""Video ID: MMm5-9yeVLY""
  },
  {
    "{": ""      ""Video ID: mUZ6VOxMm3U""
  },
  {
    "{": ""      ""Video ID: 6ZniB1zlOeQ""
  },
  {
    "{": ""      ""Video ID: FWZTirK6k10""
  },
  {
    "{": ""      ""Video ID: kcxK-iXZwsM""
  },
  {
    "{": ""      ""Video ID: _IfztKHx4ec""
  },
  {
    "{": ""      ""Video ID: 1Sw1Uc-UeBQ""
  },
  {
    "{": ""      ""Video ID: V2va-qry3e8""
  },
  {
    "{": ""      ""Video ID: BMjXCG0e_Po""
  },
  {
    "{": ""      ""Video ID: US0mQJobGwA""
  },
  {
    "{": ""      ""Video ID: -jM7NEL-BIo""
  },
  {
    "{": ""      ""Video ID: bRE3R3j_c7k""
  },
  {
    "{": ""      ""Video ID: -yVZL3ZXE-c""
  },
  {
    "{": ""      ""Video ID: gFSp9pbAWnQ""
  },
  {
    "{": ""      ""Video ID: iWGyVNriJ78""
  },
  {
    "{": ""      ""Video ID: HZ1WlQVz6EE""
  },
  {
    "{": ""      ""Video ID: Fvb7t7AAw9g""
  },
  {
  },
  {
  },
]